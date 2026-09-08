---
layout: manitoba
title: "From the Nelson River to PSCAD and RTDS: Manitoba’s Power-System Simulation Story"
lang: en
seo_title: "History of PSCAD and RTDS: Manitoba Hydro, EMTDC and Real-Time Simulation | Dehu Zou"
description: "A technical history of Manitoba Hydro, Dennis Woodford, EMTDC/PSCAD, the Manitoba HVDC Research Centre, RTDS Technologies, the University of Manitoba, real-time EMT simulation, and the commercialization path from utility engineering problems to global simulation products."
updated: "2026-09-07"
---

<!-- BLOG-TOPIC-START -->
<div class="zdh-blog-topic" style="max-width:980px;margin:18px auto 28px;padding:14px 16px;border:1px solid rgba(91,181,255,.35);border-radius:14px;background:linear-gradient(135deg,#0b1f3a,#102f52);box-shadow:0 8px 24px rgba(11,31,58,.14);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,'Noto Sans','PingFang SC','Microsoft YaHei',sans-serif;color:#fff;">
  <div style="display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap;">
    <div>
      <div style="font-size:12px;letter-spacing:.12em;color:#9be7ff;font-weight:700;">主题栏目 · FEATURED COLUMN</div>
      <div style="margin-top:4px;font-size:16px;line-height:1.45;font-weight:750;color:#fff;">邹德虎的博客 · Dehu Zou's Blog</div>
      <div style="margin-top:3px;font-size:12px;line-height:1.5;color:rgba(255,255,255,.72);">电力系统 · 工程技术 · 计算与仿真</div>
    </div>
    <a href="index.html" style="display:inline-flex;align-items:center;padding:8px 11px;border:1px solid rgba(255,255,255,.22);border-radius:10px;background:rgba(255,255,255,.08);color:#d8efff;text-decoration:none;font-size:13px;font-weight:650;white-space:nowrap;">← 返回个人主页 · Home</a>
  </div>
</div>
<!-- BLOG-TOPIC-END -->

<style>
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;line-height:1.78;color:#20242a;max-width:930px;margin:0 auto;padding:28px 24px 70px;background:#fff}a{color:#155eef;text-decoration:none}a:hover{text-decoration:underline;text-underline-offset:3px}h1{font-size:2.35rem;line-height:1.25;margin-top:18px}h2{font-size:1.75rem;line-height:1.35;margin-top:54px;padding-top:10px;border-top:1px solid #e3e7ee}h3{font-size:1.35rem;line-height:1.4;margin-top:36px}blockquote{margin:22px 0;padding:14px 18px;border-left:4px solid #7aa7ff;background:#f3f6fb;color:#344054}table{width:100%;border-collapse:collapse;margin:20px 0;font-size:.92rem}th,td{border:1px solid #e3e7ee;padding:10px 12px;vertical-align:top}th{background:#f6f8fb;text-align:left}code{background:#f4f5f7;padding:2px 5px;border-radius:5px;font-size:.92em}.article-nav{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;padding:10px 0 18px;border-bottom:1px solid #e3e7ee;margin-bottom:28px}.adapt-note{color:#667085;font-size:.9rem;margin-bottom:26px}@media(max-width:700px){body{padding:20px 16px 50px}h1{font-size:1.9rem}h2{font-size:1.5rem}h3{font-size:1.2rem}}
</style>

<div class="article-nav"><a href="曼尼托巴水电局的创业史.html">中文版 →</a></div>

<div class="adapt-note">English edition adapted for international readers; China-specific scale comparisons and reader-addressed passages have been reframed while preserving the technical history and source base.</div>

# From the Nelson River to PSCAD and RTDS: Manitoba’s Power-System Simulation Story

<div class="article-meta" style="margin:-4px 0 24px;color:#667085;font-size:.9rem;display:flex;gap:8px 18px;flex-wrap:wrap;"><span>Author: Dehu Zou</span><span>Updated: 2026-09-07</span></div>
> How did a modest-sized electric utility in the middle of Canada help give rise to two world-class power-system simulation platforms? The story did not begin with a grand entrepreneurship plan. It began with a sequence of engineering problems that could not be avoided.

The development of PSCAD and the RTDS Simulator around Manitoba Hydro is a rare end-to-end example in the power industry: **internal engineering problems drove joint research; research was tested against real systems; prototypes became products; and products eventually reached a global market**. The history is therefore useful not only as a technology story, but also as a case study in industrial innovation and R&D management.

## Prologue: Why did two world-class simulation tools emerge from a cold inland province?

### Rivers, a city, and electricity

Manitoba is not the first place most people think of when discussing global technology clusters. It sits in the middle of Canada, between the prairie provinces and the Canadian Shield, with the United States to the south and Hudson Bay to the northeast. Winters are long and severe; farther north, population density falls sharply as forests and lakes dominate the landscape. The provincial government notes that Manitoba has more than 100,000 lakes and that water covers roughly 16% of its area.

Winnipeg, the provincial capital, lies at the confluence of the Red and Assiniboine rivers. The Forks is now an urban gathering place, but the site has been used by people for at least six thousand years and has successively been a meeting ground, trading centre, Métis community hub, railway city, and immigrant gateway.

For Winnipeg, rivers have never been only lines on a map. They were once transportation corridors and later became part of the province's energy system.

The defining physical feature of Manitoba's electric system is simple: **most major hydro resources are in the north, while most load is in the south**. The Nelson River basin contains large hydroelectric resources; Winnipeg and most of the province's demand are far away. Engineers therefore had to turn remote northern water into dependable electricity hundreds of kilometres to the south.

That geography made long-distance transmission unavoidable. Manitoba chose high-voltage direct current transmission, and the Nelson River HVDC project became the engineering backbone around which much of the later simulation work developed.

This article, however, is not mainly about dams and transmission lines. It is about a less visible kind of infrastructure: the analytical and simulation tools used to understand power systems. In Winnipeg, along the chain of engineering problems created by the north-to-south transmission system, two names eventually emerged that are now familiar to power engineers around the world: **PSCAD and the RTDS Simulator**.

### Two tools, two answers to the same underlying question

For engineers who work with electromagnetic transients, PSCAD needs little introduction. A user draws a network, specifies equipment and control parameters, applies disturbances, runs the case, and observes voltages, currents, and control signals. Its numerical engine is EMTDC; in ordinary usage, “PSCAD” usually refers to the complete environment of graphical modelling, compilation and execution, result analysis, and EMTDC simulation.

It is principally an offline simulation environment. It helps answer a question such as: **What will this network, equipment, and control system do under this disturbance?**

A real-time digital simulator moves the question closer to physical equipment. A relay, HVDC controller, or other real device is connected to the simulator. The simulator represents the power system, sends voltages and currents to the real device, receives the device's actions, changes the simulated network accordingly, and feeds the resulting state back again.

It therefore asks a different question: **What will the actual device that is about to be commissioned do when it is connected to this kind of grid?**

The RTDS Simulator is consequently a combined hardware-and-software platform. Models must be built, executed, monitored, and analyzed, and the RSCAD software environment supports those tasks. Treating RTDS as merely a row of computer cabinets misses much of the product.

The key distinction is time. Offline simulation does not normally require simulated time to advance in lockstep with wall-clock time. Real-time simulation does. Offline tools are ideal for detailed mechanism studies, alternative comparison, and parameter sweeps. Real-time platforms are especially valuable for closed-loop testing of actual protection and control equipment. Their application domains overlap, but it is misleading to call RTDS simply “a faster PSCAD,” or PSCAD “RTDS without the cabinets.” They share the intellectual foundations of EMT simulation, but their implementations and code bases are different.

One organizational point also needs to be clear from the outset. This is **not** the story of one utility that wholly owned and operated two software companies from beginning to end.

Manitoba Hydro provided the original engineering environment, problems, and support. The University of Manitoba contributed research and people. The Manitoba HVDC Research Centre performed a large amount of development, collaboration, testing, and early commercialization. PSCAD and RTDS later followed different organizational paths. In particular, RTDS Technologies, founded in 1994, was a private company spun out of the Research Centre. It retained licensing and royalty relationships with the technology source, but it was not simply a Manitoba Hydro wholly owned subsidiary throughout its life.

Understanding that distinction is essential both to understanding the eventual sale and to understanding the management choices that made the technology durable.

### How large was Manitoba Hydro?

The name “Manitoba Hydro” can create the impression of a company that merely operates hydroelectric plants. In fact it is a provincially owned integrated utility with generation, transmission, distribution, retail electricity, and natural-gas operations.

For international readers, direct comparisons with individual provinces or states are less useful than the absolute scale. In fiscal year 2024–25, Manitoba Hydro delivered about **22.6 TWh** of electricity within Manitoba and about **7.97 TWh** outside the province. Its in-province peak load was about **5.11 GW**. The utility reported roughly **632,000 electricity customers**, system capability of about **6.07 GW**, and annual generation of about **31.0 TWh**.

