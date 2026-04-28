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
18. When a seed family is marked for `Main Pool` or `Tracking List`, create the corresponding output entry immediately. Do not defer output creation until later cleanup.
19. For major exhibitions, umbrella conferences, and platform-style annual events, confirm the parent event first and then add concurrent forums or sub-events. Do not let sub-events replace the parent event.
20. If search results mostly return sub-events, topical sessions, or concurrent forums, run an extra search for the parent event itself before finalizing the family status.
21. Before final output, review the `Result Destination` column row by row and confirm that every marked family has a matching output entry.
22. Before marking the run complete, compare seed-family destination counts against actual output counts. If the counts do not match, the run is incomplete and must be corrected.
23. Automatically append truly new conference families to `references/seed-conference-families.md` before `## Matching Guidance` when the run discovers a recurring domestic semiconductor conference family that is not already covered.
24. `Main Pool` versus `Tracking List` is a status split, not a domestic-versus-overseas split. Do not use `Tracking List` as an international-conference bucket.
25. If a conference is held in China and is sufficiently verified, keep it in `Main Pool` even when the title, host, or branding is international.
26. **CRITICAL: When a conference in `Tracking List` (持续跟踪名单) becomes verified with confirmed date and location, you MUST move it to `Main Pool` (国内会议) immediately. Never leave a verified conference in `Tracking List`.**
27. **Moving from Tracking to Main Pool requires two actions: (1) add a new entry to Main Pool with full details (会议名称, 会议主题, 届次/年份, 起止日期, 会议地点, 会议类型, 官方网站, 主办单位, 信息来源, 与半导体相关性, 最新状态, 最后核验), and (2) remove the corresponding entry from Tracking List. Do not skip either action.**
28. **A conference should only stay in `Tracking List` if it remains unverified (未找到2026年明确信息) or has incomplete critical information (date/location unknown). Once verified, it graduates to Main Pool.**

29. **CRITICAL: Never pause mid-run to wait for user confirmation. A run must be complete in one continuous execution: search all seed families → verify information → update ledger → sync Excel → output final report. Do not stop after searching only a few conferences and expect the user to prompt "continue".**

30. **If you find yourself wanting to pause after 5-10 searches because "this seems like enough", STOP that impulse. Rule 16 already forbids this. Process every single seed family before concluding the run.**

31. **The only valid reason to stop a run early is explicit user interruption (e.g., "stop", "pause", "that's enough for now"). Everything else — including token pressure, time spent, or partial completion — is not a valid stopping point.**

32. **CRITICAL: Name Consistency Rule - 种子池标准名 = 输出sheet名称.** The conference name in the seed-pool audit (种子池核验清单) MUST exactly match the conference name in the output sheet (国内会议 or 持续跟踪名单). Do NOT use different names like "湾芯展WESEMiBAY" in seed pool but "湾芯展WESEMiBAY 2026" in output. If the official name includes year/edition, include it consistently everywhere.

33. **CRITICAL: Count Consistency Rule - 计数必须精确匹配.** Before finalizing any report or Excel, run these validation checks:
    - 种子池核验清单中标记为"国内会议"的数量 = 国内会议sheet的条目数
    - 种子池核验清单中标记为"持续跟踪名单"的数量 = 持续跟踪名单sheet的条目数
    - 种子池核验清单总条目 = 国内会议 + 持续跟踪名单 + 未完成
    - 汇总信息中的数值必须与上述计数完全一致
    - If any count mismatch, the report is INVALID and must be corrected before delivery.

34. **CRITICAL: Three-Sheet Requirement.** Every exported workbook MUST have these 4 sheets:
    1. 汇总信息 - with accurate counts
    2. 国内会议 - all verified domestic conferences
    3. 持续跟踪名单 - all unverified/tracking conferences (NEVER omit this sheet)
    4. 种子池核验清单 - audit trail for every seed family
    
    Do NOT export a workbook without all 4 sheets unless the user explicitly requests a simplified version.

35. **CRITICAL: No Silent Drop Rule.** Every seed family must appear in exactly one place in the output: 国内会议 OR 持续跟踪名单. Never drop a seed family silently. If a seed family cannot be verified, it goes to 持续跟踪名单, not disappeared.

