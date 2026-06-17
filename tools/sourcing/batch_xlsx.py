#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
batch_xlsx —— 把一整张招聘需求表(.xlsx / .csv)批量跑成检索清单。

逐行(每个岗位)自动识别领域,生成 LinkedIn 布尔串 + Google X-ray 串,
汇总成一个 Markdown 报告(可选再导出 CSV)。内核复用同目录 jd2search.py。

用法:
  python3 batch_xlsx.py --file 需求表.xlsx --out report.md
  python3 batch_xlsx.py --file 需求表.xlsx --out report.md --csv report.csv --region us
  python3 batch_xlsx.py --file 需求表.csv --region europe --target both --intent

列识别:自动找表头行,并按表头关键词映射"岗位名称/单位/工作内容等/人数"。
  也可手动覆盖:--title-col 2 --text-cols 3,4,5 --unit-col 1 --header-row 2 (均为 1 基列号/行号)

依赖:.xlsx 需要 openpyxl(pip install openpyxl);.csv 无需任何依赖。
合规:仅生成检索式供手动检索,勿用于自动化抓取。见 ../../compliance.md。
"""
import argparse
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import jd2search as j  # noqa: E402  复用内核

# 表头关键词(小写子串匹配)
H_TITLE = ["岗位名称", "职位名称", "岗位", "职位", "position", "title", "role", "job title"]
H_UNIT = ["单位", "部门", "事业部", "公司", "团队", "unit", "department", "company"]
H_COUNT = ["招收人数", "人数", "名额", "headcount", "count", "数量", "needed"]
H_TEXT = ["工作内容", "职责", "岗位职责", "专业方向", "其他条件", "任职要求", "任职资格",
          "技能", "背景", "证书", "职位描述", "岗位描述", "要求", "jd", "description",
          "responsib", "qualif", "requirement", "skill"]


class Opts:
    """给 jd2search.build_* 用的 args 替身。"""
    def __init__(self, region, target, signal, intent):
        self.region, self.target, self.signal, self.intent = region, target, signal, intent


def read_table(path):
    """返回 list[list[str]],单元格统一成去空白字符串。"""
    ext = os.path.splitext(path)[1].lower()
    rows = []
    if ext in (".xlsx", ".xlsm"):
        try:
            import openpyxl
        except ImportError:
            sys.exit("读取 .xlsx 需要 openpyxl,请先:pip install openpyxl(或把表另存为 .csv 再跑)")
        wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
        ws = wb.active
        for r in ws.iter_rows(values_only=True):
            rows.append(["" if c is None else str(c).strip() for c in r])
    elif ext == ".csv":
        with open(path, newline="", encoding="utf-8-sig") as f:
            for r in csv.reader(f):
                rows.append([("" if c is None else str(c).strip()) for c in r])
    else:
        sys.exit("仅支持 .xlsx / .csv,当前:%s" % ext)
    return rows


def find_header_row(rows):
    """第一行满足 ≥3 个非空单元格 → 视为表头。"""
    for i, r in enumerate(rows):
        if sum(1 for c in r if c) >= 3:
            return i
    return 0


def match_col(header, keys):
    for idx, h in enumerate(header):
        hl = h.lower()
        if any(k in hl for k in keys):
            return idx
    return None


def match_cols(header, keys, exclude):
    out = []
    for idx, h in enumerate(header):
        if idx in exclude:
            continue
        hl = h.lower()
        if any(k in hl for k in keys):
            out.append(idx)
    return out


def map_columns(header, args):
    if args.title_col or args.text_cols or args.unit_col:
        title = (args.title_col - 1) if args.title_col else match_col(header, H_TITLE)
        unit = (args.unit_col - 1) if args.unit_col else match_col(header, H_UNIT)
        count = match_col(header, H_COUNT)
        if args.text_cols:
            text = [int(x) - 1 for x in args.text_cols.split(",")]
        else:
            text = match_cols(header, H_TEXT, {title, unit, count})
    else:
        title = match_col(header, H_TITLE)
        unit = match_col(header, H_UNIT)
        count = match_col(header, H_COUNT)
        text = match_cols(header, H_TEXT, {title, unit, count})
    if title is None:
        title = 1 if len(header) > 1 else 0
    if not text:  # 兜底:除已知列外全部当 JD 文本
        text = [i for i in range(len(header)) if i not in {title, unit, count}]
    return {"title": title, "unit": unit, "count": count, "text": text}


def cell(row, idx):
    return row[idx] if (idx is not None and idx < len(row)) else ""


def fence(s):
    return "```\n%s\n```" % s


def process(data_rows, cols, opts, domains):
    """对表头之后的数据行逐行生成,返回结果 dict 列表。"""
    results = []
    for r in data_rows:
        if not any(c for c in r):
            continue
        title = cell(r, cols["title"])
        unit = cell(r, cols["unit"])
        count = cell(r, cols["count"])
        jd_text = " ".join(cell(r, i) for i in cols["text"]).strip()
        blob = (title + " " + jd_text).strip()
        if not blob:
            continue
        ranked = j.detect(blob, domains)
        if ranked:
            key, score, hits = ranked[0]
            d = domains[key]
            label = d["label_zh"]
            linkedin = j.build_linkedin(d, opts)
            xray = j.build_xray(d, opts)
            companies = " / ".join(d["companies"][:12])
            schools = " / ".join(d["schools"][:12])
        else:
            key, score, hits, label = "—", 0, [], "未识别(请手动指定方向)"
            stub = {"label_zh": label,
                    "titles": ["Research Scientist", "Research Engineer", "Postdoctoral"],
                    "keywords": ["<手动补研究方向关键词>"],
                    "companies": ["<目标公司>"], "schools": ["<目标院校>"]}
            linkedin = j.build_linkedin(stub, opts)
            xray = j.build_xray(stub, opts)
            companies = schools = "—"
        results.append(dict(title=title, unit=unit, count=count, key=key, label=label,
                            score=score, hits=hits, linkedin=linkedin, xray=xray,
                            companies=companies, schools=schools))
    return results


def render_md(results, src, opts):
    out = []
    out.append("# 批量检索清单:%s\n" % os.path.basename(src))
    out.append("> 参数:region=`%s` · target=`%s` · signal=`%s` · intent=`%s` · 共 %d 个岗位。"
               % (opts.region, opts.target, opts.signal, "on" if opts.intent else "off", len(results)))
    out.append("> 仅供手动检索,合规见 `../../compliance.md`。\n")
    out.append("## 汇总\n")
    out.append("| # | 单位 | 岗位 | 识别领域 | 命中 | 人数 |")
    out.append("|---|------|------|----------|------|------|")
    for i, x in enumerate(results, 1):
        out.append("| %d | %s | %s | %s `%s` | %d | %s |"
                   % (i, x["unit"] or "—", x["title"] or "—", x["label"], x["key"], x["score"], x["count"] or "—"))
    out.append("\n---\n")
    for i, x in enumerate(results, 1):
        out.append("## %d. %s%s\n" % (i, x["title"] or "(无岗位名)",
                                       ("(%s)" % x["unit"]) if x["unit"] else ""))
        line = "- 识别领域:**%s** `%s`" % (x["label"], x["key"])
        if x["hits"]:
            line += " | 命中信号:%s" % ", ".join(x["hits"][:12])
        out.append(line)
        if x["count"]:
            out.append("- 招收人数:%s" % x["count"])
        out.append("\n**LinkedIn 站内(关键词框):**\n")
        out.append(fence(x["linkedin"]))
        out.append("\n**Google X-ray:**\n")
        out.append(fence(x["xray"]))
        out.append("\n**facet 提示:** Location=`%s` · Current company=%s · School=%s\n"
                   % (" / ".join(j.REGIONS[opts.region]), x["companies"], x["schools"]))
        out.append("---\n")
    return "\n".join(out)


def write_csv(results, path):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["#", "单位", "岗位", "领域key", "领域", "命中数", "命中信号",
                    "招收人数", "LinkedIn检索式", "GoogleX-ray检索式"])
        for i, x in enumerate(results, 1):
            w.writerow([i, x["unit"], x["title"], x["key"], x["label"], x["score"],
                        ", ".join(x["hits"]), x["count"], x["linkedin"], x["xray"]])


def main():
    p = argparse.ArgumentParser(description="批量:招聘表(.xlsx/.csv) → 每岗位检索式 → Markdown/CSV。")
    p.add_argument("--file", "-f", required=True, help="需求表路径(.xlsx 或 .csv)")
    p.add_argument("--out", "-o", help="输出 Markdown 路径(默认打印到 stdout)")
    p.add_argument("--csv", dest="csv_out", help="同时导出 CSV 路径")
    p.add_argument("--region", "-r", default="all", choices=sorted(j.REGIONS), help="地区预设(默认 all)")
    p.add_argument("--target", "-t", default="company", choices=["company", "school", "both"],
                   help="X-ray 归属信号(默认 company)")
    p.add_argument("--signal", "-s", default="school", choices=["school", "surname", "both"],
                   help="华人信号(默认 school)")
    p.add_argument("--intent", action="store_true", help="追加回国意愿过滤")
    p.add_argument("--title-col", type=int, help="手动指定岗位名列(1 基)")
    p.add_argument("--unit-col", type=int, help="手动指定单位列(1 基)")
    p.add_argument("--text-cols", help="手动指定 JD 文本列,逗号分隔(1 基),如 3,4,5")
    p.add_argument("--header-row", type=int, help="(保留)手动指定表头行号(1 基)")
    args = p.parse_args()

    rows = read_table(args.file)
    if not rows:
        sys.exit("表为空。")
    header_i = (args.header_row - 1) if args.header_row else find_header_row(rows)
    header = rows[header_i]
    cols = map_columns(header, args)
    opts = Opts(args.region, args.target, args.signal, args.intent)
    domains = j.load_domains()

    results = process(rows[header_i + 1:], cols, opts, domains)
    if not results:
        sys.exit("没解析出岗位行。试试手动 --title-col / --text-cols / --header-row。")

    md = render_md(results, args.file, opts)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print("✓ Markdown 已写出:%s(%d 个岗位)" % (args.out, len(results)))
    else:
        print(md)
    if args.csv_out:
        write_csv(results, args.csv_out)
        print("✓ CSV 已写出:%s" % args.csv_out)


if __name__ == "__main__":
    main()
