---
title: NVIDIA Corporation (NVDA)
type: entity
tags: [ticker-report, gemini-deep-research, entity, mega_cap, nvda]
category: mega_cap
ticker: NVDA
related:
  - entities/ticker-watchlist.md
maturity: validated
report_source: gemini-deep-research
report_date: 2026-04-23
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @entities/ticker-watchlist.md — parent watchlist page

## Raw Concept

- **Ticker**: NVDA
- **Category**: mega_cap
- **Report source**: Gemini Deep Research (user-commissioned template)
- **Report date**: 2026-04-23
- **Original file**: research for cemini/NVDA 4_23.docx (moved from inbox)
- **Template sections**: Business Overview · Competitive Landscape · Financial Profile · Recent Events · Forward Catalysts · Analyst & Sell-Side Context
- **Maturity**: validated (institutional-grade template; content reflects author/model synthesis as of report date)

## Narrative

*Full Gemini Deep Research report follows, preserved verbatim. Headings demoted by one level so page TOC is consistent.*

## Comprehensive Equity Research Report: NVIDIA Corporation (NVDA)

### 1. Business Overview

NVIDIA Corporation (NVDA) has fundamentally restructured the global computing architecture, transitioning over the past decade from a specialized graphics processing unit (GPU) designer into the foundational infrastructure monopoly of the artificial intelligence (AI) economy. The company’s core business model is centered on accelerated computing, providing full-stack hardware and software solutions that power the most computationally intensive workloads globally. These workloads span large language model (LLM) training, agentic AI inference, scientific computing, physical simulation, and autonomous systems.1 By tightly integrating silicon architectures with proprietary networking fabrics and software ecosystems, the company captures unprecedented economic rent across the data center value chain.

#### Revenue Segments and Geographic Exposure

NVIDIA’s revenue generation is categorized into four primary segments, though the enterprise is overwhelmingly dominated by its Data Center operations. For the fiscal year ended January 25, 2026 (FY26), the company reported a record total revenue of $215.9 billion, representing a 65% year-over-year increase.1 This scale of top-line expansion for a mega-cap technology firm is historically unprecedented and underscores the velocity of the global AI capital expenditure (CapEx) cycle.

The revenue distribution by segment highlights a profound structural reliance on enterprise infrastructure:

Data Center: Generated a record $193.7 billion in FY26, comprising 89.7% of total corporate revenue, an increase of 68% year-over-year. This segment is propelled by hyperscale cloud service providers (CSPs), enterprise AI adoption, and sovereign AI factory build-outs transitioning toward the Blackwell architecture.1

Gaming and AI PC: Generated $16.0 billion, representing 7.4% of total revenue. While this segment saw a 41% year-over-year recovery driven by AI-optimized RTX architectures and consumer PC upgrade cycles, it has essentially been relegated to a secondary business line relative to the data center.1

Professional Visualization: Generated $3.2 billion, accounting for 1.5% of total revenue. This segment is supported by enterprise adoption of Omniverse platforms and industrial digital twin technologies utilized in manufacturing and supply chain simulations.1

Automotive and Robotics: Generated $2.3 billion, representing 1.1% of total revenue. This segment grew 39% year-over-year, supported by autonomous driving platforms and Isaac robotics simulation tools.1

Geographically, NVIDIA has experienced a violent, regulation-driven shift in its revenue base. Historically, the company derived the majority of its revenue from outside the United States; international sales accounted for 56% of total revenue in FY24 and 53% in FY25.6 However, this geographic mix has shifted dramatically due to stringent U.S. export controls restricting the sale of advanced compute to Chinese entities, coupled with the aggressive acceleration of domestic U.S. hyperscaler spending. By the third quarter of FY26, revenue from customers headquartered outside the United States had compressed to just 31%.7 This indicates an increasing reliance on North American cloud providers and a structural decoupling from the Chinese market, which previously served as a primary growth vector.

#### Monetization Mechanics and Unit Economics

NVIDIA generates revenue through the sale of high-margin silicon (GPUs and CPUs), interconnected networking fabrics (InfiniBand and Spectrum-X Ethernet), and recurring enterprise software licenses.8 The unit economics of NVIDIA's hardware represent a masterclass in value-based pricing. The previous generation Hopper architecture (H100) commanded average selling prices near $29,000 per unit, delivering exceptional gross margins.10

As the company transitions to the Blackwell architecture, the value proposition fundamentally shifts from raw training compute to total cost of ownership (TCO) reduction for inference. The DGX B200 system delivers three times the training performance and an astonishing 15 times the inference performance of the DGX H100.11 Despite this exponential leap in utility, the B200 GPU is priced competitively between $30,000 and $50,000, while the ultra-high-end B300 (Blackwell Ultra) targets the $37,500 to $43,750 range.10

By delivering a 15x inference performance improvement for only a modest price premium, NVIDIA drastically lowers the cost per generated token for developers.1 This pricing strategy acts as a massive deflationary force for the broader AI ecosystem—encouraging further model scaling and application development—while simultaneously securing NVIDIA’s platform lock-in and sustaining corporate gross margins structurally in the mid-70% range. Furthermore, the monetization of software is accelerating. The NVIDIA AI Enterprise suite, featuring NVIDIA Inference Microservices (NIMs), provides a highly accretive recurring revenue layer that decouples the company's financial health from pure hardware refresh cycles.4

#### Key Products, Services, and Market Positioning

NVIDIA's product ecosystem is designed to capture every layer of the AI computing stack. The hardware layer is dominated by the Grace Blackwell platform and the forthcoming Vera Rubin architecture (slated for late 2026/2027).1 However, the physical networking layer is equally critical. As large language models scale into the trillions of parameters, single-GPU performance becomes less relevant than the communication bandwidth between thousands of GPUs across a data center. NVIDIA addresses this through NVLink and NVSwitch technologies, effectively rendering an entire server rack (such as the NVL72 architecture) as a single, massive GPU.13 This rack-scale engineering solidifies NVIDIA's positioning not just as a chip supplier, but as a holistic data center infrastructure architect.

### 2. Competitive Landscape

The total addressable market (TAM) for AI accelerators is in a phase of hyper-expansion, growing from approximately $20 billion in 2022 to an estimated $160 billion in 2025, with projections indicating it will exceed $200 billion by the end of 2026.15 NVIDIA currently controls an overwhelming share of this market, capturing between 75% and 81% of total accelerator revenue.15 However, the extraordinary profit pools available in this sector guarantee that the competitive landscape is evolving rapidly from a monopolistic dynamic into a fiercely contested oligopoly.

#### Primary Competitors and Rough Market Share

Advanced Micro Devices (AMD): AMD has established itself as NVIDIA's most formidable merchant silicon competitor. AMD's AI GPU revenue is projected to exceed $15 billion by 2026, driven by the aggressive rollout of its MI300, MI450, and MI500 series accelerators.15 AMD has specifically targeted the inference market, where high memory bandwidth and capacity are paramount. The AMD MI455X, featuring 432GB of HBM4 memory, structurally outpaces the raw memory capacity of NVIDIA's Blackwell B200 (192GB) and Vera Rubin (288GB) architectures.17 Because memory capacity is the primary constraint on inference economics for large-parameter models, AMD has carved out a legitimate leadership position in this specific, highly lucrative sub-segment.

