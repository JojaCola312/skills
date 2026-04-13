# Collection Rules

Use this file to decide what to compile across the semiconductor industry, how to keep the conference pool broad but still relevant, and how to avoid drifting into generic tech-event noise.

## Collection Goal

Build a semiconductor-industry conference pool that is useful for long-term maintenance, not just a short list of near-term meetings.

The output should therefore include:

- confirmed upcoming conferences
- recently held conferences that still matter for follow-up
- recurring conference families whose next edition is not yet announced
- partially verified but relevant meetings that should already enter the maintained pool

Do not optimize for brevity. Optimize for pool completeness under a controlled semiconductor-industry boundary.

Domestic China conference completeness is the target. Do not add overseas conferences unless the user explicitly asks for them.

## Retrieval Order

Every run should follow this order:

1. check `seed-conference-families.md`
2. sweep `mandatory-sites.md`
3. run recent and near-term searches
4. run adjacent-source searches
5. add truly new conference families not already present in the seed pool
6. produce a seed-family audit status table before finalizing the run

Do not start from generic web search alone.

Multi-hop review rule:

- do not treat the first reachable page as the final evidence page
- for each priority source family, check at least:
  - one entry page
  - one relevant section or listing page
  - one concrete detail page
- if the checked page only contains navigation, cards, banners, or list summaries, the review is not complete
- do not use a homepage-only read to decide that a conference family has no update
- for major exhibitions, umbrella conferences, and platform-style annual events, confirm the parent event before deciding that sub-events are sufficient
- if a source mostly returns concurrent forums or topical sessions, run an extra parent-event search before treating the family as covered
- if priority URLs and normal search attempts still fail to return usable evidence, switch to Chrome DevTools MCP browser search if available
- in that fallback path, search with Bing first because it is often more reachable from restricted network environments
- do not stop at the Bing results page; open the most relevant result pages and continue the same entry-page -> section-page -> detail-page review logic
- use browser fallback selectively for unresolved seed families rather than for the entire pool

Interpretation:

- `seed-conference-families.md` defines the base pool that should persist
- mandatory-source and web search are used to update the base pool, find new stable anchors, and add confirmed additions
- search is not the authority for whether a seed family exists; it is the authority for whether there is new public evidence

Role split:

- `seed-conference-families.md`: conference objects that should persist in the ledger
- `mandatory-sites.md`: source families that must be checked every run mainly to discover new conferences and new reusable anchors

Do not duplicate conference-family definitions inside `mandatory-sites.md`.

## Parent Event Priority Rule

For large exhibitions, umbrella conferences, and platform-style annual events:

1. confirm the parent event first
2. create the parent-event ledger entry first
3. then add concurrent forums, topical sessions, or sub-events that have independent tracking value
4. do not treat sub-event coverage as equivalent to parent-event coverage

Examples:

- `SEMICON China` is a parent event; `CSTIC` and other concurrent forums are sub-events
- `慕尼黑上海光博会` is a parent event; topic forums under it are sub-events
- `高交会亚洲半导体与集成电路产业展` is a parent event; concurrent topic forums under it are sub-events

## Main Pool Versus Tracking List Rule

`Main Pool` and `Tracking List` are status categories, not geography categories.

That means:

1. do not treat `Tracking List` as an overseas or international bucket
2. do not move a China-based event into `Tracking List` merely because the title contains `international`, `IEEE`, `Asia`, or other global branding
3. if an event is held in China and is sufficiently verified, keep it in `Main Pool`
4. use `Tracking List` only when the next edition is unconfirmed, the evidence is weak, or key fields remain unresolved after the required search attempts

## Seed-Family Audit Rule

Every seed family must have an explicit per-run status.

Required status values:

- `已核验`
- `多轮搜索未命中`
- `仅弱证据`
- `待人工确认`

For each seed family, record:

- standard family name
- whether a priority URL existed
- search status
- search terms actually used this round
- export destination:
  - `国内会议`
  - `持续跟踪名单`

Completion rule:

- do not finish a run if any seed family has no recorded status
- if the output does not include seed-family totals and unresolved family names, the run is incomplete
- token usage, context pressure, or model latency are not valid reasons to skip unchecked seed families
- if the run cannot complete all seed-family checks, explicitly output it as an incomplete run rather than converting partial collection results into a final report
- when a seed family is assigned to `Main Pool` or `Tracking List`, create the output entry immediately rather than deferring it to a later consolidation pass
- before finalizing the run, review the audit table row by row and verify that every destination-marked family exists in the corresponding output section
- compare destination counts against actual output counts; if the counts differ, the run is incomplete

## Scope Boundary

### Tier A: Always include

Include these when verified:

