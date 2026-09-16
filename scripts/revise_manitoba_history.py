from pathlib import Path
import re

DATE = "2026-09-16"
ZH_PATH = Path("曼尼托巴水电局的创业史.md")
EN_PATH = Path("manitoba-hydro-pscad-rtds-history.md")


def rep(text, old, new, label):
    if old not in text:
        raise RuntimeError(f"Expected text missing for {label}: {old[:120]}")
    return text.replace(old, new, 1)


def opt(text, old, new):
    return text.replace(old, new, 1) if old in text else text


def sec(text, start, end, body, label):
    a = text.find(start)
    if a < 0:
        raise RuntimeError(f"Start heading missing for {label}")
    b = text.find(end, a + len(start))
    if b < 0:
        raise RuntimeError(f"End heading missing for {label}")
    return text[:a] + body.rstrip() + "\n\n" + text[b:]


def set_date(text, lang):
    text = re.sub(r'^updated:\s*"[^"]+"', f'updated: "{DATE}"', text, count=1, flags=re.M)
    if lang == "zh":
        text = re.sub(r'更新时间：\d{4}-\d{2}-\d{2}', f'更新时间：{DATE}', text, count=1)
    else:
        text = re.sub(r'Updated: \d{4}-\d{2}-\d{2}', f'Updated: {DATE}', text, count=1)
    return text


# ---------------- Chinese edition ----------------
zh = set_date(ZH_PATH.read_text(encoding="utf-8"), "zh")

north_zh = "曼尼托巴电力系统最重要的架构特点，可以用四个字概括：**北电南送**。北方纳尔逊河流域拥有重要的水电资源，南方则集中了温尼伯及主要负荷。工程师必须让遥远的水流，成为城市里稳定可用的电流。"
zh = rep(
    zh,
    north_zh,
    north_zh + "\n\n纳尔逊河流域的水电开发也给北方克里族社区带来了长期影响。Churchill River Diversion等工程改变了河湖水位，造成淹没并扰动传统的出行、捕鱼、狩猎和土地利用。1977年的Northern Flood Agreement及之后的实施、补偿与和解协议，是这段工程史的另一条需要单独讲述的线索。本文不在这里展开，但技术史若完全略过它，叙述会失去一部分现实背景。",
    "Indigenous context zh",
)

zh = rep(
    zh,
    "1982年，研究中心对传统模拟式直流输电器询价，显然价格太贵，买不起。",
    "1982年，研究中心对传统模拟式直流输电模拟装置询价，报价显然超出其可承受范围。",
    "analog simulator wording zh",
)

zh = rep(
    zh,
    "据Wierckx口述，早期曾委托外部公司开发数字实时模拟器，但结果未达目标。随后，在Woodford主持下，才组织了一个小团队在内部继续尝试。",
    "据Wierckx口述，早期曾委托外部公司开发数字实时模拟器，但结果未达目标。随后，在Woodford主持下，才组织了一个小团队在内部继续尝试。RTDS Technologies后来的官方时间线把这项内部开发项目的启动年份明确列为**1986年**。",
    "1986 milestone zh",
)

zh = rep(
    zh,
    "### 五、先让一个滤波支路跑起来\n\nWierckx后来回忆，团队最初展示的，并不是今天宣传册里那种庞大的交直流网络，而只是一个滤波支路。",
    "### 五、先让一个滤波支路跑起来\n\n到**1989年**，研究中心实现了后来被RTDS官方历史称为“世界首次实时数字HVDC仿真”的里程碑。这个节点很重要：数字实时仿真已经从研发设想进入能够承担直流系统研究的工作状态，但离独立公司成立还有五年。\n\nWierckx后来回忆，团队最初展示的，只是一个滤波支路，而不是今天宣传册里那种庞大的交直流网络。",
    "1989 milestone zh",
)

zh = rep(
    zh,
    "在Wierckx的回忆中，团队最初开发RTDS，是为了给研究中心提供研究工具，并没有一开始就准备成立商业公司。公开发表研究成果后，Hitachi、ABB等企业表达了兴趣，商业化才逐渐成为现实议题。\n\n他还回忆，研究中心的非营利定位，使董事会认为不宜在中心内部直接完成这项商业化。1994年，四位参与开发的员工离开中心，成立RTDS公司；技术通过特许权使用费协议提供给新公司。",
    "在Wierckx的回忆中，团队最初开发RTDS，是为了给研究中心提供研究工具，并没有一开始就准备成立商业公司。公开发表研究成果后，Hitachi、ABB等企业表达了兴趣，商业化才逐渐成为现实议题。\n\n**1993年，第一套商业RTDS安装交付给日本日立。**Ametani后来回顾这段技术史时明确写到，首套RTDS由Hitachi, Japan购买。这个时间点早于RTDS Technologies成立，说明产品的第一次商业安装发生在研究中心体系内，随后才完成组织上的独立。\n\n研究中心的非营利定位，使董事会认为不宜在中心内部继续承担完整商业经营。**1994年**，四位参与开发的员工离开中心，成立RTDS Technologies；技术通过特许权使用费协议提供给新公司。于是早期时间线完整地连起来：1986年项目启动，1989年实现实时HVDC仿真，1993年完成首套商业安装，1994年成立独立公司。",
    "1993 Hitachi and 1994 milestone zh",
)

