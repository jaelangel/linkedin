# jd2search —— 贴 JD,自动生成检索式

把一段招聘 JD 自动识别成领域,生成可直接粘贴的 **LinkedIn 站内布尔串** + **Google X-ray 串**(面向"海外华人博士"寻访)。纯 Python 标准库,**零依赖**。

## 用法

```bash
# 从文件读 JD
python3 jd2search.py --file jd.txt

# 管道 stdin
cat jd.txt | python3 jd2search.py

# 直接传文本
python3 jd2search.py "负责VLA具身大模型预训练，强化学习，sim-to-real"

# 常用选项组合
python3 jd2search.py --file jd.txt --region us --target both --intent

# 强制领域(跳过识别)/ 查看所有领域
python3 jd2search.py --domain power_electronics
python3 jd2search.py --list-domains
```

## 选项

| 选项 | 说明 | 默认 |
|---|---|---|
| `text` / `--file` / stdin | JD 来源(三选一) | — |
| `--domain, -d` | 强制领域 key,跳过自动识别 | 自动识别 |
| `--top, -n` | 输出命中最高的前 N 个领域 | 1 |
| `--region, -r` | 地区预设:`us/canada/uk/europe/singapore/japan/australia/all` | all |
| `--target, -t` | X-ray 归属信号用 `company` / `school` / `both`(企业岗用 company,找高校研究者/毕业生用 school) | company |
| `--signal, -s` | 华人信号:`school`(中国院校+Mandarin)/ `surname`(拼音姓氏)/ `both` | school |
| `--intent` | 追加回国意愿过滤(会缩小结果) | 关 |
| `--list-domains` | 列出所有领域 key | — |

## 它怎么工作

1. 把 JD 文本与 `domains.json` 里每个领域的 `triggers` 比对(ASCII 词用词边界匹配避免误命中,中文用子串),按命中数排序。
2. 取最高领域,组装:`(博士) AND (目标职位) AND (研究方向关键词) AND (华人信号) [AND (回国意愿)]`。
3. X-ray 版另加"目标公司/院校"和"地区"组,并加 `-intitle:"profiles" -inurl:"/dir/"` 降噪。
4. 同时打印 **facet 提示**(Location / Current company / School 该选什么)。

## 扩展

- **加领域 / 改清单**:直接编辑 `domains.json`(label_zh、triggers、keywords、titles、companies、schools)。检索词**不要自带引号**,脚本会自动给含空格/标点的词加引号。
- **加地区**:在 `jd2search.py` 顶部 `REGIONS` 里加一项。
- 领域知识来源与方法论见仓库根目录 `../../playbook.md`、`../../examples/joyson-roles.md`。

## 批量:整张需求表一次跑完(`batch_xlsx.py`)

吃一张招聘需求表(`.xlsx` / `.csv`),**逐个岗位**自动识别领域、生成检索式,汇总成 Markdown(可选再导出 CSV)。

```bash
# 把整张 Excel 跑成一份 Markdown + 一份 CSV
python3 batch_xlsx.py --file 需求表.xlsx --out report.md --csv report.csv --region us

# CSV 输入、欧洲地区、X-ray 同时带公司+院校、附回国意愿
python3 batch_xlsx.py --file 需求表.csv --region europe --target both --intent
```

- **自动列识别**:找表头行,按表头关键词映射"岗位名称 / 单位 / 工作内容等 / 招收人数";把"工作内容+专业方向+其他条件"等多列合并成 JD 文本喂给识别。
- **手动覆盖**(列识别不准时):`--title-col 2 --unit-col 1 --text-cols 3,4,5 --header-row 2`(均为 1 基)。
- **输出**:Markdown 含①汇总表(岗位→识别领域→命中→人数)②每岗位的 LinkedIn 串 + X-ray 串 + facet 提示;CSV 便于导进表格/分配给 sourcer。
- **依赖**:`.xlsx` 需 `openpyxl`(`pip install openpyxl`);`.csv` 零依赖。
- 跨领域岗位取**命中最高**的那个;不满意可对该岗位单独用 `jd2search.py --domain xxx` 重出,或 `--top 2` 看候选。

## 合规

本工具**只生成检索式**,供你**手动**搜索、查看公开 profile。请勿用于自动化抓取/群发。详见 `../../compliance.md`。