Those figures make the basic point. Manitoba Hydro is important, but it is not one of the world's enormous power systems. Its local load is moderate by the standards of major North American and global grids.

What made Manitoba unusual was not market size. It was the concentration of several technically difficult problems that could not be avoided. **The system was modest in scale, but some of the problems it had to solve were at the international frontier.**

---

## Part I — The formative years: solving their own problems first

### 1. The HVDC line entered service, but the available tools could not simply be reused

Manitoba Hydro was formed in 1961. At roughly the same time, development of northern hydro resources and transmission of that energy southward became a defining strategy for the province. The Nelson River HVDC project was central to that strategy.

The system first transmitted power on June 17, 1972. IEEE later recognized the project for its long-distance, high-capacity transmission, bipolar configuration, control-system applications, and the mercury-arc valve technology that was advanced for its time.

To engineers familiar with today's UHVDC schemes, the voltage and power ratings of those early projects can look modest. But one cannot project today's mature equipment, software, standards, and accumulated operating knowledge backward by half a century. Many behaviours that later became textbook material still had to be learned through analysis, testing, and operating experience.

An AC system and a DC link are not joined by simply connecting conductors. Converters must operate with the AC voltage; controllers must regulate current and voltage; the system must survive faults, recovery, and operating-mode changes. DC controls can regulate power, but their actions also influence the AC network. Turbine-generators, excitation systems, reactive compensation, filters, and converter controls interact in ways that steady-state calculation alone cannot reveal.

In such a system, a commutation failure, an inappropriate control transition, or an apparently reasonable setting can create behaviour that crosses equipment boundaries. Engineers need to know not merely whether the scheduled power can be transmitted, but how the system evolves during a fault and whether it recovers cleanly afterwards.

That demanded a different level of simulation: engineers needed instantaneous waveforms; they needed control logic inside the network model; and they needed the messy details of real engineering systems to enter the calculation.

Electromagnetic-transient programs already existed, of course.

Hermann W. Dommel (1933–2025) is central to that history and is often called the father of EMTP. In 1966 he moved from Germany to the Bonneville Power Administration (BPA) in the United States and participated in development of a general digital program for electromagnetic transients. In 1973 he moved to the University of British Columbia, where he continued work on electromagnetic transients, power-system computation, and engineer education for decades.

Dommel's lasting contribution was not simply a piece of software. He organized travelling-wave treatment of transmission lines, discrete-time representations of lumped elements, nodal analysis, and sparse-matrix solution into a general computational framework for electromagnetic transients. Many modern EMT programs have different code bases and product histories, but the influence of that framework remains visible.

One motivation for BPA's work in the 1960s was switching overvoltage and insulation coordination in high-voltage transmission. Before digital methods matured, much of this work relied on transient-network analyzers and other physical analog equipment. By around 1968, BPA had a general transient program, often called the Transient Program (TP), and in 1969 Dommel published the classic paper that systematically described its principal numerical ideas.

Scott Meyer joined BPA in 1972. After Dommel left for UBC in 1973, Meyer took over development and other researchers later joined. EMTP therefore evolved from a program associated with one researcher into a family of engineering tools developed and extended by an international community.

At this point, the story reaches Manitoba.

### 2. Woodford wanted more than a program that merely ran

Dennis A. Woodford is one of the central figures in this history.

In 1973 Manitoba Hydro obtained a copy of BPA's transient program. Woodford later recalled spending roughly six months trying to use it to construct a not especially complicated DC transmission model, without achieving what he needed.

That does not mean EMTP was a poor program. Its strengths at the time lay especially in AC-network switching transients and overvoltages. Manitoba's difficult object was different: a thyristor converter together with firing control, current regulation, extinction-angle control, protection logic, and continuous interaction between the AC network and the DC controls. For a system such as Nelson River, the electrical network and the controls could not be treated as separate worlds.

Woodford eventually stopped trying to modify the existing EMTP source. Instead he went back to Dommel's 1969 paper and wrote a new program from the underlying method. He later emphasized that he deliberately avoided simply copying the EMTP code because he did not want to inherit structural limitations of the old implementation. The new program became EMTDC.

The most accurate description of the relationship is therefore not that one program was modified into the other, but that they had **a common mathematical ancestor and independent code bases**. EMTDC inherited Dommel's computational ideas while developing its own architecture and, eventually, its own product ecosystem.

Before joining Manitoba Hydro, Woodford had also worked with digital control-system simulation software. Such programs represented integrators, limiters, regulators, and other control blocks graphically. He combined that control-oriented modelling concept with Dommel-style instantaneous network solution: solve the electrical network and the control system in the same time-domain calculation and exchange signals between them continuously.

That combination directly addressed the central difficulty of Manitoba's HVDC system.

EMTDC was therefore not born from a desire to “make another EMTP.” It began with a very concrete requirement: **how can the HVDC main circuit, converters, and complex controls be simulated together in a form that is genuinely useful for engineering analysis?**

This was also the first threshold between a one-off engineering calculation and reusable industrial software. When a project ends, if its solution method, control blocks, component models, and debugging knowledge remain available for the next project, a product has begun to emerge.

### 3. The Research Centre created an organizational home for the work

Technology needs people, but it also needs an organization in which people can keep working together.

In 1980 the Manitoba government approved construction of the Manitoba HVDC Research Centre at a cost of about C$7.671 million, including roughly C$4.5 million of government funding. The mandate included insulation, controls, related equipment, and the ability to perform field tests on an operating DC system. The original plan also expected the Centre to become self-sustaining after its first five years. From the beginning, therefore, it carried three simultaneous responsibilities: technical R&D, validation against real engineering systems, and eventual economic sustainability.

The Manitoba HVDC Research Centre was established in late 1981. Early support involved Manitoba Hydro, the University of Manitoba, Teshmont Consultants, Federal Pioneer, and the provincial government.

The Centre should not be imagined as merely another department inside the utility. It had multi-party support and a mandate covering HVDC-related R&D, dissemination, and research facilities. Specialists from different organizations could be assembled around a problem. A 1987 article, for example, described cooperation among utility, equipment-company, and consulting personnel on leakage current, environmental conditions, and flashover behaviour. The operating problem existed in the field; the relevant knowledge was distributed among institutions; the Centre provided a place to combine it.

The value of that arrangement was not the number of logos on a partnership chart. It was the ability to cross normal organizational boundaries and bring in the people who actually understood the problem. A utility sees operating phenomena but may not have enough staff dedicated to numerical algorithms. A university has research capability but may lack access to actual equipment parameters and disturbance records. A manufacturer understands its device but may not understand the entire system environment. The Research Centre connected these fragmented capabilities around concrete engineering questions.

### 4. Being unable to afford an analog simulator did not automatically create RTDS

Once the Research Centre existed, it urgently needed a simulator for HVDC controls. The mature technology of the time was analog: scaled electrical components and specialized equipment were assembled in the laboratory so that real controllers could interact with a physical representation of the power system. In 1982 the Centre asked for pricing on a conventional analog HVDC simulator. It was clearly too expensive.

The question therefore changed from “Which one should we buy?” to “Can we develop a different approach ourselves?”

Entrepreneurship stories often compress everything after that into one sentence: they could not afford the existing product, so they innovated and succeeded.

The actual process was much less tidy.

According to Rudi Wierckx's later recollection, an external company was initially contracted to develop a digital real-time simulator, but the effort did not achieve the required result. Under Woodford, a small internal team then continued the work.

This was not a procurement substitution that succeeded automatically after a management decision. It involved failure, reorganization, and waiting for the right technical conditions.

Advances in information technology, especially microelectronics, gradually made previously impractical ideas feasible. Early general-purpose processors were not fast enough for what the team wanted. New floating-point digital signal processors created an opening, and the structure of power networks provided opportunities for parallel computation.

The key was not merely purchasing a faster chip. The algorithm, hardware partition, data exchange, and electrical-network representation had to be designed together.

A power network contains physical coupling. If different parts are assigned to different processors, engineers must decide what information is exchanged every time step, when it is exchanged, how interfaces affect numerical accuracy, and how switching events are handled.

More importantly, “real time” is not an adjective. It is a hard engineering constraint.

Offline simulation can take longer when a more detailed answer requires more computation. Hardware-in-the-loop testing cannot. A real controller continues to run on its own clock. The simulator must complete the calculations for each step on time, output voltages and currents, receive controller actions, and advance the simulated network without missing the deadline.

Adequate average speed is not enough. If a single step is unexpectedly late, the timing experienced by the closed-loop system can change. An observed anomaly may then come from the test tool rather than from the device under test.

The team therefore had to cross three thresholds at once: the electrical model had to be credible, the computation had to finish on time, and the software/hardware interfaces had to communicate reliably with real equipment.

