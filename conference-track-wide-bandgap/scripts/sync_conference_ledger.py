from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List, Tuple

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font


SUMMARY_SHEET = "汇总信息"
MAIN_SHEET = "国内会议"
TRACKING_SHEET = "持续跟踪名单"
AUDIT_SHEET = "种子池核验清单"
NOTES_SHEET = "检索说明"

MAIN_HEADERS = [
    "会议名称",
    "会议主题",
    "届次/年份",
    "起止日期",
    "会议地点",
    "会议类型",
    "官方网站/报名链接",
    "主办单位",
    "信息来源",
    "与半导体相关性",
    "最新状态",
    "最后核验",
]

TRACKING_HEADERS = [
    "会议名称",
    "上一届信息",
    "本轮核验结果",
    "待跟踪点",
    "优先检查网址",
]

AUDIT_HEADERS = [
    "标准名",
    "是否有优先来源",
    "本轮搜索状态",
    "本轮使用关键词",
    "结果去向",
]

SUMMARY_ALLOWED_KEYS = {
    "核验日期",
    "种子池家族总数",
    "本轮已核验",
    "确认国内会议",
    "持续跟踪",
}


def sanitize(value) -> str:
    if value is None:
        return ""
    text = str(value).replace("\r\n", "\n").replace("\r", "\n")
    return text.strip()


def parse_key_value_cell(text: str) -> Tuple[str, str]:
    if "：" in text:
        key, value = text.split("：", 1)
        return key.strip(), value.strip()
    if ":" in text:
        key, value = text.split(":", 1)
        return key.strip(), value.strip()
    return text.strip(), ""


def read_summary_sheet(ws) -> Dict[str, str]:
    result: Dict[str, str] = {}
    title = sanitize(ws.cell(1, 1).value)
    if title:
        result["Report Title"] = title
    for row in ws.iter_rows(values_only=True):
        cell = sanitize(row[0]) if row and row[0] is not None else ""
        if not cell:
            continue
        if cell == title:
            continue
        key, value = parse_key_value_cell(cell)
        if key in SUMMARY_ALLOWED_KEYS:
            result[key] = value
    return result


