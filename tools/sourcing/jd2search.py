#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jd2search —— 贴一段招聘 JD,自动识别领域并生成 LinkedIn 站内布尔检索式 + Google X-ray 检索式。

目标人群:海外华人博士(可选回国意愿),用于寻访。配套说明见 ../../README.md 与 ../../queries/。
领域知识库在同目录 domains.json,可自由增删。

用法示例:
  python3 jd2search.py --file jd.txt                 # 从文件读 JD
  cat jd.txt | python3 jd2search.py                  # 从 stdin 读
  python3 jd2search.py "负责VLA具身大模型预训练 强化学习 sim-to-real"   # 直接传文本
  python3 jd2search.py --file jd.txt --region us --target both --intent
  python3 jd2search.py --domain power_electronics    # 跳过识别,强制领域
  python3 jd2search.py --list-domains                # 看所有领域

合规:仅生成检索式供你手动搜索/查看公开 profile;勿用于自动化抓取。详见 ../../compliance.md。
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOMAINS_PATH = os.path.join(HERE, "domains.json")

# ---- 公共积木 ----
PHD_FULL = ["PhD", "Ph.D.", "Ph.D", "Doctoral", "Doctorate", "Doctor of Philosophy"]
PHD_SHORT = ["PhD", "Ph.D."]
CHINESE_SCHOOL = ["Mandarin", "Tsinghua", "Peking University", "Fudan", "Shanghai Jiao Tong",
                  "Zhejiang University", "University of Science and Technology of China", "CSSA"]
CHINESE_SHORT = ["Tsinghua", "Peking University", "Mandarin", "CSSA"]
SURNAME_BATCH = ["Wang", "Li", "Zhang", "Liu", "Chen", "Yang", "Huang", "Zhao", "Wu", "Zhou",
                 "Xu", "Sun", "Ma", "Zhu", "Hu"]
INTENT = ["open to relocation", "open to opportunities in China", "returning to China",
          "Greater China", "回国", "海归"]
REGIONS = {
    "us": ["United States", "Bay Area", "San Francisco", "Seattle", "New York", "Boston", "San Diego"],
    "canada": ["Canada", "Toronto", "Vancouver", "Montreal", "Waterloo"],
    "uk": ["United Kingdom", "London", "Cambridge", "Oxford", "Manchester", "Edinburgh"],
    "europe": ["Germany", "Munich", "Netherlands", "Amsterdam", "Switzerland", "Zurich", "France", "Paris"],
    "singapore": ["Singapore"],
    "japan": ["Japan", "Tokyo"],
    "australia": ["Australia", "Sydney", "Melbourne"],
    "all": ["United States", "Canada", "United Kingdom", "Singapore", "Germany", "Switzerland", "Australia"],
}


def q(term):
    """含空格/标点的检索词加引号;纯字母数字(含中文)裸用。"""
    return term if term.replace("&", "").isalnum() else '"%s"' % term


def or_group(terms):
    return "(" + " OR ".join(q(t) for t in terms) + ")"


def load_domains():
    with open(DOMAINS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return {k: v for k, v in data.items() if not k.startswith("_")}


def trigger_regex(t):
    """ASCII 触发词用词边界匹配避免误命中;含非 ASCII 的用子串匹配。"""
    if all(ord(c) < 128 for c in t):
        return re.compile(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])", re.I)
    return None


def detect(text, domains):
    """返回 [(key, score, matched_triggers), ...] 按命中数降序。"""
    low = text.lower()
    scored = []
    for key, d in domains.items():
        hits = []
        for t in d.get("triggers", []):
            rx = trigger_regex(t)
            if rx is not None:
                if rx.search(text):
                    hits.append(t)
            elif t.lower() in low:
                hits.append(t)
        if hits:
            scored.append((key, len(hits), hits))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored


def chinese_signal(signal):
    if signal == "surname":
        return SURNAME_BATCH
    if signal == "both":
        return CHINESE_SCHOOL + SURNAME_BATCH
    return CHINESE_SCHOOL


def build_linkedin(d, args):
    lines = [or_group(PHD_FULL),
             "AND " + or_group(d["titles"]),
             "AND " + or_group(d["keywords"]),
             "AND " + or_group(chinese_signal(args.signal))]
    if args.intent:
        lines.append("AND " + or_group(INTENT))
    return "\n".join(lines)