“Too expensive to buy” created pressure. What turned that pressure into a product opportunity was the accumulated EMT knowledge, understanding of the operating problem, the arrival of suitable processors, and a small team willing to continue after an earlier failure.

### 5. First make one filter branch run correctly

Wierckx later recalled that the team's first demonstration was not a large AC/DC network of the kind that appears in modern brochures. It was simply a filter branch. Only afterwards did the work expand to small systems and then to networks closer to real grids.

That detail is worth pausing over.

Technology demonstrations are often narrated backwards from their final scale: number of buses, converters, processors, or cabinets. R&D does not happen in brochure order. The team first had to establish that the method itself worked. A simple object whose behaviour could be understood and checked was more valuable than a large demonstration whose errors would be difficult to diagnose.

If one filter branch could not be calculated correctly and on time, a large grid would only hide the error more deeply. If the smallest meaningful object behaved reliably, engineers could then determine whether problems introduced by scaling came from models, computational load, or processor-to-processor communication.

Then the real system began to test the tool.

According to Wierckx, Manitoba Hydro asked the team to test a new controller intended for installation at the Dorsey converter station. The test not only completed the immediate assignment; it also found an engineering problem that he believed would probably not have been exposed without the simulation test.

Public sources do not describe that problem in enough detail to justify dramatic claims such as “a major blackout was prevented.” The more important point is simpler: the simulator had become capable of discovering a meaningful problem **before** an actual controller entered service.

For a professional customer, that matters far more than the phrase “advanced algorithm.”

A new tool earns credibility not merely by reproducing a simple benchmark with a known answer, but by entering work where the customer cares deeply about the result and is willing to hold the supplier accountable.

Manitoba Hydro's role as an early user was therefore critical. It did not merely provide money. It had real projects, real control equipment, and real validation requirements. Without that connection, a laboratory prototype can easily remain at the stage of “we tested it ourselves and it looks good.”

Support from an early user should not mean support without discipline. The useful form of support is access to real problems, necessary information, and test opportunities while keeping the technical result subject to engineering scrutiny.

### 6. The economic meaning of the technical breakthrough

In March 1990, *IEEE Canadian Review* published a rather dramatic correction. A previous article about digital simulation had contained a two-letter typesetting error: the intended statement was that the cost had been reduced **to 20%**, but it had been printed as **by 20%**. Woodford wrote to correct the record, and editor Richard J. Marceau apologized.

For a casual reader, the distinction may look minor. For someone deciding whether to buy a simulator, it represents a completely different budget.

Woodford estimated that, compared with an analog simulator of comparable capability, the digital approach could cost roughly one-fifth as much and occupy less than one-fifth of the space. He also noted that the Centre's total investment in developing the digital technology was less than the cost of buying the analog alternative.

This is an important lesson for engineering research. Technical novelty becomes much more consequential when it changes the economics of doing the job. The economic benefit need not be direct revenue. It may appear as avoided capital cost, reduced testing risk, fewer commissioning surprises, or lower exposure to severe system events.

### 7. Relay engineers saw a much larger application

If real-time digital simulation had remained useful only for a few HVDC projects, it is doubtful that it could have supported a long-lived standalone company. Closed-loop protection testing opened a much larger market.

A 1991 Canadian Electrical Association paper was already discussing closed-loop relay testing using electromagnetic-transient simulation. The application looked like a simple change in the device under test, but it greatly expanded the addressable problem space.

Conventional relay testing can replay calculated or recorded waveforms into a protection device and observe whether it operates. That open-loop method is valuable, especially for reproducing particular inputs. In a closed-loop test, however, the relay's trip can open a breaker in the simulated system. The system then enters a new state; new voltages and currents are produced; those signals go back to the relay; and the sequence continues.

The test therefore asks not only “Does the relay trip when it sees this waveform?” but also “What happens after it trips? Do other devices respond correctly? Do reclosing and subsequent logic coordinate as intended?”

For distance protection, line-protection coordination, and more complicated control and protection schemes, this difference is substantial. The device under test is no longer listening to a recording; it is participating in a dynamic interaction that can change what happens next.

Protection exists in far more places than HVDC converter stations. The potential user base therefore expanded from a handful of DC research facilities to utilities, equipment manufacturers, and university laboratories.

A useful commercialization pattern appears here. The team did not begin by designing an all-purpose platform and then searching for uses. It solved a hard, specific engineering problem and gradually discovered adjacent problems that could use the same underlying capability.

“Adjacent” matters because the existing technical investment remains useful. “Expansion” matters because the market is no longer trapped inside the original application.

This kind of growth may be slower than consumer-technology scaling, but it is often better suited to industrial products with high consequences and long validation cycles.

### 8. Four engineers left the Research Centre

As outside interest increased, an organizational question became unavoidable: could the Research Centre itself operate the technology as a commercial product business?

Wierckx later recalled that the real-time digital simulator had originally been developed as a research tool for the Centre, not as the foundation of a new company. After technical work was published, companies such as Hitachi and ABB expressed interest and commercialization became a serious possibility.

He also recalled that the Centre's non-profit status made its board reluctant to conduct full commercial operations inside the organization. In 1994, four employees who had participated in the development left the Centre and founded RTDS Technologies. The technology was made available to the new company under a royalty arrangement.

This was a decisive transition. The objective changed from “make it work” to “deliver it to someone else and remain responsible for it over time.”

The four engineers did not simply walk away with a piece of code and declare commercialization complete. A hardware-software product must be deliverable; interfaces must work; models must be understandable; software must be upgradeable; and customers must have someone to call when something fails. A research prototype can depend on the developer standing beside it. A commercial product has to work for users thousands of kilometres away.

The Research Centre retained a financial interest in the technology while the new company took on commercial and product responsibility. Public records show that the relationship did not disappear after the spin-out. In 2009 Wierckx still referred to the ongoing royalty agreement. He also noted that a fifth partner with real business experience later joined the company. Engineers who understand algorithms do not automatically become complete business managers, and a technology-focused company does not become less serious about engineering when it recognizes the need for commercial expertise.

Wierckx described the early company as strongly engineer-led. At board level, major decisions were often discussed until consensus emerged instead of being settled by simple majority vote. That approach depended on a small team, shared experience, a clear technical direction, and considerable mutual trust.

The lesson is not that every research team should collectively resign and form a company. It is that when a product grows beyond the natural operating boundary of its original institution, the organization needs a path that lets the product continue to develop without erasing the rights and contributions of the people and institutions that created it.

### 9. PSCAD followed a different commercialization path

While RTDS was becoming an independent company, another productization path was taking shape around EMTDC.

As a numerical engine, EMTDC could support sophisticated studies by experienced researchers. But once the user base expanded beyond the original developers, a new question appeared: should every engineer need to understand the internals of the program in order to build a network and a control system?

PSCAD's role was to turn the solver into a more complete engineering work environment. “Graphical” did not mean merely putting a prettier front end on an old program. Graphical modelling requires clear connectivity; repeatable models require consistent parameters, interfaces, and component definitions; customization must be possible without silently accepting invalid behaviour; and after a simulation, users need practical ways to compare waveforms, diagnose anomalies, save projects, and reproduce results.

The solver answers “Can the machine compute this?” The product environment must also answer “Can an engineer reliably express the problem to the machine?” Between those questions lies a great deal of work that does not always produce glamorous papers but directly determines engineering productivity.

A 1996 summer issue of the Centre's journal announced an alpha demonstration of PSCAD Version 3 during the IEEE summer power meeting in Denver. The demonstration was planned in a hotel hospitality suite, covered PC and Unix workstations, and explicitly asked prospective users for feedback before the final release.

That detail is revealing. Commercialization does not always begin with a giant trade-show booth. Sometimes it begins in a hotel suite during a technical conference, with unfinished software and a room full of engineers who know enough to criticize it.

PSCAD did not jump from laboratory code to mature product on a single day. It became a product through repeated demonstration, feedback, correction, and delivery. Customers needed more than a new algorithm: old projects had to open; outputs had to be interpretable; licensing could not obstruct ordinary work; and failures had to be diagnosable. Algorithms attract users, but mundane engineering quality often determines whether they stay.

### 10. How a PhD thesis becomes a component in an engineer's toolbox

The same 1996 summer journal recorded a smaller episode that illustrates university-industry collaboration particularly well.

Wade Enright of the University of Canterbury in New Zealand spent four months at the Research Centre. His doctoral work involved the Unified Magnetic Equivalent Circuit (UMEC) transformer model. The journal stated that the result of his PhD research would become a standard component in PSCAD Version 3.

Transformer modelling is not a problem that can be solved by drawing a nicer icon. Winding and core geometry, magnetic coupling, saturation, and operating condition can all influence electromagnetic-transient behaviour. For one class of study, a simple transformer model is sufficient; for another, the very phenomena simplified away by a basic model are the ones that matter.