- semiconductor and integrated-circuit conferences
- third-generation semiconductor conferences
- wide-bandgap semiconductor conferences
- SiC conferences
- GaN conferences
- Ga2O3 / AlN / ultra-wide-bandgap conferences
- compound semiconductor conferences
- power semiconductor and power device conferences
- semiconductor manufacturing conferences
- packaging, testing, materials, reliability, and failure-analysis conferences
- major semiconductor exhibitions and industry summits

### Tier B: Include when clearly relevant

These are broader adjacent events and should be included only when at least one of the conditions below is satisfied:

- the event materially serves the semiconductor supply chain or application ecosystem
- the agenda includes semiconductor materials, devices, packaging, testing, reliability, manufacturing, or application-side tracks
- the event is a recurring industry platform that the target workbook clearly treats as part of the tracking pool
- the event is a major exhibition, summit, or forum where semiconductors are a substantive part of the agenda, exhibitor mix, or论坛结构

Typical examples:

- advanced packaging conferences
- power module packaging and silver/copper sintering events
- semiconductor materials and metrology forums
- reliability and failure-analysis workshops
- automotive electronics and e-mobility power-device events
- major semiconductor exhibitions with semiconductor zones or forums
- packaging, thermal, or module-assembly events that clearly serve semiconductor industrialization
- application-side conferences where semiconductors are central to system performance

### Tier C: Exclude by default

Do not include these unless the semiconductor-industry link is explicit and strong:

- generic integrated-circuit investment forums
- broad AI chip or digital chip events with no power-device or material relevance
- general electronics exhibitions with no semiconductor depth
- purely optoelectronics events with no semiconductor-device or materials relevance
- talent fairs, policy briefings, or award ceremonies that are not conference-style industry events

## Search Window

Every run must cover two windows:

### Window 1: Recent and near-term search

Search:

- current year
- next year
- latest 3 to 6 months of published notices and recaps

Purpose:

- catch newly announced conferences
- update dates, venues, agendas, and registration status

### Window 2: Conference-pool completion search

Search for:

- recurring conference families already seen in prior runs
- meetings that appear in the maintained workbook pattern even if not extremely recent
- recently concluded events that should still stay in the pool for annual tracking

Purpose:

- avoid a narrow “only upcoming meetings” list
- keep the tracking pool structurally complete

### Window 3: Adjacent-source sweep

Search for relevant items from:

- organizer and association WeChat articles
- registration platforms
- invitation posters
- event aggregation pages
- industry media pages that quote organizer notices

Purpose:

- catch domestic and mid-sized events that do not maintain strong official sites
- avoid under-collecting because only “website-grade” sources were searched

## Domestic-First Bias

When time or context is limited, stay within domestic coverage rather than expanding overseas coverage.

That means:

- check domestic seed families first
- check domestic organizer, association, and WeChat source families first
- prefer collecting more domestic relevant entries over polishing a small number of flagship events
- do not let polished large-event domains crowd out lower-polish but relevant domestic events

## Seed Pool Retention Rule

Seed families are persistent ledger entries, not disposable search hits.

Therefore:

- if a seed family has fresh evidence this round, update it in the main pool
- if a seed family has no fresh evidence this round but remains active or plausible, keep it in the output
- if only a prior edition can be confirmed, keep it in `持续跟踪名单`
- only remove a seed family when there is positive evidence that it is discontinued, renamed into another family, or no longer belongs in the semiconductor conference pool

Export consequence:

- every seed family must map to exactly one export destination in each run:
  - `国内会议`
  - `持续跟踪名单`
- no seed family may silently disappear during workbook generation
- if evidence is too weak for the main pool, demote it to `持续跟踪名单` instead of dropping it

Do not silently drop a seed family just because this round's public results are sparse.

## Search Strategy

Use both English and Chinese searches. Mix semiconductor topic terms, format terms, and year terms.

For seed-family recovery, use `precision first, abstraction later`.

That means:

1. exact standard family name
2. exact numbered-title variant
3. exact abbreviation or branded short name
4. only then broader topic combinations

Do not begin no-URL seed recovery with stripped-down bag-of-words queries if the family name itself is already specific enough to search directly.

### Core topic terms

- wide bandgap semiconductor
- third generation semiconductor
- semiconductor
- integrated circuit
- SiC
- GaN
- Ga2O3
- AlN
- compound semiconductor
- power semiconductor
- power device
- semiconductor packaging
- semiconductor test
- semiconductor materials
- semiconductor reliability
- semiconductor manufacturing

### Broader-but-allowed extension terms

- advanced packaging
- power module packaging
- semiconductor packaging
- advanced assembly
- thermal management
- reliability
- failure analysis
- materials
- metrology
- automotive electronics
- e-mobility
- module
- inverter
- charger
- traction
- exhibition
- summit
- forum
- workshop
- developer forum
- user conference