Hyperscaler Custom ASICs: The most severe long-term threat to NVIDIA’s market share paradoxically stems from its own largest customers. Microsoft (Maia), Alphabet (TPU v7), Amazon (Trainium 3), and Meta (MTIA) are aggressively designing and deploying custom application-specific integrated circuits (ASICs).16 The custom ASIC segment represents a $604 billion market shift over the coming decade and is currently growing at a 44.6% compound annual growth rate (CAGR).16 Custom silicon is projected to capture over $25 billion of the accelerator market by 2026.15 Hyperscalers possess both the massive capital required to design these chips and the captive workloads to utilize them, presenting a direct threat to NVIDIA's merchant silicon dominance.

Intel Corporation: Intel has struggled severely to maintain relevance in the high-end AI accelerator market. Its Gaudi 3 processor generated approximately $500 million in 2024, far below the multi-billion-dollar traction achieved by both AMD and NVIDIA.18 Persistent governance issues and foundry execution delays have largely sidelined Intel as a primary threat in the immediate AI infrastructure cycle.18

#### Durable Moats vs. Contested Moats

NVIDIA’s historical competitive moat has been anchored by Compute Unified Device Architecture (CUDA), a proprietary parallel computing platform and programming model introduced over a decade ago. Because generations of developers have written AI and scientific computing software exclusively utilizing CUDA libraries, the switching costs to alternative hardware platforms have historically been insurmountable.15

However, this software moat is now heavily contested. A single-sourced industry analysis suggests that AMD has deployed an innovative "Equity-as-a-Service" model to dismantle the CUDA monopoly.17 According to this analysis, AMD has issued up to 320 million performance-based warrants to OpenAI and Meta, tethered to deployment milestones and AMD's stock performance.17 This aggressive financial engineering transforms NVIDIA's greatest weakness—the hyperscalers' desire to escape NVIDIA's margin stacking—into a self-reinforcing alliance. By granting hyperscalers tens of billions of dollars in equity upside, AMD financially incentivizes the two largest AI model builders to optimize the open-source ROCm software stack and port their models natively to AMD silicon.17 If this execution proves successful, the software lock-in that defined NVIDIA's early dominance will rapidly erode.

Conversely, NVIDIA's most durable remaining moat is its hardware networking ecosystem. The physics of scaling AI models dictate that network bandwidth is the ultimate bottleneck. NVIDIA's InfiniBand and NVLink interconnects—specifically the rack-scale engineering that allows hundreds of GPUs to share memory coherently—remain unmatched.13 Competitors attempting to piece together merchant GPUs with standard Ethernet fabrics face significant latency penalties, ensuring that NVIDIA remains the default choice for frontier model training where absolute performance is non-negotiable.

#### Threats from Adjacent Industries and Technology Shifts

The rapid shift from training to inference represents a dual-edged technology shift. While training LLMs requires the raw brute force and networking supremacy that NVIDIA monopolizes, inferencing is far more dispersed. As AI models become smaller, more efficient, and localized to the edge (e.g., AI PCs, automotive platforms, and enterprise edge servers), the reliance on ultra-expensive centralized GPU clusters diminishes. Furthermore, the push toward open-source foundation models enables enterprises to fine-tune smaller models on proprietary data rather than relying heavily on massive foundational training runs.19 This democratization of AI models increases the viability of lower-cost, alternative computing architectures, including advanced CPUs and neural processing units (NPUs) developed by adjacent entrants like Qualcomm and Apple.

### 3. Financial Profile

NVIDIA's financial performance over the past two fiscal years represents a paradigm shift, reflecting one of the most aggressive fundamental expansions in corporate history. The company has essentially scaled its top line by an order of magnitude while simultaneously expanding its margin profile—a phenomenon rarely observed in hardware-centric businesses.

#### Last 8 Quarters Financial Performance

The following table reconstructs the trailing eight quarters of financial performance, utilizing GAAP figures derived directly from SEC filings and official earnings transcripts.1


| Fiscal Quarter | Revenue ($M) | Diluted EPS (GAAP) | Gross Margin (GAAP) | Operating Margin (GAAP) | Net Margin (GAAP) |
|---|---|---|---|---|---|
| Q1 FY25 | $26,044 | $0.60* | 78.4% | 64.9% | 57.1% |
| Q2 FY25 | $30,040 | $0.67 | 75.1% | 62.1% | 55.3% |
| Q3 FY25 | $35,082 | $0.78 | 74.6% | 62.3% | 55.0% |
| Q4 FY25 | $39,331 | $0.89 | 73.0% | 61.1% | 56.1% |
| Q1 FY26 | $44,062 | $0.81** | 61.0%** | 38.4%** | 42.6%** |
| Q2 FY26 | $46,743 | $1.08 | 72.4% | 60.8% | 56.5% |
| Q3 FY26 | $57,006 | $1.30 | 73.4% | 63.2% | 56.0% |
| Q4 FY26 | $68,127 | $1.76 | 75.0% | 65.0% | 63.1% |


*Note: Q1 FY25 EPS is estimated based on reported net income and split-adjusted share counts. **Note: Q1 FY26 margins and EPS were severely compressed by an idiosyncratic $4.5 billion inventory write-down related to H20 export controls.3

The data illustrates massive operating leverage. While revenue scaled from $26 billion to $68 billion, operating expenses grew at a much slower absolute rate, allowing operating margins to stabilize well above 60% after absorbing the regulatory shock in early FY26.

#### Last 3 Fiscal Years Summary

The sheer volume of cash generated by the enterprise has transformed NVIDIA's capital structure.


| Metric | FY24 | FY25 | FY26 |
|---|---|---|---|
| Free Cash Flow | $27.0B | $60.9B | $96.7B*** |
| Net Debt | $(1.25B) | $(1.25B) | $(53.1B)**** |
| Shares Outstanding | 24.6B | 24.6B | 24.3B |


***Note: FY26 Free Cash Flow is estimated based on reported operating cash flow and historical capex run rates.7 ****Note: Net debt reflects $60.6B in cash/marketable securities against $7.47B in long-term debt.1

#### Capital Allocation: Buybacks, Dividends, and M&A

NVIDIA operates as a highly cash-generative entity, aggressively deploying capital to repurchase shares to offset dilution and return capital to shareholders. During FY26, the company returned $41.1 billion to shareholders via buybacks and dividends.1 The dividend remains largely tokenistic at $0.01 per share per quarter, yielding negligibly relative to the share price.1

The primary capital return mechanism is equity repurchases. In August 2025, the Board of Directors authorized an unprecedented $60.0 billion share repurchase program without an expiration date.7 By the end of FY26, $58.5 billion remained under this authorization.1 Mergers and acquisitions (M&A) activity remains structurally muted. Heightened global antitrust scrutiny, specifically from U.S., European, and Chinese regulators, effectively precludes NVIDIA from executing large-scale acquisitions in the semiconductor space. Consequently, the company directs surplus cash toward organic R&D, strategic venture investments in AI startups to cultivate the ecosystem, and massive equity repurchases.

#### Balance Sheet Health and Debt Maturity Wall

The balance sheet is fortified with profound liquidity, operating with a severely negative net debt profile. As of late FY26, NVIDIA held $60.6 billion in cash, cash equivalents, and marketable securities.7 Against this, total long-term debt stands at a modest $7.47 billion.1

Debt Maturity Wall:


| Maturity Year | Principal Amount ($M) | Interest Rate |
|---|---|---|
| 2026 | $1,000 | 3.20% |
| 2028 | $1,250 | 1.55% |
| 2030 | $1,500 | 2.85% |
| 2031 | $1,250 | 2.00% |
| 2040 & Beyond | $3,500 | ~3.50% |


Source: SEC Form 10-K and 10-Q disclosures.30

