---
title: "Spaceshift SateAIs API — Self-Serve Satellite Imagery Analytics (Sentinel-1 SAR, Proprietary β, Free Tier 500 credits/mo)"
type: source
tags: [vendor-api, satellite-imagery, sar-data, sentinel-1, proprietary-saas, japan, tokyo, ship-detection, oil-spill-detection, building-detection, time-series-change-detection, gemini-dr-wave4-osint, dual-adopt-cemini-and-workflow]
keywords: [spaceshift, sateais, sateais-api, sentinel-1-sar, c-band-sar, ship-detection, oil-spill-detection, new-building-detection, time-series-change-detection, geojson-output, asynchronous-job-processing, console-spcsft-com, copernicus-sentinel-1, free-beta-tier, 500-credits-per-month, vessel-detection-future, crop-yield-forecasting-future, sorae-info, prtimes-jp]
clusters: [alt-data, infrastructure, geospatial]
related:
  - sources/gemini-dr-wave4b-osint-2026-04-29.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
maturity: validated
read_status: read-skim
created: 2026-04-30
updated: 2026-05-17
---

## Relations

- @sources/gemini-dr-wave4b-osint-2026-04-29.md — Wave 4B URL 14 Adopt-with-caveat; promoted to dedicated source 2026-04-30
- @concepts/wiki-tooling-evaluation.md — Wave 4 evaluation parent
- @concepts/ip-sale-readiness.md — **proprietary vendor SaaS**: client codebase has zero AGPL/SSPL/MIT-Family-C concerns since Cemini doesn't redistribute Spaceshift's analysis engine. API consumption terms apply but don't trigger copyleft mechanics in Cemini's client code. Clean for IP-sale.
- @concepts/high-signal-paper-patterns.md — rubric: vendor-API + β-stage + free-tier-only-pricing-known + closed-source-analysis = different shape than github-paper Adopts. Workflow A would never have surfaced this; it came via the user's curated Wave 4B brief (correctly).

## Raw Concept

- **Vendor**: Space Shift Inc. (株式会社スペースシフト) — Tokyo, Japan; founded 2009-12; CEO Naruo Kanamoto
- **Brand**: SateAIs™ (satellite × AI analytics)
- **Product URL**: https://console.spcsft.com/
- **Type**: Commercial REST API service (β release)
- **License**: **Proprietary** (subject to vendor API Terms of Service; not specified in evaluation; pre-deployment legal review recommended)
- **Pricing**: **Free β tier**: 500 credits/month, resets 1st of each month at 00:00 JST. Post-β pricing not yet announced.
- **β release date**: 2026-04-28 (per prtimes.jp + sorae.info press release)
- **Data source**: Copernicus **Sentinel-1 C-band SAR** (Synthetic Aperture Radar)
- **Output format**: **GeoJSON** geometries (parseable structured spatial data)
- **Processing model**: **Asynchronous job-based** — submit bounding-box request → API processes → result available
- **Discovered via**: Gemini DR Wave 4B 2026-04-29 (URL 14); promoted 2026-04-30
- **Read status**: read-skim (Exa-fetched press releases + Gemini brief evaluation)

## Narrative

### What it is

A **commercial REST API** that abstracts satellite imagery procurement, preprocessing, and ML-based detection into a unified self-serve endpoint. Submit a geographic bounding box; get a **GeoJSON array** of detected physical assets back asynchronously.

**Why SAR matters**: Sentinel-1 uses **C-band Synthetic Aperture Radar**, which observes Earth's surface **regardless of cloud cover or darkness**. Unlike optical satellite imagery (which fails at night and through clouds), SAR provides continuous all-weather observation. For Cemini's macro-event detection: critical because clouds frequently obscure the most-economically-relevant locations (typhoons, monsoons, winter at northern ports).

**Four detection modules** in the β release:
1. **Ship Detection** (vessel positioning across maritime areas)
2. **Oil Spill Detection**
3. **New Building Detection** (construction activity at infrastructure sites)
4. **Time-Series Change Monitoring** (any-pixel-changed flagging at designated locations)

Future modules (per Spaceshift roadmap): vessel detection (refined), crop-yield forecasting (from 2026 onward).

### Why Cemini-direct — the "physical macro signal" use case

This is the kind of dual-adopt the rubric likes. Per Gemini brief, both surfaces have integration vectors:

**Cemini production stack (✅ Adopt)**:
- A new Python FastMCP daemon `services/ingest/sateais_client.py` polls async jobs
- Parses GeoJSON → inserts spatial coordinates into PostgreSQL
- DeepSeek orchestrator gains awareness of **physical macroeconomic movements**: shipping-choke-point congestion (Suez, Hormuz, Malacca), agricultural yield anomalies, port construction at LNG terminals, oil-spill-driven commodity moves
- Free-tier 500 credits/month covers ~50,000 km² of analysis — enough for prototyping the Ship Detection + New Building Detection workflows on critical lanes

