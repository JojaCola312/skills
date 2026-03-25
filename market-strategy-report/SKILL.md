---
name: market-strategy-report
description: "Generate structured market strategy reports when the user asks for 市场策略报告, 行业趋势分析, 发展前景研判, 市场定位, 目标客群分析, 赛道分析, 商业模式梳理, 盈利路径设计, 战略规划, or SWOT analysis."
---

# Market Strategy Report

Use this skill when the user asks for a market strategy report or any major subset of one.

Typical triggers include:

- `市场策略报告`
- `行业趋势分析`
- `发展前景研判`
- `市场定位`
- `目标客群分析`
- `赛道分析`
- `商业模式梳理`
- `盈利路径设计`
- `战略规划`
- `SWOT分析`

## Scope

This skill is for strategy-oriented business analysis. It is suitable for:

- new ventures
- new product lines
- regional market entry
- business-unit planning
- competitive positioning
- investment or incubation pre-study

## Default Workflow

### Step 1: Clarify the object

Identify:

- company, product, project, or business line
- target geography
- target industry
- report audience
- time horizon

If the user does not specify them, infer cautiously and state assumptions.

### Step 2: Build the analysis frame

Cover these dimensions:

- industry trends
- development outlook
- market positioning
- target customer groups
- track / segment analysis
- business model
- monetization path
- strategic plan
- SWOT

### Step 3: Keep the report decision-oriented

Do not produce generic descriptive text only. The report should end in actionable choices, priorities, and tradeoffs.

### Step 4: Follow the required output structure

Use `references/output-format.md`.

## Quality Rules

- Default output language is Chinese unless the user asks otherwise.
- Use concise business language rather than academic prose.
- Distinguish facts, assumptions, and recommendations.
- If the user only asks for one or two modules, keep the same overall report structure but mark unused sections as `本次未展开`.
- When evidence is weak, write `待验证假设`.
- Prefer explicit segmentation, prioritization, and go-to-market implications over vague commentary.

## Analysis Heuristics

- Trends should explain what is changing and why it matters commercially.
- Outlook should include both opportunity and constraint.
- Positioning should identify what niche is defensible.
- Target customer analysis should distinguish payer, buyer, user, and channel partner where relevant.
- Business model should specify value proposition, delivery mechanism, and revenue logic.
- Monetization should distinguish short-term cash flow from medium-term scale path.
- Strategic planning should include phased priorities, not just end-state vision.
- SWOT should be specific to the analyzed object, not boilerplate.

## References

- Required report structure: `references/output-format.md`
