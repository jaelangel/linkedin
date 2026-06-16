# 现成配方(挑一个,复制就用)

> 每个配方给两版:**【LinkedIn 站内】**(关键词框布尔 + 该用哪些 facet)和 **【Google X-ray】**(直接 Google 跑)。
> 三类人群见 `../playbook.md` §0:**P1 企业研究专家 / P2 高校研究专家 / P3 名校毕业生**。占位清单见 `../reference/`。

---

## 怎么选配方

```
先问:你更看重当前"在哪做研究"还是"什么学历背景"?
├─ 在 500 强企业做研究        → P1,再按 AI/医疗/制造/材料 选行业子配方
├─ 在 QS100 高校做研究        → P2
└─ 只要 QS100 名校学历(扩面) → P3
然后:用"地区速查"(google-xray.md §5)替换地区词,锁定海外。
最后:回国意愿别在检索层硬筛,留到资格审查(playbook.md §5)。
```

---

# P1 · 在世界 500 强做研究的海外华人博士

> 公共做法:**Location facet 锁海外**;**Current company facet 选目标 500 强**(`../reference/target-companies.md`);关键词框放"博士 + 研究职位 + 行业方向 + 华人信号"。

## P1-A · AI 方向

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Ph.D." OR "Doctoral")
AND ("Research Scientist" OR "Applied Scientist" OR "Principal Scientist" OR "Research Engineer" OR "Member of Technical Staff")
AND ("Machine Learning" OR "Deep Learning" OR "Computer Vision" OR "NLP" OR "LLM" OR "Generative AI" OR "Reinforcement Learning")
AND (Mandarin OR "Tsinghua" OR "Peking University" OR "Shanghai Jiao Tong" OR "CSSA")
```
> facet:Location = 美/加/英/欧/新…;Current company = D1 清单(NVIDIA、Google、Meta、Microsoft、Apple、Amazon、Intel、IBM、Qualcomm…)。

**【Google X-ray】**(美国例)
```
site:linkedin.com/in ("PhD" OR "Ph.D.") ("Research Scientist" OR "Applied Scientist" OR "Research Engineer") ("Machine Learning" OR "Deep Learning" OR "Computer Vision" OR "LLM") (NVIDIA OR Google OR Meta OR Microsoft OR Apple OR Amazon OR Intel) (Tsinghua OR "Peking University" OR Mandarin OR "CSSA") ("United States" OR "Bay Area" OR Seattle OR "New York") -intitle:"profiles" -inurl:"/dir/"
```

## P1-B · 医疗 / 生物医药

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Ph.D.")
AND ("Principal Scientist" OR "Senior Scientist" OR "Research Scientist" OR "Research Fellow" OR "Director, Research")
AND ("Drug Discovery" OR "Bioinformatics" OR "Computational Biology" OR "Immunology" OR "Oncology" OR "Medicinal Chemistry" OR "Cell Therapy" OR "Gene Therapy" OR "Biologics")
AND (Mandarin OR "SAPA" OR "Tsinghua" OR "Peking University" OR "Fudan")
```
> facet:Location 海外;Current company = D2(Pfizer、Roche、Genentech、Novartis、Merck、AbbVie、Eli Lilly、Amgen、Gilead、BMS、Sanofi、AstraZeneca、Moderna、Regeneron…)。

**【Google X-ray】**
```
site:linkedin.com/in ("PhD" OR "Ph.D.") ("Principal Scientist" OR "Senior Scientist" OR "Research Scientist") ("Drug Discovery" OR "Bioinformatics" OR "Immunology" OR "Oncology" OR "Cell Therapy") (Pfizer OR Roche OR Genentech OR Novartis OR Merck OR AbbVie OR "Eli Lilly" OR Amgen OR Gilead) (Tsinghua OR "Peking University" OR Fudan OR "SAPA" OR Mandarin) ("United States" OR Boston OR "San Diego" OR "New Jersey") -intitle:"profiles" -inurl:"/dir/"
```

## P1-C · 制造 / 工业

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Doctoral")
AND ("Research Scientist" OR "Principal Engineer" OR "R&D Engineer" OR "Process Engineer" OR "Staff Engineer")
AND ("Semiconductor" OR "Process Development" OR "Manufacturing" OR "Process Integration" OR "Automation" OR "Robotics" OR "Reliability" OR "Yield")
AND (Mandarin OR "Tsinghua" OR "Shanghai Jiao Tong" OR "Harbin Institute" OR "Xi'an Jiaotong")
```
> facet:Location 海外;Current company = D3 + 半导体(Intel、TSMC、Applied Materials、Siemens、Bosch、GE、Honeywell、ABB、Mitsubishi Electric、Hitachi…)。

**【Google X-ray】**
```
site:linkedin.com/in ("PhD" OR "Doctoral") ("Process Engineer" OR "R&D Engineer" OR "Principal Engineer" OR "Research Scientist") ("Semiconductor" OR "Manufacturing" OR "Process Development" OR "Automation" OR "Robotics") (Intel OR TSMC OR "Applied Materials" OR Siemens OR Bosch OR "General Electric" OR Honeywell OR ABB) (Tsinghua OR "Shanghai Jiao Tong" OR "Harbin Institute" OR Mandarin) ("United States" OR Germany OR Netherlands OR Japan) -intitle:"profiles" -inurl:"/dir/"
```

## P1-D · 材料科学

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Doctoral")
AND ("Research Scientist" OR "Senior Scientist" OR "Materials Scientist" OR "Principal Scientist" OR "R&D")
AND ("Materials Science" OR "Polymer" OR "Battery" OR "Energy Storage" OR "Nanomaterials" OR "Catalysis" OR "Thin Film" OR "Electrochemistry" OR "Semiconductor Materials" OR "Composite")
AND (Mandarin OR "Tsinghua" OR "University of Science and Technology of China" OR "Zhejiang University")
```
> facet:Location 海外;Current company = D4(BASF、Dow、DuPont、Corning、3M、Saint-Gobain、Solvay、Covestro、Toray、Shin-Etsu、Applied Materials、Umicore…)。

