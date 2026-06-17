# Worked Example:把"均胜高层次人才需求"表 → 可直接跑的检索方案

> 输入:`均胜高层次人才需求征集` 表(23 个博士岗)。
> 输出:按**岗位簇**给出针对性的 LinkedIn 站内布尔串 + Google X-ray 串,以及**每个领域真正该挖的海外公司/实验室与强校**。
> 通用方法见 `../playbook.md`;通用积木见 `../queries/`;本文件是把它们落到这张真实表上的示例。

---

## 0. 整体判断

- 招聘方:**均胜电子 / Joyson**(下属:均普具身智能、均胜具身智能、新能源研究院、均胜普瑞/Preh、均恩、均胜群英/Quin)。全球汽车电子 Tier-1,岗位均在**国内**,招"高层次人才"= **博士 / 研究院同等深度**。
- 与目标人群的契合:**海外华人博士 + 回国意愿**正是这批岗位要的人。所以 `../reference/return-intent-signals.md` 的回国信号打分在这里**权重很高**。
- **重要:目标公司不止 500 强**。具身智能顶尖人才集中在**机器人独角兽 + 高校实验室**;电力电子/电机的顶尖人才集中在**少数专业研究中心**(下面每簇都列了)。所以检索时"雇主/院校"维度要用**领域专属清单**,而不是只用 `../reference/target-companies.md` 的泛 500 强。

## 岗位 → 簇 映射

| 簇 | 对应表中岗位(行号) |
|---|---|
| **A. 具身大模型(VLA/世界模型/预训练后训练/Agent)** | R4, R5, R11, R12, R14, R20(灵巧手VLA) |
| **B. 机器人强化学习** | R5, R9, R13 |
| **C. 推理优化 / 边缘部署** | R3 |
| **D. 仿真 / 数据闭环 / 评测** | R6, R7, R8 |
| **E. 灵巧手 / 触觉力控 / 传感器** | R20, R23 |
| **F. 新能源 / 电力电子 / 电池** | R15, R16, R21, R24, R25 |
| **G. 智能座舱 / 车载光学 / HMI** | R17, R18, R19 |
| **H. 微电机 / 电磁仿真** | R22 |

> 公共前提(每簇都 AND):**海外地区(facet)+ 华人信号 + PhD**。华人信号统一用 `(Mandarin OR "Tsinghua" OR "Peking University" OR "Shanghai Jiao Tong" OR "University of Science and Technology of China" OR "CSSA")`,下面简写为 **〈华人〉**;不够再换 `../reference/chinese-surnames-pinyin.md` 的姓氏批次。地区统一用 Location facet 锁海外(美/加/英/欧/新/日),X-ray 里写 **〈地区〉**(见 `../queries/google-xray.md` §5)。

---

## A. 具身大模型(VLA / 世界模型 / 预训练 · 后训练 / Agent)