Given the company's robust free cash flow generation—approaching $100 billion annually—this maturity profile poses absolutely zero refinancing risk. The sheer volume of cash on the balance sheet provides immense strategic flexibility to outspend competitors on R&D and secure critical packaging capacity at TSMC through multi-billion dollar prepayments.2

### 4. Recent Events (Last 12 Months)

#### Earnings Surprises vs. Consensus

NVIDIA has maintained a consistent trajectory of exceeding Wall Street consensus estimates, though the magnitude of these beats has normalized as analyst models recalibrate to the reality of the company's hyper-growth. In Q4 FY26, the company reported Non-GAAP EPS of $1.62, beating the consensus estimate of $1.56 by 3.62%, alongside a slight revenue beat of 0.87% ($68.12 billion actual vs $67.53 billion consensus).20 Previous quarters demonstrated similarly tight beats: Q3 FY26 EPS beat by 1.99%, and Q2 FY26 EPS beat by 2.13%.20 This narrowing of surprise magnitude indicates that the sell-side has fully digested the AI infrastructure thesis and is highly proficient at forecasting near-term data center deployments. The era of 20%+ earnings surprises has structurally ended.

#### Product Launches, Strategic Shifts, and Restructurings

The preceding 12 months were defined by the aggressive rollout of the Blackwell architecture and the pivot toward agentic AI. As stated by CEO Jensen Huang in the Q4 FY26 earnings release, the industry has reached an "agentic AI inflection point," moving beyond passive, prompt-based generative models toward autonomous AI agents that can reason, plan, and execute multi-step tasks across enterprise software.1 This paradigm shift demands massive increases in low-latency inference compute.

To capture this, NVIDIA successfully launched the Grace Blackwell platform with NVLink, positioning it as the premier engine for inference throughput.1 Looking ahead to sustain its competitive lead, the company aggressively accelerated its roadmap, unveiling the upcoming Vera Rubin platform. Rubin comprises six new chips engineered to deliver up to a 10x reduction in inference token costs compared to Blackwell, ensuring NVIDIA maintains its architectural dominance.1 No significant corporate restructurings have occurred, as the company operates with extreme efficiency relative to its revenue footprint.

#### Management Changes and Insider Activity

The C-suite has remained highly stable, providing essential continuity during this hyper-growth phase. There have been no material management departures among the core leadership team. However, insider activity has been defined by systematic, programmatic selling. CEO Jensen Huang has been executing sales under a Rule 10b5-1 trading plan adopted in March 2025.32 The plan permits the disposal of up to 6 million shares (valued at roughly $865 million) by the end of 2025/2026.34 Huang recently executed sales of hundreds of thousands of shares across mid-to-late 2025.33 Other senior executives, including EVP Ajay Puri and CFO Colette Kress, have similarly liquidated significant equity tranches.37 While insider selling is typically interpreted as a bearish signal, these sales represent a fraction of a percent of Huang's total holdings (which exceed 900 million shares), classifying them as routine wealth diversification rather than a lack of institutional conviction.32

#### Regulatory and Legal Developments

The most material operational headwind encountered in the last 12 months was the abrupt enforcement of U.S. export controls aimed at restricting China's access to advanced computing. On April 9, 2025, the U.S. government issued new restrictions that immediately halted the sale of the H20 data center GPU—a product specifically engineered by NVIDIA to comply with previous, less stringent export thresholds.26 Crucially, the regulation was implemented without a grace period, stranding finished goods inventory and halting $2.5 billion in expected Q1 FY26 revenue.26 Consequently, NVIDIA was forced to record a massive $4.5 billion charge to write down H20 inventory and cancel non-cancellable purchase obligations.3

This regulatory action temporarily crushed Q1 FY26 GAAP gross margins down to 61.0%.3 While NVIDIA managed a minor $180 million release from this reserve in Q2 FY26 by finding alternate buyers outside China 14, the event permanently highlighted the severe geopolitical tail risks inherent in the semiconductor supply chain. Concurrently, the company continues to navigate legacy class-action litigation regarding historic disclosures of cryptocurrency mining revenue 7, though this litigation is considered immaterial compared to the systemic risk of shifting geopolitical trade policies.

### 5. Forward Catalysts (Next 6–12 Months)

#### Next Earnings Date and Consensus Expectations

NVIDIA’s next earnings release, covering Q1 FY27, is slated for late May 2026.38 This report will serve as a critical barometer for the global AI build-out. The company has explicitly guided Q1 FY27 revenue to $78.0 billion (±2%), with GAAP gross margins projected at 74.9%.1 Crucially, this outlook assumes zero Data Center compute revenue from China, effectively resetting the geographic baseline and confirming that global hyperscaler demand outside of sanctioned regions is more than sufficient to absorb diverted supply.1 The consensus expectations will tightly mirror this guidance, but market focus will immediately pivot to forward commentary regarding Q2 and Q3 deployment schedules.

#### Product Roadmap Items and Guidance Milestones

The dominant structural catalyst for the next 12 months is the volume ramp of the Blackwell Ultra (B300) systems. Investors will scrutinize deployment timelines, thermal envelope management, and gross margin stabilization as Blackwell becomes the majority of shipped units. Subsequently, early visibility into the tape-out and sampling of the Vera Rubin architecture will be a key milestone. Rubin is slated for late 2026/2027 deployment and will introduce the entirely new Vera processor.12 Furthermore, market reaction to the enterprise adoption rates of NIMs (NVIDIA Inference Microservices) and AI Enterprise software will serve as major software-centric catalysts. Demonstrating significant traction here is essential for validating the thesis that NVIDIA is evolving from a hardware vendor into a recurring software platform.4

#### Sector and Macro Events Moving the Stock

NVIDIA's valuation is inextricably linked to the capital expenditure guidance of Big Tech. Hyperscalers are projected to spend approximately $562 billion on AI infrastructure in 2026, a 30% year-over-year increase.39 Any forward guidance revisions issued by Microsoft, Alphabet, Amazon, or Meta during their respective earnings cycles will act as an immediate, sector-wide catalyst for NVIDIA equity.

On the macroeconomic front, U.S. Federal Reserve interest rate decisions and geopolitical events are paramount. A single-sourced macroeconomic thesis highlights the "Reverse Gorbachev" dynamic—a potential U.S. policy shift away from financialization and toward aggressive national security-focused industrialization and protective tariffs.40 If such protectionist policies escalate, it could disrupt the delicate TSMC supply chain and increase input costs. Conversely, a dovish pivot by the Federal Reserve would lower discount rates, immediately expanding the multiple applied to NVIDIA's long-duration growth cash flows.41

### 6. Analyst & Sell-Side Context

Wall Street maintains a highly constructive, nearly euphoric posture on NVIDIA, though deep analytical debate centers on the terminal value and duration of the AI infrastructure super-cycle.

#### Consensus Rating, Price Target, and Range

Based on recent compilations of sell-side research, NVIDIA commands a nearly universal "Buy" consensus. Approximately 55% of covering analysts issue a "Strong Buy" recommendation, with an additional 39% issuing a "Buy".43 Only a negligible 3% advise holding or selling.43 The average price target rests in the $268 to $275 range, representing substantial upside from current trading levels near $200.44 Notably, aggressive mid-case valuation models project potential terminal targets approaching $498 by the end of the decade, strictly contingent on the company sustaining an 80-90% data center CAGR and averting a cyclical hardware digestion phase.43

#### Notable Upgrades and Downgrades

Over the last six months, several structural upgrades have materialized that validate the company's transition beyond pure hardware.