section16_zh = '''### 十六、第二股浪潮：新能源大量接入的电力电子化电力系统

第一股浪潮把电磁暂态工具推向更大的交直流系统；第二股浪潮改变了这些工具在电力系统工程流程中的位置。

风电、光伏、储能以及越来越多由电力电子装置接口的设备，使快速控制从少数高压直流站和FACTS装置扩散到大量电源与负荷接入点。同步机占主导的系统积累了长期的转子运动、励磁调节和传统保护经验；换流器大量接入以后，锁相、限流、故障穿越、控制模式切换以及装置之间的动态相互作用，都可能直接改变扰动结果。

一个功率并不突出的设备，在局部电网较弱或多个控制器通过同一网络相互作用时，也可能成为系统研究的关键对象。潮流、机电暂态和电磁暂态仍各有任务，模型选择取决于当前关注的现象需要保留哪些动态细节。

2016年8月16日的美国南加州Blue Cut Fire，把“模型细节是否足够”变成了一次可以量化的运行事件。当天山火造成重要输电走廊多次故障；11:45的一次故障后，接近**1,200 MW**光伏出力消失。NERC的调查特别指出，这些光伏电站并没有因为故障而被线路直接切除，而是在电网暂态过程中自行停止出力。调查发现，一类逆变器会依据近乎瞬时的频率测量采取保护动作，故障期间的畸变波形可能造成错误跳闸；大量逆变器还采用momentary cessation，在电压越过设定范围时暂时停止电流注入，部分装置随后又以较慢斜率恢复。

这件事后来暴露出的规模比单次事故更大。NERC在Blue Cut之后发布Alert，行业反馈显示，超过**6,200 MW**、约占申报并网逆变器容量**37%**的光伏资源，存在报告所描述的错误频率计算/保护动作风险。到2017年8月底，相关受影响容量约68%已完成纠正；到10月9日，涉事制造商在CAISO范围内的输电侧光伏逆变器已有超过97%实施相应修改。

这些数字把模型问题从抽象方法争论带回工程现场。若研究模型只写着“某处接入若干MW光伏”，却没有对应现场逆变器的测频方法、低电压期间的停发逻辑、恢复斜率和控制版本，即使网络做得很大，仍可能漏掉真正决定扰动传播的机制。

澳大利亚AEMO把模型质量进一步嵌入并网流程。其现行Modelling Requirements要求申请者向AEMO和接入网络服务商提交能够代表电站结构与动态性能的模型包，并明确使用PSS®E和PSCAD™/EMTDC™开展并网研究。R1模型包至少要在投运前三个月提交；最终R2数据和模型验证报告则要在现场最终投运试验完成后三个月内提交。模型还要随着项目阶段持续更新。

这里同时存在知识产权与系统安全的约束。AEMO对不可公开的PSCAD/EMTDC模型采用受限位置存储和有限人员访问，并在项目推进、投运和后续运行中维护模型版本。设备厂商需要保护控制实现，系统运营者则需要获得可运行、可复现、可验证的模型；两者必须在同一个工程流程里同时成立。

第一股浪潮的硬数字是26个Rack、近1000片DSP、511母线和1306母线；第二股浪潮的硬约束越来越多地表现为模型版本、现场验证、保密分发和变更管理。算力仍然重要，但更快的处理器无法补齐缺失的控制逻辑，也无法自动纠正与现场装置不一致的模型。

对PSCAD与RTDS来说，新能源接入、储能控制、系统强度、局部相互作用和保护适应性扩大了应用范围，同时把产品竞争推向模型承载、验证工作流、知识产权保护和版本治理。原来那条从电网需求到研究工具的道路没有结束，只是进入了一个模型更多、参与者更多、责任边界也更复杂的系统。'''
zh = sec(
    zh,
    "### 十六、第二股浪潮：新能源大量接入的电力电子化电力系统",
    "### 十七、PSCAD的成长，并不只有求解器一条线",
    section16_zh,
    "section 16 zh",
)

zh = rep(
    zh,
    "## 第三部　走向出售：技术成功之后，还有企业的难题",
    "## 第三部　组织分岔与出售：技术成功之后，还有企业的难题",
    "Part III title zh",
)

