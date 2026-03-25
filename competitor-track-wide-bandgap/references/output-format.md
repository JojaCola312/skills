# Output Format

Every response from this skill should use the following structure.

## Top Section

Start with a 3 to 5 line summary:

- this run's verification date
- how many competitors had confirmed updates
- how many conference-related signals were found
- how many product-related signals were found
- how many companies remain in tracking status

## Main Sections

Use these sections in order:

1. `重点结论`
2. `会议动向`
3. `产品动向`
4. `其他竞争情报`
5. `持续跟踪名单`
6. `检索说明`

## Required Fields Per Signal

For each signal, output the following fields in this order:

1. `公司名称`
2. `信号类型`
3. `标题`
4. `关联会议/产品`
5. `地点`
6. `时间`
7. `规格/等级`
8. `关键内容`
9. `竞争意义`
10. `最新状态`
11. `来源`
12. `最后核验`

## Field Definitions

### 公司名称

Use the official English or Chinese company name that best matches the primary source.

### 信号类型

Use one of:

- `会议参会`
- `会议演讲`
- `会议赞助/展台`
- `新产品`
- `产品路线图`
- `合作/客户`
- `产能/工厂`
- `融资/并购`
- `其他`

### 标题

Use one concise line summarizing the verified update.

### 关联会议/产品

Use the official conference name or product family / product model when available.

### 地点

Use `城市, 国家/地区` for international items and `城市` for domestic items.

If not applicable, write `不适用` or `待确认`.

### 时间

Use exact dates if available. Otherwise use month-level precision.

Examples:

- `2026-05-14`
- `2026-09`
- `待确认`

### 规格/等级

This field is mandatory.

For conference signals, use tags such as:

- `国际旗舰会议`
- `国际专业会议`
- `国际产业展会`
- `国内全国性会议`
- `国内行业论坛`

For product signals, use tags such as:

- `正式发布`
- `产品预告`
- `样品阶段`
- `量产阶段`
- `参数更新`

Then add one short basis sentence.

### 关键内容

Summarize only the verified facts, such as:

- what was launched
- what was presented
- what booth or speaking role was confirmed
- what specification, rating, package, wafer size, or application was disclosed

### 竞争意义

Explain in one sentence why this update matters competitively.

### 最新状态

Examples:

- `官网已发布`
- `会议官网已列为赞助商`
- `产品页已上线`
- `媒体报道存在，但官网仍待确认`

### 来源

Provide 1 to 3 links, with the official link first.

### 最后核验

Use the actual date of the current run.

## Formatting Template

Use this template per item:

```md
### 1. 标题

- 公司名称：
- 信号类型：
- 关联会议/产品：
- 地点：
- 时间：
- 规格/等级：
- 关键内容：
- 竞争意义：
- 最新状态：
- 来源：
- 最后核验：
```

## 持续跟踪名单

For competitors without a confirmed update, keep a compact entry with:

- `公司名称`
- `重点跟踪方向`
- `优先检查网址`
- `待确认点`

## 检索说明

At the end, include:

- recent search keywords used
- mandatory companies checked
- mandatory conference sites checked
- unresolved ambiguities
