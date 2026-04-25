---
title: Planet Labs PBC (PL)
type: entity
tags: [ticker-report, gemini-deep-research, entity, space_tech, pl]
category: space_tech
ticker: PL
related:
  - entities/ticker-watchlist.md
maturity: validated
report_source: gemini-deep-research
report_date: 2026-04-24
created: 2026-04-24
updated: 2026-04-24
---

## Relations

- @entities/ticker-watchlist.md — parent watchlist page

## Raw Concept

- **Ticker**: PL
- **Category**: space_tech
- **Report source**: Gemini Deep Research (user-commissioned template)
- **Report date**: 2026-04-24
- **Original file**: research for cemini/PL 3_24.docx (moved from inbox)
- **Template sections**: Business Overview · Competitive Landscape · Financial Profile · Recent Events · Forward Catalysts · Analyst & Sell-Side Context
- **Maturity**: validated (institutional-grade template; content reflects author/model synthesis as of report date)

## Narrative

*Full Gemini Deep Research report follows, preserved verbatim. Headings demoted by one level so page TOC is consistent.*

## Comprehensive Equity Research Report: Planet Labs PBC (NYSE: PL)

### 1. Business Overview

Planet Labs PBC (NYSE: PL) represents a profound paradigm shift within the aerospace and geospatial intelligence sectors. Founded on the premise that the Earth should be monitored continuously rather than photographed intermittently, the company operates at the convergence of space infrastructure, global data commercialization, and advanced artificial intelligence. Planet’s operational architecture is fundamentally different from legacy aerospace contractors; it functions less as a manufacturer of bespoke orbital hardware and more as an omnipresent, data-as-a-service (DaaS) and analytics-as-a-service (AaaS) platform.

At the nucleus of Planet’s value proposition is its proprietary "line-scanner" methodology. The company operates a constellation of approximately 200 Earth-imaging satellites, universally recognized as the largest operational fleet in human history.1 Unlike traditional "point-and-shoot" architectures—where a satellite is manually tasked to capture a specific coordinate at a specific time—Planet’s constellation maintains an always-on posture. The fleet captures a high-frequency, daily scan of the entire global landmass.1 This persistent temporal resolution generates an unparalleled, continuously updating database of planetary change, establishing a deep historical archive that serves as the ultimate training ground for machine learning algorithms.1

The transition from a raw pixel provider to an AI-enabled analytics vendor represents the most material and margin-accretive shift in Planet's fundamental business model. The company's vast data repositories are now certified as 100% machine-learning ready.1 Furthermore, Planet is aggressively pushing compute capabilities to the "edge"—in this case, outer space. By deploying NVIDIA Jetson Orin modules for real-time, on-orbit object detection and partnering with Alphabet’s Google on Project SunCatcher to deploy Tensor Processing Units (TPUs) in orbit, Planet is systematically eliminating the traditional bottlenecks of satellite telemetry.3 Processing data on-orbit reduces the massive bandwidth required to downlink raw optical imagery to ground stations, delivering structured tactical insights directly to end-users with near-zero latency.3

#### Revenue Segments and Geographic Exposure

Planet categorizes its revenue generation into three primary verticals, reflecting a deliberate strategic pivot toward high-reliability, sovereign-backed contracts while incubating highly scalable commercial use cases. Based on the latest primary 10-Q and 10-K filings, the segment breakdown highlights a business increasingly anchored by government demand.5

Defense and Intelligence (D&I): This segment is the paramount growth engine for the enterprise, accounting for 52% of total revenue over the first nine months of fiscal 2026, and demonstrating accelerating momentum by capturing 54% of revenue in the third quarter of fiscal 2026.5 For the three months ended October 31, 2025, D&I contributed $49.4 million, representing an aggressive growth trajectory compared to the $28.5 million generated in the prior year period.6 Driven by escalating geopolitical instability, the modernization of defense spending across NATO, and the proliferation of asymmetric warfare tactics requiring continuous pattern-of-life monitoring, the D&I segment is buoyed by massive secular tailwinds.2 The company’s growth here is punctuated by high-profile, sticky contract awards. Notably, Planet secured a multi-year, low nine-figure agreement with the Swedish Armed Forces to deliver rapid space-based data for peace and security operations.2 Additional critical anchors include multi-million dollar renewals with the National Reconnaissance Office (NRO) and a $12.8 million initial prime contract with the National Geospatial-Intelligence Agency (NGA) for AI-driven maritime domain awareness.2

Civil Government: Representing 31% of total revenue for the nine months ended October 31, 2025, the Civil Government segment captures demand from non-defense sovereign agencies focused on planetary management.5 Applications within this vertical are deeply embedded into long-term sovereign initiatives such as climate change monitoring, disaster response, urban planning, and agricultural yield tracking. High-visibility task orders, including a $13.5 million allocation from NASA to continue providing PlanetScope data for comprehensive Earth science missions, anchor the segment.2 This segment provides highly reliable recurring revenue, as sovereign entities increasingly recognize that purchasing commercial-off-the-shelf (COTS) satellite data is vastly more capital-efficient than launching and managing their own proprietary civil satellite networks.

Commercial: While the commercial segment accounts for a smaller relative share at 17% of total revenue for the first nine months of fiscal 2026, it serves as the ultimate frontier for Planet's total addressable market expansion.5 This segment encompasses verticals such as agriculture, finance, insurance, and energy infrastructure. The commercial sector serves as the primary testing ground for Planet's AI-enabled analytics. For example, the newly released Aircraft Detection Analytic Feed and the LUNO b program for maritime tracking are designed to be sold as high-margin data feeds to hedge funds tracking supply chains or insurance companies validating disaster claims.3

Geographically, Planet maintains a highly diversified and globally resilient footprint. For the quarter ended October 31, 2025, North America led revenue generation with $35.1 million.6 However, international penetration is accelerating rapidly. The Europe, Middle East, and Africa (EMEA) region generated $27.6 million, the Asia Pacific and Japan (APJ) region contributed $14.3 million, and Latin America (LATAM) accounted for $4.2 million.6 The robust 38% year-over-year revenue growth witnessed in the APJ and EMEA regions underscores the globally distributed nature of the geospatial intelligence demand curve and insulates the company from localized budgetary contractions.3

#### Monetization Mechanics and Unit Economics

To understand Planet Labs' valuation and cash flow trajectory, one must understand how the company actually makes money. Planet operates a subscription-based, recurring revenue model that mimics an enterprise Software-as-a-Service (SaaS) entity, overlaid onto a capital-intensive aerospace foundation.