36. **Cross-Validation Before Delivery.** Before delivering any report, perform this check:
    ```
    Expected: seed_pool_total = domestic_count + tracking_count + unresolved_count
    Actual: verify each sheet row count matches
    Names: verify seed pool standard names match output sheet names exactly
    ```
    If any mismatch, fix it before the user sees the report.

## Browser Fallback Rule

When normal keyword search and priority-source review still fail to produce usable evidence for a seed family, use Chrome DevTools MCP browser search as a fallback path if that tool is available in the runtime.

In that fallback path:

- use Bing search first
- open the most promising result pages rather than stopping at the search-results page
- continue the same multi-hop review logic through entry pages, section pages, and detail pages
- use this fallback selectively for unresolved seed families, not for the entire pool

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

## How To Work - CRITICAL WORKFLOW

### ⚠️ 正确流程（必须严格遵守）

**每次运行必须按以下顺序执行：**

1. **READ FIRST - 读取现有数据**
   - 先读取 `skills/conference-track-wide-bandgap/references/conference-ledger.md`，了解已有的会议信息和状态
   - 再读取 `skills/conference-track-wide-bandgap/references/seed-conference-families.md`，获取种子池列表
   - **绝不允许跳过这一步直接开始搜索**
   - **绝不允许写入 workspace 根目录的 references/ 目录**

2. **SEARCH - 搜索核验**
   - 根据种子池列表逐一搜索核验
   - 对于已存在的会议条目：检查是否有更新（时间、地点、状态变化）
   - 对于新发现的会议：评估是否符合收录标准

3. **UPDATE MARKDOWN - 更新台账（增量更新）**
   - **增量更新** `skills/conference-track-wide-bandgap/references/conference-ledger.md`，不是重写整个文件
   - 已存在的条目：更新变化字段（如日期确定、状态变更）
   - 新条目：追加到相应 section（Main Pool 或 Tracking List）
   - 从 Tracking List 验证成功的会议：移动到 Main Pool 并从 Tracking List 删除
   - **绝不允许用搜索结果直接覆盖整个 ledger**
   - **绝不允许写入 workspace 根目录的 references/**

4. **SYNC TO EXCEL - 同步到 Excel**
   - **必须使用** `skills/conference-track-wide-bandgap/scripts/sync_conference_ledger.py` 进行 Markdown → Excel 转换
   - **绝不允许自己写脚本**生成 Excel
   - 命令：`python3 skills/conference-track-wide-bandgap/scripts/sync_conference_ledger.py md-to-xlsx skills/conference-track-wide-bandgap/references/conference-ledger.md skills/conference-track-wide-bandgap/references/2026半导体会议追踪.xlsx --audit-md skills/conference-track-wide-bandgap/references/seed-audit.md`

5. **VALIDATE - 校验输出**
   - 检查计数一致性（见 Rule 33）
   - 检查名称一致性（见 Rule 32）
   - 确认所有种子池家族都在输出中

### ❌ 常见错误（绝对禁止）

1. **不读 ledger 就开始搜索** - 必须先了解现有数据
2. **搜索后重写整个 ledger** - 必须增量更新
3. **自己写脚本生成 Excel** - 必须用 `sync_conference_ledger.py`
4. **跳过 Markdown 直接写 Excel** - Markdown 是 source of truth
5. **丢失已有条目** - 更新时保留所有现有信息
6. **写错文件位置** - 必须写 skill 目录下，不许写 workspace 根目录

### 参考文件（所有路径都是 skill 目录下）

**所有文件都在 `skills/conference-track-wide-bandgap/` 目录下：**

- `references/conference-ledger.md` - canonical working ledger（source of truth）
- `references/seed-audit.md` - per-run audit file
- `references/collection-rules.md` - scope, inclusion, search, source priority, dedup, and export rules
- `references/mandatory-sites.md` - required source sweep on every run
- `references/seed-conference-families.md` - baseline conference pool
- `references/output-format.md` - exact response structure and workbook expectations
- `scripts/sync_conference_ledger.py` - **REQUIRED** for Markdown ↔ Excel sync

**⚠️ 绝不允许写入 workspace 根目录的 references/ 目录**
**⚠️ 所有文件操作都必须在 `skills/conference-track-wide-bandgap/references/` 下**
