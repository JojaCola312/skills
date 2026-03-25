---
name: conference-track-wide-bandgap
description: "Track wide-bandgap semiconductor conferences when the user says '会议跟踪' or 'conference track', or asks to monitor domestic/international conferences about third-generation semiconductors, wide-bandgap semiconductors, SiC, GaN, Ga2O3, AlN, power semiconductors, and related devices/materials."
---

# Conference Track: Wide-Bandgap Semiconductor

Use this skill when the user says `会议跟踪` or `conference track`, or asks to follow conferences in the wide-bandgap / third-generation semiconductor field.

## Scope

Track both:

- International conferences
- Domestic China conferences, forums, summits, and recurring industry meetings

Priority topics:

- SiC
- GaN
- Ga2O3
- AlN
- ultra-wide-bandgap semiconductors
- power semiconductors and power devices
- nitride semiconductors
- compound semiconductors when clearly relevant to the wide-bandgap domain

## Mandatory Search Rule

On every invocation, do both:

1. Search recent web results using current-year and next-year queries in both Chinese and English
2. Search every required site listed in `references/mandatory-sites.md`

Do not skip the mandatory site list just because recent search results already look sufficient.

## Source Priority

Prefer sources in this order:

1. Official conference website
2. Official organizer / host / sponsoring society page
3. Official government, university, or innovation-center announcement page
4. Reliable exhibitor or partner page quoting the official event page

If multiple sources disagree, prefer the higher-priority source and mention the discrepancy.

## Search Workflow

### Step 1: Broad recent search

Use recent queries around the current year and next year. Mix Chinese and English. Include terms such as:

- `wide bandgap semiconductor conference 2026`
- `third generation semiconductor forum 2026 China`
- `SiC conference 2026 official`
- `GaN conference 2026 official`
- `宽禁带半导体 会议 2026`
- `第三代半导体 论坛 2026`
- `碳化硅 氮化镓 会议 2026`

### Step 2: Mandatory site sweep

Open or search the URLs in `references/mandatory-sites.md`.

For each required site:

- check whether a new edition, call for papers, registration, agenda, or event recap is posted
- capture the latest available edition even if the event date is not near
- prefer pages that expose the next scheduled edition

### Step 3: Normalize and deduplicate

Merge duplicate mentions of the same conference.

Keep:

- official current edition page when available
- fallback organizer page if the next edition site is not live yet

### Step 4: Output in the required structure

Follow `references/output-format.md` exactly.

## Coverage Rules

- Default output language is Chinese unless the user asks otherwise.
- Always separate `国际会议` and `国内会议`.
- Include only conferences with clear relevance to wide-bandgap / third-generation semiconductors.
- If a conference is broader than wide-bandgap, include it only when the wide-bandgap track is substantial and explicit.
- If the next edition is not announced, keep the conference in a `持续跟踪名单` section instead of pretending the schedule is known.

## Quality Rules

- For each conference, include at least one source link. Prefer official links.
- State the last verification date explicitly.
- If a required field cannot be verified, write `待确认` rather than guessing.
- Keep date format consistent: `YYYY-MM-DD` or `YYYY-MM`.
- When the location or organizer changes by year, report the current edition values only.

## References

- Output schema and formatting rules: `references/output-format.md`
- Mandatory sites to search every time: `references/mandatory-sites.md`