The unit economics of the business are characterized by massive upfront capital expenditures (CapEx) to design, manufacture, and launch the satellite constellation. Once the orbital infrastructure is operational, however, the marginal cost of data replication and distribution drops to near zero. Because Planet's satellites are continuously scanning the Earth regardless of specific customer tasking, a single captured image can be monetized infinitely across different segments. An image of a coastal port can be sold simultaneously to a defense agency monitoring naval deployments, a hedge fund counting shipping containers, and a civil government assessing coastal erosion.

This "one-to-many" data distribution model allows gross margins to expand structurally as the customer base scales over a fixed orbital footprint. The efficacy of this model is evidenced by the company's exceptional retention metrics. Exiting fiscal year 2026, Planet reported that a staggering 98% of its Annual Contract Value (ACV) was recurring in nature.2 Furthermore, over 80% of its agreements are structured as annual or multi-year contracts, providing immense forward visibility into cash flows and stabilizing the lifetime value to customer acquisition cost (LTV/CAC) ratios.1 For the full fiscal year 2026, the non-GAAP gross margin expanded to 59%, illustrating the powerful margin accretion inherent in this high-operating-leverage model.2

#### Key Products and Market Positioning

Planet’s technology stack is stratified across multiple orbital assets and sophisticated software delivery platforms, designed to offer a complete ecosystem from data capture to algorithmic insight:

PlanetScope (Super Doves): This medium-resolution fleet forms the backbone of the constellation, providing the daily, global scanning capabilities that differentiate Planet from task-based competitors.3

Pelican Constellation: A next-generation fleet designed to breach the high-resolution market. Pelicans are engineered for rapid revisit, low-latency, and high-fidelity imaging. Pelican-3 recently delivered its first commercial images of Turin, Italy, while Pelican-4 successfully demonstrated the aforementioned onboard AI capabilities via NVIDIA hardware.3

Tanager Satellites: This represents Planet's foray into hyperspectral imaging. Tanager satellites are capable of detecting chemical signatures, identifying precise material compositions, and monitoring greenhouse gases like methane invisible to the naked eye.3 This is expected to unlock massive TAM in ESG compliance and industrial monitoring.

Planet Insights Platform: The software layer that aggregates, processes, and distributes this raw telemetry. The platform allows customers to apply proprietary algorithms or utilize Planet's out-of-the-box analytical tools to detect vessels, aircraft, and infrastructural changes automatically.7

### 2. Competitive Landscape

The global commercial satellite imaging market is experiencing explosive structural growth, projected to expand from $15.17 billion in 2025 to over $50.31 billion by 2035, compounding at an annual growth rate of 12.74%.12 Within this expanding total addressable market, Planet Labs operates in a highly contested but distinctly segmented arena, facing pressure from legacy defense primes, agile startups, and adjacent technology disruptors.

#### Primary Competitors and Market Share

The satellite-based Earth observation sector is highly concentrated at the top, driven by the massive capital barriers to entry required to establish orbital infrastructure. As of 2024, the top five players held a collective market share of 56.8%.13

Maxar Technologies: Maxar remains the undisputed legacy market leader, commanding an estimated 37.7% of the total market share in 2024.13 Maxar operates a traditional "point-and-shoot" model focused on ultra-high-resolution imagery (down to 30cm class). The company is deeply entrenched within the U.S. Department of Defense and the intelligence community, holding massive legacy contracts that provide immense revenue stability.

Airbus Defence and Space: Operating as a massive European conglomerate, Airbus controls significant portions of the high-resolution optical and synthetic aperture radar (SAR) markets.12 Backed by European sovereign interests, Airbus is a formidable competitor for international defense contracts.

BlackSky Technology & Satellogic: These entities represent direct competitors to Planet within the low-earth orbit (LEO) small-satellite space. BlackSky focuses heavily on high-revisit tactical intelligence and AI-driven analytics, directly targeting Planet's defense segment.12 Satellogic competes aggressively on price, attempting to drive down the cost of sub-meter high-resolution electro-optical imaging.12

SAR Providers (ICEYE, Capella Space): These specialized entities utilize Synthetic Aperture Radar (SAR) rather than optical sensors. SAR technology can penetrate cloud cover, smoke, and operate effectively at night.12 This addresses a fundamental physical limitation of Planet's predominantly optical fleet, making SAR providers critical competitors for all-weather intelligence contracts.

#### Durable Moats vs. Contested Moats

Durable Moats: Planet's most impenetrable competitive moat is its proprietary historical data archive and its unmatched temporal frequency. Because Planet has been aggressively scanning the entire global landmass daily for years, it possesses a deeply cataloged, irreplicable time-series dataset. A well-capitalized new entrant could theoretically launch a competing fleet tomorrow, but they cannot retroactively capture the Earth as it looked five years ago.3 This historical baseline is critical for training machine learning models to detect subtle anomalies over time. Additionally, Planet's vertical integration serves as a structural moat. By designing and manufacturing satellites in-house—particularly with its newly expanded Berlin manufacturing facility—Planet achieves unparalleled agility and cost-efficiency in rapid prototyping, fleet replenishment, and technology iteration.3

Contested Moats: Spatial resolution remains a highly contested moat where Planet is playing catch-up. While Planet dominates temporal resolution (how frequently an image is taken), legacy providers like Maxar and Airbus have historically dominated spatial resolution (how clear and zoomed-in the image is). Planet is aggressively attempting to breach this high-resolution moat with its new Pelican constellation, aiming to provide sub-meter clarity.3 However, it faces an uphill battle displacing entrenched defense primes that rely on exquisite, ultra-high-resolution capabilities for critical targeting and intelligence gathering.

#### Threats from Adjacent Industries and Technology Shifts

The space economy is undergoing a violent structural restructuring driven by plummeting launch costs, proliferated LEO architectures, and the entrance of hyperscale cloud providers.15 The primary existential threat to Planet comes not just from direct optical satellite operators, but from adjacent technology shifts.

If a mega-constellation communications provider—such as SpaceX with its Starlink network or Amazon with Project Kuiper—decides to integrate optical sensors into their massive arrays, the supply of commoditized Earth imagery could flood the market, instantly collapsing raw data pricing power.15 Furthermore, the rise of edge computing in space is a double-edged sword. While Planet is actively pioneering this with Google and NVIDIA 3, the rapid commoditization of AI hardware implies that competitors will increasingly be able to process data on-orbit as well. To defend its position, Planet must ensure that its proprietary analytics algorithms and "data gravity" outpace the democratization of space-based compute infrastructure.