**研究方向关键词**
```
("VLA" OR "Vision-Language-Action" OR "OpenVLA" OR "RT-2" OR "diffusion policy" OR "world model" OR "foundation model" OR "embodied" OR "manipulation" OR "humanoid" OR "imitation learning" OR "robot learning" OR "robot foundation model")
```
**目标职位 title**
```
("Research Scientist" OR "Research Engineer" OR "Robotics Researcher" OR "Member of Technical Staff" OR "Applied Scientist" OR "Postdoctoral")
```
**海外该挖的公司 / 实验室**(用 Current company facet 多选)
```
机器人大模型/人形:Tesla (Optimus), Figure AI, Physical Intelligence, Skild AI, 1X Technologies,
  Agility Robotics, Apptronik, Sanctuary AI, Boston Dynamics, RAI Institute, Covariant, Dexterity,
  Intrinsic (Alphabet), NVIDIA (GEAR Lab / Isaac), Google DeepMind, Toyota Research Institute (TRI),
  Meta FAIR, Amazon Robotics
自驾(policy/RL 人才外溢):Waymo, Wayve, Cruise, Nuro, Zoox
```
**强校实验室**(用 School facet)
```
Stanford, UC Berkeley (BAIR), Carnegie Mellon (Robotics Institute), MIT (CSAIL), Georgia Tech,
University of Washington, UC San Diego, USC, Princeton, University of Michigan, Caltech,
ETH Zurich, EPFL, Imperial College London, Oxford, University of Toronto, NUS, NTU
```

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Ph.D." OR "Doctoral")
AND ("Research Scientist" OR "Research Engineer" OR "Robotics Researcher" OR "Member of Technical Staff" OR "Postdoctoral")
AND ("VLA" OR "Vision-Language-Action" OR "OpenVLA" OR "diffusion policy" OR "world model" OR "embodied" OR "manipulation" OR "humanoid" OR "imitation learning" OR "robot learning")
AND (Mandarin OR "Tsinghua" OR "Peking University" OR "Shanghai Jiao Tong" OR "University of Science and Technology of China" OR "CSSA")
```
> facet:Location=海外;Current company=上面公司清单(分批多选)。

**【Google X-ray】**
```
site:linkedin.com/in ("PhD" OR "Ph.D.") ("Research Scientist" OR "Research Engineer" OR "Robotics Researcher") ("VLA" OR "Vision-Language-Action" OR "diffusion policy" OR "world model" OR "embodied" OR "manipulation" OR "humanoid" OR "imitation learning") (Tesla OR Figure OR "Physical Intelligence" OR "Skild" OR "1X" OR "Agility Robotics" OR Apptronik OR NVIDIA OR DeepMind OR "Toyota Research") (Tsinghua OR "Peking University" OR Mandarin OR "CSSA") ("United States" OR "Bay Area" OR Seattle OR Boston OR "United Kingdom" OR Switzerland OR Singapore) -intitle:"profiles" -inurl:"/dir/"
```

---

## B. 机器人强化学习(R5 后训练 · R9 抓取RL · R13 RL研究员)

**关键词**
```
("reinforcement learning" OR "deep reinforcement learning" OR "PPO" OR "SAC" OR "TD-MPC" OR "model-based RL" OR "sim-to-real" OR "domain randomization" OR "manipulation" OR "grasping" OR "imitation learning" OR "RLHF")
```
**海外公司/实验室**:同 A(机器人公司)+ Berkeley RLL(Sergey Levine)、CMU、Stanford IRIS(Chelsea Finn)、ETH RSL、Google DeepMind、NVIDIA、TRI。

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Ph.D." OR "Postdoctoral")
AND ("Research Scientist" OR "Research Engineer" OR "Robotics Researcher")
AND ("reinforcement learning" OR "PPO" OR "SAC" OR "sim-to-real" OR "manipulation" OR "grasping" OR "imitation learning")
AND 〈华人〉
```
**【Google X-ray】**
```
site:linkedin.com/in ("PhD" OR "Postdoctoral") ("reinforcement learning" OR "PPO" OR "SAC" OR "sim-to-real" OR "manipulation" OR "grasping") ("robot" OR "robotics" OR "manipulation") (Tsinghua OR "Peking University" OR Mandarin OR "CSSA") ("United States" OR "United Kingdom" OR Switzerland OR Canada) -intitle:"profiles" -inurl:"/dir/"
```

---

## C. 推理优化 / 边缘部署(R3:TensorRT/ONNX/量化/Orin/Atlas)