**Workflow (✅ Adopt)**:
- Claude Code can invoke the API directly via curl or short Python scripts during ad-hoc research
- Useful for ticker-specific physical-asset verification (e.g., investigating a corporation's claimed factory expansion → use New Building Detection on the announced site)

**Wiki/librarian server stack: ❌ Not relevant** — geographic data has no value to a Markdown-compilation-and-embedding server.

### Concrete first-experiment: shipping choke-point monitoring

**Pre-adoption operational test** (free tier, no commitment):
1. Sign up for SateAIs API at https://console.spcsft.com/ ~10 min
2. Use Ship Detection on the **Suez Canal southern entrance bounding box** for the past 7 days; cost ~5 credits
3. Compare output against publicly-reported shipping-tracker data (e.g., MarineTraffic spot-checks)
4. If accuracy is reasonable: brief to cemini-prod for `services/ingest/sateais_client.py` integration

This experiment establishes the **signal quality + integration cost** before any commitment to Spaceshift as a long-term data partner.

### Risks & open questions

1. **Asynchronous processing latency** [OPEN QUESTION 2026-04-30] — API documentation doesn't specify request → result latency. Per Gemini brief: "this data stream cannot be relied upon for sub-minute, high-frequency trading execution, but must rather be utilized to inform macro-level, directional positional trading strategies." Consistent with Cemini's macro-event-analysis-not-HFT positioning anyway.
2. **β-stage pricing lock-in risk** — post-β commercial pricing is unknown. Engineering investment in `services/ingest/sateais_client.py` may become sunk costs if the future paid tiers are economically prohibitive. **Mitigation**: build the integration to be vendor-pluggable so a swap to a competing satellite-API vendor (Sentinel Hub, Capella Space, ICEYE, etc.) is feasible.
3. **Sentinel-1 revisit rate** [CONFIRMED 2026-05-17 — with correction] — verified via ESA + NASA Earthdata (Exa 2026-05-17). Sentinel-1 is a two-satellite constellation (Sentinel-1A + Sentinel-1C, after 1B's 2021 failure and 1C's Dec-2024 launch restored the pair); each individual satellite has a 12-day repeat cycle, so the **constellation global revisit is ~6 days**. **Correction to the original claim**: at the equator the repeat frequency is ~3 days (not ~6) because of orbit convergence; main shipping routes and Europe are covered in under 3 days, and the Arctic in under 1 day. So the revisit cadence is *better* at the equator than the page originally stated. The operational takeaway is unchanged in direction: even ~3-day cadence is insufficient for sub-daily monitoring of fast-changing events (real-time oil spills), but it is adequate for Cemini's macro-directional use case (shipping-choke-point congestion, construction monitoring, agricultural anomalies).
4. **API documentation completeness** — Gemini brief flags incomplete documentation at retrieval time (April 29). Pre-integration: re-fetch docs at https://console.spcsft.com/ once accessible.
5. **Vendor concentration risk** — Spaceshift is a single small Japanese vendor. Geopolitical or business-continuity risks (acquisition, pivot, shutdown) could affect Cemini's data layer. Mitigated by the vendor-pluggable design pattern in (2).
6. **Japanese-language documentation** — much of the press material is Japanese. The English Spaceshift page (`spcsft.com/en/`) covers high-level brand framing; the API docs at `console.spcsft.com` should be checked for English availability. Translation overhead may slow integration.

### Cemini-side adoption assessment

**Decision: Adopt-with-pilot**. Run the Suez Canal experiment first; commit to integration only after free-tier validation.

Concrete next-steps:
1. **Sign up + retrieve API key** ~10 min
2. **Pre-deployment legal review** of vendor TOS (15 min): does the API license permit Cemini's algorithmic-trading use? (Spaceshift markets to "infrastructure management, disaster prevention, agriculture, environmental conservation" but doesn't explicitly mention algorithmic trading; check that the standard SaaS terms aren't carved out for it)
3. **Free-tier prototype experiment** — Suez Canal Ship Detection over 7 days (~5 credits)
4. **If signal quality is reasonable**: brief to cemini-prod for `services/ingest/sateais_client.py` integration
5. **Track post-β pricing announcement** — quarterly check-in on https://www.spcsft.com/

### Citation

> Space Shift Inc. (2026, April 28). *Press Release: Space Shift launches SateAIs™ API β version — self-serve satellite data analytics*. https://prtimes.jp/main/html/rd/p/000000085.000006437.html (English summary: https://www.spcsft.com/en/news-en/2721/)

## Snippets

> **The all-weather SAR advantage (from press release English summary)**:
>
> "Space Shift Inc. has officially launched SateAIs™, a new brand that systematizes and reorganizes the company's satellite-data analytics technologies into purpose-specific, user-selectable solution packages. … New 'Time-Series Change Detection AI' and 'Water Detection AI'." [Source: https://www.spcsft.com/en/news-en/2721/, retrieved 2026-04-30 via Exa]

> **Free β tier framing (translated from Japanese press release)**:
>
> "料金：無料。クレジット付与：月500クレジット（毎月1日0:00 JSTにリセット）。対応衛星：Sentinel-1（C-band SAR）。" / "Pricing: Free. Credit allocation: 500 credits per month (resets 1st of each month at 00:00 JST). Supported satellite: Sentinel-1 (C-band SAR)." [Source: https://prtimes.jp/main/html/rd/p/000000085.000006437.html, retrieved 2026-04-30 via Exa]

> **Cemini-stack integration vector (per Gemini DR brief)**:
>
> "The SateAIs endpoint will be instituted as a primary data source within the 24/7 ingestion layer (operating alongside existing feeds like Polygon, GDELT, and FRED). A new Python FastMCP daemon (e.g., services/ingest/sateais_client.py) will be engineered to poll the asynchronous API endpoints. Upon job completion, the daemon will parse the resulting GeoJSON geometries and insert the structured coordinate data into the PostgreSQL cluster. This spatial data will inform the DeepSeek orchestration brain regarding critical physical macroeconomic movements, such as congestion at global shipping choke points." [Source: another Link Evaluation for Trading and Wiki Stacks 4_29.docx URL 14 evaluation]