pscad3_zh = '''### 二十、PSCAD留在省属体系内

同一时期，PSCAD走的是另一条组织路线。2021年曼尼托巴水电局重组MHI时，逐步收缩的是MHIUS国际咨询业务；官方公告同时明确，MHI继续作为曼尼托巴水电局的子公司存在，面向技术解决方案的业务继续以MHI名义经营和推广。PSCAD因此留在省属公用事业集团体系内，没有像RTDS那样进入独立公司出售的路径。

2024年7月，曼尼托巴省政府宣布恢复MHI国际咨询业务，并开始重建完整业务范围，包括重新参与全球能源项目的技术、咨询和培训服务。到2026年3月，PSCAD官方仍在发布v5.1.0版本介绍和技术培训资料。2021年的业务收缩没有让PSCAD退场，它经历的是母公司业务边界调整以及后来的重新扩展。

于是，同一个温尼伯技术生态形成了两种长期组织结果。RTDS在独立经营二十八年后进入AMETEK这一上市工业技术集团；PSCAD继续留在曼尼托巴水电局的全资子公司体系内经营。前者获得更大的仪器、销售与资本平台，后者保留了与省属公用事业和MHI技术业务的组织联系。

这个对照把“组织与阶段是否相称”变成了具体案例。产品需要的资本、国际渠道、治理方式、客户支持和长期研发条件不同，长期归宿也可以不同。评价这些组织选择，最终仍要看技术是否继续发展、客户是否持续得到支持，以及责任和收益是否能够清楚承接。'''
zh = rep(zh, "### 二十、RTDS换了主人", pscad3_zh + "\n\n### 二十一、RTDS换了主人", "PSCAD Part III section zh")
zh = rep(zh, "### 二十一、出售，是成功的句号，还是另一段责任的开始", "### 二十二、出售之后：商业化成果与持续责任", "final section renumber zh")

zh = rep(
    zh,
    "金额之外，另一个更关键的问题是：究竟谁卖了什么？",
    "交易结构首先要分清MHI持有的权益与RTDS私人股东持有的公司股权。",
    "sale framing zh",
)

mhi_zh = "水电局截至2022年12月31日的季度报告说明，在这次收购过程中，MHI的特许权使用费收益权在交割前转换为RTDS股权，再随交易处置。相应季度报告披露的收益约为6800万加元；2022—2023财年年报披露的一次性收益为6900万加元，并明确此后的特许权使用费将终止。"
zh = rep(
    zh,
    mhi_zh,
    mhi_zh + "\n\n水电局/MHI这一侧因此有公开财报可以追踪；RTDS私人股东这一侧的公开材料明显更少。在本文能够核实的公司历史、创始人访谈、AMETEK公告和监管文件中，没有找到一份由原股东或收购方发布的材料，说明私人股东为什么在2022年选择出售，也没有找到完整披露交割前最终股东结构的公开文件。创始工程师陆续进入职业生涯后期、接班安排，以及一个约75人规模的专业公司面对全球服务网络时可能遇到的扩张边界，都可以作为研究问题，但目前没有可靠公开证据把其中任何一项确认成交易的直接动因。AMETEK公告解释了买方的战略逻辑，没有披露卖方的决策过程。这个证据空白应当保留下来。",
    "seller evidence gap zh",
)