Deep Value Investing: Upgraded the stock to "Buy," noting that despite the equity consolidating for six months, the fundamental risk-on trade for AI infrastructure remains intact and significantly underpriced relative to actual earnings delivery.46

S&P Global Ratings: From a credit perspective, S&P revised NVIDIA’s outlook to Positive from Stable (affirming the AA- long-term rating). The agency cited robust free operating cash flow and a sustainable competitive advantage that will allow NVIDIA to maintain market leadership through the transition from model training to edge and inferencing workloads.47

#### Bull Case vs. Bear Case

The Bull Case:

Agentic AI Expansion: The transition from conversational generative AI to autonomous agentic AI requires an exponential, non-linear increase in inference compute. This ensures GPU demand will persist and compound long after the initial LLM training clusters are fully constructed.1

Pricing Power and Software Lock-in: NVIDIA maintains absolute pricing power with Blackwell, structurally supported by rising enterprise software attachment rates (NVIDIA AI Enterprise). This deepens the economic moat, creates switching costs, and drives gross margin durability independent of silicon cycles.4

Unprecedented Capital Returns: The aggressive execution of the $60 billion share repurchase authorization provides a massive structural floor for the equity, driving continuous EPS accretion and buffering against short-term macroeconomic volatility.14

The Bear Case:

Customer Concentration and CapEx Exhaustion: With a staggering 61% of compute revenue tied to just four hyperscale customers 12, any moderation in hyperscaler CapEx—potentially driven by an inability to successfully monetize AI end-user applications—would immediately trigger severe multiple compression.

The AMD/Hyperscaler Open-Source Alliance: AMD's aggressive deployment of the "Equity-as-a-Service" strategy with Meta and OpenAI directly threatens to commoditize AI hardware. By financially incentivizing hyperscalers to mature the open-source ROCm stack, NVIDIA's primary software moat (CUDA) could be rapidly neutralized.17

Geopolitical and Supply Chain Fragility: Continued U.S. export controls risk permanently erasing revenue from the global market, while extreme reliance on TSMC's CoWoS packaging exposes NVIDIA to single-point-of-failure geopolitical risks in the Taiwan Strait.15

### 7. Ownership & Positioning

#### Top Institutional Holders and Position Changes

NVIDIA operates as a cornerstone asset in global equities, functioning as a primary beta driver for the S&P 500. Institutional investors currently hold approximately 72.1% of the outstanding float.49 Passive index funds and active mutual fund positioning remain heavily saturated, mirroring the stock's outsized index weighting. Recent 13F filings indicate minor rebalancing, with mutual funds slightly decreasing holdings from 72.58% to 71.60% over the last quarter, likely an exercise in risk management and portfolio concentration limits rather than a bearish fundamental view.49 Specific institutional moves indicate tactical trading; for example, entities like Exchange Traded Concepts and AlphaStar Capital Management have actively traded the volatility, though Vanguard and BlackRock remain the unassailable anchor holders.50

#### Insider Buying and Selling

As detailed in the Recent Events section, insider activity is exclusively characterized by selling. Insiders currently hold roughly 13.9% of the company, an astronomically high figure for a multi-trillion dollar enterprise, driven almost entirely by founder Jensen Huang's stake.49 Over the last 12 months, executives have systematically sold shares via pre-arranged Rule 10b5-1 plans.32 In a single 90-day window, insiders liquidated over 1.6 million shares valued at approximately $292 million.37 While absolute dollar amounts are massive, the selling volume is negligible relative to the total insider float and is structurally anticipated by the market.

#### Short Interest and Options Skew

Short interest in NVIDIA remains structurally negligible. Only 1.20% of the float (roughly 280 million shares) is currently sold short, translating to a days-to-cover ratio of just 2.34.51 Institutional hedge funds are largely unwilling to absorb the career risk of shorting a company demonstrating 70%+ top-line growth and relentless earnings beats.

However, the derivatives market reveals profound insights into sophisticated institutional positioning. Recent options flow highlights massive short-term bullish speculation counterbalanced by significant long-term tail-risk hedging. In April 2026, highly unusual call spread volume was detected (e.g., 5,846 contracts on the 195–197.5 strikes expiring within days) that netted 56% gains intraday. This signals acute FOMO (fear of missing out) and aggressive upside momentum chasing by retail and tactical funds.52

Conversely, longer-dated options skew indicates aggressive hedging. Barchart reported significant unusual volume in October 2026 out-of-the-money puts (strike $150), where institutional sellers collected high premiums (yielding ~6.4%), establishing a downside breakeven near $140.54 The 150-day Put/Call Open Interest ratio sits at 1.18, and the 25-delta put skew remains slightly elevated.55 This dynamic confirms that while short-term sentiment remains exuberant, institutional portfolio managers are heavily insuring their books against a structural cyclical drawdown.

### 8. Risks

Investing in NVIDIA at its current scale requires navigating a complex matrix of idiosyncratic, sectoral, and macroeconomic risks.

#### Company-Specific Risks

The most critical idiosyncratic risk facing NVIDIA is extreme customer concentration. SEC filings reveal that just four direct customers accounted for 61% of total compute revenue in the third quarter of FY26 (Customer A at 22%, Customer B at 15%, Customer C at 13%, and Customer D at 11%).7 Circumstantial industry analysis universally identifies these entities as the primary Western hyperscalers (Microsoft, Meta, AWS, Alphabet).57 This establishes a fragile dependency. If the internal return on investment (ROI) on AI deployments falls short of these hyperscalers' internal models, they could synchronously defer data center upgrade cycles, leading to an abrupt, violent revenue air pocket for NVIDIA.

Furthermore, execution and supply chain risks remain heavily elevated. Transitioning the global data center footprint from Hopper to Blackwell—and subsequently to Rubin—requires orchestrating the world's most complex semiconductor supply chain. NVIDIA is entirely reliant on Taiwan Semiconductor Manufacturing Company's (TSMC) CoWoS (Chip-on-Wafer-on-Substrate) advanced packaging capacity.2 Any disruption at TSMC, whether caused by manufacturing yield issues, seismic events, or geopolitical escalation, would immediately paralyze NVIDIA's ability to fulfill its massive order backlog.

From a litigation standpoint, the company continues to defend against historic securities class actions regarding cryptocurrency mining disclosures and navigates ongoing patent infringement claims typical of apex technology firms.7 However, these legal liabilities represent immaterial financial risk compared to supply chain and customer concentration threats.

#### Sector Risks

The broader technology sector is currently engaged in a massive infrastructure arms race, but the ultimate monetization of AI remains unproven at the scale required to perpetually justify $500 billion to $700 billion in annual CapEx.59 There is a latent risk of a "trough of disillusionment." If enterprise clients balk at the high subscription costs of AI agents, the hyperscalers will ultimately throttle their hardware purchases. Additionally, the rapid proliferation of custom ASICs developed by NVIDIA's own clients ensures that inferencing—the highest volume and most critical segment of the future AI market—will face severe, structural pricing pressure over the next three years.16

#### Macro Sensitivities

NVIDIA operates as a high-beta, long-duration growth asset, rendering its equity premium highly sensitive to macroeconomic variables. The stock exhibits an inverse correlation with the U.S. 10-year Treasury yield and the U.S. Dollar Index.42 If persistent inflation forces the Federal Reserve to hold policy rates elevated, the discount rate applied to NVIDIA's calendar 2027 and 2028 terminal cash flows will mathematically compress the stock's multiple. Additionally, the geopolitical landscape represents an existential macro risk. The potential for aggressive U.S. industrial policy shifts—involving stringent protectionist tariffs and further export blockades—threatens to artificially inflate input costs, fracture global end-markets, and incite retaliatory trade policies from sovereign actors.40