### Useful Chinese query patterns

- `宽禁带半导体 会议 2026`
- `第三代半导体 论坛 2026`
- `半导体 会议 2026`
- `集成电路 论坛 2026`
- `碳化硅 氮化镓 会议 2026`
- `化合物半导体 大会 2026`
- `功率半导体 展会 2026`
- `先进封装 会议 半导体 2026`
- `半导体 可靠性 失效分析 会议 2026`
- `半导体 材料 检测 论坛 2026`
- `功率模块 封装 会议 2026`
- `碳化硅 论坛 邀请函`
- `氮化镓 开发者论坛`
- `第三代半导体 展会 2026`
- `化合物半导体 论坛 公众号`
- `宽禁带半导体 论坛 邀请函`
- `第三代半导体 大会 报名`
- `碳化硅 氮化镓 峰会 公众号`
- `半导体 封装 可靠性 公众号 会议`
- `半导体 材料 检测 公众号 论坛`
- `功率半导体 展会 深圳 武汉 苏州 上海`

## Source Priority

Prefer sources in this order:

1. official conference site
2. official organizer / host / sponsoring society page
3. official exhibition or registration page
4. official government / university / lab / park announcement
5. reliable industry-media or organizer-operated article that clearly points to the event

For many domestic events, official information may first appear in:

- organizer WeChat articles
- event mini-program pages
- registration platforms
- industry-association notices

These may be used when a standalone official site does not exist. Do not reject a domestic event only because it lacks an English-style official conference website.

Acceptable first-pass evidence for domestic events includes:

- official or organizer WeChat article
- organizer or association event notice
- registration page
- invitation poster or conference notice with verifiable organizer information

Do not require all events to have a standalone official website before entering the pool.

Long-term source-pool restriction:

- do not keep questionnaire pages, office-doc pages, short-link landing pages, or poster-only links as persistent source-pool entries
- these weak pages may be used as one-off supporting evidence in a run, but they should not become mandatory long-term source families
- do not treat an official-looking topic page as a forced source if, in practice, it mostly acts as a registration carrier, event-operation page, or repost container rather than a stable primary organizer source
- do not keep event-system subdomains or single-event registration hosts as persistent source-pool entries when they usually expire after the event closes

## Mandatory Source Sweep

Every run must do both:

1. broad recent search
2. required-site sweep using `mandatory-sites.md`

Do not skip the mandatory sweep even if the broad search already returns enough items.

Mandatory-source review must follow a multi-hop path whenever the site structure allows it.

Default path:

1. open the source-family entry page
2. open the most relevant section page, such as:
   - conference / forum / event
   - 同期活动 / 活动一览
   - program / agenda / schedule
   - news / notice / update
3. open at least one concrete detail page that contains a conference announcement, agenda, registration notice, or organizer update

Completion rule:

- if only the entry page was checked, the source review is incomplete
- if a section page exists but no detail page was opened, do not treat that source family as fully checked
- for large exhibition and organizer domains, prefer the event-list or concurrent-event branch over the homepage

When a seed family has no usable official site for the current edition, search by:

- conference family name + 公众号
- conference family name + 报名
- conference family name + 通知
- conference family name + 邀请函
- conference family name + 议程

Retry rule for no-URL seed families:

1. exact family name or exact known title variant + year
2. exact family name + edition / session number + year
3. short name / abbreviation + edition / session number + year
4. family name + organizer / topic / host-city variant

Only after at least 2 to 3 keyword variants fail may the family be marked as `多轮搜索未命中` or `待人工确认`.

Precision-first query rule:

- do not start with an over-abstracted keyword if the seed family already contains a more exact conference name
- keep distinctive tokens such as:
  - ordinal markers: `第十九届`, `第二十届`
  - fixed abbreviations: `APCSCRM`, `CSPT`, `CSTIC`, `MEMS`
  - branded family names: `湾芯展`, `行家说三代半`
  - host-city qualifiers when they are part of the stable family expression
- if the family is clearly a numbered recurring event, search the numbered form first and only broaden later
- do not drop `全国`, `国际`, `先进封装`, `晶体生长与材料`, `微纳`, `功率半导体` and similar distinctive tokens too early

Example:

- preferred:
  - `第二十届全国晶体生长与材料学术会议 2026`
  - `全国晶体生长与材料学术会议 第二十届 2026`
  - `晶体生长与材料学术会议 2026`
- avoid using only:
  - `全国晶体生长与材料 学术会议 2026`

Purpose of the search layers:

