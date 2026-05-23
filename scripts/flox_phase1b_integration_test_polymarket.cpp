/*
 * FLOX Phase 1b — live Polymarket market-channel integration test.
 * Env: FLOX_PM_TOKEN_ID (required), FLOX_PM_DURATION_SEC (default 60).
 * Emits JSON summary line prefixed with FLOX_PHASE1B_JSON=
 */

#include "flox-connectors/polymarket/polymarket_exchange_connector.h"

#include <flox/book/bus/book_update_bus.h>
#include <flox/book/bus/trade_bus.h>
#include <flox/book/events/book_update_event.h>
#include <flox/book/events/trade_event.h>
#include <flox/common.h>
#include <flox/log/atomic_logger.h>
#include <flox/log/log.h>

#include <gtest/gtest.h>

#include <atomic>
#include <chrono>
#include <cstdlib>
#include <filesystem>
#include <iostream>
#include <thread>

using namespace flox;

namespace
{

std::string getTempLogDir()
{
  auto dir = std::filesystem::temp_directory_path() / "flox_pm_test_logs";
  std::filesystem::create_directories(dir);
  return dir.string();
}

class CountingSub final : public IMarketDataSubscriber
{
 public:
  CountingSub(std::atomic<int64_t>& bookCount, std::atomic<int64_t>& tradeCount,
              std::atomic<bool>& firstBookSeen, std::chrono::steady_clock::time_point start)
      : _book(bookCount),
        _trade(tradeCount),
        _firstBookSeen(firstBookSeen),
        _start(start)
  {
  }

  SubscriberId id() const override { return 42; }

  void onBookUpdate(const BookUpdateEvent&) override
  {
    _book.fetch_add(1, std::memory_order_relaxed);
    bool expected = false;
    if (_firstBookSeen.compare_exchange_strong(expected, true))
    {
      _firstBookMs.store(
          std::chrono::duration<double, std::milli>(
              std::chrono::steady_clock::now() - _start)
              .count(),
          std::memory_order_relaxed);
    }
  }

  void onTrade(const TradeEvent&) override
  {
    _trade.fetch_add(1, std::memory_order_relaxed);
  }

  std::atomic<double> _firstBookMs{-1.0};

 private:
  std::atomic<int64_t>& _book;
  std::atomic<int64_t>& _trade;
  std::atomic<bool>& _firstBookSeen;
  std::chrono::steady_clock::time_point _start;
};

int durationSec()
{
  if (const char* v = std::getenv("FLOX_PM_DURATION_SEC"))
  {
    return std::max(5, std::atoi(v));
  }
  return 60;
}

std::string tokenId()
{
  if (const char* v = std::getenv("FLOX_PM_TOKEN_ID"))
  {
    return v;
  }
  return {};
}

}  // namespace

TEST(PolymarketExchangeConnectorIntegrationTest, ReceivesBookUpdates)
{
  const std::string tid = tokenId();
  ASSERT_FALSE(tid.empty()) << "Set FLOX_PM_TOKEN_ID";

  std::atomic<int64_t> bookCounter{0};
  std::atomic<int64_t> tradeCounter{0};
  std::atomic<bool> firstBookSeen{false};

  BookUpdateBus bookBus;
  TradeBus tradeBus;

  const auto start = std::chrono::steady_clock::now();
  auto subscriber = std::make_unique<CountingSub>(bookCounter, tradeCounter, firstBookSeen, start);
  auto* subPtr = subscriber.get();
  bookBus.subscribe(subPtr);
  tradeBus.subscribe(subPtr);
  bookBus.start();
  tradeBus.start();

  PolymarketConfig cfg;
  cfg.tokenIds = {tid};
  cfg.reconnectDelayMs = 2000;
  cfg.pingIntervalSec = 5;

  AtomicLoggerOptions logOpts;
  logOpts.directory = getTempLogDir();
  logOpts.basename = "polymarket_test.log";
  logOpts.levelThreshold = LogLevel::Warn;
  auto logger = std::make_shared<AtomicLogger>(logOpts);

  PolymarketExchangeConnector connector(cfg, &bookBus, &tradeBus, nullptr, logger);
  const auto tConnectStart = std::chrono::steady_clock::now();
  connector.start();
  const auto tConnectEnd = std::chrono::steady_clock::now();

  const int dur = durationSec();
  std::this_thread::sleep_for(std::chrono::seconds(dur));

  const double connectMs =
      std::chrono::duration<double, std::milli>(tConnectEnd - tConnectStart).count();
  const double firstBookMs = subPtr->_firstBookMs.load();
  const int64_t books = bookCounter.load();
  const int64_t trades = tradeCounter.load();

  std::cout << "FLOX_PHASE1B_JSON="
            << "{"
            << "\"impl\":\"flox-polymarket-connector\","
            << "\"duration_sec\":" << dur << ","
            << "\"connect_ms\":" << connectMs << ","
            << "\"first_book_ms\":" << (firstBookMs >= 0 ? std::to_string(firstBookMs) : "null")
            << ","
            << "\"book_updates\":" << books << ","
            << "\"trade_updates\":" << trades << ","
            << "\"updates_per_sec\":" << (static_cast<double>(books) / std::max(dur, 1)) << "}"
            << std::endl;
  std::cout.flush();

  // connector.stop() can block on WS teardown; benchmark metrics are already captured.
  if (std::getenv("FLOX_PHASE1B_SKIP_STOP") == nullptr)
  {
    connector.stop();
    bookBus.stop();
    tradeBus.stop();
  }

  EXPECT_GT(books, 0) << "Expected at least one book update from Polymarket WS";
}