**关键词**
```
("TensorRT" OR "ONNX" OR "ONNX Runtime" OR "quantization" OR "INT8" OR "model compression" OR "pruning" OR "knowledge distillation" OR "CUDA" OR "inference optimization" OR "edge inference" OR "Jetson" OR "Orin" OR "TVM" OR "operator fusion")
```
**海外公司**:NVIDIA(TensorRT/推理团队)、Qualcomm AI、Google(Edge/TFLite)、Meta(PyTorch/ExecuTorch)、Apple(CoreML)、AMD、Intel、各机器人公司的 deployment 团队。

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Ph.D." OR "Master")
AND ("Deep Learning" OR "Machine Learning" OR "MLSys" OR "Inference" OR "Deployment")
AND ("TensorRT" OR "ONNX" OR "quantization" OR "INT8" OR "model compression" OR "CUDA" OR "edge inference" OR "Jetson" OR "Orin")
AND 〈华人〉
```
**【Google X-ray】**
```
site:linkedin.com/in ("PhD" OR "Ph.D.") ("TensorRT" OR "ONNX" OR "quantization" OR "INT8" OR "model compression" OR "CUDA" OR "edge inference" OR "Orin") ("Research Engineer" OR "Deep Learning" OR "MLSys" OR "Inference") (NVIDIA OR Qualcomm OR Google OR Meta OR Apple) (Tsinghua OR "Peking University" OR Mandarin) ("United States" OR "Bay Area" OR Toronto) -intitle:"profiles" -inurl:"/dir/"
```

---

## D. 仿真 / 数据闭环 / 评测(R6 评测 · R7 仿真 · R8 数据)

**关键词**
```
("Isaac Sim" OR "Isaac Lab" OR "MuJoCo" OR "Gazebo" OR "PyBullet" OR "domain randomization" OR "synthetic data" OR "sim-to-real" OR "digital twin" OR "physics simulation" OR "benchmark" OR "data pipeline" OR "teleoperation")
```
**海外公司/实验室**:NVIDIA(Omniverse/Isaac)、各机器人公司仿真团队、自驾仿真(Applied Intuition、Waymo、Wayve)、Google DeepMind(MuJoCo)、高校机器人实验室。

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Master" OR "Ph.D.")
AND ("Research Engineer" OR "Research Scientist" OR "Simulation Engineer" OR "Robotics")
AND ("Isaac Sim" OR "Isaac Lab" OR "MuJoCo" OR "Gazebo" OR "domain randomization" OR "sim-to-real" OR "digital twin" OR "synthetic data" OR "teleoperation")
AND 〈华人〉
```
**【Google X-ray】**
```
site:linkedin.com/in ("PhD" OR "Master") ("Isaac Sim" OR "MuJoCo" OR "Gazebo" OR "sim-to-real" OR "domain randomization" OR "digital twin" OR "synthetic data") ("robot" OR "robotics" OR "simulation") (Tsinghua OR "Peking University" OR Mandarin OR "CSSA") ("United States" OR Germany OR Switzerland OR Singapore) -intitle:"profiles" -inurl:"/dir/"
```

---

## E. 灵巧手 / 触觉力控 / 传感器(R20 灵巧手VLA · R23 力觉触觉算法)

**关键词**
```
("dexterous manipulation" OR "dexterous hand" OR "tactile sensing" OR "tactile sensor" OR "force/torque sensor" OR "six-axis force" OR "force control" OR "compliant control" OR "impedance control" OR "GelSight" OR "grasping" OR "in-hand manipulation")
```
**海外公司/实验室**:Shadow Robot、Sanctuary AI、Tesla(hand team)、Meta(DIGIT 触觉)、GelSight、各人形公司的手部团队;高校:MIT、CMU、Stanford、UW、Columbia(Matei Ciocarlie)、Imperial。

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Ph.D." OR "Postdoctoral")
AND ("Research Scientist" OR "Robotics Researcher" OR "Research Engineer")
AND ("dexterous" OR "tactile" OR "force control" OR "compliant control" OR "force/torque" OR "grasping" OR "in-hand manipulation")
AND 〈华人〉
```
**【Google X-ray】**
```
site:linkedin.com/in ("PhD" OR "Postdoctoral") ("dexterous" OR "tactile" OR "force control" OR "force/torque sensor" OR "grasping" OR "in-hand manipulation") ("robot" OR "manipulation" OR "hand") (Tsinghua OR "Peking University" OR Mandarin OR "CSSA") ("United States" OR "United Kingdom" OR Switzerland) -intitle:"profiles" -inurl:"/dir/"
```

---

## F. 新能源 / 电力电子 / 电池(R15 功率电子 · R16 电源 · R21 电芯算法 · R24 汽车新能源 · R25 高压配电)

**关键词(按子方向取)**
```
功率电子/驱动:("power electronics" OR "traction inverter" OR "DC-DC" OR "on-board charger" OR "OBC" OR "SiC" OR "GaN" OR "wide bandgap" OR "EMC" OR "motor drive")
电池/BMS:("battery management" OR "BMS" OR "state of charge" OR "SOC estimation" OR "SOH" OR "electrochemical model" OR "cell modeling" OR "lithium-ion" OR "thermal management")
```
**海外该挖的公司**(用 Current company facet)
```
车企三电:Tesla, Rivian, Lucid Motors, GM, Ford
Tier-1/半导体:Bosch, Continental, BorgWarner, Vitesco, Infineon, onsemi, Wolfspeed, Texas Instruments,
  Navitas, Power Integrations, ABB, Siemens