### 9. Valuation & Peer Context

Despite NVIDIA's exceptional price appreciation over the last three years, the company's explosive earnings growth has fundamentally outpaced its stock price, resulting in a counterintuitive structural valuation multiple compression.

#### Current Multiples vs. 5-Year History and Sector Median

As of April 2026, NVIDIA trades at a forward Price-to-Earnings (P/E) ratio ranging from approximately 17.9x to 24.0x (depending heavily on the specific calendar year consensus utilized for CY27/CY28 earnings).27 This represents a severe contraction from peak euphoria multiples that exceeded 50x forward earnings in mid-2023.27

When analyzed on a capital-structure-neutral basis using Enterprise Value to EBITDA (EV/EBITDA), NVIDIA trades at roughly 36.4x.64 This current valuation is materially below its 3-year historical average of 44.8x and its 5-year average of 46.1x.65 The Price-to-Sales (P/S) multiple remains elevated at approximately 22.7x, reflecting the software-like gross margins of the hardware business.64 If the EV/EBITDA multiple were to simply mean-revert to its 3-year historical average, analytical models imply an intrinsic value near $250, representing roughly 24% upside from current levels.65

Comparatively, Broadcom (AVGO)—a primary peer in AI networking and custom hyperscaler silicon—trades at a forward P/E of ~22.4x and a much steeper EV/EBITDA of 53.1x.64 Broadcom's premium valuation is partially justified by its high-margin recurring software revenue from the VMware acquisition, which smooths cyclicality.27 However, this peer comparison highlights that NVIDIA is not trading at peak euphoria multiples relative to its semiconductor peers. While AVGO's revenue growth is modeled around 25% for the forward year, NVIDIA continues to deliver top-line revenue growth exceeding 60%.66

#### Key Correlations

NVIDIA’s valuation is intrinsically and highly correlated to the forward capital expenditure guidance of Big Tech.39 Macroeconomic analysts note that the $500 billion+ AI CapEx boom provides a massive boost to aggregate U.S. GDP, but is uniquely capturing profits within a very narrow, highly concentrated set of semiconductor firms.61 Consequently, NVIDIA's stock performance is highly correlated to the forward earnings guidance of Microsoft, Meta, Amazon, and Alphabet. If the industry narrative shifts from "infrastructure land-grab" to "capital efficiency and digestion," NVIDIA's multiple will face immediate, severe contraction, regardless of its ability to execute near-term earnings beats.

### 10. Sources

Primary Sources:

68
Nasdaq SEC Filings for NVDA. https://www.nasdaq.com/market-activity/stocks/nvda/sec-filings (Retrieved April 2026)

6
NVIDIA Q4 FY25 Financials PDF. https://s201.q4cdn.com/141608511/files/doc_financials/2025/q4/177440d5-3b32-4185-8cc8-95500a9dc783.pdf (Retrieved April 2026)

7
SEC Form 10-Q (October 26, 2025). https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm (Retrieved April 2026)

1
NVIDIA Newsroom, Q4 and FY2026 Summary. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 (Retrieved April 2026)

1
NVIDIA Newsroom, Q4 FY26 Results. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 (Retrieved April 2026)

1
NVIDIA Newsroom, Q4 FY26 Dividend and Buyback Summary. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 (Retrieved April 2026)

23
NVIDIA Newsroom, Q4 FY25 Results. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2025 (Retrieved April 2026)

9
NVIDIA Q1 FY25 PDF Highlights. https://nvidianews.nvidia.com/_gallery/download_pdf/664e53fe3d63322459a5eff6/ (Retrieved April 2026)

33
StockTitan, Form 4 Insider Trading. https://www.stocktitan.net/sec-filings/NVDA/form-4-nvidia-corp-insider-trading-activity-8095b2595117.html (Retrieved April 2026)

36
StockTitan, NVDA Open Market Sales. https://www.stocktitan.net/sec-filings/NVDA/form-4-nvidia-corp-insider-trading-activity-3aaac5bddbd1.html (Retrieved April 2026)

1
NVIDIA Q4 FY26 PDF. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 (Retrieved April 2026)

3
NVIDIA Q1 FY26 Results. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026 (Retrieved April 2026)

26
DiscountingCashFlows, Q1 FY26 Earnings Call Transcript. https://discountingcashflows.com/company/NVDA/transcripts/2026/1/ (Retrieved April 2026)

2
SEC Form 10-K (January 28, 2024). https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm (Retrieved April 2026)

21
NVIDIA Q2 FY25 Results. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2025 (Retrieved April 2026)

3
NVIDIA Q1 FY26 Results. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026 (Retrieved April 2026)

14
NVIDIA Q2 FY26 Results. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2026 (Retrieved April 2026)

7
SEC Form 10-Q (October 26, 2025). https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm (Retrieved April 2026)

23
NVIDIA Q4 FY25 Results. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2025 (Retrieved April 2026)

24
NVIDIA Q3 FY25 Results. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2025 (Retrieved April 2026)

25
NVIDIA Q3 FY26 Results. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2026 (Retrieved April 2026)

14
NVIDIA Q2 FY26 Results. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2026 (Retrieved April 2026)

1
NVIDIA Q4 FY26 FCF. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 (Retrieved April 2026)

7
SEC Form 10-Q Cash Flow. https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm (Retrieved April 2026)

1
NVIDIA Q4 FY26 Balance Sheet. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 (Retrieved April 2026)

30
NVIDIA Note 10 Debt. https://s201.q4cdn.com/141608511/files/doc_financials/2026/q2/2e217538-c226-4d05-8f74-aaca89a21b33.pdf (Retrieved April 2026)

69
SEC Form 10-Q Repurchase. https://www.sec.gov/Archives/edgar/data/1045810/000104581025000209/nvda-20250727.htm (Retrieved April 2026)

58
SEC Form 10-K Shares Out. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm (Retrieved April 2026)

7
SEC Form 10-Q Litigation. https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm (Retrieved April 2026)

31
SEC Form 10-Q Maturities. https://s201.q4cdn.com/141608511/files/doc_financials/2026/q3/13e6981b-95ed-4aac-a602-ebc5865d0590.pdf (Retrieved April 2026)

7
SEC Form 10-Q Cap Return. https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm (Retrieved April 2026)

Secondary Coverage:

32.

70

TradingView, NVIDIA CORP SEC 10-K Report. https://www.tradingview.com/news/tradingview:602edbd315060:0-nvidia-corp-sec-10-k-report/ (Retrieved April 2026)

33.

11

NVIDIA DGX B200 Architecture. https://www.nvidia.com/en-us/data-center/dgx-b200/ (Retrieved April 2026)

34.

10

IntuitionLabs, NVIDIA AI GPU Pricing Guide. https://intuitionlabs.ai/articles/nvidia-ai-gpu-pricing-guide (Retrieved April 2026)

35.

13

NVIDIA Technical Blog, Inside NVIDIA Blackwell Ultra. https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/ (Retrieved April 2026)

36.

15

Silicon Analysts, NVIDIA AI Accelerator Market Share. https://siliconanalysts.com/analysis/nvidia-ai-accelerator-market-share-2024-2026 (Retrieved April 2026)

37.

16

Introl, Custom Silicon Inflection 2026. https://introl.com/blog/custom-silicon-inflection-2026-hyperscaler-asics-nvidia-gpu (Retrieved April 2026)

