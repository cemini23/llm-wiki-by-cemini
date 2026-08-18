---
title: OSINT4ALL GEOINT catalog
type: entity
tags: [osint4all, k241, geoint]
keywords: [GEOINT, maps, ADS-B, AIS, VIN, IoT, radio, weather, real-estate, start.me]
related:
  - entities/tools/osint4all.md
  - concepts/osint4all-catalog.md
  - sources/osint4all-startme-2026-08-18.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @entities/tools/osint4all.md — hub tool entity
- @concepts/osint4all-catalog.md — KEEP / CONTEXT / CAUTION filing rules
- @sources/osint4all-startme-2026-08-18.md — ingest source (K241)

## Raw Concept

OSINT4ALL **MAPS / GEO / FLIGHT / MARITIME / VIN / IoT / RADIO / WEATHER / REAL ESTATE** section dump (~190 links) filed as one catalog. Nested GEOINT start.me board noted; Insecam-class directories listed as CONTEXT/CAUTION and not visited.

## Narrative

Keep public maps, ADS-B, AIS (MarineTraffic et al.), OSM/Mapillary, FlightAware, VIN/plate lookups, weather, and real-estate **locators**. Mark COVID map relics, dead IoT directories, **EMPORIS** (shut 2023), and **Mozilla Location Service** (retired 2024) **DEAD-OUTDATED**. DigitalGlobe Discover stays KEEP as a Maxar-legacy satellite locator (re-probe if the URL 404s). The Ontario GiveSendGo donor My Map is **CONTEXT** (leak-derived PII; sibling Bloopbase slice is CAUTION on cyber-caution). Unauthorized webcam directories (Insecam, Opentopia, Camhacker, Nest Cam Directory, …) and default-router-login pages stay **CONTEXT/CAUTION** or **CAUTION** — rows exist so the board contents are visible; agents do not open those URLs. Official traffic/gov cams and licensed tourist networks stay KEEP.