zh_rewrites = [
    ("但本文要讲的，不是大坝与输电线路的工程建设。本文的重点是另一种不那么容易从照片上看见的基础设施——电力系统的分析与仿真工具。", "本文把重点放在另一种不那么容易从照片上看见的基础设施——电力系统的分析与仿真工具。"),
    ("把这层关系弄清楚，才看得懂故事最后的出售，也才看得懂故事中间那些真正值得借鉴的管理选择。", "这层关系决定了后文应如何理解公司化、许可收益和最终出售。"),
    ("Dommel真正重要的贡献，不只是写出了一段程序，而是把输电线路的行波处理、集中参数元件的离散计算、节点分析和稀疏矩阵求解组织成了一套可以在数字计算机上推广的电磁暂态计算框架。", "Dommel的核心贡献，是把输电线路的行波处理、集中参数元件的离散计算、节点分析和稀疏矩阵求解组织成一套可以在数字计算机上推广的电磁暂态计算框架。"),
    ("所以，EMTP与EMTDC之间最准确的关系，不是“一个软件改出了另一个软件”，而是**同一个数学祖先，两套独立代码**。", "因此，更准确的关系是：**EMTP与EMTDC有同一个数学祖先，但形成了两套独立代码**。"),
    ("因此，EMTDC并不是为了“再做一个EMTP”而诞生。它一开始解决的是一个非常具体的问题：", "EMTDC从一开始就围绕一个非常具体的问题展开："),
    ("这种组织方式的价值，不在于牌子上写了多少家单位，而在于能否越过平常的单位边界，及时调用真正知道问题的人。", "这种组织方式允许团队越过平常的单位边界，及时调用真正知道问题的人。"),
    ("这里的关键，不是简单买到一颗更快的芯片，而是把算法、硬件分工、数据交换和网络模型一起设计。", "团队必须把算法、硬件分工、数据交换和网络模型一起设计。"),
    ("“买不起”只提供了压力。真正把压力变成产品机会的，是先前积累的电磁暂态知识、对现场问题的理解、新处理器出现的时机，以及一个愿意在失败后继续投入的小团队。", "“买不起”提供了压力；先前积累的电磁暂态知识、对现场问题的理解、新处理器出现的时机，以及一个愿意在失败后继续投入的小团队，共同把压力转化成了产品机会。"),
    ("公开资料没有展开那个问题的全部细节，也没有必要把它渲染成“避免了一次大停电”。真正重要的是另一件事：这个工具已经能够在真实控制器投运以前，找出有工程意义的问题。", "公开资料没有展开那个问题的全部细节，因此没有必要把它渲染成“避免了一次大停电”。可以确认的是，这个工具已经能够在真实控制器投运以前找出有工程意义的问题。"),
    ("真正值得借鉴的，不是“一定要工程师集体创业”，而是：当一个产品已经超出原机构合适的经营边界时，能否设计一种允许它继续成长、又不抹去原始贡献者权益的道路。", "更值得研究的是组织边界的转换：当产品已经超出原机构合适的经营范围时，能否让它继续成长，同时保留原始贡献者的合理权益。"),
    ("因此，工具一旦深入制造商的工程流程，就会积累一类不容易复制的知识——不是只有“客户名单”，而是大量关于真实项目怎样失败、怎样修正、怎样验证的经验。", "因此，工具一旦深入制造商的工程流程，就会积累大量关于真实项目怎样失败、怎样修正、怎样验证的经验；这种知识比一张“客户名单”更难复制。"),
    ("这不是说混合仿真错了。恰恰相反，EMT与机电暂态混合仿真后来又重新回到RTDS及相关研究中，而且在今天的大规模新能源系统研究里仍然很有价值。真正发生的事情是：在相当长的一段产品发展期，RTDS把主要赌注押在了另一边——**让硬件、并行算法和通信能力不断追赶电网规模。**", "EMT与机电暂态混合仿真后来重新回到RTDS及相关研究中，在今天的大规模新能源系统研究里仍然很有价值。只是相当长的一段产品发展期内，RTDS把主要赌注押在了另一条路线——**让硬件、并行算法和通信能力不断追赶电网规模。**"),
    ("曼尼托巴真正值得借鉴的地方，也许就在这里。它不是偶然完成了几次成功的“成果转化”，而是逐渐形成了一条能够自己循环的链条：", "曼尼托巴更值得研究的是这种长期循环能力："),
    ("因此，实时仿真产品真正困难的升级，不是“换一颗更快的芯片”，而是同时处理两件事：一边把新计算能力释放出来，一边尽量保护用户已经建立的工程体系。", "因此，实时仿真产品的升级必须同时处理两件事：释放新的计算能力，并尽量保护用户已经建立的工程体系。"),
    ("这不是说技术创业无足轻重，而是提醒我们，不同业务的规模和风险性质不能混淆。", "这提醒我们区分不同业务的规模与风险性质。"),
    ("这为中国的科研成果转化提供了一个可以认真研究的例子，却不是一份可直接照搬的合同模板。知识产权归属、持续研发贡献、政府资助条件、职务成果规定与当地法律制度都可能不同。这里真正可借鉴的，是在产品尚小的时候，就把各方关系做成能够经受长期成长和控制权变化检验的安排。", "这为中国的科研成果转化提供了一个可以认真研究的例子，但不能直接当作合同模板。知识产权归属、持续研发贡献、政府资助条件、职务成果规定与当地法律制度都可能不同。可供比较的是：产品还很小时，各方关系就需要经受长期成长和控制权变化的检验。"),
    ("PSCAD与RTDS的特别之处，不是让这些约束消失，而是把理解和应对约束的部分能力，从一群人的经验，逐渐变成许多人可以使用、检验和继续发展的工具。", "PSCAD与RTDS把一部分理解和应对这些约束的能力，从少数人的经验转化成了许多人可以使用、检验和继续发展的工具。"),
    ("大学与企业之间最珍贵的合作，不是每隔几年重新签一次协议，而是这条往返的通道能够一直工作。", "大学与企业之间最有价值的是一条能够长期工作的往返通道。"),
    ("研究中心、母公司部门、独立企业、许可经营和集团收购，不是简单的先进与落后之分。它们解决不同的问题，也制造不同的约束。", "研究中心、母公司部门、独立企业、许可经营和集团收购对应不同的发展阶段，各自解决不同的问题，也制造不同的约束。"),
    ("组织安排的价值，应当由它是否帮助技术持续进步、客户持续获得服务、风险和收益得到清楚分配来检验，而不是仅由公司牌子是否更换来判断。", "评价一种组织安排，可以看三件事：技术能否持续进步，客户能否持续获得服务，风险和收益能否被清楚分配。公司牌子是否更换本身说明不了这些结果。"),
    ("所以，这篇文章虽然写到了公司出售，却不是一篇教人怎样把公司卖出去的故事。", "因此，公司出售只是这段历史中的一个组织节点。"),
    ("从这个角度看，世界级工具真正值得骄傲的时刻，未必只在第一台设备交付，也未必只在交易公告发布。\n\n还在于某一天，远在另一片大陆的工程师，用它发现了一项控制策略的缺陷，修正了一组模型，或者在装置投运之前把问题留在了实验室里。", "世界级工程工具的价值最终要落到使用现场：某一天，远在另一片大陆的工程师，用它发现了一项控制策略的缺陷，修正了一组模型，或者在装置投运之前把问题留在了实验室里。"),
]
for old, new in zh_rewrites:
    zh = opt(zh, old, new)