### 3. Financial Profile

The financial trajectory of Planet Labs over the trailing 36 months reflects the classic lifecycle of a capital-intensive, venture-backed space entity successfully crossing the chasm into a mature, cash-flowing enterprise software profile. The true inflection point occurred in fiscal year 2026, where massive top-line expansion began to reliably drop down to operating cash flow, validating the company's high fixed-cost, zero marginal-cost business model.

#### Last 8 Quarters Financial Performance

The table below delineates the company's financial progression over the last eight quarters. It is critical to note that the Net Margin and EPS figures are severely distorted by extreme non-cash revaluations of warrant liabilities.


| Fiscal Quarter | Revenue ($M) | GAAP EPS | Gross Margin | Operating Margin | Net Margin |
|---|---|---|---|---|---|
| Q4 FY26 (Jan 2026) | $86.82 | -$0.48 | 54.02% | N/A* | -174.71% |
| Q3 FY26 (Oct 2025) | $81.25 | -$0.19 | 58.02% | N/A* | -72.84% |
| Q2 FY26 (Jul 2025) | $73.39 | -$0.07 | 57.53% | N/A* | -31.51% |
| Q1 FY26 (Apr 2025) | $66.27 | -$0.04 | 56.06% | N/A* | -19.70% |
| Q4 FY25 (Jan 2025) | $61.55 | -$0.12 | 61.29% | N/A* | -56.45% |
| Q3 FY25 (Oct 2024) | $61.27 | -$0.07 | 62.30% | N/A* | -32.79% |
| Q2 FY25 (Jul 2024) | $61.09 | -$0.13 | 52.46% | N/A* | -63.93% |
| Q1 FY25 (Apr 2024) | $60.44 | -$0.10 | 53.33% | N/A* | -48.33% |


Sources: 16 (Note: Exact quarterly GAAP operating margins are not fully disaggregated in the provided snippets, though the Annual Operating Margin for FY26 closed at -30.84% 20, demonstrating significant sequential improvement from -76.92% in FY24 as overhead absorption accelerated.)

The catastrophic collapse of the Q4 FY26 net margin to -174.71% and the corresponding EPS plunge to -$0.48 are entirely decoupled from core operational degradation. As the stock surged over 1,000% in the preceding 12 months, the fair value of Planet's outstanding public and private warrants exploded mechanically. U.S. GAAP requires these liability-classified warrants to be marked-to-market each quarter. Consequently, Planet was forced to recognize a massive $161.4 million non-cash charge on the income statement during the fiscal year.2 Stripping out these derivative accounting mechanics reveals a fundamentally strengthening underlying business, evidenced by the company achieving its first-ever full fiscal year of Adjusted EBITDA profitability ($15.5 million).2

#### Last 3 Fiscal Years: Free Cash Flow, Net Debt, and Share Dilution

The operational inflection of the enterprise is most visible in the cash flow statement, where the company officially halted its cash burn.


| Fiscal Year | Free Cash Flow ($M) | Total Debt ($M) | Cash & Short-Term Inv. ($M) | Shares Outstanding (M) |
|---|---|---|---|---|
| FY 2026 | $52.90 | $462.48 | $640.10 | 322.65 |
| FY 2025 | -$65.85 | $21.61 | $118.05 | 302.42 |
| FY 2024 | -$96.92 | $24.93 | $83.87 | 296.71 |


Sources: 2

The generation of $52.9 million in positive Free Cash Flow in FY26 marks a watershed structural moment.2 This metric validates the "build once, sell infinitely" data model. The transition from heavy cash burn (-$96.9M in FY24) to robust cash generation ensures the company can theoretically self-fund future constellation replenishments and R&D pipelines without relying strictly on the highly dilutive equity raises that plague most space startups.

#### Capital Allocation: Buybacks, Dividends, and M&A

Given its positioning in the hyper-growth phase of the space supercycle, Planet does not currently issue dividends or conduct share repurchases.3 All generated operating capital is aggressively reinvested into research, development, and constellation expansion (CapEx for FY26 was approximately $83 million).21 From a Mergers and Acquisitions (M&A) perspective, Planet's strategy is focused on targeted capability acquisition rather than sheer market share aggregation. The recent acquisition of Bedrock Research was executed surgically to integrate specialized personnel and proprietary algorithms, accelerating Planet's in-house AI and national security remote sensing capabilities.3

#### Balance Sheet Health: Liquidity and Debt Maturity Wall

Planet's balance sheet is fortress-like for a company of its size and cash flow profile, effectively derisking the enterprise from a credit perspective. Exiting fiscal year 2026, the company held $640.1 million in cash, cash equivalents, and short-term investments, representing a 188% year-over-year increase in liquidity.2

Total debt surged to $462.48 million, a dramatic increase from the $21.61 million held in the prior year.21 This debt spike was driven entirely by a strategic capital structure event in September 2025, when Planet successfully priced a private offering of convertible senior notes. Initially marketed at $300 million, insatiable institutional demand allowed the company to upsize the offering twice, ultimately closing at $460 million.10 Crucially, these notes do not mature until October 15, 2030, meaning Planet faces absolutely no near-term debt maturity wall.10 Short-term liquidity remains exceptional, with the current ratio hovering near 1.7x, indicating that current assets are more than sufficient to cover operating liabilities.24

### 4. Recent Events (Last 12 Months)

#### Earnings Surprises and Financial Milestones

Planet's recent financial disclosures have been a study in extreme contrasts, heavily penalizing algorithmic traders who focus solely on headline GAAP metrics. For Q4 FY26, the company delivered a monumental top-line beat, printing $86.82 million in revenue against consensus expectations of $78.17 million (an 11.55% upside surprise).18 This capped off a record $307.7 million fiscal year, up 26% year-over-year.2

However, the headline GAAP EPS for Q4 came in at -$0.48, radically missing consensus estimates of -$0.05.18 As previously established, this -$0.43 magnitude miss was driven almost entirely by the structural accounting requirements of liability-classified warrants responding to a parabolic stock chart.2 Institutional investors largely ignored the EPS miss, focusing instead on the leading indicators of future cash flow: Remaining Performance Obligations (RPOs) surged 106% year-over-year to $852 million, and the total backlog exploded by 79% to eclipse $900 million.2

#### Product Launches, Strategic Shifts, and Restructurings