The value of the university research was therefore not that the software could advertise “advanced theory.” The research entered a model library that working engineers could call directly. A user might never know the author's name or read the thesis, yet still benefit from the work in an engineering project.

The same issue of the Centre's journal also reported a high-speed transient-stability development effort involving researchers from the China Electric Power Research Institute (CEPRI), including Tang Yong, with support from the Canadian International Development Agency. For an international audience, the important point is not the nationality of the visitors. It is that the Centre was already functioning as an **international technical node** where researchers from different institutions could join a common development team.

One facility could host doctoral researchers and visiting engineers, improve detailed component models, and explore computation at different time scales. Knowledge did not move through a one-way pipeline in which a university “finished” a result and a company simply received it. It circulated through shared technical work.

By the end of this formative period, two paths had become clear. RTDS turned real-time solution, dedicated computing hardware, and interaction with physical devices into an independent product business. PSCAD organized accumulated EMT analysis capability into a software environment that many more engineers could use directly.

Both grew out of concrete engineering problems, but neither remained confined to the original problem.

---

## Part II — Growth: from solving an HVDC problem to entering the global power industry

### 11. Seventeen people serving laboratories around the world

At a January 1998 luncheon of the Manitoba engineering association, RTDS's Paul Forsyth described the company. A report published that April stated that the four-year-old firm had 17 employees, had sold more than 100 simulator racks worldwide, exported more than 95% of its products, and served universities, equipment manufacturers, and utilities.

Seventeen people were selling a product that combined specialized hardware, simulation software, models, training, and long-term technical support. The scale says a great deal about the organization.

The engineers who built the first real-time simulator were close to what would now be called full-stack engineering specialists. They needed to understand electromagnetic-transient algorithms, DSPs and parallel computation, I/O, software, protection and control interfaces, and field testing. When a problem occurred, it was difficult to say “that belongs to another module,” because the power system, the algorithm, and the hardware often sat on the same failure chain.

As the company grew, however, it did not preserve “everyone does everything” as an organizational ideal. The 1998 report already identified Paul Forsyth as a product/marketing manager. Only four years after incorporation, commercial roles were beginning to differentiate from the original technical core.

The division of labour continued to become clearer. A 2006 RTDS newsletter noted that the company was adding staff in production and customer support. By the period before its sale, RTDS had roughly 75 employees, with hardware development, software development, model development, customer support, sales and marketing, finance, product assembly, and testing all located in Winnipeg.

One organizational feature stands out: **functions became more specialized, but engineering responsibility did not become excessively fragmented.**

Public role descriptions and employee histories suggest that RTDS did not evolve into a structure where R&D “throws code over the wall” to testing, testing throws it to support, and a customer problem passes through several layers before reaching someone who understands the implementation. Many engineers combined model development with support, training, commissioning, or troubleshooting. Software developers participated in specification, testing, debugging, and post-release problem resolution.

That does not mean RTDS lacked testing. Product assembly and testing became explicit functions, and models were repeatedly checked against benchmarks and physical devices. The point is that it is misleading to imagine a huge QA organization completely separated from development. RTDS resembles a specialized engineering company: it has division of labour, but technical staff still need to understand the path from a model to a customer's laboratory.

This helps explain how a firm with only dozens of people could serve laboratories worldwide. Headquarters could not personally perform every routine activity in every country. RTDS used representatives, training, and local partners to build reach, while difficult technical problems were escalated to engineers in Winnipeg who understood the product internally.

For an industrial software and hardware company, that creates a valuable feedback loop. A protection device that cannot be connected properly, a model that behaves unexpectedly, or a large case that does not meet real-time performance is not only a support ticket. It is information about what the next product release may need.

Global sales therefore did more than ship identical machines to more countries. They continuously brought new engineering problems back to Winnipeg.

### 12. Entering an equipment manufacturer's engineering process matters more than winning praise

For a simulation company, equipment manufacturers are especially important customers.

A utility may use a simulator intensively during a particular project. A manufacturer must repeatedly design, modify, and validate control systems across many projects. Once a tool enters that workflow, it can remain relevant across a long sequence of projects rather than a single acceptance test.

A December 2000 RTDS newsletter described how ALSTOM's power-electronics operation in Stafford, United Kingdom used control-system simulation. The material reviewed applications dating back to 1994 in HVDC and static-var-compensator control testing and discussed the relationship between software control models and physical control systems. To a non-specialist this may look like a customer case study. To an HVDC engineer it means the simulator had moved close to the core design and validation loop of the control system.

In that environment, a controller cannot be judged in isolation. It has to operate in an AC network with neighbouring devices, converter stations, reactive-power controls, protection, and system operating constraints. A controller that works with an idealized source may fail once the real network boundary conditions are introduced.

An ABB case in a 2006 RTDS newsletter documented another upgrade of a FACTS test platform. ABB was already an RTDS user; the new value came from voltage-source-converter models, smaller time-step capability, larger capacity, and improved usability. Real-time digital simulation was not a one-time replacement for an old analog instrument. Power-electronic equipment evolved, and the simulator had to evolve with it.

PSCAD and RTDS can be complementary in such workflows. PSCAD is well suited to offline analysis of schemes and control mechanisms; RTDS is well suited to connecting the physical controller and checking implementation behaviour in closed loop. But complementarity does not imply identical models or lossless file interchange. Component representations, initialization, interfaces, and control timing still require engineering judgment.

The more important the customer, the less likely it is to be satisfied by a demonstration. It will ask whether model limitations are documented, abnormal conditions are repeatable, old tests still reproduce after an upgrade, and the control version used in the lab actually matches the equipment being commissioned.

Once a simulation tool becomes embedded in a manufacturer's workflow, it accumulates knowledge that is difficult to copy. The advantage is not merely a customer list. It is a history of how real projects fail, how they are corrected, and how the corrections are validated.

That accumulated experience can also become a burden. If every customer demands an unmaintainable custom version, the supplier is trapped in project work. If the supplier standardizes so aggressively that it refuses to understand site-specific differences, the tool loses engineering value. Mature industrial products live between those extremes.

### 13. The first wave: larger grids and more HVDC

PSCAD and RTDS originally dealt mainly with local HVDC systems and the surrounding AC network. As their use expanded, the scale of the questions changed. Users no longer asked only how one converter station behaved; they wanted to know how multiple HVDC links, several FACTS devices, and a large AC system interacted. They no longer examined only one controller, but complete control and protection systems, special protection schemes, and system operating conditions.

This was the first major wave in the products' growth: **large AC/DC power systems required more detailed simulation.**

That immediately exposed a fundamental tension. Large and detailed are competing objectives.

Electromagnetic-transient models retain instantaneous waveforms, three-phase unbalance, fast controls, and power-electronic switching. The cost is computation. Conventional transient-stability programs can model much larger systems by deliberately discarding many fast phenomena. In real-time simulation the trade-off is even sharper because the computer is not allowed simply to run more slowly; every time step has a deadline.

By 1996 the Manitoba group was already standing at a technical fork that remains familiar today.

The Research Centre worked on a High Speed Transient Stability Program in collaboration with researchers from the China Electric Power Research Institute. The idea was technically forward-looking: represent the wide-area AC system with electromechanical transient models, keep detailed EMT models around HVDC, FACTS, and control/protection systems, and make the two domains cooperate in real time. This could provide both system scale and local detail. The project was tested on a 500-bus system, and researchers explicitly considered simultaneous operation of EMTP-class EMT calculation and transient-stability calculation.

The idea did not disappear immediately. Wieslaw Kwasnicki developed related work into his 1998 PhD thesis, *High Speed Transient Stability: Multiprocessing Solutions*, studying parallel acceleration of large transient-stability calculations and implementation on the RTDS parallel-processing platform.

But hybrid simulation did not become the principal commercial path RTDS used to scale its product over the following decade.

RTDS largely chose the harder hardware path: **preserve the EMT level of representation and make the computer system larger and faster.**

Multi-rack parallelism was not an afterthought. In 1992 Rudi Wierckx had already described high-speed communication between simulator racks. The network could be partitioned using natural decoupling created by transmission-line models; different subsystems could run in parallel on different racks and exchange the required interface data.

That architecture became one of the principal ways RTDS increased scale: when one rack was insufficient, add racks; when processors became the limit, replace them; when calculation was fast enough but data exchange was not, improve the backplane and inter-rack communication.

Korea Electric Power Corporation's large KEPS installation pushed this approach to unprecedented scale at the time.

Around 2001, the KEPS real-time simulator had 26 racks and nearly 1,000 DSPs. Researchers reported a three-phase EMT model with roughly 320 buses and 90 generators running in real time. The model was too large for convenient whole-system verification with offline EMTP or EMTDC, so results were compared with PSS/E transient-stability simulation. The principal dynamic responses agreed well; some differences reflected the greater physical detail retained by the EMT representation.

The significance was not simply “more cabinets.”