**NESTED-HUB:** [GEOINT start.me](https://start.me/p/W1kDAj/geoint) (`W1kDAj`) — follow-on board; do not treat this page as a complete scrape of that hub.

## MAPS

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Google Maps | https://www.google.com/maps | — | KEEP | Primary basemap / street-view locator |
| Bing Maps | https://www.bing.com/maps | — | KEEP | Basemap + bird's-eye / Streetside locator |
| Yandex.Maps | https://yandex.com/maps/ | — | KEEP | Basemap strong for RU/CIS coverage |
| Generate a panorama | https://www.udeuschle.de/panoramas/makepanoramas_en.htm | — | KEEP | Panorama generator from DEM/viewpoint |
| Mapillary | https://www.mapillary.com/app/ | — | KEEP | Crowdsourced street-level imagery |
| Geonarra.com | https://www.geonarra.com/ | — | KEEP | Geo-narration / place storytelling maps |
| Waze | https://www.waze.com/live-map | — | KEEP | Live traffic / incident overlay |
| 百度地图 | https://map.baidu.com/ | — | KEEP | China basemap (Baidu) |
| DigitalGlobe | https://discover.digitalglobe.com/ | — | KEEP | Maxar-legacy satellite discovery locator — re-probe if URL 404s |
| MapQuest | https://www.mapquest.com/ | — | KEEP | Basemap / directions locator |
| OpenStreetMap | https://www.openstreetmap.org/ | — | KEEP | Open basemap + editable POI layer |
| Maps.descarteslabs.com | https://maps.descarteslabs.com/ | — | KEEP | Satellite analytics map viewer |
| ArcGIS Wildfire Map | https://www.arcgis.com/home/webmap/viewer.html?webmap=df8bcc10430f48878b01c96e907a1fc3#! | — | KEEP | Wildfire incident ArcGIS layer |
| Living Atlas of the World \| ArcGIS | https://livingatlas.arcgis.com/en/browse/ | — | KEEP | Esri curated global GIS layers |
| FIRMS | https://firms.modaps.eosdis.nasa.gov/map/ | — | KEEP | NASA active fire / thermal anomalies |
| COVID-19 Map | https://coronavirus.jhu.edu/map.html | — | DEAD-OUTDATED | COVID-19 map relic — no longer primary GEOINT |
| Ukraine Interactive map | https://liveuamap.com/ | — | KEEP | Conflict event map (Ukraine theatre) |
| Satellites.pro | https://satellites.pro/ | — | KEEP | Multi-provider satellite map viewer |
| Military bases around the world. - uMap | https://umap.openstreetmap.fr/en/map/military-bases-around-the-world_510207 | — | KEEP | OSM uMap of military installations |
| Wikimapia | http://wikimapia.org/ | — | KEEP | Crowdsourced annotated satellite map |
| Map of Syrian Civil War | https://syria.liveuamap.com/ | — | KEEP | Syria conflict live map |
| Radio Garden | http://radio.garden/search | — | KEEP | Geolocated radio station map |
| Windy | https://www.windy.com/-Webcams/webcams | — | KEEP | Weather + webcam layer |
| Gpx File Editor | https://gpx.studio/ | — | KEEP | GPX track editor / map |
| OALLEY | https://www.oalley.net/app/ | — | KEEP | Isochrone / catchment mapping |
| fgdc_gp_demos's public fiddles | https://jsfiddle.net/user/fgdc_gp_demos/fiddles/ | — | KEEP | FGDC geoprocessing demo fiddles |
| KartaView | https://kartaview.org/map/ | — | KEEP | Crowdsourced street imagery (OSM) |
| Google Map Search Engine | https://cse.google.com/cse?cx=013991603413798772546:mofb1uoaebi | — | KEEP | CSE over map-related sites |
| Power Plants in the United States | https://www.arcgis.com/apps/dashboards/201fc98c0d74482d8b3acb0c4cc47f16 | — | KEEP | US power-plant dashboard |
| UK Onshore Oil and Gas Activity | https://www.arcgis.com/apps/webappviewer/index.html?id=29c31fa4b00248418e545d222e57ddaa | — | KEEP | UK onshore oil/gas activity |
| Walmart Store Status | https://www.arcgis.com/apps/dashboards/4e573c79e1224081805165d25b4f33c7 | — | KEEP | Walmart store-status dashboard |
| MODIS Wildfire | https://www.arcgis.com/apps/dashboards/bf5df3a49a624521844a2e5e1ec7df05 | — | KEEP | MODIS wildfire dashboard |
| Earthquake Watch | https://www.arcgis.com/apps/dashboards/c8af9c5411814584b460cc87cb7c3780 | — | KEEP | Earthquake watch dashboard |
| InciWeb | https://inciweb.nwcg.gov/ | — | KEEP | US wildfire incident portal |
| Earth | https://earth.nullschool.net/#current | — | KEEP | Global wind/ocean/particle viz |
| US Labor Strike Map | https://www.google.com/maps/d/viewer?mid=1hE1nDR-Ff_sVgOS67IteJSxGZlvqIP3k | — | KEEP | US labor-strike My Map |
| Active Agency Map | https://www.google.com/maps/d/viewer?mid=1eYVDPh5itXq5acDT9b0BVeQwmESBa4cB | — | KEEP | Active-agency My Map |
| Ontario GiveSendGo Donors | https://www.google.com/maps/d/viewer?mid=1heAgrb9bDuk287yqseyvhZ7-U_kz64hM | — | CONTEXT | Leak-derived 2022 convoy donor map (DDoSecrets/GiveSendGo) — listed-only; do not operationalize |
| Live-action-map.com | https://www.live-action-map.com/ | — | KEEP | Live-action / event map aggregator |
| awesome-maps-ukraine | https://github.com/Symbian9/awesome-maps-ukraine | — | KEEP | Curated Ukraine maps list |
| Допомога | https://dopomoha.pl | — | KEEP | UA refugee aid map (Poland) |
| Ukraine Live Cams | https://nagix.github.io/ukraine-livecams | — | KEEP | Ukraine public live-cam map |
| Ukraine War Map/Heatmap | https://ruarq.github.io/ukraine-war-heatmap | — | KEEP | Ukraine war heatmap viz |
| Live map of London Underground trains | https://traintimes.org.uk/map/tube/ | — | KEEP | London Underground live train map |
| Livecorona.co.kr | https://livecorona.co.kr | — | DEAD-OUTDATED | COVID map relic — outdated Korea corona live map |
| TfL JamCams | https://www.tfljamcams.net | — | KEEP | TfL traffic JamCams |
| Cesium Stories | https://cesium.com/ion/stories/viewer/?id=8be6f99c-0d4c-46ce-91a3-313e3cac62fe | — | KEEP | Cesium 3D globe story viewer |

## GEO

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| GEOINT | https://start.me/p/W1kDAj/geoint | — | NESTED-HUB | Follow-on GEOINT start.me board — scrape/file separately; not mass-scraped here |
| GeoNames | https://www.geonames.org/ | — | KEEP | Gazetteer / place-name database |
| Geoseer.net | https://www.geoseer.net/ | — | KEEP | Geospatial dataset search |
| GeoINT Search | https://cse.google.com/cse?cx=015328649639895072395:sbv3zyxzmji#gsc.tab=0 | — | KEEP | GEOINT-focused Google CSE |
| GeoIP Tracker tool | https://shadowcrypt.net/tools/geoip | — | KEEP | IP→geo lookup tool |
| Earth Engine Dataset | https://developers.google.com/earth-engine/datasets/ | — | KEEP | Earth Engine public dataset catalog |
| GeoPlatform Portal | https://www.geoplatform.gov/ | — | KEEP | US federal geospatial portal |
| Inspire-geoportal.eu | http://www.inspire-geoportal.eu/ | — | KEEP | EU INSPIRE geoportal |
| FAO Map Catalog | https://data.apps.fao.org/map/catalog/srv/eng/catalog.search#/home | — | KEEP | FAO map/catalog search |
| Datacore-gn.unepgrid.ch | https://datacore-gn.unepgrid.ch/ | — | KEEP | UNEP GRID geodata hub |
| ISRIC Data Hub | https://data.isric.org/geonetwork/srv/eng/catalog.search#/home | — | KEEP | Soil / ISRIC geodata hub |
| geocreepy | http://www.geocreepy.com/ | — | KEEP | Social-media geolocation helper |
| US Crisis Monitor | https://acleddata.com/special-projects/us-crisis-monitor/ | — | KEEP | ACLED US crisis event monitor |
| Toronto Live | https://apps.esri.ca/torontolive/ | — | KEEP | Toronto live city ops map |
| Residential Fire Fatalities in Indiana | https://www.arcgis.com/apps/dashboards/4d1289ab105145a1b1f80c1ad3cf19fb | — | KEEP | Indiana residential fire fatalities |
| geoprotests API | https://rapidapi.com/gisfromscratch/api/geoprotests/ | — | KEEP | Geoprotests API (RapidAPI) |
| geoint-py | https://github.com/gisfromscratch/geoint-py | — | KEEP | Python GEOINT helper repo |

## FLIGHT TRACKER

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| FlightAirMap | https://www.flightairmap.com/ | — | KEEP | ADS-B / flight map viewer |
| ADS-B Exchange | https://globe.adsbexchange.com/ | — | KEEP | ADS-B Exchange live globe |
| Icarus.flights | https://icarus.flights/ | — | KEEP | Flight tracking / OSINT flight tool |
| FlightAware | https://flightaware.com/ | — | KEEP | Commercial flight tracking |
| Flightradar24 | https://www.flightradar24.com/ | — | KEEP | Live ADS-B / flight radar |
| Live Air Traffic Control | https://www.liveatc.net/ | — | KEEP | Live ATC audio feeds |
| Planespotters.net | https://www.planespotters.net/ | — | KEEP | Aircraft photos / registration |
| Skyscanner | https://www.skyscanner.com/ | — | KEEP | Flight schedule / fare locator (not ADS-B) |
| RadarBox | https://www.radarbox.com/ | — | KEEP | Flight tracking / radarbox |
| ICAO Civil and Military airspace SUASHP | https://www.arcgis.com/apps/webappviewer/index.html?id=5db021bcb221498f81be055b3e238bf8 | — | KEEP | ICAO civil/military airspace map |

## MARITIME

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Marine Traffic | https://www.marinetraffic.com/ | — | KEEP | AIS ship tracking (MarineTraffic) |
| VesselFinder | https://www.vesselfinder.com/ | — | KEEP | AIS vessel finder |
| FlightAirMap | https://www.flightairmap.com/ | — | KEEP | Flight/AIS map (also under FLIGHT TRACKER) |
| OSINT on the Ocean | https://wondersmithrae.medium.com/osint-on-the-ocean-maritime-intelligence-gathering-techniques-2ee39e554fe1 | — | KEEP | Maritime OSINT tradecraft article |
| ShipAIS.uk | https://shipais.uk/ | — | KEEP | UK AIS ship map |
| FleetMon | https://www.fleetmon.com/ | — | KEEP | AIS fleet monitoring |
| AIS Ships Map | https://www.shipfinder.com/Monitor/Index | — | KEEP | AIS ships map |
| Ais.boatnerd.com | https://ais.boatnerd.com/ | — | KEEP | Great Lakes AIS |
| Live Cruise Ship Tracker | https://www.livecruiseshiptracker.com/ | — | KEEP | Cruise-ship live tracker |
| ShippingExplorer | https://www.shippingexplorer.net/en/map | — | KEEP | Shipping map explorer |
| SUBMARINE TRACKER | https://www.marinevesseltraffic.com/submarine-vessels-tracking-map | — | KEEP | Submarine vessel traffic map |
| Maritime Awareness Project | https://map.nbr.org/interactivemap/ | — | KEEP | NBR maritime awareness map |
| Shipping Database | https://theshippingdatabase.com/ | — | KEEP | Shipping company/vessel DB |
| Crewlist.org.uk | https://www.crewlist.org.uk/#Data | — | KEEP | Historical crew lists (UK) |
| Live Piracy Map | https://www.icc-ccs.org/piracy-reporting-centre/live-piracy-map | — | KEEP | ICC live piracy map |
| Military Ship Tracker | https://www.marinevesseltraffic.com/2013/02/military-ship-track.html | — | KEEP | Military ship tracker |
| Container Tracking | http://container-tracking.org/ | — | KEEP | Container tracking aggregator |
| Container tracking | https://www.track-trace.com/container | — | KEEP | Track-Trace container lookup |
| Maersk Tracking | https://www.maersk.com/tracking/ | — | KEEP | Maersk container tracking |

## LICENSE PLATE / VIN / VEHICLE

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Plate Recognizer | https://platerecognizer.com/ | — | KEEP | ALPR / plate recognition API (commercial) |
| License Plates of the World | http://www.worldlicenseplates.com/ | — | KEEP | Worldwide plate design reference |
| VIN decoder | http://www.vindecoderz.com/ | — | KEEP | Public VIN decoder |
| Poctra.com | https://poctra.com/ | — | KEEP | Vehicle auction / VIN locator |
| FAXVIN | https://www.faxvin.com/ | — | KEEP | Public VIN history lookup |
| AutoCheck | https://www.autocheck.com/ | — | KEEP | Vehicle history (paywalled) |
| VIN Lookup | https://thatsthem.com/vin-lookup | — | KEEP | Public VIN people/vehicle lookup |
| VINCheck® | https://www.nicb.org/vincheck | — | KEEP | NICB VINCheck theft/export |
| Autogespot | https://www.autogespot.us/spots | — | KEEP | Spotted-car photo map |
| Nomerogram.ru | https://www.nomerogram.ru/ | — | KEEP | RU plate photo search |
| COSINT – OSINT on Cars | https://osintcurio.us/2021/02/17/cosint-osint-on-cars/ | — | KEEP | COSINT tradecraft article |
| 🚗License Plates in Canada 🇨🇦 | https://www.google.com/maps/d/viewer?mid=1zXYL2BF2MByEduLzYN5brVnli9J3cIlv | — | KEEP | Canada license-plate styles My Map |
| Carnet.ai | https://carnet.ai/ | — | KEEP | Vehicle make/model AI classifier |
| Car/Vehicle Model Recognition Online | https://carmodel.toolpie.com/ | — | KEEP | Online car-model recognition |
| Tools | https://intelx.io/tools?tab=vin | — | KEEP | IntelX VIN tools tab |
| VIN Check Reports | https://vincheck.info/check/vin-check.php | — | KEEP | Public VIN check reports |
| VIN Decoder | https://vindecoder.pl/ | — | KEEP | EU-oriented VIN decoder |
| autodna | https://www.autodna.com/ | — | KEEP | Vehicle history / VIN reports |
| VIN decoder | https://www.vindecoder.net/ | — | KEEP | Public VIN decoder |
| Orto.website | https://orto.website/ | — | KEEP | Vehicle/plate OSINT helper |
| Europlates.eu | https://www.europlates.eu/ | — | KEEP | European plate reference |
| How's My Driving NY | https://www.howsmydrivingny.nyc/ | — | KEEP | NYC plate → parking/ticket lookup |
| Deciphering Number Plates | https://www.skoda-storyboard.com/en/series/deciphering-number-plates/ | — | KEEP | Plate-decoding explainer |
| VIN Decoder & Lookup | https://driving-tests.org/vin-decoder/ | — | KEEP | Public VIN decoder & lookup |
| Check Any VIN | https://www.vehiclehistory.com/license-plate-search | — | KEEP | Plate/VIN history search |
| Partial Number Plate Search | https://www.partialnumberplate.co.uk/ | — | KEEP | UK partial plate search |
| License Plate Lookup | https://www.searchquarry.com/free-license-plate-number-lookup/ | — | KEEP | US plate lookup (ToS-gated) |
| Vehicle Enquiry | https://vehicleenquiry.service.gov.uk/?locale=en | — | KEEP | UK gov vehicle enquiry (official) |
| Number Plate Check | https://www.checkcardetails.co.uk/number-plate-check | — | KEEP | UK number-plate check |
| License Plate Lookup | https://findbyplate.com/ | — | KEEP | US plate → vehicle lookup |

## IoT

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Webcam Search Engine | https://cse.google.com/cse?cx=013991603413798772546:gjcdtyiytey#gsc.tab=0 | — | CONTEXT/CAUTION | CSE tuned for open webcams — can surface unauthorized streams |
| Insecam | http://www.insecam.org/ | — | CONTEXT/CAUTION | Unauthorized open-webcam directory — list only; do not visit |
| Camhacker.com | https://www.camhacker.com/ | — | CONTEXT/CAUTION | Unauthorized webcam directory — list only; do not visit |
| EarthCam | https://www.earthcam.com/ | — | KEEP | Licensed tourist/city webcam network |
| Airport Webcams | https://airportwebcams.net/ | — | KEEP | Airport webcam aggregator (public feeds) |
| The Webcam Network | http://www.the-webcam-network.com/ | — | DEAD-OUTDATED | Dead/outdated webcam network directory |
| Default Router Login | https://www.cleancss.com/router-default/ | — | CAUTION | Default router-login catalog — dual-use; do not use against third parties |
| Live Bar and Pub Webcams | http://gobefore.me/cams/ | — | CONTEXT/CAUTION | Bar/pub webcam aggregator — authorization unclear; do not visit for ops |
| Webcams Abroad live images | https://www.webcamsabroad.com/ | — | KEEP | Travel webcam gallery |
| WEBCAM LIVE | https://www.whatsupcams.com/en/ | — | KEEP | Public live webcam portal |
| city-webcams.com | https://city-webcams.com/ | — | KEEP | City webcam index |
| thingful | http://www.thingful.net/ | — | DEAD-OUTDATED | Dead IoT discovery directory — service long defunct |
| Live World Webcam | http://liveworldwebcam.net/ | — | CONTEXT/CAUTION | Webcam directory of uncertain authorization — list only |
| Live Cams \| Iplivecams | https://www.iplivecams.com/live-cams/ | — | CONTEXT/CAUTION | IP live-cam directory often aggregates unsecured streams — list only |
| Webcamtaxi | https://www.webcamtaxi.com/en/ | — | KEEP | Public webcam portal |
| Explorecams.com | https://explorecams.com/ | — | CONTEXT/CAUTION | Webcam explorer; may index unsecured cams — list only |
| C4-cams | http://c4-cams.qwazwsx.xyz/c4-cams/ | — | DEAD-OUTDATED | Dead/sketchy IoT cam directory host — ignore |
| Nest Cam Directory | https://www.nestcamdirectory.com/ | — | CONTEXT/CAUTION | Third-party Nest cam directory — unauthorized camera aggregation |
| Opentopia | http://www.opentopia.com/ | — | CONTEXT/CAUTION | Classic open-webcam directory — unauthorized; do not visit |
| WorldCam | https://worldcam.eu/ | — | KEEP | EU/world public webcam index |
| Hawaii Traffic Cameras | http://goakamai.org/home | — | KEEP | Hawaii official traffic cams |
| Honolulu Traffic Cams | http://www2.honolulu.gov/honolulumyway/?trafficcam | — | KEEP | Honolulu traffic cams (gov) |
| Lake County Fire Cameras | https://www.arcgis.com/apps/webappviewer/index.html?id=0f7aa08cc4b74fc6a0c4308d4eace6b3 | — | KEEP | Lake County fire cameras |
| VDOT Traffic Cams | https://www.arcgis.com/apps/dashboards/a0d3fb34cda44f5b8b10be1b245f24a3 | — | KEEP | VDOT traffic cams |
| Lubbock Live Traffic Cameras | https://www.arcgis.com/apps/webappviewer/index.html?id=affe50ac55824c7a8c757d3980787e31 | — | KEEP | Lubbock traffic cams |
| Hong Kong Traffic Data & Cams | https://www.arcgis.com/apps/dashboards/47be6372a0434beaba99ae9c9f1d598d | — | KEEP | Hong Kong traffic data & cams |
| Baton Rouge Traffic Cams | https://www.arcgis.com/apps/webappviewer/index.html?id=0ec05ffb0d2d4735a969e8f31f820a7b | — | KEEP | Baton Rouge traffic cams |
| Surveillance under Surveillance | https://sunders.uber.space/ | — | KEEP | Surveillance-camera map (SuS) |
| Ukraine Live Cams | https://nagix.github.io/ukraine-livecams/#5.5/47.774/31.685/0/45 | — | KEEP | Ukraine public live-cam map |
| Fisgonia | http://www.fisgonia.com/ | — | CONTEXT/CAUTION | Open-webcam directory — unauthorized; do not visit |

## [CAN] IOT

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| 511on.ca | https://511on.ca/ | — | KEEP | Ontario 511 traffic/cams |
| Toronto area Live Traffic Cams | https://gtaupdate.com/traffic/ | — | KEEP | GTA live traffic cams |
| Outage map | https://www.torontohydro.com/outage-map | — | KEEP | Toronto Hydro outage map |
| PlowTO | https://www.toronto.ca/services-payments/streets-parking-transportation/road-maintenance/winter-maintenance/plowto/ | — | KEEP | Toronto plow tracker |
| tpscalls.live | https://www.tpscalls.live/ | — | KEEP | Toronto Police calls live map |

## RADIO

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Broadcastify | https://www.broadcastify.com/listen/ | — | KEEP | Public safety radio streams |
| Calls Node Status | https://www.broadcastify.com/calls/status/ | — | KEEP | Broadcastify Calls node status |
| Free WiFi Search Engine | http://instabridge.com/free-wifi/ | — | KEEP | Public WiFi hotspot search |
| RadioReference | https://www.radioreference.com/apps/db/ | — | KEEP | Radio frequency database |
| Feeds.talonvoice.com | https://feeds.talonvoice.com/ | — | KEEP | Radio/voice feed aggregator |
| Automated transcription for radio stations | https://sonix.ai/radio-stations | — | KEEP | Radio-station transcription service |
| Scanmap | https://scanmap.mobi/ | — | KEEP | Scanner / radio map |
| WiGLE: Wireless Network Mapping | https://wigle.net/ | — | KEEP | Wireless network geolocation DB |
| Ham Radio QRZ Callsign Database Search | https://www.qrz.com/lookup | — | KEEP | Ham callsign database |
| Radio-Locator | https://radio-locator.com/ | — | KEEP | AM/FM station locator |
| Mozilla Location Service | https://location.services.mozilla.com/map#0.7/0/0 | — | DEAD-OUTDATED | MLS retired 2024 — ignore |
| RadioID Database | https://database.radioid.net/database/search#! | — | KEEP | DMR RadioID database |
| Radio-Sherlock | http://dxmaps.com/search.html | — | KEEP | HF/DX radio map search |
| Rfsearch.com | http://rfsearch.com/ | — | KEEP | RF search / spectrum helper |
| Radiocells.org | https://radiocells.org/ | — | KEEP | Open cell-tower database |
| @murph_live | https://twitter.com/murph_live | — | KEEP | Live radio/ops Twitter account |
| Wifispc.com | https://wifispc.com/ | — | KEEP | WiFi map / SPC locator |
| Wiman | https://www.wiman.me/ | — | KEEP | Public WiFi map |

## WEATHER

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| OpenWeatherMap | https://openweathermap.org/ | — | KEEP | Weather API / maps |
| Weather History & Data Archive | https://www.wunderground.com/history | — | KEEP | Weather history archive |
| World Temperatures — Weather Around The World | https://www.timeanddate.com/weather/ | — | KEEP | World temperature / weather |
| AccuWeather | https://www.accuweather.com | — | KEEP | Forecast / radar locator |

## REAL ESTATE

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| PrimeLocation | https://www.primelocation.com/ | — | KEEP | UK property listing locator |
| Realtor | https://www.realtor.com/ | — | KEEP | US property listing locator |
| EMPORIS | https://www.emporis.com/ | — | DEAD-OUTDATED | Building database shut 2023 — ignore |
| rehold | https://rehold.com/ | — | KEEP | Property / parcel locator |
| Zillow | https://www.zillow.com/ | — | KEEP | US real-estate locator (Zestimate) |
| Zillow Canada | https://www.zillow.com/z/canada/canada-homes/ | — | KEEP | Canada Zillow homes locator |
| Zoopla | https://www.zoopla.co.uk/ | — | KEEP | UK property listing locator |
| homemetry | https://homemetry.com/ | — | KEEP | Address / home metrics locator |
| Explore Canada's Real Estate Market | https://www.remax.ca/find-real-estate | — | KEEP | Canada RE/MAX listing locator |
| Onondaga County Home Sales | https://b2.caspio.com/dp.asp?AppKey=18321000d7j6h9j6c1i4e8f0i5a9 | — | KEEP | Onondaga County home-sales map |

## Counts

| Section | n |
|---------|---|
| MAPS | 47 |
| GEO | 17 |
| FLIGHT TRACKER | 10 |
| MARITIME | 19 |
| LICENSE PLATE / VIN / VEHICLE | 30 |
| IoT | 30 |
| [CAN] IOT | 5 |
| RADIO | 18 |
| WEATHER | 4 |
| REAL ESTATE | 10 |
| **Total rows** | **190** |

| Disposition | n |
|-------------|---|
| KEEP | 173 |
| NESTED-HUB | 1 |
| CONTEXT/CAUTION | 10 |
| CAUTION | 1 |
| DEAD-OUTDATED | 5 |

Source JSON: `.local/osint4all/groups/05-geoint.json` (n_links=190). Agents must not visit Insecam or other CONTEXT/CAUTION webcam directories.