The trailing twelve months have been defined by an aggressive and highly successful operational pivot from raw optical data provision to in-orbit compute and AI analytics.

AI on Orbit Validation: The successful demonstration of the NVIDIA Jetson Orin module on the Pelican-4 satellite proved that complex AI models can operate in the harsh radiation environment of space.4 The module enabled real-time object detection with ~80% accuracy before the data ever reached the ground.4 This drastically reduces downlink bottlenecks and allows for immediate tipping-and-cueing of terrestrial defense assets.

Project SunCatcher: Planet formalized an R&D partnership with Google to explore the concept of "data centers in space".3 Specifically, the project targets the deployment of two prototype AI compute satellites powered by Google TPUs in early 2027, aimed at creating a scalable mesh network of orbital processing power.3

Analytic Feeds: The launch of the Aircraft Detection Analytic Feed marked the industry's first automated daily detection of commercial, private, and military aircraft on a global scale, immediately opening new avenues for hedge fund and intelligence monetization.7

Constellation Expansion: During the fiscal year, Planet successfully launched 40 satellites.23 Notably, the company published the "first light" images from its Pelican-3 satellite over Turin, Italy, proving the operational viability of its next-generation high-resolution architecture.10

#### Management Changes

Strategic realignment at the executive level indicates a deliberate maturation of the corporate governance structure. Thomas Murphy was promoted to General Counsel, and Trevor Hammond—a seasoned veteran who previously guided the company through its complex public listing—returned as Chief Communications Officer to streamline policy priorities and government affairs lobbying.26 At the board level, venture capital stalwart Heidi Roizen and public market expert Niccolo de Massi stepped down after seven and four years of service, respectively, signaling a shift away from early-stage venture governance toward mature public enterprise management.27

#### Regulatory and Legal Developments

The most pressing regulatory and legal mechanic currently impacting the stock's microstructure is the company's initiation of a forced warrant redemption. Planet exercised its contractual right to redeem all outstanding Public Warrants after the stock traded at or above $18.00 per share for 20 trading days within a 30-day period.28 Holders have until April 27, 2026, to exercise these warrants at a strike price of $11.50 per share.29 Warrants not exercised by this deadline will be forcibly voided and receive a nominal $0.01 redemption price.28 This event is actively clearing a massive capital structure overhang, which has contributed to acute near-term stock volatility and complex arbitrage shorting as holders lock in their spreads.29

### 5. Forward Catalysts (Next 6–12 Months)

#### Next Earnings Date and Consensus Expectations

Planet is slated to report Q1 FY2027 earnings on or around June 3, 2026.18 Management's guidance for the quarter is highly constructive, projecting revenue between $87 million and $91 million, which implies continued sequential growth and robust year-over-year expansion.2 Full-year FY2027 revenue is guided aggressively between $415 million and $440 million.2 However, Adjusted EBITDA for Q1 is expected to show a slight loss of $6 million to breakeven, primarily due to front-loaded strategic CapEx investments in AI infrastructure and an acceleration of satellite manufacturing at the Berlin facility to meet the $900 million backlog demand.30

#### Product Roadmap Items and Guidance Milestones

The operational roadmap over the next 6 to 12 months is dense with highly visible execution catalysts:

Tanager and Pelican Scaling: The aggressive scaling of the Pelican (high-resolution) and Tanager (hyperspectral) constellations out of the Berlin manufacturing facility will be heavily scrutinized.3 Successful deployment will directly dictate Planet's ability to steal lucrative defense market share from Maxar and Airbus in the contested sub-meter resolution sector.3

Project Owl Tech Demo: Late 2026 will see the launch of a critical technology demonstration for the next-generation "Owl" fleet—a one-meter class monitoring constellation with upgraded onboard compute capabilities designed to replace the legacy Super Doves.3

AI Monetization Validation: Investors will demand explicit uptake metrics regarding the LUNO b program and other AI-driven maritime and aviation analytics platforms during the Q1 and Q2 earnings calls to validate the transition to an Analytics-as-a-Service valuation model.3

#### Sector and Macro Events

Planet's stock acts as a high-beta proxy for two distinct macroeconomic vectors: global geopolitical instability and AI infrastructure build-outs.

Defense Spending & Geopolitics: Flashpoints such as the U.S. blockade of the Strait of Hormuz directly translate into heightened urgency for maritime domain awareness and pattern-of-life intelligence.4 As European nations dramatically increase defense budgets to meet or exceed NATO 2% GDP thresholds, Planet is exceptionally well-positioned to capture sovereign business, evidenced by its recent low nine-figure contract with the Swedish Armed Forces.2

Space Symposium 2026: Planet's prominent feature at the 2026 Space Symposium alongside massive defense primes like Palantir and L3Harris serves as a major validation catalyst, keeping the company in the crosshairs of federal procurement officers and institutional analysts.4

### 6. Analyst & Sell-Side Context

#### Current Consensus Rating, Price Target, and Range

The sell-side community is currently experiencing a massive dislocation in target pricing, reflecting the stock's rapid and violent transition from a speculative space hardware play to an AI-driven enterprise software valuation framework. The overall consensus rating from aggregate algorithmic platforms remains a muted "Hold" with an outdated average price target of $27.70.31 However, recent actions by top-tier Wall Street firms tell a drastically different, highly bullish story that is actively pricing in the AI premium.

#### Notable Upgrades and Downgrades

Trailing the stock's aggressive appreciation over the last six months, top-tier analysts have rushed to revise targets upward:

Needham (Ryan Koontz): Maintained a "Buy" rating and aggressively raised the price target to $40.00 on March 20, 2026, anchoring their thesis on the 79% backlog growth and the structural inflection to positive FCF.25

Cantor Fitzgerald (Colin Canfield) & Wedbush (Dan Ives): Both prominent technology desks issued $40.00 price targets with "Buy" or "Outperform" ratings in late March 2026, heavily emphasizing the NVIDIA AI on-orbit capabilities and the D&I segment explosion.32

Citigroup (John Godyn) & Morgan Stanley (Kristine Liwag): Raised target prices to $35.00, acknowledging the improved fundamental cash flow profile while remaining slightly more conservative on the multiple expansion.32

Goldman Sachs (Anthony Valentini): Represents the notable institutional bear, maintaining a "Neutral" rating with a deeply lagging $18.00 to $20.00 price target as of April 2026.25

#### Bull Case vs. Bear Case

The institutional debate surrounding Planet Labs is highly polarized.