**【Google X-ray】**
```
site:linkedin.com/in ("PhD" OR "Doctoral") ("Research Scientist" OR "Senior Scientist" OR "Materials Scientist") ("Materials Science" OR "Polymer" OR "Battery" OR "Nanomaterials" OR "Catalysis" OR "Thin Film") (BASF OR Dow OR DuPont OR Corning OR "Applied Materials" OR "3M" OR Solvay OR Covestro OR "Shin-Etsu") (Tsinghua OR "University of Science and Technology of China" OR "Zhejiang University" OR Mandarin) ("United States" OR Germany OR Japan) -intitle:"profiles" -inurl:"/dir/"
```

---

# P2 · 在 QS 前 100 高校做研究的海外华人博士

> 公共做法:**Location facet 锁海外**;**School facet** 或 **Current company facet** 选 QS100 院校(`../reference/qs-top100-universities.md`);关键词框放"研究职位 + 华人信号(+ 行业方向)"。

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Ph.D." OR "Postdoctoral" OR "Postdoc")
AND ("Professor" OR "Assistant Professor" OR "Associate Professor" OR "Research Scientist" OR "Research Fellow" OR "Principal Investigator" OR "Lecturer")
AND (Mandarin OR "Tsinghua" OR "Peking University" OR "Fudan" OR "CSSA" OR "University of Science and Technology of China")
AND ("Machine Learning" OR "Materials Science" OR "Bioinformatics" OR "Drug Discovery" OR "Semiconductor" OR "Robotics")
```
> facet:Location 海外;Current company / School = QS100(MIT、Stanford、Berkeley、Oxford、Cambridge、ETH、NUS、NTU…,按地区分批)。行业那行可删/可换。

**【Google X-ray】**
```
site:linkedin.com/in ("PhD" OR "Postdoctoral" OR "Postdoc") ("Professor" OR "Assistant Professor" OR "Research Scientist" OR "Research Fellow" OR "Principal Investigator") (MIT OR Stanford OR Harvard OR "UC Berkeley" OR Caltech OR Oxford OR Cambridge OR "Imperial College" OR ETH OR "National University of Singapore" OR Nanyang) (Tsinghua OR "Peking University" OR Fudan OR Mandarin OR "CSSA") -intitle:"profiles" -inurl:"/dir/"
```

---

# P3 · 毕业于 QS 前 100 的海外华人(扩面)

> 身份最宽:只要"教育经历 ∈ QS100"。**School facet 选 QS100** + Location facet 锁海外。常见高价值子集:**中国本科 + 海外 QS100 博士**(典型海归画像)。

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Ph.D." OR "Doctoral" OR "Master")
AND (Mandarin OR "Tsinghua" OR "Peking University" OR "Fudan" OR "Zhejiang University" OR "Shanghai Jiao Tong" OR "CSSA")
```
> facet:School = QS100(MIT、Stanford、Oxford、Cambridge、Toronto、ETH、NUS…);Location = 海外。
> 想只要博士:把 `Master` 去掉。想只要"中国本科+海外名校",School facet 同时勾选**一所中国本科**和**一所 QS100 海外校**。

**【Google X-ray】**(中国本科 + 海外 QS100 博士)
```
site:linkedin.com/in ("PhD" OR "Ph.D." OR "Doctoral") (MIT OR Stanford OR Harvard OR "UC Berkeley" OR Caltech OR Oxford OR Cambridge OR "Imperial College London" OR UCL OR "University of Toronto" OR McGill OR "ETH Zurich" OR EPFL OR "National University of Singapore") (Tsinghua OR "Peking University" OR Fudan OR "Zhejiang University" OR "Shanghai Jiao Tong") ("United States" OR Canada OR "United Kingdom" OR Singapore OR Germany OR Australia) -intitle:"profiles" -inurl:"/dir/"
```

---

## 通用调参建议

- **召回太少** → 删掉行业那行;把华人信号从"院校"放宽到 `Mandarin`;地区放宽到整国;OR 串拆批多跑几轮。
- **噪声太多** → 加 facet(Location/Company/School)替代关键词;华人信号收紧成"中国本科院校";职位词收紧到研究岗;加 `NOT (Sales OR Recruiter OR "Account Manager")`。
- **要"已毕业非在读"** → 追加 `NOT ("PhD Candidate" OR "PhD Student")`(注意可能误伤刚毕业)。
- **要回国意愿** → 命中后按 `../playbook.md` §5 打分,不在检索层硬筛。
- **去重 / 存档** → 用 `linkedin.com/in/<id>` 作唯一键记表,遵守 `../compliance.md`。