38.

18

AI Multiple, AI Chip Makers. https://aimultiple.com/ai-chip-makers (Retrieved April 2026)

39.

17

Investing.com, AMD's AI Deals Provide Visibility. https://www.investing.com/analysis/amds-ai-deals-provide-visibility-on-future-revenue-through-2027-200678987 (Retrieved April 2026)

40.

20

ChartMill, NVDA Earnings Surprise History. https://www.chartmill.com/stock/quote/NVDA/earnings (Retrieved April 2026)

41.

27

TIKR, Broadcom vs NVIDIA Valuation. https://www.tikr.com/blog/broadcom-vs-nvidia-are-investors-still-overpaying-for-ai-growth (Retrieved April 2026)

42.

43

Public.com, NVDA Forecast & Price Target. https://public.com/stocks/nvda/forecast-price-target (Retrieved April 2026)

43.

59

HeyGoTrade, 5 AI Stocks Beyond NVIDIA. https://www.heygotrade.com/en/blog/5-ai-stocks-beyond-nvidia/ (Retrieved April 2026)

44.

44

Zacks, NVDA Price Target & Stock Forecast. https://www.zacks.com/stock/research/NVDA/price-target-stock-forecast (Retrieved April 2026)

45.

71

QuiverQuant, NVDA Analyst Ratings. https://www.quiverquant.com/news/NVIDIA+Stock+%28NVDA%29+Opinions+on+AI+Partnerships+and+Infrastructure+Deals (Retrieved April 2026)

46.

49

Trendlyne, NVIDIA Institutional Holders. https://us.trendlyne.com/us/equity/ownership/1554267/NVDA/latest/nvidia-corp/ (Retrieved April 2026)

47.

51

Fintel, NVDA Short Interest. https://fintel.io/s/us/nvda (Retrieved April 2026)

48.

39

RBC Wealth Management, Big Tech's AI Expansion. https://www.rbcwealthmanagement.com/en-us/insights/big-techs-ai-expansion-from-investment-to-scalable-returns (Retrieved April 2026)

49.

60

The Motley Fool, $700 Billion AI Capex Boom. https://www.fool.com/investing/2026/04/02/prediction-the-700-billion-artificial-intelligence/ (Retrieved April 2026)

50.

4

NVIDIA Blog, State of AI. https://blogs.nvidia.com/blog/state-of-ai-report-2026/ (Retrieved April 2026)

51.

19

NVIDIA Blog, AI in Financial Services. https://blogs.nvidia.com/blog/ai-in-financial-services-survey-2026/ (Retrieved April 2026)

52.

40

Velocity Meter, Big Tech's $650B AI Bet. https://www.velocitymeter.com/big-techs-650b-ai-bet-windfall-for-nvidia-saas-apocalypse-lurks/ (Retrieved April 2026)

53.

8

StockTitan, Q2 FY25 Results. https://www.stocktitan.net/news/NVDA/nvidia-announces-financial-results-for-second-quarter-fiscal-grc4w22riad8.html (Retrieved April 2026)

54.

32

Cryptopolitan, Jensen Huang 10b5-1 Sales. https://www.mitrade.com/insights/shares-analysis/us-stocks/cryptopolitan-NVDA-202506241353 (Retrieved April 2026)

55.

34

Fox Business, Nvidia CEO Sells Stock. https://www.foxbusiness.com/markets/nvidia-ceo-sells-15m-worth-stock-part-planned-sale (Retrieved April 2026)

56.

35

Investing.com, Huang Begins Selling Shares. https://www.investing.com/news/stock-market-news/nvidia-ceo-huang-begins-selling-shares-under-800-mln-plan-4106919 (Retrieved April 2026)

57.

64

AllInvestView, AVGO vs NVDA. https://www.allinvestview.com/compare/AVGO-vs-NVDA/ (Retrieved April 2026)

58.

66

Trefis, NVDA, MU vs AVGO. https://www.trefis.com/stock/avgo/articles2/595444/nvda-mu-top-broadcom-stock-on-price-potential/2026-04-01 (Retrieved April 2026)

59.

65

AlphaSpread, NVDA EV/EBITDA. https://www.alphaspread.com/security/nasdaq/nvda/relative-valuation/ratio/enterprise-value-to-ebitda (Retrieved April 2026)

60.

52

MarketChameleon, NVDA Call Spread Options. https://marketchameleon.com/articles/b/2026/4/14/nvda-call-spread-buyers-56-3-percent-gain-quantum-ai-bullish-technicals-slightly-bearish-skew (Retrieved April 2026)

61.

54

Barchart, Unusual NVDA Put Volume. https://www.barchart.com/story/news/824936/huge-unusual-trading-in-nvidia-put-options-investors-bullish-on-nvda (Retrieved April 2026)

62.

53

Morningstar, Option Flow FOMO. https://www.morningstar.com/news/marketwatch/2026042139/traders-pile-into-call-options-as-fear-of-missing-out-grows-according-to-cboe (Retrieved April 2026)

63.

45

TIKR, NVIDIA Breakout. https://www.tikr.com/blog/nvidia-stock-is-up-18-in-10-days-is-the-six-month-consolidation-finally-over (Retrieved April 2026)

64.

37

InsiderFinance, NVDA Upgrades. https://www.insiderfinance.io/news/nvidia-earnings-strengthened-by-analyst-upgrades (Retrieved April 2026)

65.

67

Bridgewater, Macro Implications of AI Capex. https://www.bridgewater.com/research-and-insights/the-macro-implications-of-the-ai-capex-boom (Retrieved April 2026)

66.

61

UBP, AI Long-Term Winners. https://www.ubp.com/en/news-insights/newsroom/artificial-intelligence-s-long-term-winners-investment-outlook-2026 (Retrieved April 2026)

67.

39

RBC Wealth Management, Capex Cycles. https://www.rbcwealthmanagement.com/en-us/insights/big-techs-ai-expansion-from-investment-to-scalable-returns (Retrieved April 2026)

68.

4

NVIDIA Blog, State of AI. https://blogs.nvidia.com/blog/state-of-ai-report-2026/ (Retrieved April 2026)

69.

57

Economic Times, Mystery Customers. https://m.economictimes.com/news/international/us/two-mystery-customers-made-up-40-of-nvidias-revenue-who-are-they/articleshow/123635412.cms (Retrieved April 2026)

70.

12

The Motley Fool, Customer Concentration. https://www.fool.com/investing/2025/11/27/blackwell-off-charts-nvidia-customer-concentration/ (Retrieved April 2026)

71.

55

AlphaQuery, Put-Call Ratio. https://www.alphaquery.com/stock/NVDA/volatility-option-statistics/150-day/put-call-ratio-oi (Retrieved April 2026)

72.

43

Public.com, Upgrades/Downgrades. https://public.com/stocks/nvda/forecast-price-target (Retrieved April 2026)

73.

62

Investing.com, Dollar Dynamics. https://www.investing.com/analysis/us-dollars-2026-decline-more-cyclical-than-structural-200675481 (Retrieved April 2026)

74.

41

Yahoo Finance, Rate Cuts. https://www.youtube.com/watch?v=uvtTWGorfHE (Retrieved April 2026)

75.

63

JP Morgan, Navigating Rate Risks. https://www.jpmorgan.com/insights/markets/top-market-takeaways/tmt-navigating-rate-risks-how-bonds-are-better-positioned-in-2025 (Retrieved April 2026)

76.

47

S&P Global, NVIDIA Outlook. https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3463383 (Retrieved April 2026)