电池:Panasonic Energy, LG Energy Solution, Samsung SDI, Northvolt, QuantumScape, Solid Power
```
**强校 / 专业研究中心**(电力电子&电机的世界级中心,部分不在 QS 综合前100,但本领域顶尖):
```
Virginia Tech (CPES), University of Wisconsin–Madison (WEMPEC), University of Tennessee,
Georgia Tech, University of Michigan, MIT, Stanford, ETH Zurich (PES), RWTH Aachen, KU Leuven,
University of Sheffield / Newcastle(电机方向,英国)
```
> 招聘逻辑提示:这一簇看重**专业深度 > 学校综合排名**。建议放宽"QS 前100"硬卡,改用"上述专业中心 + 目标公司经历"作资历信号(并在 `../compliance.md` 框架下,把硬标准落在岗位相关资历上)。

**【LinkedIn 站内 · 关键词框 · 功率电子例】**
```
("PhD" OR "Ph.D." OR "Doctoral")
AND ("Power Electronics Engineer" OR "Research Engineer" OR "Power Electronics" OR "Powertrain" OR "Research Scientist")
AND ("traction inverter" OR "DC-DC" OR "on-board charger" OR "SiC" OR "GaN" OR "power electronics" OR "motor drive")
AND 〈华人〉
```
**【Google X-ray · 电池算法例】**
```
site:linkedin.com/in ("PhD" OR "Ph.D.") ("battery management" OR "BMS" OR "SOC estimation" OR "SOH" OR "electrochemical model" OR "cell modeling") ("algorithm" OR "Research" OR "Estimation") (Tesla OR Rivian OR Bosch OR Panasonic OR "LG Energy" OR "Samsung SDI" OR QuantumScape) (Tsinghua OR "Shanghai Jiao Tong" OR "Harbin Institute" OR Mandarin) ("United States" OR Germany OR "South Korea") -intitle:"profiles" -inurl:"/dir/"
```

---

## G. 智能座舱 / 车载光学 / HMI(R17 HMI · R18 显示光学 · R19 座舱AI多模态)

**关键词(按子方向)**
```
车载光学/HUD:("HUD" OR "AR-HUD" OR "head-up display" OR "waveguide" OR "optical design" OR "freeform optics" OR "Zemax" OR "CODE V" OR "Mini-LED" OR "VCSEL" OR "laser display" OR "imaging optics" OR "illumination")
座舱AI/多模态:("smart cockpit" OR "in-cabin" OR "driver monitoring" OR "multimodal" OR "HCI" OR "human-machine interface" OR "speech interaction" OR "ToF" OR "3D perception" OR "in-cabin perception")
```
**海外该挖的公司**
```
Tier-1/座舱:Continental, Bosch, Visteon, Harman (Samsung), Panasonic Automotive, LG Display, Aptiv
HUD/光学:Texas Instruments (DLP), Envisics, WayRay, Lumus, DigiLens
AR/VR 光学(人才外溢):Apple (Vision Pro), Meta Reality Labs, Magic Leap, Microsoft (HoloLens), Google
```
**强校(光学顶尖院系,注意不全在 QS 综合前100)**
```
University of Rochester (Institute of Optics), University of Arizona (Wyant College of Optical Sciences),
MIT, Stanford, Caltech, Imperial College London, ETH Zurich, KAIST
```
**【LinkedIn 站内 · 车载光学例】**
```
("PhD" OR "Ph.D." OR "Doctoral")
AND ("Optical Engineer" OR "Optical Scientist" OR "Research Scientist" OR "Display Engineer")
AND ("HUD" OR "AR-HUD" OR "waveguide" OR "optical design" OR "freeform" OR "Zemax" OR "Mini-LED" OR "laser display" OR "imaging optics")
AND 〈华人〉
```
**【Google X-ray · 座舱多模态AI例】**
```
site:linkedin.com/in ("PhD" OR "Ph.D.") ("multimodal" OR "driver monitoring" OR "in-cabin" OR "3D perception" OR "ToF" OR "speech interaction" OR "HCI") ("cockpit" OR "automotive" OR "perception" OR "interaction") (Continental OR Bosch OR Visteon OR Harman OR Apple OR "Meta Reality") (Tsinghua OR "Peking University" OR Mandarin) ("United States" OR Germany OR "United Kingdom") -intitle:"profiles" -inurl:"/dir/"
```

---

## H. 微电机 / 电磁仿真(R22:车规级 BLDC/PMSM,ANSYS Maxwell)

**关键词**
```
("BLDC" OR "PMSM" OR "stepper motor" OR "brushless motor" OR "electric machine" OR "electromagnetic" OR "FEA" OR "ANSYS Maxwell" OR "JMAG" OR "motor design" OR "actuator" OR "magnetics" OR "traction motor")
```
**海外公司**:Nidec、Bosch、Maxon、Johnson Electric、Continental、Mabuchi、Allied Motion、ABB、Siemens、Tesla/Rivian(电机团队)。
**强校(电机方向世界级,英国尤强)**:University of Sheffield(Z.Q. Zhu 团队)、Newcastle University、University of Nottingham、University of Wisconsin–Madison(WEMPEC)、Georgia Tech、ETH。

**【LinkedIn 站内 · 关键词框】**
```
("PhD" OR "Ph.D." OR "Doctoral")
AND ("Motor Design Engineer" OR "Electric Machine" OR "Research Engineer" OR "Electromagnetic" OR "Research Scientist")
AND ("BLDC" OR "PMSM" OR "stepper" OR "electric machine" OR "electromagnetic" OR "ANSYS Maxwell" OR "motor design" OR "actuator" OR "traction motor")
AND 〈华人〉
```
**【Google X-ray】**
```
site:linkedin.com/in ("PhD" OR "Ph.D.") ("BLDC" OR "PMSM" OR "electric machine" OR "electromagnetic" OR "ANSYS Maxwell" OR "motor design" OR "traction motor") (Nidec OR Bosch OR Maxon OR "Johnson Electric" OR Continental OR Tesla OR ABB OR Siemens) (Tsinghua OR "Harbin Institute" OR "Xi'an Jiaotong" OR Mandarin) ("United States" OR "United Kingdom" OR Germany OR Japan) -intitle:"profiles" -inurl:"/dir/"
```

---

## 这张表的"回国意愿"特别提示

这些都是**国内岗位招高层次人才**,所以回国信号尤其值得抓(详见 `../reference/return-intent-signals.md`):
- 这批人很多是**博士毕业 3–7 年、在海外大厂/名校实验室**的华人——正处回流窗口。
- 对**具身智能 / 新能源**方向,国内机会(均胜这类 Tier-1 + 国内人形/新能源浪潮)对海外华人吸引力强,首触时点明"国内具身智能/新能源产业爆发 + 平台 + 安家/科研经费"转化率高。
- 看到 profile 提**国内人才计划申报 / 关注国内机器人公司 / 近期开 Open-to-work** = 强信号,优先联系。

## 怎么扩展

- 把上面每簇的"海外公司/实验室"沉淀进 `../reference/`(可新建 `companies-by-niche.md`),下次同领域直接复用。
- 招聘方给新岗位时,按同一套路:**抽研究方向关键词 → 配目标职位 title → 列该领域海外公司/实验室与强校 → AND 上〈华人〉+PhD+〈地区〉**。
- 需要的话我可以把这套"岗位 JD → 检索式"的转换做成一个**小脚本**:贴 JD 文本,自动吐出 LinkedIn 串和 X-ray 串。