zh = rep(
    zh,
    "[55] Ametani, A. **Electromagnetic Transients Program: History and Future**. IEEJ Transactions on Electrical and Electronic Engineering, 2021, 16: 1150–1158. DOI: 10.1002/tee.23192。用于EMTP早期开发、后续分支及EMT类程序技术谱系背景。",
    "[55] Ametani, A. **Electromagnetic Transients Program: History and Future**. IEEJ Transactions on Electrical and Electronic Engineering, 2021, 16: 1150–1158. DOI: 10.1002/tee.23192。用于EMTP技术谱系背景；文中同时明确记载RTDS首个原型形成于1989年、1993年第一套RTDS由日本Hitachi购买、1994年成立RTDS Technologies。",
    "reference 55 zh",
)
zh = rep(
    zh,
    "[61] RTDS Technologies. **Practical Use of Real Time Simulation for De-risking HVDC Integration**. 公司技术演示资料，约2020—2021年。资料列出公司约75名员工，以及hardware/software development、model development、customer support、sales and marketing、finance、product assembly and testing等职能集中于温尼伯。入口：`https://knowledge.rtds.com/hc/en-us/article_attachments/360102163454`。",
    "[61] RTDS Technologies. **Practical Use of Real Time Simulation for De-risking HVDC Integration**. 公司技术演示资料，约2020—2021年。资料列出公司约75名员工，以及hardware/software development、model development、customer support、sales and marketing、finance、product assembly and testing等职能集中于温尼伯。入口：`https://knowledge.rtds.com/hc/en-us/article_attachments/360102163454`。\n\n[62] RTDS Technologies. **History of Real-Time Simulation**. 官方培训/技术演示时间线，明确列出1986年RTDS development project begins、1989年world’s first real-time digital HVDC simulation、1993年first commercial installation、1994年RTDS Technologies Inc. created。入口：`https://knowledge.rtds.com/hc/en-us/article_attachments/360069828073`。",
    "reference 62 zh",
)


# ---------------- English edition ----------------
en = set_date(EN_PATH.read_text(encoding="utf-8"), "en")

north_en = "The defining physical feature of Manitoba's electric system is simple: **most major hydro resources are in the north, while most load is in the south**. The Nelson River basin contains large hydroelectric resources; Winnipeg and most of the province's demand are far away. Engineers therefore had to turn remote northern water into dependable electricity hundreds of kilometres to the south."
en = rep(
    en,
    north_en,
    north_en + "\n\nHydroelectric development in the Nelson River system also had long-term consequences for northern Cree communities. The Churchill River Diversion and related projects altered water levels and flooded land, affecting travel, fishing, hunting, and other traditional land uses. The 1977 Northern Flood Agreement and later implementation, compensation, and settlement agreements are a separate history that deserves fuller treatment; even in a technical history, omitting the issue entirely would remove part of the context.",
    "Indigenous context en",
)

en = rep(
    en,
    "According to Rudi Wierckx's later recollection, an external company was initially contracted to develop a digital real-time simulator, but the effort did not achieve the required result. Under Woodford, a small internal team then continued the work.",
    "According to Rudi Wierckx's later recollection, an external company was initially contracted to develop a digital real-time simulator, but the effort did not achieve the required result. Under Woodford, a small internal team then continued the work. RTDS Technologies' later official timeline dates the start of this internal development project to **1986**.",
    "1986 milestone en",
)

en = rep(
    en,
    "### 5. First make one filter branch run correctly\n\nWierckx later recalled that the team's first demonstration was not a large AC/DC network of the kind that appears in modern brochures. It was simply a filter branch.",
    "### 5. First make one filter branch run correctly\n\nBy **1989**, the Research Centre had achieved what RTDS Technologies now describes as the world's first real-time digital HVDC simulation. That date matters: digital real-time simulation had become a working HVDC research capability five years before the independent company was incorporated.\n\nWierckx later recalled that the team's first demonstration was simply a filter branch, not a large AC/DC network of the kind that appears in modern brochures.",
    "1989 milestone en",
)

