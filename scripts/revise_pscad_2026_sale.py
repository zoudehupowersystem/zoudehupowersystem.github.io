from pathlib import Path

zhp = Path('曼尼托巴水电局的创业史.md')
enp = Path('manitoba-hydro-pscad-rtds-history.md')

zh = zhp.read_text(encoding='utf-8')
en = enp.read_text(encoding='utf-8')

zh_drop = '第一股浪潮的硬数字是26个Rack、近1000片DSP、511母线和1306母线；第二股浪潮的硬约束越来越多地表现为模型版本、现场验证、保密分发和变更管理。算力仍然重要，但更快的处理器无法补齐缺失的控制逻辑，也无法自动纠正与现场装置不一致的模型。\n\n'
en_drop = 'The hard numbers of the first wave were 26 racks, nearly 1,000 DSPs, 511 buses, and 1,306 buses. The hard constraints of the second wave increasingly include model version, field validation, controlled distribution, and change management. Computing power still matters, but a faster processor cannot reconstruct control logic that was never supplied or repair a model that no longer matches the device in service.\n\n'

if zh_drop not in zh:
    raise RuntimeError('Chinese paragraph to delete not found')
if en_drop not in en:
    raise RuntimeError('English paragraph to delete not found')
zh = zh.replace(zh_drop, '', 1)
en = en.replace(en_drop, '', 1)

zh_anchor = '2024年7月，曼尼托巴省政府宣布恢复MHI国际咨询业务，并开始重建完整业务范围，包括重新参与全球能源项目的技术、咨询和培训服务。到2026年3月，PSCAD官方仍在发布v5.1.0版本介绍和技术培训资料。2021年的业务收缩没有让PSCAD退场，它经历的是母公司业务边界调整以及后来的重新扩展。'
zh_add = zh_anchor + '\n\n但到2026年，这个“继续留在省属体系内”的状态也出现了新的变量。7月27日，曼尼托巴水电局CEO Allan Danroth在省公共事业委员会（PUB）听证会上公开谈到PSCAD的资产价值。8月的媒体报道引述他的证词称，全球能源企业曾对这套电网建模软件提出“严肃”的收购报价，金额达到**数亿加元**；CBC的报道进一步明确，他所说的软件就是PSCAD。这里需要区分“收到收购报价”与“已经出售”：截至本文2026年9月更新时，公开资料中没有PSCAD完成控制权转移的公告，PSCAD与MHI的公开网站仍将其作为MHI的产品和业务运营。更准确地说，母公司已经把PSCAD潜在的交易价值公开摆到了桌面上，但是否出售、以何种方式出售以及最终估值，仍没有公开的确定结果。'
if zh_anchor not in zh:
    raise RuntimeError('Chinese section 20 anchor not found')
zh = zh.replace(zh_anchor, zh_add, 1)

en_anchor = "In July 2024, the Province of Manitoba announced the restart of MHI's international consulting business and a process to rebuild the full scope of its operations, including technical and advisory services and international training. By March 2026 PSCAD was still publishing official material for version 5.1.0 and associated technical training. The 2021 contraction did not remove PSCAD from the market; it was an adjustment in the parent's business boundary followed by a later expansion."
en_add = en_anchor + "\n\nBy 2026, however, that continued public-sector ownership had become less settled. At the opening of Manitoba's Public Utilities Board hearings on July 27, Manitoba Hydro CEO Allan Danroth publicly discussed PSCAD's asset value. News reports in August, citing his testimony, said global energy companies had made \"serious\" offers to buy the grid-modelling software, in the **hundreds of millions of Canadian dollars**; CBC's report identified the software explicitly as PSCAD. An acquisition offer is not a completed divestiture. As of this article's September 2026 update, no public announcement reviewed here shows that control of PSCAD has transferred, and PSCAD/MHI's public sites still present PSCAD as an MHI product and business. The more precise conclusion is that Manitoba Hydro has publicly put PSCAD's potential transaction value on the table, while whether it will be sold, through what structure, and at what final valuation remain unresolved in the public record."
if en_anchor not in en:
    raise RuntimeError('English section 20 anchor not found')
en = en.replace(en_anchor, en_add, 1)

zh_ref = '\n[63] Winnipeg Free Press；CBC News（Yahoo News转载）. **2026年PSCAD潜在收购报价相关报道**. 2026-08-28。两篇报道均引述Manitoba Hydro CEO Allan Danroth在2026-07-27曼尼托巴省公共事业委员会（PUB）听证会上的发言；Winnipeg Free Press报道其称全球能源企业曾对电网建模软件提出数亿美元的“严肃”报价，CBC报道明确将该软件识别为PSCAD。本文据此说明存在收购报价和潜在出售可能性，不将其写成已经完成的交易。入口：`https://www.winnipegfreepress.com/business/2026/08/28/hydro-ceo-leaving-job-two-years-after-appointment`；`https://malaysia.news.yahoo.com/allan-danroth-ceo-manitoba-hydro-154716063.html`。\n\n[64] PSCAD / Manitoba Hydro International. **About Us；PSCAD product pages**. 2026-09访问的官方网页仍将PSCAD作为Manitoba Hydro International的软件开发、工程及产品业务介绍；用于核对2026年收购报价公开后尚未见控制权转移公告的当前状态。入口：`https://www.pscad.com/about-us`；`https://www.mhi.ca/products/pscad`。\n'
en_ref = '\n[63] *Winnipeg Free Press*; CBC News (republished by Yahoo News). **Reporting on potential purchase offers for PSCAD**. August 28, 2026. Both reports cite Manitoba Hydro CEO Allan Danroth\'s July 27, 2026 testimony before Manitoba\'s Public Utilities Board. The *Winnipeg Free Press* reported that global energy companies had made serious offers in the hundreds of millions of dollars for the grid-modelling software; the CBC report identified the software explicitly as PSCAD. These sources establish the existence of acquisition offers and a possible divestiture, not a completed transaction. https://www.winnipegfreepress.com/business/2026/08/28/hydro-ceo-leaving-job-two-years-after-appointment; https://malaysia.news.yahoo.com/allan-danroth-ceo-manitoba-hydro-154716063.html.\n\n[64] PSCAD / Manitoba Hydro International. **About Us; PSCAD product pages**. Official pages accessed in September 2026 continued to describe PSCAD as a Manitoba Hydro International software-development, engineering, and product business; used here to check the post-offer public ownership/operating status. https://www.pscad.com/about-us; https://www.mhi.ca/products/pscad.\n'

if '[63] Winnipeg Free Press' not in zh:
    zh = zh.rstrip() + '\n' + zh_ref
if '[63] *Winnipeg Free Press*' not in en:
    en = en.rstrip() + '\n' + en_ref

zhp.write_text(zh, encoding='utf-8')
enp.write_text(en, encoding='utf-8')