Traditionally, real-time EMT simulation was assumed to be suitable for local networks while an entire grid belonged in a stability program. KEPS began to demonstrate another possibility: with sufficient parallel computing, systems once considered “transient-stability scale” could move into real-time EMT simulation.

The hardware of 2001 was not powerful enough to represent the entire Korean grid in full detail without reduction. Dynamic equivalents and network reduction were still required. But the direction was clear.

Around 2005, the Giga Processor Card added a new level of computing power. In 2006 the 26 KEPS racks were upgraded with GPCs, and a “Largest Equivalent System” of 511 buses and 136 generators was demonstrated. Another upgrade in 2011 expanded the installation to 100 GPCs and introduced a high-speed backplane.

That upgrade exposed a classic problem in large real-time systems: eventually the bottleneck is no longer simply processor speed, but whether all processors can exchange the required data within the same simulation step. In hard real time, average throughput is irrelevant; the slowest computation and communication path determines whether the deadline is met.

After 2015, KEPRI and RTDS planned another large expansion. By 2016 the KEPS installation had grown to 34 racks. A published model used a processed representation of the Korean transmission system with about 1,306 buses and reported that the complete KEPCO transmission network could now run in real-time EMT without the artificial network equivalencing previously required for hardware limits, while still accommodating detailed models such as planned MMC-HVDC systems.

The contrast across two decades is striking.

In 1996 engineers were seriously asking whether a 500-bus problem should be split between transient stability for the large system and EMT for a detailed local area. Twenty years later, 34 racks could bring a thousand-bus-class real transmission system into real-time EMT computation.

That does not mean hybrid simulation was wrong. EMT–transient-stability hybrid simulation later returned in RTDS-related work and remains valuable today, especially for large inverter-dominated systems. What happened is that, for a long period of product development, RTDS placed its main bet elsewhere: **hardware, parallel algorithms, and communication technology would keep chasing the growth of system size.**

This route had another advantage. From relay testing to HVDC controller HIL and then to very large AC/DC systems, users could remain largely within the same EMT modelling world. Physical representation was more consistent, and direct connection of real protection and control equipment remained natural. For a platform whose defining value is hardware-in-the-loop testing, that consistency is attractive.

Large real-time simulation laboratories later appeared at utilities, manufacturers, and research institutes around the world. RTDS therefore evolved from “selling a test instrument” toward participation in a new class of power-system laboratory infrastructure.

### 14. Real university–industry collaboration is still alive when people are modifying the model ten years later

In 2005, Canada's Natural Sciences and Engineering Research Council presented a Synergy Award for Innovation to the long-running collaboration among the University of Manitoba, the Manitoba HVDC Research Centre, and RTDS Technologies. The official description highlighted two types of output: commercialized power-system simulation technologies such as PSCAD and RTDS, and the development of highly qualified people.

Putting technology and people in the same description was not ceremonial language.

A. M. Gole of the University of Manitoba is representative of the academic side of this history. In 1983 he had already published work with Dennis Woodford and R. W. Menzies on digital simulation of DC links and AC machines, during the early development of EMTDC. He then spent decades working on HVDC, FACTS, power electronics, and electromagnetic-transient simulation. Woodford was closely associated with engineering problems and the creation of practical tools; Gole remained in the university system, continuously bringing new models, algorithms, and successive generations of graduate students into the technical ecosystem.

Later RTDS figures such as Trevor Maguire and Rudi Wierckx also grew out of the University of Manitoba and Research Centre environment. Wierckx later emphasized that graduate training in power-system simulation algorithms meant the team did not merely know how to use processors; they could design the real-time hardware architecture around the structure of the algorithms.

At that point, “university research” and “company R&D” were difficult to separate cleanly. A doctoral project might become a model in a product. A graduate student might become a core developer several years later. A problem exposed by a commercial product could return to the university as a new research question.

This continuity helps explain why the collaboration lasted for decades. It was not a simple sequence in which a company defined a project, a university completed it, and both parties signed an acceptance form. The Research Centre, utility, university, and later product companies remained around the same broad technical line. HVDC problems led to FACTS; more detailed models created real-time computation problems; larger systems required new parallel algorithms; more power electronics required new control models and smaller time steps. The problems changed, but the accumulated people, models, software, and test facilities did not scatter after every project.

For a power-system simulation tool, that continuity is particularly important. Publication of a new model is often the beginning rather than the end. Once a model enters PSCAD or RTDS, someone must implement it robustly, validate it on engineering cases, deal with extreme parameter combinations, answer customer questions, and keep it working as processors and software platforms change. Much of that work is not naturally rewarded with a new paper, but it determines whether a research result survives for three years or becomes part of an engineering tool used for thirty.

One practical way to judge university–industry collaboration is therefore to ask more than how many joint projects, papers, patents, or awards it generated:

**Ten years later, are these people still working on the same class of problems? If a model developed a decade ago reveals a new defect, is anyone still willing and able to fix it?**

That may be the most transferable lesson from Manitoba. The region did not merely complete several successful “technology-transfer projects.” It gradually built a self-reinforcing loop: engineering generated problems; research deepened them; results entered products; products entered engineering practice; new engineering problems returned to research. At the same time, students became engineers and engineers carried new questions back to the university.

When that loop survives for twenty or thirty years, university–industry collaboration stops being a project format and becomes a real regional technical capability.

### 15. A small company does not need to manufacture its own processor, but it must understand how to use one

RTDS's increasing ability to simulate larger systems can create a misleading impression: processors simply became faster, so the product naturally improved.

Processor performance was only part of the story.

Real-time simulation requires the processor, network partition, task scheduling, memory system, rack backplane, inter-rack data exchange, and I/O to operate as one deterministic system. A CPU with twice the peak throughput does not automatically double the size of a grid that can be simulated. If communication and synchronization cannot complete within the time step, hard real time is lost.

The Giga Processor Card introduced around 2005 is a good example. It used IBM PowerPC processors and gradually displaced the earlier DSP architecture, providing more headroom for larger AC networks and more complex power-electronic models. The 2006 and 2011 KEPS upgrades show how a general-purpose processor improvement can be converted into actual simulation capability.

But RTDS did not design the PowerPC processor itself.

That distinction is important for a small specialist engineering company: **it does not need to manufacture everything, but it must know which knowledge cannot be outsourced.**

A general-purpose CPU can come from IBM. What RTDS has to retain is understanding of the real-time simulation workload: how to partition the network, control communication latency, design I/O, map processor capability into simulation resources that users can actually access, and maintain the correctness of existing models when hardware changes.

In April 2017 RTDS introduced the NovaCor platform using IBM POWER8 processors, developed with support from the OpenPOWER ecosystem and IBM. For a company with only dozens of employees in Winnipeg, the strategy was rational: do not compete with semiconductor giants in CPU design; instead, reorganize world-class general computing technology into a highly specialized real-time power-system simulation platform.

The deeper product problem appears when hardware changes: what happens to the customer's existing investment?

A laboratory owns more than cabinets. It has accumulated models, wiring, interface adaptations, test scripts, staff skills, and validation records. If every performance upgrade forces those assets to be discarded, the fastest new processor may still be unattractive.

The difficult part of a real-time simulator upgrade is therefore to do two things at once: expose new computing capability while preserving as much as possible of the engineering system customers have already built.

This is why specialized industrial tools do not evolve like consumer electronics. Customers are not buying a processor. They are buying an engineering capability expected to remain useful for many years.

### 16. The second wave: inverter-dominated power systems

If the first wave forced EMT tools to deal with larger AC/DC systems, the second wave changed the role of those tools within the power industry itself.

Wind generation, photovoltaics, energy storage, and many other inverter-interfaced resources moved fast controls from a few HVDC and FACTS installations to thousands of connection points. In systems dominated by synchronous machines, engineers accumulated decades of intuition around rotor dynamics, excitation, and conventional protection. With large amounts of converter-interfaced generation, system response becomes more dependent on implementation details: phase-locked loops, current limiting, fault ride-through, control-mode switching, and interactions among controllers can determine the outcome of a disturbance.

A device that is modest in MW rating can become important if it is connected to a weak local grid or if many controllers interact through the same network.

Power-electronic dominance does not invalidate synchronous-machine knowledge, nor does it imply that every study should use the most detailed EMT representation. Power flow, electromechanical transient simulation, and electromagnetic-transient simulation each have appropriate domains. The central modelling question is whether the chosen representation contains the phenomena relevant to the problem being studied.

For PSCAD and RTDS, this transition created both opportunity and difficulty.

In the past, many users needed such tools primarily for a specific HVDC project. Today renewable integration, storage, system strength, local control interactions, and protection adaptation can all require EMT analysis.

A larger user base does not mean a vendor can simply sell more copies of an old program. The number of device models increases, vendor controls become less transparent, parameters change more frequently, and problems increasingly cross traditional organizational boundaries.

