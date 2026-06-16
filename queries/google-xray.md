# Google / Bing X-ray 检索式

> **X-ray** = 用搜索引擎的 `site:` 直接搜 LinkedIn **公开** profile,绕开站内搜索配额,适合**没有付费账号 / 破了 Commercial Use Limit / 想批量导链接到表格**的场景。
> 你仍然是**人工**点开公开页面核对——这不是抓取,请保持手动、适量(见 `../compliance.md`)。

---

## 0. 原理与语法

- 基础前缀:`site:linkedin.com/in`(只搜个人 profile;`/in/` 是个人页路径)。
- Google 语法:`OR` 大写;短语 `"..."`;分组 `( )`;排除 `-词`;站内 `site:`。
- **地区**:LinkedIn 公开页全球都在 `linkedin.com/in`,所以**地点要写进检索词**(profile 文本里通常含 city/region),例:`("San Francisco" OR "Boston" OR "United States")`。
- **降噪**:加 `-intitle:"profiles"` `-inurl:"/dir/"` `-inurl:"/pub/dir"` 去掉目录页/聚合页。
- **国别站**:可用 `site:cn.linkedin.com/in`、`site:uk.linkedin.com/in` 等子域偏向某地区(非绝对)。

通用骨架:
```
site:linkedin.com/in
( "PhD" OR "Ph.D." OR "Doctoral" )
( <华人信号> )
( <博士研究/行业方向> )
( <公司 或 院校> )
( <地区词> )
-intitle:"profiles" -inurl:"/dir/"
```

---

## 1. P1 · 海外华人博士 · 在 500 强做研究

**P1-AI(美国)**
```
site:linkedin.com/in ("PhD" OR "Ph.D." OR "Doctoral") ("Research Scientist" OR "Applied Scientist" OR "Research Engineer") ("Machine Learning" OR "Deep Learning" OR "Computer Vision" OR "NLP" OR "LLM") (NVIDIA OR Google OR Meta OR Microsoft OR Apple OR Amazon OR Intel OR Qualcomm) (Tsinghua OR "Peking University" OR Fudan OR Mandarin OR "CSSA") ("United States" OR "San Francisco" OR "Seattle" OR "New York" OR "Boston") -intitle:"profiles" -inurl:"/dir/"
```

**P1-医疗/生物医药(美国)**
```
site:linkedin.com/in ("PhD" OR "Ph.D.") ("Principal Scientist" OR "Senior Scientist" OR "Research Scientist") ("Drug Discovery" OR "Bioinformatics" OR "Immunology" OR "Oncology" OR "Medicinal Chemistry" OR "Cell Therapy") (Pfizer OR Roche OR Genentech OR Novartis OR Merck OR AbbVie OR "Eli Lilly" OR Amgen OR Gilead OR "Bristol Myers Squibb") (Tsinghua OR "Peking University" OR "Fudan" OR "SAPA" OR Mandarin) ("United States" OR "Boston" OR "San Diego" OR "New Jersey" OR "South San Francisco") -intitle:"profiles" -inurl:"/dir/"
```

**P1-制造/工业(美国+欧洲)**
```
site:linkedin.com/in ("PhD" OR "Doctoral") ("Process Engineer" OR "R&D Engineer" OR "Research Scientist" OR "Principal Engineer") ("Semiconductor" OR "Manufacturing" OR "Process Development" OR "Automation" OR "Robotics") (Intel OR TSMC OR "Applied Materials" OR Siemens OR Bosch OR "General Electric" OR Honeywell OR ABB) (Tsinghua OR "Shanghai Jiao Tong" OR "Harbin Institute" OR Mandarin) ("United States" OR Germany OR Netherlands) -intitle:"profiles" -inurl:"/dir/"
```

**P1-材料科学(美国+欧洲)**
```
site:linkedin.com/in ("PhD" OR "Doctoral") ("Research Scientist" OR "Senior Scientist" OR "Materials Scientist") ("Materials Science" OR "Polymer" OR "Battery" OR "Nanomaterials" OR "Catalysis" OR "Thin Film" OR "Electrochemistry") (BASF OR Dow OR DuPont OR Corning OR "Applied Materials" OR "3M" OR Solvay OR Covestro OR "Shin-Etsu") (Tsinghua OR "University of Science and Technology of China" OR "Zhejiang University" OR Mandarin) ("United States" OR Germany OR Japan) -intitle:"profiles" -inurl:"/dir/"
```

