---
name: conference-track-semiconductor-industry
description: "Compile and maintain a domestic-China semiconductor conference ledger when the user says '会议跟踪' or 'conference track', or asks to collect conference information about semiconductors, integrated circuits, compound semiconductors, third-generation semiconductors, packaging, materials, manufacturing, testing, reliability, automotive electronics, and related industry events."
---

# Conference Ledger: Semiconductor Industry

Use this skill when the user asks for `会议跟踪` or `conference track` in the semiconductor / integrated-circuit industry domain, and the goal is to compile, update, or maintain a conference ledger.

## What This Skill Covers

- Domestic China conferences
- Dedicated semiconductor, compound-semiconductor, and third-generation semiconductor events
- Broader semiconductor industry events across design, manufacturing, packaging, materials, testing, reliability, and applications

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

## How To Work

- Use `references/collection-rules.md` for scope, inclusion, search, source priority, dedup, and export rules.
- Use `references/mandatory-sites.md` for the required source sweep on every run.
- Use `references/seed-conference-families.md` as the baseline conference pool that should be checked first.
- Use `references/output-format.md` for the exact response structure and workbook expectations.
