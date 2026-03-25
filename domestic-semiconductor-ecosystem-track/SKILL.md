---
name: domestic-semiconductor-ecosystem-track
description: "Track domestic semiconductor-related projects, talent-plan applications, and awards. Trigger when the user asks about 半导体人才申报, 人才申报, 人才计划, 人才项目, 项目申报, 半导体项目申报, 奖项申报, 科技奖项, 集成电路项目, 第三代半导体人才, or regional semiconductor ecosystem monitoring. In this skill, 人才 means talent-plan application, recognition, subsidy, and policy support rather than job seeking. Prioritize Zhejiang, Shanghai, and especially Ningbo Qianwan New Area."
---

# Domestic Semiconductor Ecosystem Track

Use this skill when the user asks to track domestic semiconductor-related:

- projects
- talent programs and申报
- awards
- regional policy and ecosystem signals

This skill should also trigger when the request focuses on only one dimension, for example:

- `项目跟踪`
- `人才跟踪`
- `奖项跟踪`
- `人才申报`
- `半导体人才申报`
- `项目申报`
- `半导体项目申报`
- `奖项申报`
- `半导体人才`
- `集成电路项目`
- `科技奖项`

In this skill, `人才` means:

- 人才计划
- 人才项目
- 人才认定
- 人才申报
- 人才奖励和资助

It does not primarily mean:

- 招聘岗位
- 求职信息
- 普通社会招聘
- 校园招聘

Default regional priority:

1. 宁波前湾新区
2. 宁波
3. 上海
4. 浙江
5. Other domestic regions only when clearly relevant

## Scope

Track three signal groups in parallel:

- `项目`
- `人才`
- `奖项`

Relevant domains include:

- semiconductors
- integrated circuits
- third-generation semiconductors
- wide-bandgap semiconductors
- semiconductor equipment and materials
- EDA, design, manufacturing, packaging, testing, and core components

## Mandatory Search Rule

On every invocation, do both:

1. Search recent results using current-year and previous-year queries in Chinese
2. Search every required site listed in `references/mandatory-sites.md`

Do not skip the mandatory site list just because broad search results already look sufficient.

## Source Priority

Prefer sources in this order:

1. Official government site
2. Official park / district / new-area site
3. Official science, industry, or talent authority page
4. Official award, project, or recruitment notice page
5. Official university / laboratory / institute page
6. Reliable media quoting the official source

If multiple sources disagree, prefer the highest-priority source and note the discrepancy.

## Search Workflow

### Step 1: Broad recent search

Use recent Chinese queries around the current year and previous year. Include combinations such as:

- `半导体 项目 人才 奖项 2026 浙江`
- `集成电路 项目 2026 上海`
- `第三代半导体 人才 2026 宁波 前湾`
- `集成电路 奖项 2026 浙江`
- `前湾新区 半导体 项目 人才 奖项`

### Step 2: Mandatory site sweep

Open or search the URLs in `references/mandatory-sites.md`.

For each required site:

- check project notices, signing news, industrialization progress, and key laboratory/platform updates
- check talent plans, talent application notices, title review, recognition, subsidy, and special reward notices
- check science and technology awards, engineering awards, innovation competitions, and recognition lists

### Step 3: Normalize and classify

Classify each verified signal into one of:

- `项目`
- `人才`
- `奖项`

Merge duplicates and keep the highest-confidence source.

### Step 4: Output in the required structure

Follow `references/output-format.md` exactly.

## Coverage Rules

- Default output language is Chinese.
- If the user asks for all three dimensions, separate `项目信号`, `人才信号`, and `奖项信号`.
- If the user asks for only one dimension, output the same overall structure but keep the requested signal section populated and mark the other sections as `本次未展开`.
- If the user asks for two dimensions, populate only those requested sections and mark the remaining one as `本次未展开`.
- If a signal is not clearly semiconductor-related, exclude it.
- For `人才` requests, prioritize talent-plan application, title recognition, policy support, subsidy, shortlist, and award signals rather than job openings.
- If a source is regionally important but the semiconductor relevance is indirect, include it only when the connection is explicit.
- If a tracked region or organization has no new verified update, keep it in `持续跟踪名单`.

## Quality Rules

- Every signal must include at least one source link. Prefer official links.
- State the last verification date explicitly.
- If a field cannot be verified, write `待确认` rather than guessing.
- Keep date format consistent: `YYYY-MM-DD` or `YYYY-MM`.
- Distinguish `已确认` from `待进一步核验`.

## References

- Output schema and formatting rules: `references/output-format.md`
- Mandatory regional site list: `references/mandatory-sites.md`