---

## 2. P2 · 海外华人博士 · 在 QS 前 100 高校做研究

```
site:linkedin.com/in ("PhD" OR "Ph.D." OR "Postdoctoral" OR "Postdoc") ("Professor" OR "Assistant Professor" OR "Research Scientist" OR "Research Fellow" OR "Principal Investigator" OR "Postdoctoral") (MIT OR Stanford OR Harvard OR "UC Berkeley" OR Caltech OR Princeton OR "Carnegie Mellon" OR Oxford OR Cambridge OR "Imperial College" OR ETH OR "National University of Singapore" OR "Nanyang") (Tsinghua OR "Peking University" OR Fudan OR Mandarin OR "CSSA") ("Machine Learning" OR "Materials Science" OR "Bioinformatics" OR "Drug Discovery" OR "Semiconductor") -intitle:"profiles" -inurl:"/dir/"
```
> 把第 4 组(QS 院校)按地区拆小批量跑,召回更全。完整院校别名见 `../reference/qs-top100-universities.md`。

---

## 3. P3 · 海外华人 · 毕业于 QS 前 100(身份最宽)

```
site:linkedin.com/in ("PhD" OR "Ph.D." OR "Doctoral") (MIT OR Stanford OR Harvard OR "UC Berkeley" OR Caltech OR Princeton OR Yale OR Cornell OR Columbia OR "Carnegie Mellon" OR Oxford OR Cambridge OR "Imperial College London" OR UCL OR "University of Toronto" OR McGill OR "ETH Zurich" OR EPFL OR "National University of Singapore") (Tsinghua OR "Peking University" OR Fudan OR "Zhejiang University" OR "Shanghai Jiao Tong" OR Mandarin OR "CSSA") ("United States" OR Canada OR "United Kingdom" OR Singapore OR Germany OR Australia) -intitle:"profiles" -inurl:"/dir/"
```
> 这里 `(Tsinghua OR …)` 作华人/本科信号,`(MIT OR …)` 作 QS100 学历信号——两者都命中即"中国本科 + 海外名校博士"的典型海归画像。

---

## 4. 加"回国意愿"过滤(可选,缩小到有回流信号者)

在任意上面的串后追加:
```
("open to relocation" OR "open to opportunities in China" OR "returning to China" OR "Greater China" OR "回国" OR "海归")
```
> 会大幅缩小结果且漏掉很多"没明说但可挖"的人——建议**先不加**,把回国意愿留到人工资格审查阶段(`playbook.md` §5)。

---

## 5. 地区词速查(替换检索式里的地区组)

| 地区 | 可用词 |
|---|---|
| 美国 | `"United States"`,城市:`"San Francisco" OR "Bay Area" OR Seattle OR "New York" OR Boston OR "San Diego" OR "Los Angeles" OR Austin OR Chicago` |
| 加拿大 | `Canada OR Toronto OR Vancouver OR Montreal OR Waterloo` |
| 英国 | `"United Kingdom" OR London OR Cambridge OR Oxford OR Manchester OR Edinburgh` |
| 欧陆 | `Germany OR Munich OR Berlin OR Netherlands OR Amsterdam OR Switzerland OR Zurich OR France OR Paris` |
| 新加坡 | `Singapore` |
| 澳洲 | `Australia OR Sydney OR Melbourne` |
| 日本 | `Japan OR Tokyo` |

---

## 6. Bing / DuckDuckGo 变体

语法基本相同(`site:linkedin.com/in`,`OR` 大写,`"短语"`,`-排除`)。换引擎可在某引擎被限速或结果不同时补盲。Bing 对 `site:` 与 LinkedIn 收录通常不错,值得作为 Google 的备份。

---

## 7. 实操提示

- **分批 + 翻页**:院校/公司 OR 串太长会降低召回质量;**拆成小批量、跑多轮**反而更全。
- **导出**:把命中的 `linkedin.com/in/...` 链接收集到表格,回站内逐个核对(§4 清单),用 URL 去重。
- **别自动化**:不要用脚本翻 Google 结果页批量抓链接——手动翻页、适量即可,既稳又合规。