| The Bull Case | The Bear Case |
|---|---|
| Impenetrable Visibility: A massive $900 million backlog growing at 79% YoY, coupled with 98% recurring ACV, provides unprecedented revenue visibility and downside fundamental support.2 | Priced for Perfection: Trading near 39x forward sales and a mathematical anomaly of 1,345x forward EV/EBITDA, the stock multiple leaves absolutely zero margin for execution error.4 |
| AI Edge Compute Monopoly: Strategic partnerships with Google (TPUs) and NVIDIA give Planet an insurmountable lead in low-latency, on-orbit data processing, effectively positioning them as the "AWS of space".3 | Customer Concentration: The top two customers account for roughly 26% of accounts receivable and over 26% of quarterly revenue, making the company highly vulnerable to shifting government budgets.5 |
| Margin Expansion Engine: As the capital-intensive constellation reaches optimal density, the zero marginal cost of software distribution will force gross margins sustainably above 60%, generating massive compounding FCF.2 | Heavy Insider Distribution: Consistent insider selling by the CEO and CFO near $35-$40 levels suggests management believes the stock is fully valued in the near term, generating a psychological overhang.33 |


### 7. Ownership & Positioning

The institutional ownership mechanics and derivative positioning of Planet Labs are currently displaying hallmarks of a highly volatile, momentum-driven market structure vulnerable to acute squeezes.

#### Top Institutional Holders and Position Changes

Institutional investors and hedge funds control approximately 41.71% of Planet's outstanding float.35 Top legacy holders include Alphabet Inc. (a strategic necessity given Project SunCatcher), BlackRock, D.E. Shaw, and the Canada Pension Plan Investment Board.37

Recent 13F filings reveal aggressive institutional accumulation as funds attempt to chase the stock's momentum. Oppenheimer & Co. boosted its position by 74.1%, acquiring over 851,000 shares, while Goldman Sachs (despite its bearish equity research arm) increased its internal holdings by 54.3%.35

Note regarding circumstantial data anomalies: A Schedule 13G/A filing from Vanguard Group on January 12, 2026, indicated it no longer beneficially owned any PL stock (0% ownership).28 However, careful analysis of the filing text explicitly denotes this as an "internal realignment" that disaggregated holdings among various Vanguard subsidiaries, rather than a wholesale liquidation of the asset.28

#### Insider Buying and Selling

Insider transaction activity has been definitively skewed toward heavy selling over the last 12 months, accelerating rapidly as the stock breached 52-week highs.

Ashley Johnson (CFO/President): On April 2, 2026, Johnson executed open-market sales of 200,000 shares at average prices between $34.75 and $35.22, netting roughly $7 million.33 Days later, she executed a non-cash transfer of 525,708 shares into a family trust.33 Following these maneuvers, she retains significant exposure via 1.36 million direct shares and 1.29 million unvested RSUs.33

Robert H. Schingler (Co-Founder): Executed a sale of 73,683 shares on April 6, 2026, at an average price of $35.07.34

An additional director sold roughly 50,000 shares on April 15, 2026, under a pre-arranged 10b5-1 trading plan.38

While this is standard wealth diversification practice for executives realizing gains after a 1,000% historic run, the sheer volume of equity distribution (~492,000 shares over a 90-day window) provides a stiff psychological headwind for retail momentum.4

#### Short Interest and Recent Trends

Short interest has been steadily climbing as value-oriented hedge funds attempt to fade the astronomical valuation multiples. As of the end of March 2026, total shares sold short eclipsed 41 million, up from 33.5 million in mid-December 2025.39 This represents a dense 14.5% to 15.1% of the total float.39 The total dollar volume sold short is now $1.15 billion.39 This elevated short interest creates systemic vulnerability to short-squeeze dynamics, particularly when combined with the forced execution of warrants that is actively clearing capital structure overhang.

#### Options Skew and Unusual Derivatives Activity

The derivatives market is actively pricing in explosive near-term convexity. Mid-April 2026 saw highly unusual options activity, with traders purchasing 28,645 call options in a single session—a 42% spike above normal volume baselines.34 The implied volatility (IV) on the calls relative to puts is inverted, with the Put-Call IV ratio near 1.02, indicating extreme demand for upside tail protection and speculative leverage.40 Open interest is heavily concentrated in the $40.00 and $42.00 strike calls for late April expirations, aligning exactly with the April 27th warrant redemption deadline.29 This structural dynamic—dealers hedging deep out-of-the-money calls alongside aggressive retail momentum and short covering—sets the stage for acute gamma squeezes.

### 8. Risks

Despite the fundamental cash flow inflection and the immense $900 million backlog, Planet Labs faces a gauntlet of structural, macroeconomic, and idiosyncratic risks that could rapidly compress its premium valuation.

#### Company-Specific Risks

Customer Concentration: The D&I and Civil Government segments are highly concentrated. Based on the 10-Q for the quarter ended October 31, 2025, one customer accounted for 22% of total accounts receivable, and another accounted for 12%.5 On a revenue basis for the nine months ended October 31, 2025, the top three customers accounted for 15%, 13%, and 10% of revenue, respectively.5 The loss of a single keystone contract—such as the NRO or NGA—would immediately derail the revenue trajectory and shatter the 98% recurring ACV narrative.

Execution Risk: Planet is attempting a difficult transition from medium-resolution ubiquity (Super Doves) to high-resolution precision (Pelican) and hyperspectral specialty (Tanager). Manufacturing delays at the Berlin facility, launch vehicle anomalies, or on-orbit calibration errors with these unproven next-generation platforms would severely impact the realization of the massive backlog.2

Litigation and Warrant Mechanics: The ongoing forced redemption of public warrants causes intense short-term dilution and technical selling pressure as arbitrageurs short the common stock against their unexercised warrants. Failure to navigate this capital structure event smoothly could trigger cascading liquidations.

#### Sector Risks

Orbital Congestion and Kessler Syndrome: Low Earth Orbit is becoming increasingly crowded. A collision event or the generation of excessive space debris could render specific orbital planes unusable, physically destroying Planet's revenue-generating infrastructure.

Launch Bottlenecks: While launch costs have fallen dramatically, the space industry's reliance on a concentrated oligopoly of launch providers (namely SpaceX) creates systemic bottleneck risk. If a primary launch vehicle is grounded due to an anomaly, Planet cannot replenish its decaying orbital assets.

#### Macro Sensitivities