def read_table_sheet(ws, headers: List[str]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    actual_headers = [sanitize(c.value) for c in ws[1][: len(headers)]]
    if actual_headers != headers:
        raise ValueError(f"{ws.title} headers do not match expected template.")
    for row in ws.iter_rows(min_row=2, values_only=True):
        values = [sanitize(v) for v in row[: len(headers)]]
        if not any(values):
            continue
        rows.append(dict(zip(headers, values)))
    return rows


def read_notes_sheet(ws) -> List[Tuple[str, str]]:
    notes: List[Tuple[str, str]] = []
    for row in ws.iter_rows(values_only=True):
        left = sanitize(row[0]) if len(row) >= 1 else ""
        right = sanitize(row[1]) if len(row) >= 2 else ""
        if not left and not right:
            continue
        notes.append((left, right))
    return notes


def workbook_to_data(xlsx_path: Path) -> Dict[str, object]:
    wb = load_workbook(xlsx_path)
    return {
        "summary": read_summary_sheet(wb[SUMMARY_SHEET]),
        "main_pool": read_table_sheet(wb[MAIN_SHEET], MAIN_HEADERS),
        "tracking_list": read_table_sheet(wb[TRACKING_SHEET], TRACKING_HEADERS),
        "seed_audit": read_table_sheet(wb[AUDIT_SHEET], AUDIT_HEADERS),
        "search_notes": read_notes_sheet(wb[NOTES_SHEET]),
    }


def dump_record_block(lines: List[str], title: str, record: Dict[str, str], ordered_keys: List[str]) -> None:
    lines.append(f"### {title}")
    for key in ordered_keys:
        lines.append(f"- {key}: {sanitize(record.get(key, ''))}")
    if "Retrieval Hint" in record:
        lines.append(f"- Retrieval Hint: {sanitize(record.get('Retrieval Hint', ''))}")
    lines.append("")


def data_to_markdown(data: Dict[str, object]) -> str:
    lines: List[str] = [
        "# Conference Ledger",
        "",
        "This file is the canonical ledger. Update this Markdown first, then regenerate Excel from it.",
        "",
        "## Ledger Rules",
        "",
        "- Treat this file as the source of truth. Do not update Excel first.",
        "- Keep section names unchanged: `Summary`, `Main Pool`, `Tracking List`, `Search Notes`.",
        "- Keep one `###` block per conference entry. Do not merge multiple conferences into one block.",
        "- In `Main Pool`, keep only sufficiently verified China-based events.",
        "- In `Tracking List`, keep unresolved, weak-evidence, or next-edition-unconfirmed events.",
        "- Prefer stable official or organizer links in `官方网站/报名链接`. If unavailable, keep `待确认` and record weak sources under `信息来源`.",
        "- Keep values concise and field-based. Do not turn this ledger into a narrative report.",
        "",
        "## Summary",
        "",
        "Use this section only for run-level facts and short status bullets. Do not add long narrative paragraphs here.",
        "Keep this section to a minimal state snapshot only.",
        "",
    ]
    for key, value in data["summary"].items():
        lines.append(f"- {key}: {sanitize(value)}")
    lines.extend(["", "## Main Pool", ""])
    lines.extend(
        [
            "",
            "Rules for this section:",
            "",
            "- One conference entry per `###` block.",
            "- Use the conference's stable family-or-edition name as the block title.",
            "- Preserve the field order inside each block.",
            "- This section is for confirmed main entries, not unresolved candidates.",
            "",
        ]
    )
    for record in data["main_pool"]:
        dump_record_block(lines, record["会议名称"], record, MAIN_HEADERS)
    lines.extend(["## Tracking List", ""])
    lines.extend(
        [
            "",
            "Rules for this section:",
            "",
            "- Keep entries here only when the next edition is unconfirmed, evidence is weak, or key fields remain unresolved after retries.",
            "- `Tracking List` is a status bucket, not an overseas bucket.",
            "- If a China-based event becomes sufficiently verified, move it to `Main Pool`.",
            "",
        ]
    )
    for record in data["tracking_list"]:
        dump_record_block(lines, record["会议名称"], record, TRACKING_HEADERS)
    lines.extend(["## Search Notes", ""])
    lines.extend(
        [
            "",
            "Keep this section as short operational notes:",
            "",
            "- sources checked",
            "- browser fallback usage",
            "- unresolved gaps",
            "- newly added conference families or anchors",
            "",
        ]
    )
    for left, right in data["search_notes"]:
        if right:
            lines.append(f"- {left}: {right}")
        else:
            lines.append(f"- {left}")
    lines.append("")
    return "\n".join(lines)


def audit_to_markdown(data: Dict[str, object]) -> str:
    lines: List[str] = [
        "# Seed Audit",
        "",
        "This file stores per-run seed-family verification state. It is operational state, not the canonical business ledger.",
        "",
        "## Seed Audit",
        "",
    ]
    for record in data["seed_audit"]:
        dump_record_block(lines, record["标准名"], record, AUDIT_HEADERS)
    lines.append("")
    return "\n".join(lines)


def parse_markdown_records(lines: List[str], section: str, record_key: str, ordered_keys: List[str]) -> List[Dict[str, str]]:
    records: List[Dict[str, str]] = []
    current: Dict[str, str] | None = None
    in_section = False
    for line in lines:
        stripped = line.strip()
        if stripped == f"## {section}":
            in_section = True
            current = None
            continue
        if in_section and stripped.startswith("## "):
            break
        if not in_section:
            continue
        if stripped.startswith("### "):
            if current:
                records.append(current)
            current = {record_key: stripped[4:].strip()}
            continue
        if current is not None and stripped.startswith("- "):
            body = stripped[2:]
            if ":" in body:
                key, value = body.split(":", 1)
                current[key.strip()] = value.strip()
    if current:
        records.append(current)
    normalized: List[Dict[str, str]] = []
    for record in records:
        normalized.append({key: sanitize(record.get(key, "")) for key in ordered_keys})
    return normalized


def read_existing_hints(md_path: Path) -> Dict[Tuple[str, str], str]:
    if not md_path.exists():
        return {}
    lines = md_path.read_text(encoding="utf-8").splitlines()
    hints: Dict[Tuple[str, str], str] = {}
    for section, record_key in [("Main Pool", "会议名称"), ("Tracking List", "会议名称")]:
        in_section = False
        current_title: str | None = None
        current_hint = ""
        for line in lines:
            stripped = line.strip()
            if stripped == f"## {section}":
                in_section = True
                current_title = None
                current_hint = ""
                continue
            if in_section and stripped.startswith("## "):
                if current_title is not None:
                    hints[(section, current_title)] = current_hint
                break
            if not in_section:
                continue
            if stripped.startswith("### "):
                if current_title is not None:
                    hints[(section, current_title)] = current_hint
                current_title = stripped[4:].strip()
                current_hint = ""
                continue
            if current_title is not None and stripped.startswith("- Retrieval Hint:"):
                current_hint = stripped.split(":", 1)[1].strip()
        if in_section and current_title is not None:
            hints[(section, current_title)] = current_hint
    return hints


def parse_markdown_summary(lines: List[str]) -> Dict[str, str]:
    summary: Dict[str, str] = {}
    in_section = False
    for line in lines:
        stripped = line.strip()
        if stripped == "## Summary":
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if in_section and stripped.startswith("- "):
            body = stripped[2:]
            if ":" in body:
                key, value = body.split(":", 1)
                summary[key.strip()] = value.strip()
    return summary


def parse_markdown_notes(lines: List[str]) -> List[Tuple[str, str]]:
    notes: List[Tuple[str, str]] = []
    in_section = False
    for line in lines:
        stripped = line.strip()
        if stripped == "## Search Notes":
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if in_section and stripped.startswith("- "):
            body = stripped[2:]
            if ":" in body:
                left, right = body.split(":", 1)
                notes.append((left.strip(), right.strip()))
            else:
                notes.append((body.strip(), ""))
    return notes


def parse_audit_markdown(lines: List[str]) -> List[Dict[str, str]]:
    return parse_markdown_records(lines, "Seed Audit", "标准名", AUDIT_HEADERS)


def markdown_to_data(md_path: Path, audit_md_path: Path | None = None) -> Dict[str, object]:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    audit_records: List[Dict[str, str]] = []
    if audit_md_path and audit_md_path.exists():
        audit_records = parse_audit_markdown(audit_md_path.read_text(encoding="utf-8").splitlines())
    return {
        "summary": parse_markdown_summary(lines),
        "main_pool": parse_markdown_records(lines, "Main Pool", "会议名称", MAIN_HEADERS),
        "tracking_list": parse_markdown_records(lines, "Tracking List", "会议名称", TRACKING_HEADERS),
        "seed_audit": audit_records,
        "search_notes": parse_markdown_notes(lines),
    }


def attach_hints(data: Dict[str, object], hint_map: Dict[Tuple[str, str], str]) -> Dict[str, object]:
    for section_name, key_name, data_key in [
        ("Main Pool", "会议名称", "main_pool"),
        ("Tracking List", "会议名称", "tracking_list"),
    ]:
        for record in data[data_key]:
            hint = hint_map.get((section_name, record[key_name]), "")
            record["Retrieval Hint"] = hint
    return data


def style_sheet(ws) -> None:
    bold = Font(bold=True)
    for cell in ws[1]:
        cell.font = bold
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")


def write_summary_sheet(ws, summary: Dict[str, str]) -> None:
    title = summary.get("Report Title", "Conference Ledger Export")
    ws.cell(1, 1, title)
    row = 2
    for key, value in summary.items():
        if key == "Report Title":
            continue
        ws.cell(row, 1, f"{key}: {value}")
        row += 1
    ws.column_dimensions["A"].width = 80


def write_table_sheet(ws, headers: List[str], rows: List[Dict[str, str]]) -> None:
    ws.append(headers)
    for record in rows:
        ws.append([record.get(h, "") for h in headers])
    style_sheet(ws)
    for idx, header in enumerate(headers, start=1):
        width = max(len(header) + 4, 16)
        ws.column_dimensions[ws.cell(1, idx).column_letter].width = min(width, 28)


def write_notes_sheet(ws, notes: List[Tuple[str, str]]) -> None:
    for left, right in notes:
        ws.append([left, right])
    ws.column_dimensions["A"].width = 36
    ws.column_dimensions["B"].width = 100
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")


def data_to_workbook(data: Dict[str, object], output_path: Path) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = SUMMARY_SHEET
    write_summary_sheet(ws, data["summary"])
    write_table_sheet(wb.create_sheet(MAIN_SHEET), MAIN_HEADERS, data["main_pool"])
    write_table_sheet(wb.create_sheet(TRACKING_SHEET), TRACKING_HEADERS, data["tracking_list"])
    write_table_sheet(wb.create_sheet(AUDIT_SHEET), AUDIT_HEADERS, data["seed_audit"])
    write_notes_sheet(wb.create_sheet(NOTES_SHEET), data["search_notes"])
    wb.save(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync conference ledger between XLSX and Markdown.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("xlsx-to-md")
    p1.add_argument("xlsx")
    p1.add_argument("md")
    p1.add_argument("--audit-md", dest="audit_md")

    p2 = sub.add_parser("md-to-xlsx")
    p2.add_argument("md")
    p2.add_argument("xlsx")
    p2.add_argument("--audit-md", dest="audit_md")

    args = parser.parse_args()
    if args.cmd == "xlsx-to-md":
        data = workbook_to_data(Path(args.xlsx))
        data = attach_hints(data, read_existing_hints(Path(args.md)))
        Path(args.md).write_text(data_to_markdown(data), encoding="utf-8")
        if args.audit_md:
            Path(args.audit_md).write_text(audit_to_markdown(data), encoding="utf-8")
    else:
        data = markdown_to_data(Path(args.md), Path(args.audit_md) if args.audit_md else None)
        data_to_workbook(data, Path(args.xlsx))


if __name__ == "__main__":
    main()
