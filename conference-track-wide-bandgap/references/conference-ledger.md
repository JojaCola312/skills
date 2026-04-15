# Conference Ledger

This file is the canonical ledger. Update this Markdown first, then regenerate Excel from it.

## Ledger Rules

- Treat this file as the source of truth. Do not update Excel first.
- Keep section names unchanged: `Summary`, `Main Pool`, `Tracking List`, `Search Notes`.
- Keep one `###` block per conference entry. Do not merge multiple conferences into one block.
- In `Main Pool`, keep only sufficiently verified China-based events.
- In `Tracking List`, keep unresolved, weak-evidence, or next-edition-unconfirmed events.
- Prefer stable official or organizer links in `官方网站/报名链接`. If unavailable, keep `待确认` and record weak sources under `信息来源`.
- Use `Retrieval Hint` to record how the event was found last time, such as source type, effective query, multi-hop path, or browser fallback.
- Use a fixed `Retrieval Hint` template. Do not invent free-form prose.
- Keep values concise and field-based. Do not turn this ledger into a narrative report.

`Retrieval Hint` template:

- with stable URL:
  - `source=<source-type>; query=<effective-query>; path=<navigation-path>; url=<stable-url>`
- without stable URL:
  - `source=<source-type>; query=<effective-query>; note=<short-note>`

Allowed `source-type` values:

- `official-site`
- `organizer-site`
- `association-site`
- `government-or-park`
- `industry-media`
- `wechat`
- `browser-bing`

Formatting rules:

- keep fields in the exact order shown above
- use semicolons as separators
- keep `path` short, for example `homepage->events->detail`
- keep `note` short, for example `weak-source-only` or `official-site-not-found`
- do not add extra fields beyond `source`, `query`, `path`, `url`, and `note`

## Summary

Use this section only for run-level facts and short status bullets. Do not add long narrative paragraphs here.
Keep this section to a minimal state snapshot only.

- Report Title:
- 核验日期:
- 种子池家族总数:
- 本轮已核验:
- 确认国内会议:
- 持续跟踪:

## Main Pool

Rules for this section:

- One conference entry per `###` block.
- Use the conference's stable family-or-edition name as the block title.
- Preserve the field order inside each block.
- `Retrieval Hint` is optional but recommended for repeat lookups.
- If present, `Retrieval Hint` must follow the fixed template above.
- This section is for confirmed main entries, not unresolved candidates.

### Example Conference
- 会议名称:
- 会议主题:
- 届次/年份:
- 起止日期:
- 会议地点:
- 会议类型:
- 官方网站/报名链接:
- 主办单位:
- 信息来源:
- 与半导体相关性:
- 最新状态:
- 最后核验:
- Retrieval Hint:

## Tracking List

Rules for this section:

- Keep entries here only when the next edition is unconfirmed, evidence is weak, or key fields remain unresolved after retries.
- `Tracking List` is a status bucket, not an overseas bucket.
- If a China-based event becomes sufficiently verified, move it to `Main Pool`.
- Use `Retrieval Hint` here to record the most effective recovery path for the next run.
- If present, `Retrieval Hint` must follow the fixed template above.

### Example Tracking Conference
- 会议名称:
- 上一届信息:
- 本轮核验结果:
- 待跟踪点:
- 优先检查网址:
- Retrieval Hint:

## Search Notes

Keep this section as short operational notes:

- sources checked
- browser fallback usage
- unresolved gaps
- newly added conference families or anchors

- 本次核验的种子会议家族:
- 本轮使用的核心搜索词:
- 本轮检查的强制来源:
- 本轮新增会议家族:
- 未解决问题:
