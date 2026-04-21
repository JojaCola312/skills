# Output Format

Use this structure for every run. The goal is a maintainable semiconductor conference ledger, not a loose narrative summary.

Do not output only a short curated list. Output every collected domestic conference that passes the inclusion threshold in `collection-rules.md`.

## Top Summary

Start with 2 to 4 lines:

- 核验日期
- 确认国内会议数量
- 持续跟踪数量

Then add a short `重点提示` block before the main sections:

- `高相关会议：` list 3 to 8 entries with the strongest semiconductor relevance
- `临近会议：` list 3 to 8 entries that are not yet held and are currently actionable for attendance, registration, call for papers, exhibition, or agenda follow-up

Rules for `临近会议`:

- prioritize events that you can still attend, register for, submit to, exhibit at, or schedule against
- prefer statuses such as `报名中`, `征稿中`, `议程已发布`, `即将举办`
- do not include already ended events unless the user explicitly asks for retrospective review
- if there are not enough upcoming actionable events, list fewer items rather than filling the block with expired meetings

## Section Order

Use these sections in order:

1. `种子池核验清单`
2. `国内会议`
3. `持续跟踪名单`
4. `检索说明`

## Seed-Family Audit Section

The first main section must be `种子池核验清单`.

At the top of this section, output:

- `种子池家族总数`
- `已核验家族数`
- `未完成家族数`
- `未完成家族列表`

Then provide one compact line per seed family with these fields:

- `标准名`
- `是否有优先来源`
- `本轮搜索状态`
- `本轮使用关键词`
- `结果去向`

Rules:

- every seed family must appear once in this section
- if a seed family has no line here, the run is incomplete
- `未完成家族列表` must name every unresolved family explicitly
- do not replace this section with a narrative summary
- if any seed family remains unchecked, label the run as incomplete in this section instead of presenting the document as a finalized report
- if a seed family is marked for `Main Pool` or `Tracking List`, the corresponding output row must already exist before finalization

Within `国内会议`, sort all entries by `起止日期` ascending.

This ordering is mandatory for:

- the visible text output
- any exported workbook / Excel table

Before writing the final answer or generating the workbook, normalize dates and sort the main pool first.

Ordering rules:

- earlier upcoming events first
- month-only dates after exact earlier dates within the same broad period
- `待确认` dates last
- already-ended events still stay in chronological position based on their actual event date
- do not group entries by source, seed priority, relevance, or importance before date ordering
- `Main Pool` versus `Tracking List` is a status split, not a domestic-versus-overseas split
- if an event is held in China and is sufficiently verified, keep it in `Main Pool` even when the event title or organizer branding is international

## Required Fields Per Confirmed Conference

For each conference in the main pool, output the following fields in this order:

1. `会议名称`
2. `会议主题`
3. `届次/年份`
4. `起止日期`
5. `会议地点`
6. `会议类型`
7. `官方网站/报名链接`
8. `主办单位/承办单位`
9. `信息来源渠道`
10. `与半导体相关性`
11. `最新状态`
12. `最后核验`

## Field Guidance

### 会议名称

Use the official current-edition title if available.

### 会议主题

Keep it short and factual. Prefer the official theme. If unavailable, summarize the conference focus in one line.

### 届次/年份

Examples:

- `第十二届 / 2026年`
- `2026年`
- `待确认`

### 起止日期

Use exact dates when possible.

Examples:

- `2026-04-17 至 2026-04-19`
- `2026-11`
- `待确认`

### 会议地点

Use `城市` or `城市 + 场馆` for domestic events.

### 会议类型

Use concise labels, for example:

- `国内全国性会议`
- `国内行业论坛`
- `展会+论坛`
- `专题研讨会`
- `线上研讨会`

### 官方网站/报名链接

Prefer the official site or registration page. If neither exists, use the highest-confidence official organizer page.

If there is no standalone official site, use the best available registration or organizer link and do not exclude the event for that reason.

### 主办单位/承办单位

List host, organizer, sponsor, and co-organizer when available.

### 信息来源渠道

State the source type, not just the URL.

Examples:

- `官网`
- `主办方通知`
- `协会/联盟公告`
- `微信公众号`
- `报名平台`
- `展会官网`

You may append 1 to 3 links after the source-channel description.

### 与半导体相关性

This field is mandatory. Explain why the event belongs in this skill.

Use one of these patterns:

- `直接相关：会议主题即半导体/集成电路产业。`
- `高度相关：设有SiC/GaN/化合物半导体/封装/材料/制造/测试专场。`
- `扩展相关：虽为 broader industry event，但对半导体器件、封装、材料、可靠性、制造或应用有直接价值。`

### 最新状态

Examples:

- `已公布时间地点，报名开放中。`
- `已发布议程，会议即将举行。`
- `本届已结束，下一届尚未公布。`
- `仅能确认本届信息，下一届待确认。`
- `仅确认到会议通知/报名信息，更多细节待确认。`

When possible, use status wording that makes actionability obvious, for example:

- `报名中`
- `征稿中`
- `招商中`
- `议程已发布`
- `即将举办`
- `已结束`

### 最后核验

Use the actual verification date of the run.

## Ongoing Tracking List

For conferences without a confirmed next edition, keep a compact entry with:

- `会议名称`
- `上一届信息`
- `本轮核验结果`
- `待跟踪点`
- `优先检查网址`

Seed-pool entries with no fresh update this round should appear here rather than disappearing.

Keep `持续跟踪名单` grouped logically, but it does not need the same strict chronological ordering as the main pool.

## Search Notes Requirement

Use the final section label `Search Notes` here.

In the final `Search Notes` section, explicitly state whether browser fallback was used in this run.

If browser fallback was used, include:

- which seed families required browser fallback
- that Bing search was used through Chrome DevTools MCP browser tools
- whether the browser path produced a usable detail page or only weak evidence

## Workbook Export Requirements

Canonical-state rule:

- update `conference-ledger.md` first
- export Excel only after the Markdown ledger reflects the latest run state
- do not manually diverge the workbook from the Markdown ledger

If the run produces an Excel workbook, do not collapse the result into a single simplified sheet unless the user explicitly asks for a one-sheet version.

Default workbook structure:

1. `汇总信息`
2. `国内会议`
3. `持续跟踪名单`

Workbook rules:

- `汇总信息` must include at least:
  - 核验日期
  - 确认国内会议数量
  - 持续跟踪数量
- `国内会议` must contain the full domestic main pool, sorted by `起止日期` ascending
- `持续跟踪名单` must contain seed-pool families whose next edition is still unconfirmed or weakly confirmed
- do not merge `持续跟踪名单` into the main pool just to make the workbook shorter
- do not omit `持续跟踪名单` from the workbook if the text response mentions it

Coverage rule for workbook export:

- every seed family must appear either in `国内会议` or in `持续跟踪名单`
- do not reduce workbook coverage below the assembled text-response pool
- if the workbook is narrower than the text pool, that is an export error, not an acceptable simplification

## CRITICAL: Count Validation Before Delivery （计数验证规则）

**Before delivering any report or Excel workbook, you MUST run these validation checks:**

### 1. 种子池核验清单验证
```
种子池核验清单总条目数
= (标记为"国内会议"的数量)
+ (标记为"持续跟踪名单"的数量)
+ (未完成/待确认的数量)
```

### 2. Sheet计数一致性验证
```
汇总信息中"确认国内会议" = 国内会议sheet数据行数
汇总信息中"持续跟踪名单" = 持续跟踪名单sheet数据行数
国内会议sheet数据行数 = 种子池核验清单中"结果去向"为"国内会议"的条目数
持续跟踪名单sheet数据行数 = 种子池核验清单中"结果去向"为"持续跟踪名单"的条目数
```

### 3. 命名一致性验证
```
对于种子池核验清单中的每个条目：
  如果"结果去向" = "国内会议"：
    此条目的"标准名"必须在"国内会议"sheet中找到完全匹配的"会议名称"
  如果"结果去向" = "持续跟踪名单"：
    此条目的"标准名"必须在"持续跟踪名单"sheet中找到完全匹配的"会议名称"
```

**如果任何验证失败，报告无效，必须在交付前修正。**

### 验证示例

正确的报告：
```
种子池核验清单: 100条
  - 国内会议: 70条
  - 持续跟踪名单: 25条
  - 未完成: 5条

国内会议sheet: 70条数据
持续跟踪名单sheet: 25条数据
汇总信息: 确认国内会议=70, 持续跟踪=25

验证通过 ✓
```

错误的报告（需要修正）：
```
种子池核验清单: 显示76条标记为"国内会议"
国内会议sheet: 只有61条数据  ← 错误！计数不匹配

种子池核验清单: "湾芯展WESEMiBAY" 标记为国内会议
国内会议sheet: 只有 "湾芯展WESEMiBAY 2026"  ← 错误！名称不匹配
```

**Never deliver a report with count or name mismatches.**

## Sparsity Rule

Missing fields must be written as `待确认`.

Do not omit a relevant conference solely because:

- official site is weak
- agenda is not yet posted
- organizer information is partial
- the event is smaller than flagship conferences

The output should prefer completeness with explicit uncertainty over a sparse but over-filtered list.

## Retrieval Notes

At the end, include:

- 本次优先核验的种子会议家族
- 种子池家族总数 / 已核验数 / 未完成数
- 本次使用的核心搜索词
- 本次检查的强制来源
- 本次新增会议家族
- 仍未解决的歧义或缺口
