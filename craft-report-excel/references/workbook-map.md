# Workbook Map

The template is a single-sheet workbook with fixed row pairs per unit.

## Fixed Date Layout

The report columns are fixed and must always be used in this exact order:

- `B`: previous Friday
- `C`: current Monday
- `D`: current Tuesday
- `E`: current Wednesday
- `F`: current Thursday
- `G`: current Friday

Semantic meaning:

- `B`: weekly summary / next-week plan
- `C`: daily summary / next-day plan
- `D`: daily summary / next-day plan
- `E`: daily summary / next-day plan
- `F`: daily summary / next-day plan
- `G`: weekly summary / next-week plan

Row `1` stores the fixed date labels for `B:G`.

## Units And Rows

- `光刻`: rows `2-3`
- `刻蚀`: rows `4-5`
- `薄膜`: rows `6-7`
- `掺杂`: rows `8-9`
- `晶背`: rows `10-11`
- `检测`: rows `12-13`
- `生产`: rows `14-15`
- `整合`: rows `16-17`

For each unit:

- Upper row = summary row
- Lower row = plan row

Column `A` holds the unit name and is merged across the two rows.

## Cell Semantics

For a given unit:

- `upper` means the upper row cell in a column
- `lower` means the lower row cell in a column

Example for `光刻`:

- `B2` = upper
- `B3` = lower
- `C2` = upper
- `C3` = lower
- ...
- `G2` = upper
- `G3` = lower

Example for `刻蚀`:

- `B4` = upper
- `B5` = lower

## Formatting Rules

- Do not recreate the workbook from scratch.
- Always start from the provided workbook or the bundled template copy.
- Preserve merged cells, widths, heights, alignment, and styles by only replacing cell values.
- Keep line breaks inside cell text.
- Keep unit order unchanged.
