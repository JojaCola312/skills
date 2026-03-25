# Output Format

Every response from this skill should use the following structure.

## Top Section

Start with a 3 to 5 line summary:

- this run's verification date
- how many project signals were confirmed
- how many talent signals were confirmed
- how many award signals were confirmed
- how many entities remain in tracking status

## Main Sections

Use these sections in order:

1. `重点结论`
2. `项目信号`
3. `人才信号`
4. `奖项信号`
5. `持续跟踪名单`
6. `检索说明`

## Required Fields Per Signal

For each signal, output the following fields in this order:

1. `地区/机构`
2. `信号类型`
3. `标题`
4. `关联主体`
5. `地点`
6. `时间`
7. `级别/规格`
8. `关键内容`
9. `跟踪意义`
10. `最新状态`
11. `来源`
12. `最后核验`

## Field Definitions

### 地区/机构

Use the official region, district, park, bureau, laboratory, or institution name.

### 信号类型

Use one of:

- `项目签约`
- `项目申报`
- `项目进展`
- `重点平台`
- `人才计划`
- `人才申报`
- `职称/认定`
- `人才奖励`
- `科技奖项`
- `产业奖项`
- `竞赛/榜单`
- `其他`

### 标题

Use one concise line summarizing the verified update.

### 关联主体

List the key company, laboratory, university, institute, team, or award name.

### 地点

Use `城市` or `城市, 区域`.

### 时间

Use exact dates if available. Otherwise use month-level precision.

### 级别/规格

This field is mandatory.

Recommended examples:

- `国家级项目`
- `省级重点项目`
- `市级重点项目`
- `国家级人才计划`
- `省级人才计划`
- `市级人才计划`
- `国家级科技奖`
- `省级科技奖`
- `市级科技奖`
- `行业奖项`

Then add one short basis sentence.

### 关键内容

Summarize only verified facts:

- what project was launched, signed, approved, or progressed
- what talent plan, application, recognition, subsidy, or support policy was announced
- what award, shortlist, or honor was granted

### 跟踪意义

Explain in one sentence why this matters for regional semiconductor ecosystem tracking.

### 最新状态

Examples:

- `官网已发布`
- `项目已签约`
- `申报已开启`
- `名单已公示`
- `已完成表彰`
- `仍待下一步公告`

### 来源

Provide 1 to 3 links, with the official link first.

### 最后核验

Use the actual date of the current run.

## Formatting Template

Use this template per item:

```md
### 1. 标题

- 地区/机构：
- 信号类型：
- 关联主体：
- 地点：
- 时间：
- 级别/规格：
- 关键内容：
- 跟踪意义：
- 最新状态：
- 来源：
- 最后核验：
```

## 持续跟踪名单

For regions or entities without a confirmed new update, keep a compact entry with:

- `地区/机构`
- `重点跟踪方向`
- `优先检查网址`
- `待确认点`

## 检索说明

At the end, include:

- recent search keywords used
- mandatory sites checked
- unresolved ambiguities