Geopolitical Dependency: Ironically, global peace is a bearish indicator for Planet Labs. The company's exponential growth in the D&I sector relies heavily on elevated global threat levels, border disputes, and kinetic conflicts. A sudden stabilization in geopolitical hotspots (e.g., Ukraine, Taiwan, Middle East) could result in sweeping defense procurement austerity.2

Interest Rates and Discounting: As a company trading purely on terminal value and futuristic FCF projections, Planet's intrinsic valuation is hyper-sensitive to the risk-free rate. If inflation reignites and the Federal Reserve holds rates higher for longer, the discount mechanisms applied to Planet's out-year cash flows will mathematically crush its present value.

### 9. Valuation & Peer Context

Planet Labs presents one of the most complex valuation puzzles in the modern equity market. Traditional aerospace and defense multiples fail to capture its software-like gross margins, while traditional SaaS multiples fail to account for its massive hardware CapEx requirements.

#### Current Multiples vs. Sector Medians

The current valuation is severely stretched across every traditional metric, pricing in years of flawless operational execution.

Price-to-Sales (P/S): Planet currently trades at a staggering ~39x trailing sales.4 To contextualize this euphoria, the broader Professional Services industry average sits at 1.1x, and Planet's direct peer average is around 2.6x.42

Enterprise Value to EBITDA (EV/EBITDA): On a trailing twelve-month basis for the period ending January 2026, the EV/EBITDA multiple sits at a nonsensical -272.2x.43 Looking forward, Barchart analytics flagged a forward EV/EBITDA multiple of 1,345x.4 Compare this to the broader Industrials sector, where the median EV/EBITDA multiple is a grounded 6.4x.43

Discounted Cash Flow (DCF) Reality Check: Quantitative modeling platforms flag massive fundamental downside. A standard DCF model discounting projected free cash flow through 2035 yields an estimated intrinsic value of ~$2.21 per share.42 With the stock trading near $38 to $39, purely mechanical DCF models calculate the stock to be roughly 1,470% overvalued.4

#### Key Correlations

Planet's stock has entirely uncoupled from traditional industrial cohorts and is currently trading as a high-beta proxy for Artificial Intelligence infrastructure.

AI Capex Correlation: The stock trades in near lockstep with NVIDIA and Google product cycles. The announcements of Project SunCatcher (TPUs) and Pelican-4 (Jetson Orin) have effectively rebranded Planet as a "data-center-in-space" company, allowing it to command AI software multiples rather than satellite hardware multiples.3

Defense Procurement: There is a high positive correlation between Planet's stock and legislative approvals for U.S. and NATO defense budgets.2

Commodity Exposure: Planet holds tangential negative correlation to energy prices in a macro context; however, high oil prices (e.g., oil surging above $100/barrel due to Strait of Hormuz blockades) actually drive increased demand for Planet's maritime and pipeline monitoring analytics, providing a highly unique, counter-cyclical hedge.4

### 10. Sources

#### Primary Sources

5 SEC Form 10-Q (October 31, 2025), Planet Labs PBC. Retrieved April 24, 2026. https://www.sec.gov/Archives/edgar/data/1836833/000119312525314295/pl-20251031.htm

2 Planet Labs Investor Relations: Q4/FY26 Financial Results and Quarterly Data. Retrieved April 24, 2026. https://investors.planet.com/financials/quarterly-results/default.aspx/1000/

3 Motley Fool Earnings Call Transcript: Planet Labs Q3 2026. Retrieved April 24, 2026. https://www.fool.com/earnings/call-transcripts/2025/12/10/planet-labs-pl-q3-2026-earnings-call-transcript/

9 Morningstar Earnings Call Transcript: Planet Labs Q4 2026. Retrieved April 24, 2026. https://www.morningstar.com/stocks/xnys/pl/earnings-transcript

45 Planet Labs Investor Relations: Events and Presentations. Retrieved April 24, 2026. https://investors.planet.com/events-and-presentations/events/event-details/2026/Planet-Labs-PBC-Fiscal-Fourth-Quarter-and-Full-Year-2026-Earnings-Call/default.aspx

1 Planet Labs Investor Relations: Corporate Overview. Retrieved April 24, 2026. https://investors.planet.com/overview/default.aspx

23 Business Wire Press Release: Planet Reports Financial Results for Fourth Quarter and Full Fiscal Year 2026. Retrieved April 24, 2026. https://www.businesswire.com/news/home/20260319782110/en/Planet-Reports-Financial-Results-for-Fourth-Quarter-and-Full-Fiscal-Year-2026

26 Planet Pulse Corporate Blog: Strategic Additions to Our Board & Executive Team Members. Retrieved April 24, 2026. https://www.planet.com/pulse/guiding-planet-s-next-chapter-strategic-additions-to-our-board/

#### Secondary Coverage

24 StockTitan: Planet Labs SEC Filings and Financial Health Signals. Retrieved April 24, 2026. https://www.stocktitan.net/sec-filings/PL/

16 Macrotrends: Planet Labs PBC Revenue, Gross Margin, and Shares Outstanding. Retrieved April 24, 2026. https://www.macrotrends.net/stocks/charts/PL/planet-labs-pbc/revenue

6 TradingView News: Planet Labs PBC SEC 10-Q Report & FY26 Revenue. Retrieved April 24, 2026. https://www.tradingview.com/news/tradingview:b6027134929cf:0-planet-labs-pbc-sec-10-q-report/

50 Simply Wall St: Assessing Planet Labs Valuation. Retrieved April 24, 2026. https://simplywall.st/stocks/us/commercial-services/nyse-pl/planet-labs-pbc/news/assessing-planet-labs-pl-valuation-after-ai-on-satellite-bre

29 Quiver Quantitative: Planet Labs Warrant Redemption Mechanics and Institutional Holders. Retrieved April 24, 2026. https://www.quiverquant.com/news/Planet+Labs+jumps+as+investors+weigh+warrant-redemption+mechanics+and+recent+contract-driven+momentum

18 MarketBeat: Planet Labs Short Interest, Earnings, and Institutional Ownership. Retrieved April 24, 2026. https://www.marketbeat.com/stocks/NYSE/PL/short-interest/

37 Fintel: Planet Labs Institutional Ownership and Short Interest. Retrieved April 24, 2026. https://fintel.io/so/us/pl

12 Spherical Insights: Global Commercial Satellite Imaging Market Report (2026–2035). Retrieved April 24, 2026. https://www.sphericalinsights.com/blogs/top-25-companies-in-global-commercial-satellite-imaging-market-global-share-market-size-revenue-report-2026-2035

15 MLQ Research: The Space Economy Market Map and Planet Labs Shares Outstanding. Retrieved April 24, 2026. https://mlq.ai/research/the-space-economy-market-map-86-companies-across-11-subsectors/

30 Investing.com: Planet Labs EV to EBITDA LTM and Q4 2026 Results. Retrieved April 24, 2026. https://ng.investing.com/pro/NYSE:PL/explorer/ev_to_ebitda_ltm

4 Perplexity AI Finance: Planet Labs Valuation Multiples and Space Symposium Context. Retrieved April 24, 2026. https://www.perplexity.ai/finance/PL?comparing=PL,SNDR,FCN,ICFI,FC,CRAI

42 Sahm Capital: Is Planet Labs Share Surge Justified by Current Valuation Metrics? Retrieved April 24, 2026. https://www.sahmcapital.com/news/content/is-planet-labs-pl-share-surge-justified-by-its-current-valuation-metrics-2026-04-12

44 NYU Stern (Aswath Damodaran): Enterprise Value Multiples by Sector. Retrieved April 24, 2026. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html

10 Motley Fool: Why Planet Labs Stock Rocketed. Retrieved April 24, 2026. https://www.fool.com/investing/2025/09/12/why-planet-labs-stock-rocketed-almost-50-higher-th/

40 AlphaQuery: Planet Labs Volatility and Option Statistics. Retrieved April 24, 2026. https://www.alphaquery.com/stock/PL/volatility-option-statistics/20-day/put-call-iv-ratio

41 OptionCharts: Planet Labs Unusual Options Activity. Retrieved April 24, 2026. https://optioncharts.io/options/PL/unusual-options

13 Global Market Insights: Satellite-Based Earth Observation Market Size. Retrieved April 24, 2026. https://www.gminsights.com/industry-analysis/satellite-based-earth-observation-market

##### Works cited

Investor Relations - Planet Labs PBC, accessed April 24, 2026, https://investors.planet.com/overview/default.aspx

Financials - Quarterly Results - Planet Labs PBC, accessed April 24, 2026, https://investors.planet.com/financials/quarterly-results/default.aspx/1000/

Planet Labs (PL) Q3 2026 Earnings Call Transcript | The Motley Fool, accessed April 24, 2026, https://www.fool.com/earnings/call-transcripts/2025/12/10/planet-labs-pl-q3-2026-earnings-call-transcript/

Planet Labs PBC Stock Price: Quote, Forecast, Splits & News (PL) - Perplexity, accessed April 24, 2026, https://www.perplexity.ai/finance/PL?comparing=PL,SNDR,FCN,ICFI,FC,CRAI

10-Q - Planet Labs PBC - SEC.gov, accessed April 24, 2026, https://www.sec.gov/Archives/edgar/data/1836833/000119312525314295/pl-20251031.htm

Planet Labs PBC SEC 10-Q Report - TradingView, accessed April 24, 2026, https://www.tradingview.com/news/tradingview:b6027134929cf:0-planet-labs-pbc-sec-10-q-report/

fiscal 4q'26 - update, accessed April 24, 2026, https://s29.q4cdn.com/903184914/files/doc_earnings/2026/q4/presentation/Planet-Fiscal-4Q-26-Update-Presentation.pdf

Financials - Quarterly Results - Planet Labs PBC, accessed April 24, 2026, https://investors.planet.com/financials/quarterly-results/default.aspx

PL - Planet Labs PBC Class A Earnings Call Transcripts - Morningstar, accessed April 24, 2026, https://www.morningstar.com/stocks/xnys/pl/earnings-transcript

Why Planet Labs Stock Rocketed Almost 50% Higher This Week | The Motley Fool, accessed April 24, 2026, https://www.fool.com/investing/2025/09/12/why-planet-labs-stock-rocketed-almost-50-higher-th/

Planet Labs Delivers Record FY26 Revenue $307.7M, Backlog $900M, FY26 Adj. EBITDA $15.5M - TradingView, accessed April 24, 2026, https://www.tradingview.com/news/tradingview:709103f111d6b:0-planet-labs-delivers-record-fy26-revenue-307-7m-backlog-900m-fy26-adj-ebitda-15-5m/

Top 25 Companies in Global Commercial Satellite Imaging Market - Spherical Insights, accessed April 24, 2026, https://www.sphericalinsights.com/blogs/top-25-companies-in-global-commercial-satellite-imaging-market-global-share-market-size-revenue-report-2026-2035

Satellite-Based Earth Observation Market Size & Share 2025 - 2034, accessed April 24, 2026, https://www.gminsights.com/industry-analysis/satellite-based-earth-observation-market

Earth Observation Market Size, Share | Growth Report [2034] - Fortune Business Insights, accessed April 24, 2026, https://www.fortunebusinessinsights.com/earth-observation-market-114486

The Space Economy: Mapping 86 Companies Across 11 Subsectors - MLQ.ai, accessed April 24, 2026, https://mlq.ai/research/the-space-economy-market-map-86-companies-across-11-subsectors/

Planet Labs PBC Gross Margin 2021-2026 | PL - Macrotrends, accessed April 24, 2026, https://www.macrotrends.net/stocks/charts/PL/planet-labs-pbc/gross-margin

Planet Labs PBC Revenue 2021-2026 | PL - Macrotrends, accessed April 24, 2026, https://www.macrotrends.net/stocks/charts/PL/planet-labs-pbc/revenue

Planet Labs PBC (PL) Earnings Date and Reports 2026 - MarketBeat, accessed April 24, 2026, https://www.marketbeat.com/stocks/NYSE/PL/earnings/

Planet Labs PBC Net Profit Margin 2021-2026 | PL - Macrotrends, accessed April 24, 2026, https://www.macrotrends.net/stocks/charts/PL/planet-labs-pbc/profit-margins

Planet Labs PBC Operating Margin 2021-2026 | PL - Macrotrends, accessed April 24, 2026, https://www.macrotrends.net/stocks/charts/PL/planet-labs-pbc/operating-margin

PL - Planet Labs PBC Class A Key Metrics | Morningstar, accessed April 24, 2026, https://www.morningstar.com/stocks/xnys/pl/key-metrics

Planet Labs PBC Shares Outstanding | PL - MLQ.ai, accessed April 24, 2026, https://mlq.ai/stocks/PL/shares-outstanding/

