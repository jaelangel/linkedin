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

## 合规

本工具**只生成检索式**,供你**手动**搜索、查看公开 profile。请勿用于自动化抓取/群发。详见 `../../compliance.md`。