en = rep(
    en,
    "Wierckx later recalled that the real-time digital simulator had originally been developed as a research tool for the Centre, not as the foundation of a new company. After technical work was published, companies such as Hitachi and ABB expressed interest and commercialization became a serious possibility.\n\nHe also recalled that the Centre's non-profit status made its board reluctant to conduct full commercial operations inside the organization. In 1994, four employees who had participated in the development left the Centre and founded RTDS Technologies. The technology was made available to the new company under a royalty arrangement.",
    "Wierckx later recalled that the real-time digital simulator had originally been developed as a research tool for the Centre, not as the foundation of a new company. After technical work was published, companies such as Hitachi and ABB expressed interest and commercialization became a serious possibility.\n\n**In 1993 the first commercial RTDS installation was delivered to Hitachi in Japan.** Ametani's later technical history states explicitly that the first RTDS was bought by Hitachi, Japan. The first commercial installation therefore preceded the independent company and was made while the product still sat within the Research Centre structure.\n\nThe Centre's non-profit status made its board reluctant to carry a full commercial business indefinitely. In **1994**, four employees who had participated in the development left the Centre and founded RTDS Technologies. The technology was made available to the new company under a royalty arrangement. The early chronology is therefore 1986 project start, 1989 first real-time digital HVDC simulation, 1993 first commercial installation, and 1994 company formation.",
    "1993 Hitachi and 1994 milestone en",
)

section16_en = '''### 16. The second wave: inverter-dominated power systems

The first wave pushed EMT tools toward larger AC/DC networks. The second wave changed where those tools sit in the engineering process.

Wind generation, photovoltaics, energy storage, and other inverter-interfaced resources moved fast controls from a small number of HVDC and FACTS installations to thousands of connection points. In synchronous-machine-dominated systems, engineers accumulated decades of intuition around rotor dynamics, excitation, and conventional protection. With large amounts of converter-interfaced generation, phase-locked loops, current limits, fault ride-through logic, control-mode transitions, and interactions among controllers can directly determine the result of a disturbance.

A device with a modest MW rating can matter when it is connected to a weak local grid or when many controllers interact through the same network. Power flow, electromechanical transient simulation, and EMT simulation still have distinct roles; the model must retain the dynamics relevant to the phenomenon being studied.

The **Blue Cut Fire disturbance of August 16, 2016** turned the question of model fidelity into a measurable operating event. Multiple faults occurred on a major transmission corridor in southern California. Following an 11:45 disturbance, nearly **1,200 MW** of solar photovoltaic generation ceased producing. NERC emphasized that the affected PV plants had not simply been disconnected by the transmission fault itself. Inverters stopped producing during the transient. The investigation identified, among other behaviours, inverter protection based on near-instantaneous frequency measurements that could misinterpret distorted fault waveforms, together with widespread use of momentary cessation when voltage moved outside specified ranges.

The scale revealed after the event was larger than one disturbance. In response to a NERC Alert, industry data indicated that more than **6,200 MW**, about **37%** of the reported installed inverter capacity, could be susceptible to the erroneous frequency-calculation/protection behaviour described in the report. By the end of August 2017 about 68% of the affected capacity had been corrected; by October 9, more than 97% of the transmission-connected PV inverters from the implicated manufacturer in the CAISO area had implemented the relevant changes.

Those numbers make the modelling issue concrete. A study model that says only “several hundred megawatts of PV are connected here” may miss the mechanism that actually controls the disturbance if it does not represent the inverter's frequency measurement, low-voltage current-injection logic, recovery ramp, and software/control version.

Australia provides a second, institutional example. AEMO's current Modelling Requirements require connection applicants to provide model packages that represent the physical structure and dynamic performance of their plant, and AEMO explicitly uses both PSS®E and **PSCAD™/EMTDC™** for connection studies. The R1 model package must be submitted at least three months before commissioning; validated R2 data and the model-verification report are due within three months after final commissioning tests. The model package is revised as the project moves through the connection process.

The workflow also has to accommodate intellectual property. AEMO stores non-releasable PSCAD/EMTDC models in restricted locations with access limited to selected authorized staff and consultants, and maintains model iterations through connection, commissioning, and ongoing operation. OEMs need to protect control implementation; the system operator needs models that can be executed, reproduced, and validated. Both requirements have to coexist in the same engineering process.

The hard numbers of the first wave were 26 racks, nearly 1,000 DSPs, 511 buses, and 1,306 buses. The hard constraints of the second wave increasingly include model version, field validation, controlled distribution, and change management. Computing power still matters, but a faster processor cannot reconstruct control logic that was never supplied or repair a model that no longer matches the device in service.

For PSCAD and RTDS, renewable integration, storage controls, system strength, local interactions, and protection adaptation expanded the market while pushing product competition toward vendor-model hosting, validation workflow, IP protection, and version governance. The original path from grid problem to simulation tool did not end; it entered a system with more models, more participants, and more complicated responsibility boundaries.'''
en = sec(en, "### 16. The second wave: inverter-dominated power systems", "### 17. PSCAD's growth was not only about the solver", section16_en, "section 16 en")

en = rep(
    en,
    "## Part III — Toward the sale: technological success does not remove business problems",
    "## Part III — Organizational divergence and the sale: technological success does not remove business problems",
    "Part III title en",
)