Planet Reports Financial Results for Fourth Quarter and Full Fiscal Year 2026, accessed April 24, 2026, https://www.businesswire.com/news/home/20260319782110/en/Planet-Reports-Financial-Results-for-Fourth-Quarter-and-Full-Fiscal-Year-2026

PL Financials: Income Statement, Balance Sheet & Cash Flow | Planet Labs Pbc, accessed April 24, 2026, https://www.stocktitan.net/financials/PL/

Planet Labs to redeem all outstanding public warrants April 27 - Investing.com, accessed April 24, 2026, https://www.investing.com/news/company-news/planet-labs-to-redeem-all-outstanding-public-warrants-april-27-93CH-4585086

Planet Rings in 2025 by Welcoming Two New Executive Team Members, accessed April 24, 2026, https://www.planet.com/pulse/planet-rings-in-2025-by-welcoming-two-new-executive-team-members/

Guiding Planet's Next Chapter: Strategic Additions to Our Board, accessed April 24, 2026, https://www.planet.com/pulse/guiding-planet-s-next-chapter-strategic-additions-to-our-board/

PL SEC Filings - Planet Labs Pbc 10-K, 10-Q, 8-K Forms - Stock Titan, accessed April 24, 2026, https://www.stocktitan.net/sec-filings/PL/

Planet Labs jumps as investors focus on strong FY26 results and warrant clean-up, accessed April 24, 2026, https://www.quiverquant.com/news/Planet+Labs+jumps+as+investors+focus+on+strong+FY26+results+and+warrant+clean-up

Planet Labs Q4 2026 slides: first profitable year, backlog surges 79% - Investing.com, accessed April 24, 2026, https://www.investing.com/news/company-news/planet-labs-q4-2026-slides-first-profitable-year-backlog-surges-79-93CH-4572057

Planet Labs PBC (NYSE:PL) Sets New 12-Month High - What's Next? - MarketBeat, accessed April 24, 2026, https://www.marketbeat.com/instant-alerts/planet-labs-pbc-nysepl-sets-new-12-month-high-whats-next-2026-04-08/

Planet Labs jumps as investors weigh warrant-redemption mechanics and recent contract-driven momentum | Quiver Quantitative, accessed April 24, 2026, https://www.quiverquant.com/news/Planet+Labs+jumps+as+investors+weigh+warrant-redemption+mechanics+and+recent+contract-driven+momentum

Planet Labs CFO sells 200,000 company shares | PL Insider Trading - Stock Titan, accessed April 24, 2026, https://www.stocktitan.net/sec-filings/PL/form-4-planet-labs-pbc-insider-trading-activity-3bae97fde0bd.html

Planet Labs PBC Target of Unusually High Options Trading (NYSE:PL) - MarketBeat, accessed April 24, 2026, https://www.marketbeat.com/instant-alerts/planet-labs-pbc-target-of-unusually-high-options-trading-nysepl-2026-04-16/

Planet Labs PBC (NYSE:PL) Hits New 1-Year High - Here's Why - MarketBeat, accessed April 24, 2026, https://www.marketbeat.com/instant-alerts/planet-labs-pbc-nysepl-hits-new-1-year-high-heres-why-2026-04-16/

Planet Labs PBC (NYSE:PL) Hits New 1-Year High - What's Next? - MarketBeat, accessed April 24, 2026, https://www.marketbeat.com/instant-alerts/planet-labs-pbc-nysepl-hits-new-1-year-high-whats-next-2026-04-22/

PL - Planet Labs PBC Stock - Stock Price, Institutional Ownership, Shareholders (NYSE), accessed April 24, 2026, https://fintel.io/so/us/pl

Planet Labs director sells 36,500 shares in plan | PL Insider Trading - Stock Titan, accessed April 24, 2026, https://www.stocktitan.net/sec-filings/PL/form-4-planet-labs-pbc-insider-trading-activity-ed4dfd7757f8.html

Planet Labs PBC (PL) Short Interest & Short Float | Updated Apr 2026 - MarketBeat, accessed April 24, 2026, https://www.marketbeat.com/stocks/NYSE/PL/short-interest/

Planet Labs PBC (PL) - Put-Call Implied Volatility Ratio (20-Day) - AlphaQuery, accessed April 24, 2026, https://www.alphaquery.com/stock/PL/volatility-option-statistics/20-day/put-call-iv-ratio

PL: Planet Labs PBC Unusual Options - Optioncharts.io, accessed April 24, 2026, https://optioncharts.io/options/PL/unusual-options

Is Planet Labs (PL) Share Surge Justified By Its Current Valuation Metrics - Sahm Capital, accessed April 24, 2026, https://www.sahmcapital.com/news/content/is-planet-labs-pl-share-surge-justified-by-its-current-valuation-metrics-2026-04-12

Planet Labs PBC (NYSE:PL) EV/EBITDA - Investing.com NG, accessed April 24, 2026, https://ng.investing.com/pro/NYSE:PL/explorer/ev_to_ebitda_ltm

Enterprise Value Multiples by Sector (US) - NYU Stern, accessed April 24, 2026, https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html

Planet Labs PBC Fiscal Fourth Quarter and Full Year 2026 Earnings Call, accessed April 24, 2026, https://investors.planet.com/events-and-presentations/events/event-details/2026/Planet-Labs-PBC-Fiscal-Fourth-Quarter-and-Full-Year-2026-Earnings-Call/default.aspx

Events & Presentations - Planet Labs PBC, accessed April 24, 2026, https://investors.planet.com/events-and-presentations/default.aspx

Stock Info - Planet Labs PBC, accessed April 24, 2026, https://investors.planet.com/stock-info/default.aspx

Planet Labs PBC Free Cash Flow 2021-2026 | PL - Macrotrends, accessed April 24, 2026, https://www.macrotrends.net/stocks/charts/PL/planet-labs-pbc/free-cash-flow

Planet Labs PBC Shares Outstanding 2021-2026 | PL | MacroTrends, accessed April 24, 2026, https://www.macrotrends.net/stocks/charts/PL/planet-labs-pbc/shares-outstanding

Assessing Planet Labs (PL) Valuation After AI-On-Satellite Breakthrough And New Defense Contracts, accessed April 24, 2026, https://simplywall.st/stocks/us/commercial-services/nyse-pl/planet-labs-pbc/news/assessing-planet-labs-pl-valuation-after-ai-on-satellite-bre

PL - - Planet Labs PBC (NYSE) Stock - Earnings History - Fintel, accessed April 24, 2026, https://fintel.io/seps/us/pl