The original path from utility engineering problem to simulation tool therefore did not end. It entered a more crowded and rapidly changing system.

The renewable-energy transition also shifted simulation from “Can we compute fast enough?” toward “Is the model information truthful and complete enough?”

No amount of computing power can reconstruct a control logic that was never provided. A solver can execute an incorrect model with extraordinary numerical precision and still produce an incorrect engineering conclusion.

A new competitive dimension therefore appears: which platform can best host vendor models, protect necessary intellectual property, and still give system engineers models that are credible, executable, and verifiable?

### 17. PSCAD's growth was not only about the solver

A winter 2000 issue of the Centre's journal described cooperation with Electrotek Concepts. Electrotek promoted PSCAD in the United States and selected other markets, while the Research Centre continued to handle product orders and core technical support.

Specialized engineering software often needs technically literate channels. A user is not buying a licence to collect; the user has to integrate the tool into an existing engineering workflow.

PSCAD's organizational home also changed. A 2014 issue of *Pulse* described the Manitoba HVDC Research Centre as a business unit of Manitoba Hydro International (MHI) and reviewed the 2009 organizational consolidation. MHI was a wholly owned subsidiary of Manitoba Hydro.

That path differed from RTDS's independent-company route. The two products shared technical roots but did not remain inside one unchanging corporate structure.

Over time, PSCAD's value increasingly included the entire workflow: not only how many seconds a simulation took, but how long modelling took, how easily errors could be found, whether hundreds of cases could be automated, and whether results could be audited and reproduced.

That does not diminish the solver. On the contrary, only when the underlying numerical results are trustworthy is it worth building a large engineering workflow around them.

By the early 2020s, PSCAD and RTDS had each accumulated a substantial technical base. They adapted to the two waves of larger AC/DC systems and inverter-dominated grids while continuing to support old projects. The engineering problems that created them never disappeared simply because the products became global.

But technological success does not produce a permanent happy ending. The more important a tool becomes, the more customers demand from it. The more mature a market becomes, the more reason competitors have to enter. And the parent organizations that helped create the technology still face their own financial and governance constraints.

---

## Part III — Toward the sale: technological success does not remove business problems

### 18. World-class does not mean competition-free

In a 2009 interview, Wierckx described a turning point in the competitive environment. Early on, many people doubted that a mathematical model could be more trustworthy than scaled analog equipment, and suppliers of established analog simulators questioned the digital approach. Later, when large companies introduced their own digital simulators, the RTDS team worried that it would have to compete directly with organizations possessing far greater resources.

According to Wierckx, however, the entry of large competitors also helped legitimize digital simulation. Competitors did not merely take market share; they could also persuade previously skeptical customers that the technology itself was credible.

That is one participant's interpretation and should not be elevated into a universal rule that competition is always beneficial. It does illustrate, however, that a small technology company's competitive environment is not a simple downward pressure curve. Sometimes a market must first be convinced that an entire technical method is valid before suppliers can compete over implementation.

In offline electromagnetic-transient simulation, EMTP continued along a technical lineage independent of Manitoba. Its official history describes a major redevelopment effort beginning in the late 1990s and the introduction of a new-generation product in 2003.

Real-time simulation also had alternatives. By at least 2015, OPAL-RT was publicly describing commercial HYPERSIM projects for large power-system real-time simulation. This is enough to show that RTDS did not operate in a market without technically credible alternatives before its eventual sale.

For RTDS, long-term advantage therefore could not rest only on how many cabinets customers had already purchased. An installed base creates switching costs, but it also creates obligations. Hardware life cycle, software compatibility, interfaces, support, and engineer training all require continuing investment.

PSCAD faces a similar constraint. A large installed base of models is an advantage, but it also limits how casually a new release can change behaviour. Users need to know whether old cases still work, when revalidation is necessary, and which changes may affect results.

Competition in a mature engineering market is therefore a long examination: can a position earned by solving an original hard problem be defended by continuing to solve new ones?

### 19. The problems of the parent utility

Moving the camera back from the laboratory to Manitoba's transmission corridors reveals another class of responsibility.

In 1996 a severe storm damaged 19 transmission towers in the corridor shared by Bipoles I and II. Manitoba Hydro's official retrospective says repairs took four days and that customers voluntarily reduced consumption to help lower system demand.

Simulation can help engineers understand risk, but it cannot substitute for transmission routes, physical redundancy, repair resources, or recovery capability. The more sophisticated analytical tools become, the more important it is to remember what they can answer and what physical infrastructure must still do.

Bipole III, placed in service in 2018, follows a separate transmission path and includes a new southern converter station. Manitoba Hydro lists it at 2,000 MW and roughly 1,400 km. One of its main purposes is to reduce dependence on the existing HVDC corridor and the Dorsey converter station.

From a business perspective, projects like this and simulation products are very different enterprises.

Software and specialized technical equipment can be sold worldwide and their core knowledge reused. A transmission corridor or hydroelectric plant must be built in a specific place and carry long approval, construction, financing, maintenance, environmental, and social obligations. The businesses can reinforce one another, but the success of one does not remove the risk of the other.

Hydroelectric utilities are also exposed to hydrology. Manitoba Hydro's 2021–22 annual report documented a severe drought and its financial consequences. The utility recorded a net loss attributable to Manitoba Hydro of approximately C$248 million that year.

This does not make the technology businesses unimportant. It simply prevents us from confusing business scale and risk type. A highly valuable simulation company cannot make a capital-intensive public utility immune to drought, storms, and major infrastructure decisions.

### 20. RTDS changed owners

The main corporate story reaches 2022.

In October of that year, AMETEK acquired RTDS Technologies. On November 1, AMETEK publicly announced two acquisitions including RTDS. In its quarterly filing with the U.S. Securities and Exchange Commission, AMETEK disclosed the consideration for the RTDS transaction separately: **C$325 million, approximately US$240 million, in cash.**

The number is striking, but another question is more important: who actually sold what?

RTDS had already been an independent private company since 1994. The Research Centre and later related rights holders retained licensing and royalty relationships with the company. Manitoba Hydro did not simply wait until 2022 and then sell a software subsidiary that it had wholly owned all along.

Manitoba Hydro's quarterly report for the nine months ended December 31, 2022 explains that, before closing, MHI's royalty entitlement was converted into RTDS equity and then disposed of in the transaction. That quarterly report recorded a gain of roughly C$68 million; the 2022–23 annual report reported a one-time gain of C$69 million and stated that the royalty stream would terminate.

The organizational history can therefore be summarized more accurately as follows. Public institutions, a university, a utility, and industry partners helped incubate the technology. The product later operated as an independent company under a licence/royalty relationship. Decades later, an external strategic buyer acquired the company, and the old royalty relationship was converted and concluded as part of that transaction.

That is much more precise than saying “Manitoba Hydro sold its software company.”

AMETEK publicly described the strategic logic in terms of grid modernization, renewable energy, distributed resources, storage, and the way RTDS real-time simulation complemented its electronic instruments business.

From a technology-history perspective, the acquisition closes a circle. RTDS was created to help engineers understand HVDC systems and their protection and controls. When it was acquired, the buyer still valued the need to validate increasingly complex grids—only the range of devices and applications had become much broader.

### 21. Is a sale the final proof of success, or the beginning of another responsibility?

RTDS operated independently for more than two decades between its 1994 incorporation and the 2022 acquisition. If one starts from the earlier real-time digital simulation research, the technical history is longer still.

The transaction can certainly be viewed as a commercialization success. A tool developed initially because an institution needed a better and less expensive research capability became a global industrial product valuable enough to attract a large strategic acquirer.

But this history is not a contract template that can be copied into another jurisdiction. Intellectual-property rules, employee invention law, public funding conditions, the allocation of continuing R&D contributions, and corporate governance differ across countries and institutions. The transferable lesson is more general: when a product is still small, the relationships among contributors should be structured in a way that can survive growth, changes in control, and decades of further development.

The entrepreneurial history itself ends here.

A simulation technology that grew beside the Nelson River project passed through prototype, testing, customers, commercialization, and global markets before becoming part of another industrial group. Water still flows in northern Manitoba and electricity still moves south. But the tools developed to understand that grid have travelled much farther.

---

## Epilogue — Looking back from 2026

Return to Manitoba.

The province did not cease to experience winter, storms, drought, or transmission risk simply because it produced world-class simulation tools. The Nelson River still follows its hydrology. Transmission lines still cross real land. Winnipeg still depends on reliable physical infrastructure.

What makes PSCAD and RTDS distinctive is not that they removed those constraints. They converted part of the ability to understand and manage them from the experience of a small group of specialists into tools that many engineers could use, test, and continue to develop.

The path included an engineer sketching a solver, a research centre unable to afford an analog simulator, a team making a single filter branch work, physical controllers bringing real problems into the laboratory, and simulation tests finding problems before commissioning. It included doctoral research becoming a software model, international researchers joining development work, engineers leaving a research centre to form a company, and technology-source organizations still receiving benefits decades later under agreements created in the early years.