pscad3_en = '''### 20. PSCAD remained inside the provincial utility group

During the same period, PSCAD followed a different organizational path. When Manitoba Hydro reorganized MHI in 2021, the business being gradually wound down was MHIUS international consulting. Manitoba Hydro's announcement explicitly said that MHI would continue as a subsidiary and that its technology-solutions lines would continue to operate and be marketed under the Manitoba Hydro International banner. PSCAD therefore remained inside the provincially owned utility group rather than following RTDS into an independent-company sale.

In July 2024, the Province of Manitoba announced the restart of MHI's international consulting business and a process to rebuild the full scope of its operations, including technical and advisory services and international training. By March 2026 PSCAD was still publishing official material for version 5.1.0 and associated technical training. The 2021 contraction did not remove PSCAD from the market; it was an adjustment in the parent's business boundary followed by a later expansion.

The Winnipeg technology ecosystem therefore produced two long-term organizational outcomes. RTDS operated independently for twenty-eight years before joining AMETEK, a listed industrial-technology group. PSCAD remained within Manitoba Hydro's wholly owned subsidiary structure. The former gained the platform of a larger instrumentation, sales, and capital organization; the latter retained its organizational link to the provincial utility and MHI's technology business.

The contrast makes the question of organizational fit concrete. Different products can require different capital, distribution, governance, support, and R&D arrangements at different stages. The useful test is whether the chosen structure continues to support technical development, customers, and a clear allocation of responsibility and return.'''
en = rep(en, "### 20. RTDS changed owners", pscad3_en + "\n\n### 21. RTDS changed owners", "PSCAD Part III section en")
en = rep(en, "### 21. Is a sale the final proof of success, or the beginning of another responsibility?", "### 22. After the sale: commercialization success and continuing responsibility", "final section renumber en")

en = rep(
    en,
    "The number is striking, but another question is more important: who actually sold what?",
    "The transaction structure first requires a distinction between MHI's economic rights and the equity held by RTDS's private shareholders.",
    "sale framing en",
)

mhi_en = "Manitoba Hydro's quarterly report for the nine months ended December 31, 2022 explains that, before closing, MHI's royalty entitlement was converted into RTDS equity and then disposed of in the transaction. That quarterly report recorded a gain of roughly C$68 million; the 2022–23 annual report reported a one-time gain of C$69 million and stated that the royalty stream would terminate."
en = rep(
    en,
    mhi_en,
    mhi_en + "\n\nThat side of the transaction can therefore be traced through Manitoba Hydro's public financial reports. The private-shareholder side is much less visible. In the company histories, founder interviews, AMETEK announcements, and regulatory filings reviewed for this article, I found no public statement from the selling shareholders or the acquirer explaining why the private shareholders chose to sell in 2022, and no public document that fully sets out the final pre-closing shareholder structure. Founder retirement, succession planning, or the service-network limits faced by a roughly 75-person specialist company are reasonable questions to investigate, but the available public evidence does not establish any of them as the transaction's direct cause. AMETEK explained the buyer's strategic logic; it did not disclose the sellers' decision process. The gap should remain visible rather than being filled with speculation.",
    "seller evidence gap en",
)

en_rewrites = [
    ("The value of that arrangement was not the number of logos on a partnership chart. It was the ability to cross normal organizational boundaries and bring in the people who actually understood the problem.", "The arrangement allowed the Centre to cross normal organizational boundaries and bring in the people who actually understood the problem."),
    ("The key was not merely purchasing a faster chip. The algorithm, hardware partition, data exchange, and electrical-network representation had to be designed together.", "The algorithm, hardware partition, data exchange, and electrical-network representation had to be designed together."),
    ("The lesson is not that every research team should collectively resign and form a company. It is that when a product grows beyond the natural operating boundary of its original institution, the organization needs a path that lets the product continue to develop without erasing the rights and contributions of the people and institutions that created it.", "The organizational lesson is about boundary changes: when a product grows beyond the natural operating scope of its original institution, it needs a path that supports further development while preserving the rights and contributions of its creators."),
    ("That does not mean RTDS lacked testing. Product assembly and testing became explicit functions, and models were repeatedly checked against benchmarks and physical devices. The point is that it is misleading to imagine a huge QA organization completely separated from development.", "RTDS did have explicit product-assembly and testing functions, and models were repeatedly checked against benchmarks and physical devices. Public material nevertheless does not support imagining a huge QA organization completely separated from development."),
    ("That does not diminish the solver. On the contrary, only when the underlying numerical results are trustworthy is it worth building a large engineering workflow around them.", "The solver remains foundational: a large engineering workflow is worth building only when the underlying numerical results are trustworthy."),
    ("This does not make the technology businesses unimportant. It simply prevents us from confusing business scale and risk type.", "The distinction is one of business scale and risk type."),
    ("But this history is not a contract template that can be copied into another jurisdiction.", "This history is useful as a comparison case, not as a contract template for another jurisdiction."),
    ("What makes PSCAD and RTDS distinctive is not that they removed those constraints. They converted part of the ability to understand and manage them from the experience of a small group of specialists into tools that many engineers could use, test, and continue to develop.", "PSCAD and RTDS converted part of the ability to understand and manage those constraints from the experience of a small group of specialists into tools that many engineers could use, test, and continue to develop."),
    ("The most valuable university–industry relationship is not the periodic signing of a new agreement, but a channel through which questions and results can continue to move in both directions.", "The most valuable university–industry relationship is a channel through which questions and results continue to move in both directions."),
    ("A research centre, a department of a parent organization, an independent company, a licence arrangement, and a later strategic acquisition are not simply “better” or “worse” organizational forms. They solve different problems and create different constraints.", "A research centre, a department of a parent organization, an independent company, a licence arrangement, and a later strategic acquisition fit different stages and create different constraints."),
    ("The value of an organizational arrangement should therefore be judged by whether it helps the technology continue to improve, helps users continue to receive support, and allocates risk and reward clearly—not merely by whether the corporate name changes.", "An organizational arrangement can be judged by whether the technology continues to improve, users continue to receive support, and risk and reward remain clearly allocated. A change of corporate name does not answer those questions by itself."),
    ("This article reaches a company sale, but it is not a manual for how to sell a company.", "The company sale is one organizational transition in a longer technical history."),
    ("The most important moment in a world-class engineering tool's history may therefore not be the first shipment and not the acquisition announcement.\n\nIt may be the day when an engineer on another continent uses the tool to discover a flaw in a control strategy, correct a model, or keep a problem in the laboratory instead of allowing it to reach the operating grid.", "The value of a world-class engineering tool ultimately appears in use: an engineer on another continent discovers a flaw in a control strategy, corrects a model, or keeps a problem in the laboratory instead of allowing it to reach the operating grid."),
]
for old, new in en_rewrites:
    en = opt(en, old, new)