- mandatory-source review: discover new conference families and recover new reusable anchors from expected source families
- web search: find missing updates, alternate pages, and new conference families
- both together should expand and maintain the seed pool rather than replace it

Operational rule:

- do not let mandatory-source review replace seed-family tracking
- if a seed family already exists, its presence in the output should be governed by the seed pool first
- use mandatory-source review mainly to enrich the seed pool with newly found conference families, stronger organizer pages, and new stable page anchors
- never stop at "enough collected items" while unchecked seed families still remain

Important source-pool repair rule:

- when a major exhibition or organizer domain has a dedicated `同期活动`, `论坛一览`, `program`, or topic-event index page, treat that page family as a first-class source rather than relying only on the homepage
- this applies especially to `SEMICON China`, society annual-event pages, and official topic-conference portals

Examples of acceptable multi-hop confirmation:

- `semiconchina.org` homepage -> concurrent-event / summit / forum index -> concrete forum page
- society homepage -> conference list / annual-event page -> concrete conference notice
- organizer portal -> semiconductor channel -> article or event detail page

## Normalization Rules

- Merge duplicate mentions of the same conference family.
- Prefer the current-edition official page when available.
- If the next edition is not announced, keep the event in `持续跟踪名单`.
- Keep one record per conference edition, not one record per article.
- When multiple sources disagree, keep the higher-confidence value and mention the unresolved point in `检索说明`.

## Ordering Rule

Within `国内会议`, sort entries by date in ascending order.

This is a hard requirement for both:

- the text response
- any generated workbook / Excel ledger

Do not leave entries in retrieval order, source order, seed order, or relevance order after the main pool is assembled.

Sorting guidance:

- use the start date when exact range is available
- use the known month when only month-level precision is available
- put `待确认` dates after all dated entries
- for already-ended events, still sort by their actual event date rather than pushing them to the top arbitrarily

Date interpretation order:

1. exact start date
2. exact end date if the range is partially known
3. month-level date
4. year-level date
5. `待确认`

Excel / workbook rule:

- sort the main conference sheet by `起止日期` ascending before export
- if separate sheets exist, sort the main domestic sheet by `起止日期` ascending
- if there is one combined main sheet, sort the full main pool chronologically
- `持续跟踪名单` may remain grouped logically, but the main conference pool must be chronological

The ledger should read like a chronological pipeline, not a random search dump.

## Minimum Inclusion Threshold

An event may enter the main pool if all of the following are true:

1. the event name is identifiable
2. at least one reliable source is available
3. semiconductor-industry relevance is direct, high, or valid extended relevance
4. at least one core fact is known beyond the name, such as date, location, organizer, or event type

If these conditions are met, include the item even when some fields remain `待确认`.

Seed families should be held to an even lower threshold:

- if the family match is clear and at least one current or recent source exists, keep it in the pool
- if only the prior edition is confirmed, move it to `持续跟踪名单` rather than omitting it
- if no current-edition source is found after required retries, keep the family in `持续跟踪名单` and surface it in the audit list instead of silently downgrading it to vague `待确认`

## Completeness Rules

- Do not output only “major confirmed meetings”.
- List all collected meetings that pass the inclusion threshold.
- Use concise field values instead of dropping an event because the dossier is not rich enough.
- If the same event only has limited information, keep it in the main section with `待确认` fields rather than silently omitting it.
- Reserve `持续跟踪名单` for conference families whose next edition is not yet confirmed, not for every partially filled entry.
- Seed families that are still active should almost never disappear from the output entirely.
- `待确认` is allowed only for specific fields or for seed families that already completed the required search retries.

## Prioritization Rule For Presentation

After building the full pool, highlight two subsets for quick reading:

1. high-relevance entries
2. near-term entries

High-relevance entries usually include:

- third-generation semiconductor
- compound semiconductor
- SiC / GaN / Ga2O3 / AlN
- power semiconductor / power device
- semiconductor packaging, materials, testing, reliability, or manufacturing events with direct strategic value

Near-term entries usually include:

- events happening within the next 90 days
- events currently open for registration, call for papers, sponsorship, or agenda release
- events not yet held and still operationally actionable for attendance, submission, exhibition, or follow-up

Near-term entries should exclude:

- events already closed or already held, unless the user explicitly asks for retrospective summary
- events whose only recent signal is a post-event recap

If an event has already ended, it may stay in the main pool, but it should not be highlighted in `临近会议`.

Do not let prioritization shrink the pool. Highlight first, then still output the full pool.

## Output Intent

The response should behave more like a maintained semiconductor conference ledger than a pure narrative report.

That means the output should favor:

- full-pool coverage
- domestic coverage completeness
- standardized fields
- explicit source channels
- stable date and location formatting
- repeatable inclusion logic

Use the structure in `output-format.md`.