Taken together, those events form the entrepreneurial story.

For organizations developing industrial power-system technology today, three connected questions are especially useful.

**First: can an internal engineering need be turned into a problem that external users are willing to pay to solve?**

Internal projects provide the most authentic problems, but they also create a trap. Software may become dependent on one organization's data conventions, parameter practices, and a few experts. When the original author leaves, nobody else can use it; when the project changes, half the code must be rewritten.

Productization requires deliberately separating project-specific details from reusable solvers, models, interfaces, and test capabilities. The first time an external user completes a real job independently can be more meaningful than another impressive demonstration performed by the original development team.

Early users should not merely act as friendly supporters of a new tool. They should provide real problems and necessary information while insisting on reproducible results and traceable defects. Good early-user support provides opportunity without removing technical pressure.

**Second: can research enter the product, while the product continues to generate new research questions?**

A paper entering a model library requires implementation, testing, documentation, and maintenance. Once the model is used in engineering, it reveals operating conditions that the original publication did not cover. The most valuable university–industry relationship is not the periodic signing of a new agreement, but a channel through which questions and results can continue to move in both directions.

Evaluation systems should therefore recognize work that is less visible but essential: improving numerical robustness, maintaining regression cases, documenting parameter sources, strengthening interfaces, and fixing difficult defects. These tasks need clear owners and professional value.

Otherwise, an organization can possess many “research results” while possessing surprisingly little capability that an engineer can actually use.

Exploration also needs room, but with clear technical accountability. A filter branch can be a meaningful first prototype. A test that fails to observe the expected phenomenon can still generate useful knowledge. But a team should be able to explain what was validated, what was ruled out, and why the next step is worth taking. Patience cannot substitute for technical judgment; short-term metrics cannot substitute for it either.

**Third: can the capability be placed inside an organization appropriate to its stage of development?**

A research centre, a department of a parent organization, an independent company, a licence arrangement, and a later strategic acquisition are not simply “better” or “worse” organizational forms. They solve different problems and create different constraints.

In the early stage, when work depends on shared facilities and people from multiple institutions, forcing every research task to behave like a standalone profit centre may be counterproductive. Once a product serves international customers, running it indefinitely as an internal research project may also become inappropriate. When control changes, the rights of early contributors, the value of continuing investment, and future product responsibility all have to be addressed.

The value of an organizational arrangement should therefore be judged by whether it helps the technology continue to improve, helps users continue to receive support, and allocates risk and reward clearly—not merely by whether the corporate name changes.

This article reaches a company sale, but it is not a manual for how to sell a company.

It is a story about how, beside a very large physical power project, another kind of capability emerged—one that could travel much farther than the transmission line itself. It is also a story about how a group of engineers moved from “only we know how to do this” toward “people who have never met us can perform the task reliably.”

The most important moment in a world-class engineering tool's history may therefore not be the first shipment and not the acquisition announcement.

It may be the day when an engineer on another continent uses the tool to discover a flaw in a control strategy, correct a model, or keep a problem in the laboratory instead of allowing it to reach the operating grid.

That engineer may never have visited Winnipeg or seen the Nelson River.

But Manitoba's engineering history has already become part of that engineer's work.

---

## References

*Reference numbering follows the Chinese source edition. References [4]–[6] supported a China-specific scale comparison that is intentionally omitted from this international English adaptation.*

[1] Manitoba Government. **The Land and Climate; Lakes, Beaches and Rivers**. https://www.gov.mb.ca/jec/mbadvantage/theland.html; https://www.gov.mb.ca/sd/water/lakes-beaches-rivers/index.html.

[2] Parks Canada. **The Forks National Historic Site of Canada**. https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=151; https://parks.canada.ca/voyage-travel/promotion/manitoba/decouverte-discovery/fourche-forks.

[3] Manitoba Hydro. **Annual Report 2024–25**. 2025. https://www.hydro.mb.ca/docs/corporate/annual_report_2024_25.pdf.

[7] IEEE History Center / Engineering and Technology History Wiki. **Milestones: Nelson River HVDC Transmission System, 1972**. https://ethw.org/Milestones:Nelson_River_HVDC_Transmission_System,_1972.

[8] Manitoba Hydro. **Transmission**. https://www.hydro.mb.ca/corporate/operations/transmission/.

[9] Manitoba Government; Nisichawayasihk Cree Nation. **Hydroelectric Development Compensation and Settlement Agreements; Northern Flood Agreement**. https://www.gov.mb.ca/nrnd/settlements/index.html; https://www.ncncree.com/about-ncn/our-history/northern-flood-agreement/.

[10] Electranix Corporation. **Dennis Woodford and the Birth of EMTDC/PSCAD**. https://www.electranix.com/dennis-woodford-and-the-birth-of-emtdc-pscad/.

[11] Woodford, D. A.; Gole, A. M.; Menzies, R. W. **Digital Simulation of DC Links and AC Machines**. *IEEE Transactions on Power Apparatus and Systems*, 1983, PAS-102(6): 1616–1623. https://ieeexplore.ieee.org/document/4112117/; https://www.electranix.com/publication/digital-simulation-of-dc-links-and-ac-machines/.

[12] Woodford, D. A. **Manitoba HVDC Research Centre: World Leader in High Voltage**. *The Manitoba Professional Engineer*, October 1987. https://heritage.enggeomb.ca/images/5/5f/1987-10_Manitoba_Professional_Engineer.pdf.

[13] Wierckx, R. P.; Maguire, T. L.; Woodford, D. A.; Rosendahl, G. K. **Canadian Developments in Power System Simulation**. *IEEE Canadian Review*, No. 6, December 1989. https://canrev.ieee.ca/en/cr06/cr06.pdf.

[14] Woodford, D. A.; Marceau, R. J. **Letter to the Editor and editorial response concerning the cost/space correction for real-time digital simulation**. *IEEE Canadian Review*, No. 7, March 1990. https://canrev.ieee.ca/en/cr07/cr07.pdf.

[15] Minhaz, R. **Pep Talks with Rudi Wierckx**. *The Keystone Professional*, Summer 2009: 26–27. https://www.enggeomb.ca/pdf/Keystone/09Summer.pdf.

[16] McLaren, P.; Wierckx, R.; Kuffel, R.; Arendt, L.; Giesbrecht, J.; Lucas, J. R. **Closed Loop Relay Testing with Electromagnetic Transients Simulation**. Canadian Electrical Association, Toronto, May 1991.

[17] McLaren, P. G.; Kuffel, R.; Wierckx, R.; Giesbrecht, J.; Arendt, L. **A Real Time Digital Simulator for Testing Relays**. *IEEE Transactions on Power Delivery*, 1992, 7(1): 207–213. DOI: 10.1109/61.108909. https://ieeexplore.ieee.org/document/108909/.

[18] Kuffel, R.; Giesbrecht, J.; Maguire, T.; Wierckx, R. P.; McLaren, P. **RTDS—A Fully Digital Power System Simulator Operating in Real Time**. WESCANEX 95, 1995, Vol. 2: 300–305. DOI: 10.1109/WESCAN.1995.494045. https://doi.org/10.1109/WESCAN.1995.494045; https://knowledge.rtds.com/hc/en-us/articles/1500005393041-RTDS-A-Fully-Digital-Power-System-Simulator-Operating-in-Real-Time.

[19] Fedirchuk, D. J. **RTDS Technology Explained**. *The Manitoba Professional Engineer*, April 1998. https://heritage.enggeomb.ca/images/1/1e/98apr.pdf.

[20] Manitoba HVDC Research Centre. **Centre Journal, Summer 1996**, Vol. 9, No. 1. https://www.pscad.com/knowledge-base/download/centrejournal_summer96.pdf.

[21] Manitoba HVDC Research Centre. **Centre Journal, Winter 1996**. https://www.pscad.com/knowledge-base/download/centrejournal_winter96.pdf.

[22] Manitoba HVDC Research Centre. **Centre Journal, Winter 2000**, Vol. 11, Issue 4. https://www.pscad.com/knowledge-base/download/centrejournal_winter00.pdf.

[23] Gole, A. M.; Woodford, S. A.; Nordstrom, J. E.; Irwin, G. D. **A Fully Interpolated Controls Library for Electromagnetic Transients Simulation of Power Electronic Systems**. IPST 2001, Paper 01IPST115. https://www.ipstconf.org/papers/Proc_IPST2001/01IPST115.pdf.

[24] Government of Canada / NSERC. **NSERC to Present National Awards for University-Industry Innovation Tonight in Halifax**. October 19, 2005. https://www.canada.ca/en/news/archive/2005/10/nserc-present-national-awards-university-industry-innovation-tonight-halifax.html.

