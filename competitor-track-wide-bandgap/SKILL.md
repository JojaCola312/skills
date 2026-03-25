---
name: competitor-track-wide-bandgap
description: "Track competitor companies in the wide-bandgap semiconductor ecosystem when the user says '竞争跟踪' or 'competitor track', especially their conference participation, new products, roadmap signals, partnerships, fab or capacity news, and other competitive intelligence."
---

# Competitor Track: Wide-Bandgap Semiconductor

Use this skill when the user says `竞争跟踪` or `competitor track`, or asks to track competitor companies in the wide-bandgap / third-generation semiconductor field.

## Scope

Track competitor signals related to:

- conference participation
- keynote, booth, sponsorship, exhibition, tutorial, or paper appearances
- new product releases
- product roadmap updates
- design-win and customer announcements
- partnerships, MOU, and ecosystem cooperation
- fab, expansion, capacity, and manufacturing updates
- financing, acquisitions, strategic investment, and major personnel changes

Priority technical areas:

- SiC
- GaN
- Ga2O3
- AlN
- ultra-wide-bandgap semiconductors
- power semiconductors and power devices
- related epitaxy, substrates, modules, and packaging

## Mandatory Search Rule

On every invocation, do all of the following:

1. Search recent web results using current-year and next-year queries in both Chinese and English
2. Search every company and URL listed in `references/mandatory-companies.md`
3. Search every event site listed in `references/mandatory-conference-sites.md`

Do not skip the mandatory lists just because broad search results already look sufficient.

## Source Priority

Prefer sources in this order:

1. Official company website
2. Official company newsroom / investor relations / product page
3. Official conference website or official exhibitor/sponsor page
4. Official government, exchange, university, or park announcement
5. Reliable media or industry report quoting the official source

If sources disagree, prefer the highest-priority source and note the discrepancy.

## Search Workflow

### Step 1: Broad recent search

Use recent queries around the current year and next year. Mix Chinese and English. Include combinations such as:

- `SiC company new product 2026 official`
- `GaN company conference 2026 official`
- `wide bandgap semiconductor company booth summit 2026`
- `第三代半导体 企业 新产品 2026`
- `碳化硅 公司 会议 2026`
- `氮化镓 企业 发布 2026`

### Step 2: Mandatory company sweep

Open or search the URLs in `references/mandatory-companies.md`.

For each company:

- check homepage, news, product, and event/exhibition pages when available
- capture newly announced products, conference attendance, partnerships, expansion, and major updates
- prefer primary pages over reposted media summaries

### Step 3: Mandatory conference sweep

Open or search the URLs in `references/mandatory-conference-sites.md`.

For each required event:

- check exhibitor, sponsor, speaker, agenda, and partner pages
- search for tracked competitors appearing as sponsors, exhibitors, speakers, or paper authors
- capture conference-side evidence even if the company site has not yet posted a recap

### Step 4: Normalize and deduplicate

Merge duplicate signals that describe the same event, product, or announcement.

Keep:

- the highest-confidence primary source
- conference-side proof if it materially strengthens the evidence

### Step 5: Output in the required structure

Follow `references/output-format.md` exactly.

## Coverage Rules

- Default output language is Chinese unless the user asks otherwise.
- Separate updates by `会议动向`, `产品动向`, and `其他竞争情报`.
- If there is no verified update for a mandatory company, keep it in `持续跟踪名单`.
- If a broader company announcement is not clearly relevant to the wide-bandgap business, exclude it.
- If a product page exists but key specifications are missing, mark unknown fields as `待确认`.

## Quality Rules

- Every signal must include at least one source link. Prefer official links.
- State the last verification date explicitly.
- If a field cannot be verified, write `待确认` rather than guessing.
- Keep date format consistent: `YYYY-MM-DD` or `YYYY-MM`.
- Distinguish between `已确认` and `高概率但待确认`.

## References

- Output schema and formatting rules: `references/output-format.md`
- Mandatory competitor list: `references/mandatory-companies.md`
- Mandatory conference list: `references/mandatory-conference-sites.md`