77.

46

SeekingAlpha, Analyst Upgrades. https://seekingalpha.com/news/4575264-sa-analyst-upgrades-downgrades-nvda-jnj-ko-acn (Retrieved April 2026)

78.

56

MarketChameleon, Volatility Skew. https://marketchameleon.com/Overview/NVDA/VolatilitySkew/ (Retrieved April 2026)

79.

29

MacroTrends, Net Debt. https://www.macrotrends.net/stocks/charts/NVDA/nvidia/net-long-term-debt (Retrieved April 2026)

80.

28

MacroTrends, Free Cash Flow. https://www.macrotrends.net/stocks/charts/NVDA/nvidia/free-cash-flow (Retrieved April 2026)

81.

42

Schwab, Market Outlook. https://www.schwab.com/learn/story/us-stock-market-outlook (Retrieved April 2026)

##### Works cited

NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2026, accessed April 23, 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026

nvda-20240128 - SEC.gov, accessed April 23, 2026, https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm

NVIDIA Announces Financial Results for First Quarter Fiscal 2026, accessed April 23, 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026

How AI Is Driving Revenue, Cutting Costs and Boosting Productivity for Every Industry in 2026 | NVIDIA Blog, accessed April 23, 2026, https://blogs.nvidia.com/blog/state-of-ai-report-2026/

NVIDIA Announces Financial Results for Third Quarter Fiscal 2025, accessed April 23, 2026, https://nvidianews.nvidia.com/_gallery/download_pdf/673e52d63d6332ce4bb72f56/

FORM 10-K NVIDIA CORPORATION, accessed April 23, 2026, https://s201.q4cdn.com/141608511/files/doc_financials/2025/q4/177440d5-3b32-4185-8cc8-95500a9dc783.pdf

nvda-20251026 - SEC.gov, accessed April 23, 2026, https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm

NVIDIA Announces Financial Results for Second Quarter Fiscal 2025 | NVDA Stock News, accessed April 23, 2026, https://www.stocktitan.net/news/NVDA/nvidia-announces-financial-results-for-second-quarter-fiscal-grc4w22riad8.html

NVIDIA Announces Financial Results for First Quarter Fiscal 2025, accessed April 23, 2026, https://nvidianews.nvidia.com/_gallery/download_pdf/664e53fe3d63322459a5eff6/

NVIDIA AI GPU Prices: H100 ($27K-$40K) & H200 ($315K/8-GPU) Cost Guide, accessed April 23, 2026, https://intuitionlabs.ai/articles/nvidia-ai-gpu-pricing-guide

DGX B200: The Foundation for Your AI Factory - NVIDIA, accessed April 23, 2026, https://www.nvidia.com/en-us/data-center/dgx-b200/

"Blackwell Sales Are Off the Charts" for Nvidia -- and Worryingly, so Is Its Customer Concentration | The Motley Fool, accessed April 23, 2026, https://www.fool.com/investing/2025/11/27/blackwell-off-charts-nvidia-customer-concentration/

Inside NVIDIA Blackwell Ultra: The Chip Powering the AI Factory Era, accessed April 23, 2026, https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/

NVIDIA Announces Financial Results for Second Quarter Fiscal 2026, accessed April 23, 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2026

NVIDIA AI GPU Market Share 2026: ~80% of AI Accelerators | Silicon Analysts, accessed April 23, 2026, https://siliconanalysts.com/analysis/nvidia-ai-accelerator-market-share-2024-2026

The Custom Silicon Inflection Point: Hyperscaler ASICs Challenge NVIDIA's GPU Dominance in 2026 - Introl, accessed April 23, 2026, https://introl.com/blog/custom-silicon-inflection-2026-hyperscaler-asics-nvidia-gpu

AMD's AI Deals Provide Visibility on Future Revenue Through 2027 | Investing.com, accessed April 23, 2026, https://www.investing.com/analysis/amds-ai-deals-provide-visibility-on-future-revenue-through-2027-200678987

Top 20+ AI Chip Makers: NVIDIA & Its Competitors - AIMultiple, accessed April 23, 2026, https://aimultiple.com/ai-chip-makers

From Pilot to Profit: Survey Reveals the Financial Services Industry Is Doubling Down on AI Investment and Open Source - NVIDIA Blog, accessed April 23, 2026, https://blogs.nvidia.com/blog/ai-in-financial-services-survey-2026/

NVIDIA CORP (NVDA) Earnings History & Surprises - ChartMill, accessed April 23, 2026, https://www.chartmill.com/stock/quote/NVDA/earnings

NVIDIA Announces Financial Results for Second Quarter Fiscal 2025, accessed April 23, 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2025

NVIDIA Announces Financial Results for Second Quarter Fiscal 2025 - SEC.gov, accessed April 23, 2026, https://www.sec.gov/Archives/edgar/data/1045810/000104581024000262/q2fy25pr.htm

NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2025, accessed April 23, 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2025

NVIDIA Announces Financial Results for Third Quarter Fiscal 2025, accessed April 23, 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2025

NVIDIA Announces Financial Results for Third Quarter Fiscal 2026, accessed April 23, 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2026

NVIDIA Corporation (NVDA) Earnings Call Transcripts - Discounting Cash Flows, accessed April 23, 2026, https://discountingcashflows.com/company/NVDA/transcripts/2026/1/

Broadcom vs. Nvidia: Are Investors Still Overpaying for AI Growth?, accessed April 23, 2026, https://www.tikr.com/blog/broadcom-vs-nvidia-are-investors-still-overpaying-for-ai-growth

NVIDIA Free Cash Flow 2012-2026 | NVDA - Macrotrends, accessed April 23, 2026, https://www.macrotrends.net/stocks/charts/NVDA/nvidia/free-cash-flow

NVIDIA Net Long-Term Debt 2012-2026 | NVDA - Macrotrends, accessed April 23, 2026, https://www.macrotrends.net/stocks/charts/NVDA/nvidia/net-long-term-debt

FORM 10-Q NVIDIA CORPORATION, accessed April 23, 2026, https://s201.q4cdn.com/141608511/files/doc_financials/2026/q2/2e217538-c226-4d05-8f74-aaca89a21b33.pdf

FORM 10-Q NVIDIA CORPORATION, accessed April 23, 2026, https://s201.q4cdn.com/141608511/files/doc_financials/2026/q3/13e6981b-95ed-4aac-a602-ebc5865d0590.pdf

Nvidia CEO begins stock sales under $865M plan - Mitrade, accessed April 23, 2026, https://www.mitrade.com/insights/shares-analysis/us-stocks/cryptopolitan-NVDA-202506241353

NVDA CEO Sells 225k Shares via 10b5-1, Retains 858M Stake | NVDA Insider Trading, accessed April 23, 2026, https://www.stocktitan.net/sec-filings/NVDA/form-4-nvidia-corp-insider-trading-activity-8095b2595117.html

Nvidia CEO sells $15M worth of stock as part of planned sale - Fox Business, accessed April 23, 2026, https://www.foxbusiness.com/markets/nvidia-ceo-sells-15m-worth-stock-part-planned-sale

Nvidia CEO Huang begins selling shares under $800 mln plan - Investing.com, accessed April 23, 2026, https://www.investing.com/news/stock-market-news/nvidia-ceo-huang-begins-selling-shares-under-800-mln-plan-4106919

NVDA CEO reports 10b5-1 plan sales; large indirect stakes listed - Stock Titan, accessed April 23, 2026, https://www.stocktitan.net/sec-filings/NVDA/form-4-nvidia-corp-insider-trading-activity-3aaac5bddbd1.html