def build_xray(d, args):
    groups = [or_group(PHD_SHORT), or_group(d["titles"][:4]), or_group(d["keywords"])]
    if args.target in ("school", "both"):
        groups.append(or_group(d["schools"][:10]))
    if args.target in ("company", "both"):
        groups.append(or_group(d["companies"][:10]))
    groups.append(or_group(CHINESE_SHORT))
    groups.append(or_group(REGIONS[args.region]))
    if args.intent:
        groups.append(or_group(INTENT))
    return "site:linkedin.com/in " + " ".join(groups) + ' -intitle:"profiles" -inurl:"/dir/"'


def emit(key, d, args, score=None, hits=None):
    head = "领域识别: %s  [%s]" % (d["label_zh"], key)
    if score is not None:
        head += "  | 命中信号(%d): %s" % (score, ", ".join(hits[:12]))
    print("=" * 78)
    print(head)
    print("=" * 78)
    print("\n— LinkedIn 站内(粘进关键词框 / People 标签)—\n")
    print(build_linkedin(d, args))
    print("\n  facet 提示:")
    print("  • Location           = " + " / ".join(REGIONS[args.region]))
    print("  • Current company(多选)= " + " / ".join(d["companies"][:12]))
    print("  • School(P2/P3 可选)  = " + " / ".join(d["schools"][:12]))
    print("\n— Google X-ray(直接 Google 跑)—\n")
    print(build_xray(d, args))
    print()


def main():
    p = argparse.ArgumentParser(
        description="贴 JD → 生成 LinkedIn 布尔 + Google X-ray 检索式(海外华人博士寻访)。",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("text", nargs="?", help="JD 文本(也可用 --file 或 stdin)")
    p.add_argument("--file", "-f", help="从文件读取 JD")
    p.add_argument("--domain", "-d", help="强制指定领域 key(跳过自动识别)")
    p.add_argument("--top", "-n", type=int, default=1, help="输出命中最高的前 N 个领域(默认 1)")
    p.add_argument("--region", "-r", default="all", choices=sorted(REGIONS),
                   help="地区预设(默认 all 海外主要地区)")
    p.add_argument("--target", "-t", default="company", choices=["company", "school", "both"],
                   help="X-ray 用公司还是院校做归属信号(默认 company)")
    p.add_argument("--signal", "-s", default="school", choices=["school", "surname", "both"],
                   help="华人信号用中国院校(默认)/拼音姓氏/两者")
    p.add_argument("--intent", action="store_true", help="追加回国意愿过滤(会缩小结果)")
    p.add_argument("--list-domains", action="store_true", help="列出所有领域 key 并退出")
    args = p.parse_args()

    domains = load_domains()

    if args.list_domains:
        print("可用领域:")
        for k, d in domains.items():
            print("  %-20s %s" % (k, d["label_zh"]))
        return

    if args.domain:
        if args.domain not in domains:
            sys.exit("未知领域 '%s'。用 --list-domains 查看。" % args.domain)
        emit(args.domain, domains[args.domain], args)
        return

    # 取 JD 文本
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    elif args.text:
        text = args.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        sys.exit("请提供 JD:--file 文件 / 直接传文本 / 管道 stdin。或用 --list-domains。")

    if not text.strip():
        sys.exit("JD 文本为空。")

    ranked = detect(text, domains)
    if not ranked:
        print("⚠ 未识别到明确领域。可用 --domain 指定,或看 --list-domains。\n")
        print("仍给一个通用骨架(只含 博士 + 华人信号 + 地区,需你手动补研究方向关键词):\n")
        skeleton = {"label_zh": "通用骨架", "titles": ["Research Scientist", "Research Engineer", "Postdoctoral"],
                    "keywords": ["<在此补研究方向关键词>"], "companies": ["<目标公司>"], "schools": ["<目标院校>"]}
        emit("generic", skeleton, args)
        return

    if len(ranked) > 1:
        print("领域候选排名:", ", ".join("%s(%d)" % (k, s) for k, s, _ in ranked[:5]), "\n")
    for key, score, hits in ranked[: max(1, args.top)]:
        emit(key, domains[key], args, score, hits)


if __name__ == "__main__":
    main()
