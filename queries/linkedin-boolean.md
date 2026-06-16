# LinkedIn 站内布尔检索式(模块化积木)

> 把下面的"积木"按需 **AND** 起来贴进 LinkedIn 搜索关键词框(People 标签),地区/公司/院校尽量用**左侧 facet 过滤器**,关键词框只放 facet 覆盖不到的语义。
> 现成的整套组合见 `query-recipes.md`;占位清单(公司/院校/姓氏/信号词)见 `../reference/`。

---

## 0. 操作与语法

- **运算符大写**:`AND` `OR` `NOT`;短语用引号 `"machine learning"`;分组用括号 `( )`。
- **优先用 facet**:Location、Current company、School、Industry、(Recruiter 还有)Language、Seniority、Function。facet 比关键词干净得多。
- **关键词框只放语义信号**:博士、研究职位、行业方向、华人社群、回国意愿等。
- **OR 串别太长**:LinkedIn 对超长布尔串会截断/报错。公司、院校的长 OR 串请**分批跑**,或直接改用 facet 多选。
- **大小写不敏感**,但保持引号包短语。

---

## A. 华人代理信号(选一种或叠加;详见 `playbook.md` §3)

> ⚠️ 不要单用姓氏串(噪声大)。**首选"中国本科院校"或"华人社群"做高精度信号。**

**A1 · 华人专业社群 / 协会(高精度)**
```
("CSSA" OR "Chinese Students and Scholars Association" OR "SAPA" OR "Sino-American Pharmaceutical" OR "CAPA" OR "Chinese American Association" OR "ACSE" OR "CABS" OR "Chinese Biopharmaceutical" OR "1990 Institute")
```

**A2 · 中国大陆本科院校(高精度;更推荐用 School facet 选这些)**
```
("Tsinghua" OR "Peking University" OR "Fudan" OR "Zhejiang University" OR "Shanghai Jiao Tong" OR "University of Science and Technology of China" OR "Nanjing University" OR "Harbin Institute of Technology" OR "Huazhong University" OR "Xi'an Jiaotong" OR "Wuhan University" OR "Sun Yat-sen University" OR "Tianjin University" OR "Beihang" OR "Tongji" OR "Sichuan University" OR "Southeast University" OR "Beijing Institute of Technology")
```
> 完整中国院校别名见 `../reference/qs-top100-universities.md` 末尾"中国院校"段。

**A3 · 语言信号(中精度)**
```
(Mandarin OR "Simplified Chinese" OR "native Chinese")
```
> Recruiter 有 **Language=Mandarin** facet,比关键词更准。

**A4 · 拼音姓氏(中精度,只作补充扫描;每轮 10–15 个,分多批)**
```
(Wang OR Li OR Zhang OR Liu OR Chen OR Yang OR Huang OR Zhao OR Wu OR Zhou OR Xu OR Sun OR Ma OR Zhu OR Hu)
```
> 全量分批姓氏串见 `../reference/chinese-surnames-pinyin.md`。

---

## B. 博士 / 研究身份

**B1 · 博士学位**
```
("PhD" OR "Ph.D." OR "Ph.D" OR "Doctor of Philosophy" OR "Doctoral" OR "Doctorate" OR "DPhil" OR "ScD" OR "博士")
```

**B2 · 研究类职位(判断"研究专家",P1/P2 用)**
```
("Research Scientist" OR "Principal Scientist" OR "Senior Scientist" OR "Staff Scientist" OR "Research Fellow" OR "Postdoctoral" OR "Postdoc" OR "Principal Investigator" OR "Research Engineer" OR "Member of Technical Staff" OR "Distinguished Scientist" OR Professor OR "Research Associate")
```

> 想要"已毕业、非在读":排除 `NOT ("PhD Candidate" OR "PhD Student" OR "PhD researcher")`(按需,可能误伤刚毕业者)。

---

## C. 行业 / 研究方向(四选一或叠加)

**C1 · AI / 机器学习**
```
("Machine Learning" OR "Deep Learning" OR "Artificial Intelligence" OR "Computer Vision" OR "Natural Language Processing" OR "NLP" OR "Large Language Model" OR "LLM" OR "Reinforcement Learning" OR "Generative AI" OR "Speech Recognition" OR "Recommender" OR "MLOps" OR "AI Research")
```

**C2 · 医疗 / 生物医药 / 医疗器械**
```
("Drug Discovery" OR "Drug Development" OR "Medicinal Chemistry" OR "Computational Biology" OR "Bioinformatics" OR "Biostatistics" OR "Translational" OR "Immunology" OR "Oncology" OR "Clinical Development" OR "Pharmacology" OR "Cell Therapy" OR "Gene Therapy" OR "Biologics" OR "Medical Device" OR "Genomics" OR "Antibody" OR "CMC")
```