[25] Manitoba HVDC Research Centre. **Pulse, Spring 2007**. https://www.pscad.com/knowledge-base/article/142.

[26] RTDS Technologies. **RTDS News, December 2000: ALSTOM T&D Power Electronics—Innovative Use of Control System Simulations**. https://knowledge.rtds.com/hc/en-us/articles/360039292473-RTDS-News-December-2000.

[27] RTDS Technologies. **RTDS News, Summer 2006**. https://knowledge.rtds.com/hc/en-us/articles/360039284993-RTDS-News-Summer-2006.

[28] Manitoba Hydro International / Manitoba HVDC Research Centre. **Pulse, August 2014**. https://www.pscad.com/knowledge-base/download/pulse_aug2014.pdf.

[29] PSCAD / Manitoba Hydro International. **PSCAD V5 Features**. https://www.pscad.com/software/pscad/v5-features.

[30] Manitoba Hydro; archived by RTDS Technologies Knowledge Base. **Manitoba Hydro Simulation Centre Development for Nelson River HVDC Systems**. https://knowledge.rtds.com/hc/en-us/articles/360049759473-Manitoba-Hydro-Simulation-Centre-development-for-Nelson-River-HVDC-systems.

[31] RTDS Technologies. **RTDS Technologies Unveils Revolutionary Real-Time Simulation Platform Leveraging IBM POWER8 Technology**. April 3, 2017. https://www.newswire.ca/news-releases/rtds-technologies-unveils-revolutionary-real-time-simulation-platform-leveraging-ibm-power8-technology-617919973.html.

[32] Sidwall, K.; Forsyth, P. **Advancements in Real-Time Simulation for the Validation of Grid Modernization Technologies**. *Energies*, 2020, 13(16): 4036. DOI: 10.3390/en13164036. https://www.mdpi.com/1996-1073/13/16/4036.

[33] North American Electric Reliability Corporation (NERC); Cauley, G. W. **1,200 MW Fault Induced Solar Photovoltaic Resource Interruption Disturbance Report; Defining Reliability in a Transforming Electricity Industry**. https://docs.house.gov/meetings/IF/IF03/20170914/106383/HHRG-115-IF03-Wstate-CauleyG-20170914-U1.pdf.

[34] Australian Energy Market Operator (AEMO). **Modelling Requirements**. https://www.aemo.com.au/energy-systems/electricity/national-electricity-market-nem/participate-in-the-market/network-connections/modelling-requirements.

[35] NERC Inverter-Based Resource Performance Subcommittee. **White Paper: EMT Models in NERC MOD, TPL, and FAC Standards**. April 2022. https://www.nerc.com/globalassets/our-work/white-papers/supporting_paper_emt_models_mod_tpl_fac-003.pdf.

[36] OPAL-RT Technologies. **OPAL-RT Technologies Closes Year with Sale of Record-Breaking HYPERSIM Real-Time Digital Simulator**. January 30, 2015. https://www.opal-rt.com/press-room/opal-rt-technologies-closes-year-sale-record-breaking-hypersim-real-time-digital-simulator/.

[37] DIgSILENT. **Electromagnetic Transients (EMT)**. https://www.digsilent.de/en/electromagnetic-transients-emt.html.

[38] Typhoon HIL. **Test Automation; TyphoonTest**. https://www.typhoon-hil.com/resources/services/test-automation/; https://www.typhoon-hil.com/products/software/typhoontest/.

[39] EMTP. **EMTP History**. https://emtp.com/about-us/emtp-history.

[40] Manitoba Hydro. **Manitoba Hydro Reorganizes Subsidiary**. February 16, 2021. https://www.hydro.mb.ca/articles/2021/02/manitoba_hydro_reorganizes_subsidiary/.

[41] Manitoba Hydro. **Annual Report 2021–22**. 2022. https://www.hydro.mb.ca/docs/corporate/annual_report_2021_22.pdf.

[42] Manitoba Hydro. **Annual Report 2022–23**. 2023. https://www.hydro.mb.ca/docs/corporate/annual_report_2022_23.pdf.

[43] Manitoba Hydro. **Quarterly Report for the Nine Months Ended December 31, 2022**. https://www.hydro.mb.ca/docs/corporate/quarterly_report_221231.pdf.

[44] AMETEK, Inc. **Form 10-Q for the Quarter Ended September 30, 2022**. U.S. Securities and Exchange Commission filing. https://www.sec.gov/Archives/edgar/data/1037868/000103786822000054/ame-20220930.htm.

[45] AMETEK, Inc. **AMETEK Announces Two Acquisitions**. November 1, 2022. https://investors.ametek.com/news-releases/news-release-details/ametek-announces-two-acquisitions-1.

[46] Province of Manitoba. **Manitoba Hydro International Resuming Operations**. July 29, 2024. https://news.gov.mb.ca/news/?item=64397.

[47] AEMO. **Power System Model Development**. https://www.aemo.com.au/initiatives/major-programs/nem-distributed-energy-resources-der-program/managing-distributed-energy-resources-in-operations/power-system-model-development.

[48] Xiong, M.; Wang, B.; Vaidhynathan, D.; Maack, J.; Reynolds, M.; Hoke, A.; Sun, K.; Tan, J. **ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids**. *IEEE Transactions on Power Delivery*, 2024, 39(2): 911–921. DOI: 10.1109/TPWRD.2023.3342715. https://docs.nrel.gov/docs/fy24osti/86059.pdf.

[49] National Institute of Standards and Technology (NIST). **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile**. NIST AI 600-1, July 2024. DOI: 10.6028/NIST.AI.600-1. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf.

[50] RTDS Technologies. **NovaCor 2.0**. https://www.rtds.com/blogposts/novacor-2.

[51] PSCAD / Manitoba Hydro International. **PSCAD v5.1.0 Overview (March 31, 2026)**. https://www.pscad.com/knowledge-base/article/948.

[52] Union College, Electrical, Computer and Biomedical Engineering Department. **Steinmetz Memorial Lecture: Dennis Woodford, Engineers and the Strength of Our National Communities**. October 24, 2005. https://www.union.edu/ecbe/steinmetz-memorial-lecture.

[53] University of British Columbia, Department of Electrical and Computer Engineering. **Hermann Dommel**. https://ece.ubc.ca/hermann-dommel/.

[54] Dommel, H. W. **Digital Computer Solution of Electromagnetic Transients in Single- and Multiphase Networks**. *IEEE Transactions on Power Apparatus and Systems*, 1969, PAS-88(4): 388–399. DOI: 10.1109/TPAS.1969.292459.

[55] Ametani, A. **Electromagnetic Transients Program: History and Future**. *IEEJ Transactions on Electrical and Electronic Engineering*, 2021, 16: 1150–1158. DOI: 10.1002/tee.23192.

[56] Wierckx, R. P. **Fully Digital Real-Time Electromagnetic Transients Simulator**. IERE International Electric Research Exchange, Workshop on New Issues in Power System Simulation, Caen, France, 1992: 201–228. https://knowledge.rtds.com/hc/en-us/articles/1500005391421-Fully-Digital-Real-Time-Electromagnetic-Transients-Simulator.

[57] Kwasnicki, W. T. **High Speed Transient Stability: Multiprocessing Solutions**. PhD thesis, University of Manitoba, 1998. https://library-archives.canada.ca/eng/services/services-libraries/theses/Pages/item.aspx?idNumber=1356772696.

[58] Kim, T.-K.; Yoon, Y.-B.; Choo, J.-B.; Kuffel, R.; Wierckx, R. **Development and Testing of a Large Scale Digital Power System Simulator at KEPCO**. International Conference on Power Systems Transients (IPST), 2001. https://knowledge.rtds.com/hc/en-us/articles/360049483314-Development-and-Testing-of-a-Large-Scale-Digital-Power-System-Simulator-at-KEPCO.

[59] Forsyth, P.; Kuffel, R.; Wierckx, R.; Choo, J.; Yoon, Y.; Kim, T. **Comparison of Transient Stability Analysis and Large-Scale Real Time Digital Simulation**. IEEE Porto PowerTech, 2001. https://knowledge.rtds.com/hc/en-us/articles/360050253053-Comparison-of-Transient-Stability-Analysis-and-Large-Scale-Real-Time-Digital-Simulation.

[60] Park, I. K.; Lee, J.; Song, J.; Kim, Y.; Kim, T. **Large-scale AC/DC EMT Level System Simulations by a Real Time Digital Simulator (RTDS) in KEPRI-KEPCO**. *KEPCO Journal on Electric Power and Energy*, 2017, 3(1): 17–21. DOI: 10.18770/KEPCO.2017.03.01.017.

[61] RTDS Technologies. **Practical Use of Real Time Simulation for De-risking HVDC Integration**. Technical presentation, c. 2020–2021. https://knowledge.rtds.com/hc/en-us/article_attachments/360102163454.