Nvidia Earnings Strengthened by Analyst Upgrades | InsiderFinance, accessed April 23, 2026, https://www.insiderfinance.io/news/nvidia-earnings-strengthened-by-analyst-upgrades

Events & Presentations - NVIDIA Investor Relations, accessed April 23, 2026, https://investor.nvidia.com/events-and-presentations/events-and-presentations/default.aspx

Big Tech's AI expansion: From investment to scalable returns - RBC Wealth Management, accessed April 23, 2026, https://www.rbcwealthmanagement.com/en-us/insights/big-techs-ai-expansion-from-investment-to-scalable-returns

Big Tech's $650B AI Bet: Windfall for Nvidia, 'SaaS Apocalypse' Lurks - Velocity Meter, accessed April 23, 2026, https://www.velocitymeter.com/big-techs-650b-ai-bet-windfall-for-nvidia-saas-apocalypse-lurks/

Analyst says Nvidia's setup for 2026 is 'very strong,' expectations on Fed's December rate decision - YouTube, accessed April 23, 2026, https://www.youtube.com/watch?v=uvtTWGorfHE

2026 Outlook: U.S. Stocks and Economy | Charles Schwab, accessed April 23, 2026, https://www.schwab.com/learn/story/us-stock-market-outlook

NVIDIA (NVDA) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026, accessed April 23, 2026, https://public.com/stocks/nvda/forecast-price-target

What is the current Price Target and Forecast for NVIDIA (NVDA), accessed April 23, 2026, https://www.zacks.com/stock/research/NVDA/price-target-stock-forecast

NVIDIA Stock Is Up 18% in 10 Days. Is the Six-Month Consolidation Finally Over?, accessed April 23, 2026, https://www.tikr.com/blog/nvidia-stock-is-up-18-in-10-days-is-the-six-month-consolidation-finally-over

SA analyst upgrades/downgrades: NVDA, JNJ, KO, ACN | Seeking Alpha, accessed April 23, 2026, https://seekingalpha.com/news/4575264-sa-analyst-upgrades-downgrades-nvda-jnj-ko-acn

NVIDIA Corp. Outlook Revised To Positive On Stron | S&P Global Ratings, accessed April 23, 2026, https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3463383

Research Update: NVIDIA Corp. Outlook Revised To | S&P Global Ratings, accessed April 23, 2026, https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3463382

NVIDIA Ownership Pattern for Latest - Insider, Institutional, Mutual Fund shareholdings, accessed April 23, 2026, https://us.trendlyne.com/us/equity/ownership/1554267/NVDA/latest/nvidia-corp/

NVDA - NVIDIA Corporation Stock - Stock Price, Institutional Ownership, Shareholders (NasdaqGS) - Fintel, accessed April 23, 2026, https://fintel.io/so/us/nvda

NVDA - NVIDIA Corporation (NasdaqGS) - Share Price and News - Fintel, accessed April 23, 2026, https://fintel.io/s/us/nvda

NVDA Call Spread Buyers See 56.3% Gain as Stock Jumps on Quantum AI News: Technicals Remain Bullish Despite Slightly Bearish Skew - Market Chameleon, accessed April 23, 2026, https://marketchameleon.com/articles/b/2026/4/14/nvda-call-spread-buyers-56-3-percent-gain-quantum-ai-bullish-technicals-slightly-bearish-skew

Traders pile into call options as fear of missing out grows, according to Cboe - Morningstar, accessed April 23, 2026, https://www.morningstar.com/news/marketwatch/2026042139/traders-pile-into-call-options-as-fear-of-missing-out-grows-according-to-cboe

Huge, Unusual Trading in Nvidia Put Options - Investors Bullish on NVDA - Barchart, accessed April 23, 2026, https://www.barchart.com/story/news/824936/huge-unusual-trading-in-nvidia-put-options-investors-bullish-on-nvda

NVIDIA Corporation (NVDA) - Put-Call Ratio (Open Interest) (150-Day) - AlphaQuery, accessed April 23, 2026, https://www.alphaquery.com/stock/NVDA/volatility-option-statistics/150-day/put-call-ratio-oi

NVDA Volatility Skew Nvidia - Market Chameleon, accessed April 23, 2026, https://marketchameleon.com/Overview/NVDA/VolatilitySkew/

Two mystery customers made up 40% of Nvidia's revenue — who are they?, accessed April 23, 2026, https://m.economictimes.com/news/international/us/two-mystery-customers-made-up-40-of-nvidias-revenue-who-are-they/articleshow/123635412.cms

nvda-20260125 - SEC.gov, accessed April 23, 2026, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm

5 AI Stocks Beyond NVIDIA: Underrated Plays for 2026, accessed April 23, 2026, https://www.heygotrade.com/en/blog/5-ai-stocks-beyond-nvidia/

Prediction: The $700 Billion Artificial Intelligence (AI) Capex Boom Will Create the Best Buying Opportunity of 2026 for These 3 Stocks | The Motley Fool, accessed April 23, 2026, https://www.fool.com/investing/2026/04/02/prediction-the-700-billion-artificial-intelligence/

Artificial intelligence's long-term winners - Investment Outlook 2026 - UBP, accessed April 23, 2026, https://www.ubp.com/en/news-insights/newsroom/artificial-intelligence-s-long-term-winners-investment-outlook-2026

US Dollar's 2026 Decline: More Cyclical Than Structural | Investing.com, accessed April 23, 2026, https://www.investing.com/analysis/us-dollars-2026-decline-more-cyclical-than-structural-200675481

Navigating Rate Risks: How Bonds Are Better Positioned In 2025 | J.P. Morgan, accessed April 23, 2026, https://www.jpmorgan.com/insights/markets/top-market-takeaways/tmt-navigating-rate-risks-how-bonds-are-better-positioned-in-2025

AVGO vs NVDA — Stock Comparison 2026 | AllInvestView, accessed April 23, 2026, https://www.allinvestview.com/compare/AVGO-vs-NVDA/

NVDA EV/EBITDA - NVIDIA Corp - Alpha Spread, accessed April 23, 2026, https://www.alphaspread.com/security/nasdaq/nvda/relative-valuation/ratio/enterprise-value-to-ebitda

NVDA, MU Top Broadcom Stock on Price & Potential - Trefis, accessed April 23, 2026, https://www.trefis.com/stock/avgo/articles2/595444/nvda-mu-top-broadcom-stock-on-price-potential/2026-04-01

The Macro Implications of the AI Capex Boom - Bridgewater Associates, accessed April 23, 2026, https://www.bridgewater.com/research-and-insights/the-macro-implications-of-the-ai-capex-boom

NVIDIA Corporation Common Stock (NVDA) SEC Filings - Nasdaq, accessed April 23, 2026, https://www.nasdaq.com/market-activity/stocks/nvda/sec-filings

nvda-20250727 - SEC.gov, accessed April 23, 2026, https://www.sec.gov/Archives/edgar/data/1045810/000104581025000209/nvda-20250727.htm

NVIDIA CORP SEC 10-K Report - TradingView, accessed April 23, 2026, https://www.tradingview.com/news/tradingview:602edbd315060:0-nvidia-corp-sec-10-k-report/

NVIDIA Stock (NVDA) Opinions on AI Partnerships and Infrastructure Deals, accessed April 23, 2026, https://www.quiverquant.com/news/NVIDIA+Stock+%28NVDA%29+Opinions+on+AI+Partnerships+and+Infrastructure+Deals
