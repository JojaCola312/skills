---
name: competitor-track-semiconductor-industry
description: "Track domestic semiconductor competitors when the user says '竞争跟踪' or 'competitor track', especially their products, roadmap signals, partnerships, fab or capacity news, customer progress, and other competitive intelligence."
---

# Competitor Track: Domestic Semiconductor Industry

Use this skill when the user says `竞争跟踪` or `competitor track`, or asks to track competitor companies across the domestic semiconductor industry.

## Scope

Track competitor signals related to:

- new product releases
- product roadmap updates
- design-win and customer announcements
- partnerships, MOU, and ecosystem cooperation
- fab, expansion, capacity, and manufacturing updates
- financing, acquisitions, strategic investment, and major personnel changes

Priority technical areas:

- semiconductors and integrated circuits
- third-generation semiconductors
- power semiconductors and power devices
- substrates, epitaxy, modules, and packaging
- semiconductor materials, manufacturing, testing, and reliability
- automotive, energy, industrial, and other application-side semiconductor businesses

## Mandatory Search Rule

On every invocation, do all of the following:

1. Search recent web results using current-year and next-year queries in both Chinese and English
2. Search every company and URL listed in `references/mandatory-companies.md`

Do not skip the mandatory lists just because broad search results already look sufficient.

## Source Priority

Prefer sources in this order:

1. Official company website
2. Official company newsroom / investor relations / product page
3. Official government, exchange, university, park, or major partner announcement
4. Reliable media or industry report quoting the official source

If sources disagree, prefer the highest-priority source and note the discrepancy.

## Search Workflow

### Step 1: Broad recent search

Use recent queries around the current year and next year. Mix Chinese and English. Include combinations such as:

- `semiconductor company new product 2026 official`
- `power semiconductor company roadmap 2026 official`
- `domestic semiconductor company expansion 2026 official`
- `第三代半导体 企业 新产品 2026`
- `半导体 企业 扩产 2026`
- `半导体 企业 合作 客户 2026`

### Step 2: Mandatory company sweep

Open or search the URLs in `references/mandatory-companies.md`.

For each company:

- check homepage, news, product, solution, IR, and application pages when available
- use a multi-hop review path: entry page -> relevant section page -> concrete detail page
- capture newly announced products, roadmap updates, partnerships, customer progress, expansion, and major updates
- prefer primary pages over reposted media summaries

### Step 3: Normalize and deduplicate

Merge duplicate signals that describe the same event, product, or announcement.

Keep:

- the highest-confidence primary source
- government, exchange, park, or partner-side proof if it materially strengthens the evidence

### Step 4: Output in the required structure

Follow `references/output-format.md` exactly.

## Coverage Rules

- Default output language is Chinese unless the user asks otherwise.
- Separate updates by `产品动向`, `合作与客户`, `产能与资本动向`, and `其他竞争情报`.
- If there is no verified update for a mandatory company, keep it in `持续跟踪名单`.
- If a broader company announcement is not clearly relevant to semiconductor business, exclude it.
- If a product page exists but key specifications are missing, mark unknown fields as `待确认`.
- Do not use conference participation as a core collection dimension unless the user explicitly asks for it.

## Quality Rules

- Every signal must include at least one source link. Prefer official links.
- State the last verification date explicitly.
- If a field cannot be verified, write `待确认` rather than guessing.
- Keep date format consistent: `YYYY-MM-DD` or `YYYY-MM`.
- Distinguish between `已确认` and `高概率但待确认`.
- Do not stop at a homepage, news list, or category page. A company review is incomplete until at least one concrete detail page is opened.

## References

- Output schema and formatting rules: `references/output-format.md`
- Mandatory competitor list: `references/mandatory-companies.md`