**C3 · 制造 / 工业 / 工艺**
```
("Process Engineering" OR "Manufacturing" OR "Process Development" OR "Process Integration" OR "Industrial Engineering" OR "Mechanical Engineering" OR "Automation" OR "Robotics" OR "Quality Engineering" OR "Reliability" OR "Yield" OR "Failure Analysis" OR "Semiconductor" OR "Wafer" OR "Additive Manufacturing")
```

**C4 · 材料科学**
```
("Materials Science" OR "Materials Engineer" OR "Materials Scientist" OR "Polymer" OR "Metallurgy" OR "Nanomaterials" OR "Nanotechnology" OR "Composite" OR "Battery" OR "Energy Storage" OR "Electrochemistry" OR "Catalysis" OR "Thin Film" OR "Semiconductor Materials" OR "Ceramic" OR "Coating" OR "Corrosion" OR "Crystal Growth")
```

---

## D. 雇主(P1 用;首选 **Current company facet**,关键词为备选)

> 公司名 OR 串很容易超长,**强烈建议用 Current company facet 多选**。下面按行业给"关键词备选"短串,真正全清单见 `../reference/target-companies.md`。

**D1 · AI / 科技 / 半导体(节选)**
```
(NVIDIA OR Google OR "Alphabet" OR Microsoft OR Apple OR Amazon OR Meta OR Intel OR IBM OR Qualcomm OR Broadcom OR "Samsung" OR TSMC OR AMD OR Micron OR Oracle)
```

**D2 · 医疗 / 制药(节选)**
```
("Johnson & Johnson" OR Pfizer OR Roche OR Genentech OR Novartis OR Merck OR AbbVie OR AstraZeneca OR "Bristol Myers Squibb" OR "Eli Lilly" OR Amgen OR "Gilead" OR Sanofi OR GSK OR Bayer OR Takeda OR Moderna OR Regeneron OR "Thermo Fisher" OR Medtronic OR Abbott)
```

**D3 · 制造 / 工业(节选)**
```
("General Electric" OR "GE Aerospace" OR Siemens OR Honeywell OR Boeing OR Airbus OR "3M" OR Caterpillar OR Toyota OR Bosch OR ABB OR "Schneider Electric" OR Emerson OR "Rockwell Automation" OR Hitachi OR "Mitsubishi Electric")
```

**D4 · 材料 / 化工(节选)**
```
(BASF OR Dow OR DuPont OR "3M" OR Corning OR "Saint-Gobain" OR Linde OR "Air Liquide" OR "Air Products" OR Covestro OR Solvay OR Evonik OR Toray OR "Shin-Etsu" OR "Applied Materials" OR "Lam Research" OR ASML OR Umicore)
```

---

## E. 院校(P2/P3 用;首选 **School facet** 选 QS 前 100)

> 校名 OR 串极易超长,**优先用 School facet 多选 QS100**。全名+别名清单见 `../reference/qs-top100-universities.md`。关键词备选(美国节选):
```
("MIT" OR "Massachusetts Institute of Technology" OR Stanford OR Harvard OR "UC Berkeley" OR "California Institute of Technology" OR Caltech OR Princeton OR Yale OR "Carnegie Mellon" OR "Cornell" OR "University of Chicago" OR Columbia OR "Johns Hopkins" OR "University of Michigan" OR UCLA OR "UC San Diego")
```

---

## F. 回国意愿(软信号,精度低,仅作试探,主要靠人工 §5)
```
("open to relocation" OR "open to relocate" OR "open to opportunities in China" OR "open to opportunities in Asia" OR "returning to China" OR "relocate to China" OR "back to China" OR "回国" OR "海归" OR "Greater China" OR "国内机会")
```

---

## 怎么把积木拼起来

把"公共前提"和"某个身份"AND 起来。例:**P1 · AI 方向 · 在 500 强做研究的华人博士**(地区、公司用 facet):
```
关键词框:
( "PhD" OR "Ph.D." OR "Doctoral" )
AND ( "Research Scientist" OR "Principal Scientist" OR "Senior Scientist" OR "Research Engineer" )
AND ( "Machine Learning" OR "Deep Learning" OR "Computer Vision" OR "NLP" OR "LLM" )
AND ( Mandarin OR "Tsinghua" OR "Peking University" OR "CSSA" )

左侧 facet:
  Location = United States / Canada / United Kingdom / Singapore …(海外)
  Current company = NVIDIA / Google / Meta / Microsoft …(D1 全清单)
```
更多现成组合(P1/P2/P3 × 行业 × 地区)直接抄 `query-recipes.md`。
