---
name: conference-track-semiconductor-industry
description: "Compile and maintain a domestic-China semiconductor conference ledger when the user says '会议跟踪' or 'conference track', or asks to collect conference information about semiconductors, integrated circuits, compound semiconductors, third-generation semiconductors, packaging, materials, manufacturing, testing, reliability, automotive electronics, and related industry events."
---

# Conference Ledger: Semiconductor Industry

Use this skill when the user wants to compile, update, or maintain a semiconductor-industry conference ledger for domestic China.

## What This Skill Covers

- domestic China conferences
- dedicated semiconductor, compound-semiconductor, and third-generation semiconductor events
- broader semiconductor industry events across design, manufacturing, packaging, materials, testing, reliability, and applications

## Non-Negotiable Rules

1. Always search both recent results and the mandatory source list, but use the mandatory source list mainly to find new conference families or new anchors that can expand the seed pool.
2. Default to Chinese output.
3. Only maintain domestic China conferences unless the user explicitly asks to add overseas coverage.
4. Keep seed-pool conference families in the output unless they are clearly irrelevant, merged, or discontinued.
5. Output the full collected conference pool, not just a handful of major meetings.
6. Sort the main conference pool by conference date before writing the final answer or exporting any workbook.
7. If exporting Excel, default to a 3-sheet ledger: `汇总信息`, `国内会议`, `持续跟踪名单`. Do not collapse it into a simplified one-sheet workbook unless the user explicitly asks for that.
8. Every seed-pool conference family must appear in exactly one place for each run: `国内会议` or `持续跟踪名单`. Do not silently drop seed entries during export.
9. Do not turn this into a generic semiconductor conference dump.
10. If semiconductor relevance is weak, exclude the event. If relevance is valid but fields are incomplete, keep it and mark missing fields as `待确认`.
11. For every priority source family, use a multi-hop review path: entry page -> relevant section page -> concrete event detail page. Do not stop at a homepage or channel page.
12. Treat a source review as incomplete if it never reaches at least one concrete detail page with conference-specific information.
13. Every seed-pool family must be individually processed in every run. If a seed family has no priority URL, search it by keywords rather than skipping it.
14. A run is not complete until it outputs a seed-family audit summary with: total seed families, verified seed families, unresolved seed families, and the unresolved family names.
15. For no-URL seed families, search exact family names, numbered-title variants, and abbreviations before falling back to broader bag-of-words queries.
16. Token usage, context pressure, or "enough collected items" are not valid reasons to stop before every seed family has been processed.
17. Do not use `待确认` as a shortcut to stop searching. For a seed family without a usable URL, retry with at least 2 to 3 keyword variants before marking it unresolved.
18. Automatically append truly new conference families to `references/seed-conference-families.md` before `## Matching Guidance` when the run discovers a recurring domestic semiconductor conference family that is not already covered.

## New Seed-Family Append Rule

When adding a new conference family to `references/seed-conference-families.md`, use this structure:

```md
#### 新会议家族名称

- 标准名: 新会议家族名称
- 优先来源:
  - https://官方链接（如已确认）
- 追踪关键词:
  - 关键词1
  - 关键词2
- 默认去向: 国内会议
```

Add a new family only when all of the following are true:

- it does not already map to an existing seed family
- its topic is directly or highly relevant to the semiconductor industry
- there is at least one stable organizer, official, or high-confidence source
- it is expected to recur rather than being a one-off activity

## How To Work

- Use `references/collection-rules.md` for scope, inclusion, search, source priority, dedup, and export rules.
- Use `references/mandatory-sites.md` for the required source sweep on every run.
- Use `references/seed-conference-families.md` as the baseline conference pool that should be checked first.
- Use `references/output-format.md` for the exact response structure and workbook expectations.
