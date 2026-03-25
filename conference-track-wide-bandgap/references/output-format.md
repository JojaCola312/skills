# Output Format

Every response from this skill should use the following structure.

## Top Section

Start with a 2 to 4 line summary:

- this run's verification date
- how many international and domestic conferences were confirmed
- how many entries remain in tracking status

## Main Sections

Use these sections in order:

1. `国际会议`
2. `国内会议`
3. `持续跟踪名单`
4. `检索说明`

## Required Fields Per Conference

For each conference, output the following fields in this order:

1. `会议名称`
2. `简称`
3. `会议方向`
4. `地点`
5. `时间`
6. `规格`
7. `举办组织`
8. `流程`
9. `最新状态`
10. `关注理由`
11. `来源`
12. `最后核验`

## Field Definitions

### 会议名称

Use the official current edition title if available.

### 简称

Use the commonly recognized abbreviation, otherwise write `无`.

### 会议方向

One short line, for example:

- `SiC / 功率器件`
- `GaN / 氮化物材料与器件`
- `第三代半导体 / 产业与应用`

### 地点

Use `城市, 国家/地区` or `城市` for domestic events.

### 时间

Use exact dates if available. Otherwise use month-level precision.

Examples:

- `2026-06-07 至 2026-06-11`
- `2026-11`
- `待确认`

### 规格

This is mandatory. Describe it using short tags and one sentence.

Recommended tag set:

- `国际顶级学术会议`
- `国际专业会议`
- `国际产业论坛`
- `国内全国性会议`
- `国内行业论坛`
- `国内区域活动`

Then add one short basis sentence, such as:

- `由 IEEE/专业学会主导，连续举办，学术影响力高。`
- `由国家级创新平台和产业联盟推动，偏产业生态与合作。`

### 举办组织

List the host, organizer, sponsor, or technical co-sponsor when available.

### 流程

Summarize the event process or milestone chain. Prefer this order:

- `征稿`
- `投稿截止`
- `录用通知`
- `注册`
- `议程/教程`
- `会议举行`

If the event is an industry forum without papers, use:

- `报名/注册`
- `议程发布`
- `论坛举办`
- `展览/对接活动`

If only partial milestones are known, list only verified steps and mark the rest as `待确认`.

### 最新状态

Examples:

- `官网已公布 2026 届时间与地点`
- `2025 届已结束，下一届尚未公布`
- `已开放征稿`
- `已开放注册`

### 关注理由

Explain in one sentence why this event matters for wide-bandgap tracking.

### 来源

Provide 1 to 3 links, with the official link first.

### 最后核验

Use the actual date of the current run.

## Formatting Template

Use this template per item:

```md
### 1. 会议名称

- 简称：
- 会议方向：
- 地点：
- 时间：
- 规格：
- 举办组织：
- 流程：
- 最新状态：
- 关注理由：
- 来源：
- 最后核验：
```

## 持续跟踪名单

For conferences without a confirmed next edition, keep a compact entry with:

- `会议名称`
- `上一届信息`
- `待跟踪点`
- `优先检查网址`

## 检索说明

At the end, include:

- recent search keywords used
- mandatory sites checked
- any unresolved ambiguities
