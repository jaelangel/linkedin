# 华人姓名信号:常见姓氏拼音

> 用途:作为**华人代理信号的补充扫描**(`../playbook.md` §3 的"中精度"层)。
> ⚠️ **不要单用姓氏串**——噪声大(同名非华人、跨族裔),务必与"中国本科院校 / 华人社群 / Mandarin"等更高精度信号 **AND** 起来用。
> 用法:每轮取**一批(10–15 个)**贴进关键词框做 `OR`,分多轮跑,合并去重。

---

## 一、中国大陆姓氏(汉语拼音)—— 主力

按人口大致从高到低,已切成可直接复制的批次。

**Batch 1**
```
(Wang OR Li OR Zhang OR Liu OR Chen OR Yang OR Huang OR Zhao OR Wu OR Zhou OR Xu OR Sun OR Ma OR Zhu OR Hu)
```
**Batch 2**
```
(Guo OR Lin OR He OR Gao OR Luo OR Zheng OR Liang OR Xie OR Song OR Tang OR Han OR Feng OR Deng OR Cao OR Peng)
```
**Batch 3**
```
(Zeng OR Xiao OR Tian OR Dong OR Pan OR Yuan OR Cai OR Jiang OR Yu OR Du OR Ye OR Cheng OR Wei OR Su OR Lu)
```
**Batch 4**
```
(Ding OR Ren OR Yao OR Shen OR Zhong OR Cui OR Tan OR Lu OR Fan OR Liao OR Shi OR Qin OR Mao OR Bai OR Xue)
```
**Batch 5**
```
(Yan OR Long OR Duan OR Hao OR Kong OR Shao OR Wan OR Qian OR Gu OR Meng OR Wu OR Jia OR Fu OR Yin OR Lai)
```

> 说明:`Lu` 可对应 卢/陆/路,`Yu` 对应 于/余/俞/虞,`Jiang` 对应 江/姜/蒋——拼音同形会带来噪声,靠组合其他信号消解。

---

## 二、含特殊拼写的姓氏(大陆拼音里的少数情况)

```
(Lyu OR Lv OR "Lü"   ← 吕)
(Lye OR Nye)
(Xu OR Hsu)          ← 徐/许(Hsu 多为台湾拼写)
```

---

## 三、粤语 / 台湾 / 海外常见罗马拼写(华人但非大陆拼音)

港澳、东南亚、北美老移民、台湾背景的华人,姓氏拼写不同,**若你的"华人"范围包含他们**,补这一批:

**粤语拼写(港澳/广东裔常见)**
```
(Wong OR Lee OR Chan OR Cheung OR Cheong OR Lau OR Ng OR Ho OR Leung OR Tsang OR Yip OR Ip OR Choi OR Tsoi OR Lam OR Chu OR Chow OR Kwok OR Lo OR Yuen OR Mak OR Lai OR Hui OR Fong OR Tam OR Pang OR Szeto)
```

**台湾 / 威妥玛拼写常见**
```
(Hsu OR Hsieh OR Tsai OR Chang OR Hwang OR Chiang OR Chien OR Chao OR Kuo OR Tseng OR Hsiung OR Chien OR Chou OR Cheng OR Tsao OR Chu)
```

> 注意:这些拼写**也可能是韩裔/越裔等**(如 Lee 也常见于韩裔)。所以**粤/台拼写更要配合其他华人信号**使用,否则误判率高。

---

## 四、使用建议

1. **优先级**:中国本科院校 / 华人社群 / Mandarin **>** 姓氏串。姓氏串只在前者召回不够时补量。
2. **小批量、多轮**:别把几十个姓氏塞一个超长 OR(会被截断),按上面 Batch 分轮跑。
3. **务必 AND 高精度信号**:例如
   ```
   (Batch 1 姓氏…) AND ("PhD" OR "Doctoral") AND (Mandarin OR "Tsinghua" OR "Peking University")
   ```
4. **名(given name)一般不入检索**:拼音名变化太多、噪声极大,留到人工核对阶段看。