en = rep(
    en,
    "[55] Ametani, A. **Electromagnetic Transients Program: History and Future**. *IEEJ Transactions on Electrical and Electronic Engineering*, 2021, 16: 1150–1158. DOI: 10.1002/tee.23192.",
    "[55] Ametani, A. **Electromagnetic Transients Program: History and Future**. *IEEJ Transactions on Electrical and Electronic Engineering*, 2021, 16: 1150–1158. DOI: 10.1002/tee.23192. Also records the first RTDS prototype in 1989, the first RTDS purchase by Hitachi in Japan in 1993, and the formation of RTDS Technologies in 1994.",
    "reference 55 en",
)
en = rep(
    en,
    "[61] RTDS Technologies. **Practical Use of Real Time Simulation for De-risking HVDC Integration**. Technical presentation, c. 2020–2021. https://knowledge.rtds.com/hc/en-us/article_attachments/360102163454.",
    "[61] RTDS Technologies. **Practical Use of Real Time Simulation for De-risking HVDC Integration**. Technical presentation, c. 2020–2021. https://knowledge.rtds.com/hc/en-us/article_attachments/360102163454.\n\n[62] RTDS Technologies. **History of Real-Time Simulation**. Official training/technical presentation timeline listing the RTDS development project start in 1986, the world's first real-time digital HVDC simulation in 1989, the first commercial installation in 1993, and creation of RTDS Technologies Inc. in 1994. https://knowledge.rtds.com/hc/en-us/article_attachments/360069828073.",
    "reference 62 en",
)

# Sanity checks
for token in ["1986年", "1989年", "第一套商业RTDS", "Blue Cut", "AEMO", "PSCAD留在省属体系内", "没有找到一份由原股东或收购方发布的材料"]:
    if token not in zh:
        raise RuntimeError(f"Chinese sanity check failed: {token}")
for token in ["**1986**", "**1989**", "first commercial RTDS installation", "Hitachi in Japan", "Blue Cut", "AEMO", "PSCAD remained inside the provincial utility group", "I found no public statement"]:
    if token not in en:
        raise RuntimeError(f"English sanity check failed: {token}")

ZH_PATH.write_text(zh, encoding="utf-8")
EN_PATH.write_text(en, encoding="utf-8")

# Update sitemap dates; GITHUB_TOKEN pushes do not trigger the normal metadata workflow.
sm = Path("sitemap.xml")
xml = sm.read_text(encoding="utf-8")
targets = [
    "https://zoudehupowersystem.github.io/%E6%9B%BC%E5%B0%BC%E6%89%98%E5%B7%B4%E6%B0%B4%E7%94%B5%E5%B1%80%E7%9A%84%E5%88%9B%E4%B8%9A%E5%8F%B2.html",
    "https://zoudehupowersystem.github.io/manitoba-hydro-pscad-rtds-history.html",
]
for target in targets:
    pattern = r'(<loc>' + re.escape(target) + r'</loc>\s*<lastmod>)(\d{4}-\d{2}-\d{2})(</lastmod>)'
    xml, n = re.subn(pattern, r'\g<1>' + DATE + r'\g<3>', xml, count=1)
    if n != 1:
        raise RuntimeError(f"Sitemap entry not updated: {target}")
sm.write_text(xml, encoding="utf-8")

print("Bilingual Manitoba history revisions applied successfully")
