---
layout: article
lang: en
title: "The Remarkable Life of Robert H. Park"
permalink: "/robert-h-park-remarkable-life.html"
seo_title: "The Remarkable Life of Robert H. Park | Dehu Zou"
description: "Robert H. Park’s life across electrical engineering, chemistry, wartime research, and manufacturing, with four appendices on machine theory, stability, and converters."
updated: "2026-10-30"
---

# The Remarkable Life of Robert H. Park

In the theory of modern power system analysis, Park is a name known to every engineer. For nearly a century, his equations have remained a fundamental tool for modeling synchronous machines and analyzing power system stability. Yet the engineer who laid these important theoretical foundations at the age of twenty-seven soon left the power industry. Over the following decades, he devoted his talents to chemicals, defense technology, and mechanical manufacturing, producing inventive work in several fields.

How could an engineer in his twenties, working in an industrial company almost a century ago, create theoretical tools that remain fundamental to power system research today? The question is particularly relevant now. We have far more advanced computers, simulation platforms, and experimental equipment, as well as much larger research and development organizations. Even so, foundational engineering theories with lasting influence remain exceptionally valuable.

<details markdown="1">
<summary><strong>Contents</strong></summary>

- [I. Family and Early Years](#family-and-early-years)
- [II. Research at General Electric](#general-electric)
- [III. The Chemical Industry and Color Matching](#chemical-industry)
- [IV. Wartime Research](#wartime-research)
- [V. Innovation in Manufacturing](#manufacturing)
- [VI. Return to the Power Industry](#return-to-power)
- [VII. Conclusion](#conclusion)
- [Appendix I. Core Derivations of Park’s Theory](#appendix-i)
- [Appendix II. From the Ku Transformation to the Park Transformation](#appendix-ii)
- [Appendix III. The Equal-Area Criterion and Critical Clearing Angle](#appendix-iii)
- [Appendix IV. The Park Transformation in Converters](#appendix-iv)
- [References and Original Sources](#references)

</details>

---

<a id="family-and-early-years"></a>

## I. Park's Family and Early Years

### The Youngest Son of a Distinguished Sociologist

Robert Hiram Park was born on March 15, 1902, in Strasbourg, then part of the German Empire and now in France, to American parents living in Europe. His father, Robert Ezra Park (1864–1944), was studying philosophy and sociology at Heidelberg University. Thus, a pivotal figure in the history of twentieth-century electrical engineering was born into a family steeped in the humanities and social sciences.

His father, Robert Ezra Park, would become a celebrated American sociologist. The elder Park worked as a journalist in his youth before traveling to Germany to study philosophy and social questions. After returning to the United States, he worked at Tuskegee Institute and eventually became a central figure in sociology at the University of Chicago. He emphasized fieldwork and the investigation of urban life, seeking to understand social structures through immigrants, neighborhoods, competition, and cooperation. His research and that of his colleagues helped establish the Chicago school of sociology. For historians of sociology, Robert Ezra Park is an indispensable figure.

Park's mother, Clara Cahill Park, was also a woman of considerable talent. She wrote, participated in social reform, and took up painting later in life. The family had four children. The eldest, Edward, went on to study law; his sister Theodosia became a portrait painter; another sister, Margaret, pursued anthropological research and married the anthropologist Robert Redfield. The youngest child, Robert Hiram, chose a path of mathematics, machinery, and invention.

The family placed great value on ideas, reading, and independent judgment, but this did not mean that the children would enter the same profession. The father was concerned with people in cities; the son would become concerned with magnetic fields in rotating machines. Their subjects were very different, but both sought the structures underlying complex phenomena.

### A Journey Across America

One of the most vivid family memories of Park's youth dates from the winter of 1917. The United States had yet to build a modern interstate highway network, and many roads crossing state lines were little more than muddy ruts in rain or snow. Because fifteen-year-old Park was in poor health, his family decided that he should escape Chicago's cold, damp winter for the sunshine of California. His companion was his twenty-one-year-old sister Theodosia, and their vehicle was a secondhand Ford Model T.

The long journey brought all the hardships and adventurous pleasures of early motoring. His sister carried her painting supplies, imagining that she would sketch along the way. Instead, the reality was an endless succession of breakdowns, blowouts, puncture repairs, and tire changes. They camped overnight in the wilderness, and on difficult stretches they sometimes made only about twenty miles in a day. Throughout the trip, the fifteen-year-old repeatedly had to contend with the temperamental internal combustion engine, rudimentary transmission, and fragile rubber tires. Years later, as a portrait painter working with sitters in her studio, Theodosia still delighted in recounting the adventures she and her brother had shared in their old Ford in the American West. She also wrote a travel account that circulated within the family.

### From Wollaston to MIT

Park grew up in Wollaston, a neighborhood of Quincy, Massachusetts, and subsequently entered the Massachusetts Institute of Technology (MIT) to study electrical engineering. The year 1923 was an eventful and important one for him. On January 13, before his twenty-first birthday, he married Miriam Elizabeth Helenius / Nelson in Quincy. They later had four sons and one daughter; three sons and a daughter were still living when Park died. That same year, he received his bachelor's degree in electrical engineering from MIT.

After graduation, the young Park traveled to Stockholm, Sweden, for further study at the Royal Institute of Technology (KTH) under Henning Pleijel, a scholar of theoretical electrical engineering. He specialized in Heaviside's operational calculus. In the 1920s, before the Laplace transform became widely used, operational calculus was a leading mathematical tool for converting higher-order linear differential equations into algebraic operations and solving transient problems in circuits and electromechanical systems. This advanced training in mathematics and physics in Europe, together with his early practical experience with machinery, prepared the ground for his later theoretical breakthroughs at General Electric.

<a id="general-electric"></a>

## II. Research and Innovation at General Electric

### A Problem That Defied the Engineering Profession

After returning from Sweden, Park joined General Electric (GE). In Schenectady, New York, he completed the company's renowned Advanced Course in Engineering and worked closely with leading electrical machine specialists, including Robert E. Doherty and C. A. Nickle.

The American electric power industry was then rapidly expanding its large generating stations and long-distance, high-voltage transmission networks. Engineers found that understanding how much power a synchronous generator produced under normal steady-state conditions was no longer sufficient. When a network experienced a lightning-induced short circuit, a line trip, or a sharp load change, armature currents, field flux linkages, induced currents in damper windings, and the rotor's mechanical oscillations all interacted. The three-phase stator windings remained stationary, while the salient-pole rotor carried its field winding at high speed. Consequently, the inductance coefficients between stator and rotor—and even between the stator phases themselves—varied periodically with rotor position.

Researchers before Park had already written differential equations for synchronous machines. But equations expressed directly in the three-phase stator frame were filled with time-varying trigonometric coefficients. They were cumbersome to solve and difficult to apply to engineering design or power system fault analysis. David M. Jones, a department manager at GE, recognized the heart of the problem and saw that the young Park possessed the mathematical insight needed to bring simplicity to it. He entrusted Park with the task of putting the synchronous machine equations into a more useful form.

### System Stability as a Design Problem

Before publishing his celebrated two-reaction theory, Park and his GE colleague E. H. Bancker had already completed a foundational power systems paper, “System Stability as a Design Problem.” This twenty-four-page paper was presented at the Pacific Coast Convention of the American Institute of Electrical Engineers (AIEE), held in Spokane, Washington, on August 28–31, 1928, and formally published in the *Transactions of the AIEE* in January 1929. Park was only twenty-six when he took the podium.

The paper began with a clear argument: the power transfer capability of a long transmission line was constrained not only by conductor heating and economically acceptable voltage drop, but also by system stability. Whether generators could remain in synchronism after disturbances such as short circuits directly affected the power that a line could carry. Stability therefore needed to be a central criterion in planning generating stations and transmission networks, informing the entire process of equipment selection and control design.

The two young researchers brought generator short-circuit ratio and reactance parameters, automatic voltage regulators and fast excitation, neutral grounding impedance, prime-mover governors, rotor damper windings, and intermediate synchronous condensers into a single analytical framework. To demonstrate how strongly equipment choices and control strategies could affect the stability limit, they conducted comparative tests on a laboratory model of a 500-mile transmission line. Their baseline had no intermediate synchronous condenser and used manual excitation control on the machines at both ends. Adding only automatic voltage regulators at the two ends raised the steady-state power transfer limit by 21%. Adding only a synchronous condenser at the weak midpoint raised it by 25%. When the intermediate condenser and automatic voltage regulators on all machines operated together, the steady-state transfer limit rose by an astonishing 99%—almost doubling.

### Quantifying the Equal-Area Criterion and Critical Clearing Time

For the more severe problem of transient stability, Park and Bancker systematically explained and promoted the equal-area criterion, which would later appear in every power system textbook.

When a transmission system suffers a short circuit, the generator's electromagnetic power output capability drops abruptly, while the mechanical input from the steam or hydraulic turbine initially remains unchanged. The excess mechanical torque accelerates the rotor. Even after a circuit breaker trips and clears the fault, the relative speed the rotor has accumulated does not disappear immediately, and its power angle continues to increase. To avoid crossing the boundary of synchronism, the restored electromagnetic braking power must exceed the mechanical input, allowing the subsequent “decelerating area” to offset the entire “accelerating area”—the excess kinetic energy accumulated during the fault.

Park and Bancker used clear area diagrams on power–angle curves to explain the physical processes associated with sudden load increases and fault clearing. They also carefully distinguished two engineering situations. In one, clearing a fault on a tie feeder restored the main transmission network to its original condition. In the other, clearing a fault removed one circuit of a double-circuit or multicircuit transmission line, leaving the system in a weaker network configuration. In the latter case, three distinct power–angle curves—before, during, and after the fault—had to be considered together to calculate the net decelerating area.

In the paper's appendix, they went further, deriving an explicit formula for the critical clearing angle and converting it, through angle–time integration, into the maximum permissible fault clearing time for a circuit breaker. In one representative example, they calculated that the fault had to be cleared within 0.097 seconds—about six cycles at the North American frequency of 60 Hz—to preserve synchronism. They also plotted the maximum safe initial loading against switching time. For more complicated cases involving flux-linkage decay, excitation control, damping, and interactions among multiple generators, the paper presented a rigorous step-by-step integration method: time was divided into small increments, and each machine's flux linkages, voltage, electromagnetic torque, and rotor angular acceleration were updated at every step. Before the advent of electronic digital computers, this combination of graphical criteria, analytical formulas, and incremental numerical calculation provided a direct methodological foundation for modern power system dynamic simulation.

### Two-Reaction Theory and the Birth of Park's Equations

As Park clarified the principles of stability-oriented design at the network level, his central breakthrough in the dynamic modeling of individual machines also took shape. In 1928, he and B. L. Robertson coauthored “The Reactances of Synchronous Machines,” systematically organizing the definitions and measurement methods for steady-state, transient, and subtransient reactances. Then, in July 1929, “Two-Reaction Theory of Synchronous Machines: Generalized Method of Analysis—Part I” appeared in the *Transactions of the AIEE*, on pages 716–727. Part II followed in June 1933.

The idea of resolving the armature reaction of a salient-pole synchronous machine along the rotor pole axis—the direct or $d$ axis—and the interpolar axis—the quadrature or $q$ axis—can be traced to the two-reaction concept proposed by the French scholar André Blondel. Doherty and Nickle had also extended it to harmonic and steady-state analysis. Park took the decisive further step: he introduced a transformation into a reference frame rotating with the rotor, subsequently known as the Park transformation. Instantaneous voltages, currents, and flux linkages in the three stationary stator windings could thereby be projected directly into the direct-axis component $d$, quadrature-axis component $q$, and zero-sequence component $0$.

This change of perspective greatly simplified the calculations. In an idealized machine model, the stator–rotor inductance matrix, previously varying periodically as the rotor turned, became stationary in the rotor's own reference frame and could be expressed in constant parameters. The speed-dependent cross-coupling terms introduced by the rotating coordinates—the speed-emf terms—remained in the voltage equations with a clear physical interpretation. From balanced steady-state operation to short-circuit faults and oscillations during interconnected operation, engineers could use these celebrated Park equations as a common basis for analysis, incorporating the field and damper circuits into a unified set of differential equations with clearly defined parameters.

### Initial Silence and a Worldwide Legacy

In the memorial tribute he later wrote for the National Academy of Engineering, Charles Concordia recalled a striking episode. When the twenty-seven-year-old Park first presented the paper that would make him famous around the world, the audience fell silent: it prompted no discussion at all. Many engineers present may not yet have fully absorbed its highly abstract operators and coordinate transformations, or realized that they were witnessing a turning point in the analysis of electrical machines.

Yet a powerful theoretical tool does not depend on acclaim to prove its worth. As a later analogy put it, Park's work was like placing a ladder against a steep wall, or opening a gate into a fertile garden. The first to benefit and hurry through were the young engineers and students at the foot of the ladder who urgently needed to solve practical calculation problems. Over the following decades, “Park” became a household name among electrical engineering students throughout the world. His work underpinned transient analysis of synchronous machines and power system stability calculations. Half a century later, with the rise of power electronics, it also became a core mathematical tool for modern AC motor vector control, or field-oriented control (FOC), electric vehicle inverters, wind turbine converters, and even electronic speed controller algorithms for drones. In 2000, when the North American Power Symposium (NAPS) organized a selection of the most influential power engineering papers of the twentieth century, Park's 1929 paper ranked second, behind only Fortescue's 1918 paper on symmetrical components.

### Circuit Breaker Recovery Voltages and an Early Best Paper Award

During his few years at GE, Park also applied his talents to high-voltage switchgear. When a high-voltage circuit breaker interrupts a short-circuit current, the arc extinguishes at a current zero, and a transient recovery voltage (TRV) develops very rapidly across the contacts. If the voltage magnitude or its rate of rise exceeds the recovery of dielectric strength between the contacts, the arc can reignite, causing interruption failure and potentially even an equipment explosion.

Working with W. F. Skeats, Park used traveling-wave theory for transmission lines and two-reaction machine parameters to analyze voltage transients during the interruption of short circuits on the generator and busbar sides. Their classic paper, “Circuit Breaker Recovery Voltages: Magnitudes and Rates of Rise,” appeared in the *Transactions of the AIEE* in March 1931. The work quantified the severity of recovery voltages and directly encouraged industry to improve arc-extinguishing structures and substantially reduce high-voltage circuit breaker interrupting times. It thus completed the engineering picture behind the rapid fault clearing advocated in his stability paper. In 1930, Park and Skeats received the AIEE best paper award in the theory and research category for this work; the journal publication followed a year later.

### How a Young Engineer Could Achieve Such Breakthroughs

There is a clear developmental path behind Park's early achievements. He established his electrical engineering foundation at MIT, studied operational calculus in greater depth in Sweden, and continued his advanced engineering training at GE while working alongside machine specialists such as Doherty and Nickle. His strong mathematical education enabled him to reconsider equations that others had come to take for granted. The industrial research environment exposed him to urgent engineering problems. These experiences converged while he was still in his twenties, producing theoretical results of far-reaching importance.

Great engineering theories emerge from the effort to resolve pressing practical bottlenecks and make complex physical phenomena manageable; they are not assembled in isolation in an ivory tower. Park held no doctorate, and all these early achievements were made in industrial research. The development of large generators and long-distance transmission compelled engineers to investigate electromagnetic changes and rotor motion after faults. Whether calculation methods could handle these processes had direct consequences for equipment design and grid operation. Park's problems arose from precisely these engineering needs. Such work also requires capable research and development management within companies. Jones could assign Park an important problem because he understood its significance and could recognize the abilities needed to solve it. Power companies and equipment manufacturers depend on researchers who know field conditions, understand theory, and can organize experiments. They must judge which operating conditions a model can represent, identify discrepancies between calculations and measurements, and bring those discrepancies back into subsequent research.

<a id="chemical-industry"></a>

## III. Into the Chemical Industry and Optical Color Matching

### From Power Engineering Consultancy to the Dye Laboratory

In 1929, just after completing his landmark contribution to synchronous machine theory, Park left GE to become an electrical engineer at Stone & Webster, the prominent engineering consultancy in Boston. Only two years later, in 1931, against the backdrop of the Great Depression, he made another decision that surprised his colleagues in power engineering. He moved into the chemical industry, joining the Calco Chemical Division of American Cyanamid in Bound Brook, New Jersey, with the title of chemical engineer in charge of physical research.

Why would a gifted young engineer who had just established a generalized system of synchronous machine analysis choose successive changes of employer, and eventually leave the power industry altogether, instead of continuing his research at GE? Park did not leave an autobiography describing his thoughts at the time, but the historical setting of 1929–1931 allows us to suggest some possible motives. One was the devastating impact of the Great Depression on the power and infrastructure industries. His move to Stone & Webster in Boston in 1929 had initially taken him from manufacturing at GE into the planning and design of power networks and large generating stations—a direction consistent with the argument of “System Stability as a Design Problem,” which he had advanced in late 1928. Boston was also close to his childhood home in Wollaston, Quincy, and to his alma mater, MIT. Returning to the area would have been a reasonable choice for a man who already had several young children.

But the Wall Street crash of October 1929 plunged the United States into the worst economic depression in its history. Stone & Webster, a major owner and builder of utility power stations across the country, suffered heavily in its large-scale power infrastructure business in 1930–1931. Orders for generating equipment and grid expansion projects across the United States virtually stalled. By comparison, American Cyanamid, whose principal businesses included synthetic dyes, pharmaceuticals, and everyday chemical products, was more resilient to the downturn. It had acquired Calco Chemical in 1929, and that company urgently needed technological upgrades. There was a pressing need for modern physical measurement and automation to transform traditional chemical production.

To outsiders, moving from large rotating electrical machines to a dye and pigment plant might have seemed a complete change of profession. For Park, however, physical laws and mathematical methods did not stop at industrial boundaries. During his decade at Calco, he immersed himself in optical measurements, spectrophotometers, automatic light-absorption recording devices, and electrically heated appliances. He brought the mathematical skills honed in the electromagnetic fields of electrical machines into the world of color and light.

### Pioneering Algorithms for Computer Color Matching

The textile dyeing and plastics coloring industries faced a problem that had troubled craftspeople for generations. When a customer supplied a standard color sample, a dye house had to formulate a mixture of basic dyes—such as red, yellow, and blue—at concentrations that would produce an identical visual appearance under daylight or artificial lighting. Traditionally, experienced technicians relied on visual judgment and repeated trial dyeings, a laborious and time-consuming process.

Park recognized that the GE recording spectrophotometer invented by A. C. Hardy could already measure a material's reflectance accurately across the visible spectrum. The International Commission on Illumination (CIE) had also established the integral system of standard-observer tristimulus values, $X, Y, Z$. Could mathematical calculation replace manual trial and error, deriving dye recipes directly from spectrophotometric data?

Working with E. I. Stearns, he combined the Kubelka–Munk theory of light absorption and scattering in turbid media with colorimetry. They developed an iterative method of successive approximation using a linearized matrix of partial derivatives. Initial concentrations were obtained from sums involving reflectance at characteristic wavelengths. They then calculated the Jacobian sensitivity matrix relating deviations in tristimulus values to the concentrations of the individual dyes, and solved a system of three linear equations—or six under two illuminants—to obtain concentration corrections $\Delta a, \Delta b, \Delta c$. This work was published in February 1944 in the *Journal of the Optical Society of America* under the title “Spectrophotometric Formulation.” A dedicated calculating device he invented for this purpose was also granted a United States patent in 1951, “Color Predictions” (US 2,542,654). In the history of color science and textile dyeing, the Park–Stearns paper is widely recognized as one of the pioneering works of modern computer color matching. The mathematician who had mastered three-phase coordinate transformations in electrical machines was now using matrices and calculus to bring order to elusive colors in a chemical plant.

### An Inventor in the Kitchen

Alongside his work in sophisticated spectrophotometry, Park's inventive interests reached into the everyday kitchen. In September 1938, he filed a patent application for an “Electric Cooking Device” (US 2,233,485, granted in 1941). In November 1946, after the war, he filed another application for an improved “Electric Cooking Apparatus” (US 2,509,533, granted in 1950).

These patents described cooking vessels with built-in electric heating elements. Park linked the mechanical clamping action of the handle to the making and breaking of electrical contacts, preventing arcing and electric shock from connecting or disconnecting a live appliance or from accidental contact. He also incorporated a precise temperature-sensitive bimetallic protective mechanism into the base. If the vessel boiled dry and its bottom temperature rose abnormally, the mechanism quickly interrupted the heating circuit, preventing damage or fire. The scale of his subject had shrunk by many thousands of times, from synchronous generators rated at tens of thousands of kilowatts to domestic cooking appliances rated at a few hundred watts. His central concerns remained consistent: how heat and current flow, how mechanical actions and electrical switching can work reliably together, and how a system can protect itself under abnormal conditions.

<a id="wartime-research"></a>

## IV. Defense Research and Development

### Answering the Call at the Naval Ordnance Laboratory

By the late 1930s, the threat of war hung over Europe. In conversations with visiting Czechoslovak engineers in 1938, Park became acutely aware of the danger posed by Nazi Germany's expansion. After German forces swept through France in 1940, he resolved to set aside civilian industrial research and apply his engineering skills directly to defense preparations. Through a recommendation from Vannevar Bush, then chairman of the National Defense Research Committee (NDRC) and a senior figure from MIT, Park joined the United States Naval Ordnance Laboratory (NOL) in Washington, D.C. He took on major responsibilities in mine research and development and became deeply involved in the Bureau of Ordnance's work on underwater weapons and torpedoes. At the wartime peak, he led a research and development team of about one hundred engineers.

The Second World War was in part a technological struggle over sea routes, and magnetic influence mines were among the most advanced underwater weapons of the period. A traditional contact mine required an enemy vessel to strike a firing horn. A magnetic mine could remain on the seabed without touching the hull: as a steel ship passed overhead and caused a minute local distortion of the Earth's magnetic field, on the order of milligauss or even microgauss, the mine's magnetic sensor could detect the signal and initiate the explosive charge.

### Mine Development and the Navy's Highest Civilian Honor

Turning this concept into a reliable underwater weapon posed severe engineering challenges. The sensor had to be extremely sensitive while resisting false triggering by magnetic storms, wave-induced motion, or distant explosions. It had to survive the violent impact of being dropped from an aircraft into the sea, then remain submerged for long periods at depths of tens of meters without electrical leakage or failure.

The former specialist in the electromagnetic fields of electrical machines was in his element. In June 1941, six months before Pearl Harbor, Park and his colleague Wilson R. Maltby jointly filed an application for “Magnetic Detector” (US 2,436,394). In February 1942, he filed another application for a magnetic induction device with an improved slender core of high permeability and a mechanism for periodically driving it into saturation and resetting it. By combining the sharp saturation characteristics of a high-permeability alloy core near the knee of its hysteresis curve with flux-collecting pole pieces and differential sensing coils, they enabled a compact detector to produce a clear electrical output in response to the weak magnetic disturbance of a passing ship.

Park's contributions extended beyond magnetic fuzes to the hydrodynamics of underwater weapons and electromechanical power supplies for fuzes. With members of his team, he designed the “Streamline Depth Charge” (US 2,599,579, filed in 1946 and granted in 1952). Improvements to the body shape and the hydrodynamic design of the tail fins substantially increased its sinking speed and trajectory stability, allowing it to intercept fast-moving submerged submarines more quickly. He also invented an “Inertia Responsive Magneto Generator” (US 2,820,411), which used the large inertial forces arising during launch or impact to drive a permanent-magnet armature and generate a current pulse, providing a reliable power source for electric ammunition fuzes without conventional chemical batteries.

During the Second World War, Park's work on mines, depth charges, and ordnance fuzes resulted in seventeen patents, all assigned to the United States government without payment. In the spring and summer of 1945, American forces carried out Operation Starvation against shipping routes around the Japanese home islands. B-29 bombers laid more than twelve thousand influence mines of various types, sinking or severely damaging approximately 670 Japanese vessels and crippling the maritime transport on which Japan's war industries depended. In 1945, the United States Navy awarded Park its highest civilian honor, the Navy Distinguished Civilian Service Award, recognizing his outstanding wartime contributions to magnetic mine design.

Shortly after the war, this decorated engineer, already in his forties, returned to the classroom at George Washington University. He took a systematic course of study in electronics, like any other student, to keep abreast of the rapid wartime advances in vacuum-tube and pulse-circuit technology.

<a id="manufacturing"></a>

## V. Innovation on the Factory Floor

### Entering Manufacturing After the War

In 1946, Park joined Emhart Manufacturing Company in Hartford, Connecticut, as the head of research, development, and engineering. Emhart was then a well-known American manufacturer of glass-container forming machinery and packaging equipment. There Park recognized that lightweight, shatter-resistant thermoplastic containers—particularly polyethylene bottles—were on the verge of widespread industrial adoption. Existing blow molding processes, however, still involved many inefficient manual and semiautomatic operations.

In July 1954, he filed two closely related core patent applications: “Method for Blow Molding Hollow Articles” (US 3,008,191, granted in 1961) and “Apparatus for Blow Molding Hollow Articles” (US 3,089,186, granted in 1963). He assigned their commercial rights to the prominent container manufacturer Brockway Glass Company. The equipment incorporated a precise, continuously coordinated mechanism with multiple stations. A tubular thermoplastic parison emerged continuously from an extruder, whereupon a rotating or reciprocating mold-closing mechanism accurately enclosed and clamped it. High-pressure gas was then introduced through a blow tube, forcing the plastic against the inner mold surfaces. The process also provided precise neck finishing, cooling, and automatic release and ejection. Park organized the previously separate operations of extrusion, mold closing, blowing, cooling, and demolding into a tightly synchronized cycle of mechanical and pneumatic interlocks, making rapid, high-volume automated production of plastic bottles possible.

### Hybrid Vehicles and Electrode Experiments

Even in his seventies, Park retained an extraordinary instinct for emerging engineering problems. After the two oil crises of the 1970s, the automobile industry began to reconsider hybrid propulsion combining internal combustion engines with electric motors. Park immediately identified a central difficulty: onboard batteries subjected to frequent acceleration discharges and high-current charging during regenerative braking could fail prematurely because of overcharging, gassing, and electrode deterioration.

His United States patent “Method of Charge Control for Vehicle Hybrid Drive Batteries” (US 4,313,080), filed in May 1978 and granted in January 1982, records in detail six years of investigation from the age of seventy to seventy-six. In 1971, he visited the head of electrochemical research at General Motors to discuss traction battery characteristics. In 1972, he held further discussions with Ford researchers. After receiving a technical inquiry in 1976, the seventy-four-year-old personally cut and fabricated positive and negative electrode plates measuring two inches square and built a charge–discharge cycling test rig. In test after test, he measured polarization and gas evolution at different states of charge (SOC), temperatures, and terminal voltages.

Using these experimental measurements, he designed a hybrid energy management scheme that combined electromechanical sensing with microprocessor-based digital control. The system continuously measured engine speed, braking commands, battery current, temperature, and terminal voltage, feeding the signals through an analog-to-digital converter (ADC) to an onboard microprocessor and memory. It dynamically adjusted generator excitation and regenerative current so that the battery could absorb as much braking energy as possible while remaining within a safe gassing-voltage limit. Half a century had passed since the publication of Park's equations, yet he was still working at the leading edge of engineering.

<a id="return-to-power"></a>

## VI. A Return to the Power Industry

### Returning to the Problems of His Youth

After more than three decades away from the power industry, Park returned in the mid-1960s to the field in which he had made his name as a young man: power system transient stability.

He had renewed his interest in power system stability in the early 1960s. The 1965 blackout further underscored the reliability challenges of interconnected grids and encouraged industry discussion of fast valving. As large thermal generating units and extra-high-voltage interconnected networks developed, a nearby three-phase short circuit could create a power imbalance large enough to drive a generator out of synchronism within a fraction of a second. Park recalled the equal-area diagrams that he and Bancker had drawn in 1928 for “System Stability as a Design Problem.” If transient loss of synchronism occurred because the prime mover's mechanical input greatly exceeded the electromagnetic output during a fault, why rely solely on circuit breakers to clear the faulted line? Why not act at the source, rapidly closing down the turbine's steam admission valves immediately after the disturbance and deliberately reducing the mechanical power accelerating the rotor?

In February 1966, Park filed a patent application for “Method of Improving the Stability of Interconnected Power Systems” (US 3,515,893, granted in 1970 and reissued in 1973 as US RE27,842). At the top of its references, he placed the 1929 stability paper he had written with Bancker. A theoretical idea from his youth had become a control invention nearly forty years later. In 1968, at the age of sixty-six, he founded Fast Load Control, Inc., in Brewster and served as its president. That same year, he presented a paper at the American Power Conference, formally promoting fast turbine valving to the North American power industry.

### System Engineering Inside the Boiler and Turbine

To make the mechanical power $P_m$ on a power–angle curve fall rapidly, practical problems inside the turbine and boiler first had to be solved. In a thermal generating unit of roughly one million kilowatts, high-temperature, high-pressure steam enters the turbine at very high velocity. Abruptly closing the valves within a tenth of a second can cause a rapid pressure rise in the boiler and superheater, repeatedly lift safety valves, and potentially threaten boiler piping and reheaters. Reopening the valves at the wrong time can also produce a second power surge.

Park demonstrated the ability to integrate multiple disciplines that had characterized his entire career. In “Fast Turbine Valving,” published in the *IEEE Transactions on Power Apparatus and Systems* in 1973, and in the patent of the same name granted in 1974 (US 3,848,138), he went beyond analyzing rotor-angle swings to examine the details of boiler–turbine coordination. He investigated how rapidly opening the hydraulic actuators' pilot oil dump valves could close the intermediate-pressure intercept valves and high-pressure control valves within a fraction of a second, followed by partial or complete reopening along controlled trajectories over the next several seconds. In Figure 2 of the patent, he even provided a complete diagram of steam bypass, desuperheating and depressurization discharge, and rapid reduction of furnace firing rate, or fast runback, specifically for Unit 2 of the Tennessee Valley Authority's Cumberland plant, equipped with a Brown Boveri cross-compound turbine and a Babcock & Wilcox once-through boiler. His control logic also incorporated digital signals and stored lookup tables to distinguish severe faults from minor disturbances.

As late as 1988, when Park was eighty-six, engineers from American Electric Power (AEP) published an analysis of field tests of fast turbine valving at the Rockport plant in the *IEEE Transactions on Power Systems*. At the end of the paper, readers could still find a technical discussion signed “R. H. Park.” Even in the closing years of his life, he continued to scrutinize the measured curves from generating-station field tests.

### Formal Recognition, Late in Life

His old friend Charles Concordia described Park as intellectually sharp, direct in manner, and deeply confident in his technical judgments. In scholarly debate or engineering discussions, he defended his views firmly and incisively, with little concern for social diplomacy. He received sixty-four United States patents over his lifetime and took particular pride in later years in being able to draft complete patent claims and specifications himself. Friends and younger colleagues who consulted him found his advice incisive, dependable, and illuminating.

Because Park had left the power industry before he turned thirty, formal recognition from leading professional institutions came relatively late:

In 1965, at the age of sixty-three, he was elected a Fellow of the Institute of Electrical and Electronics Engineers (IEEE).

In 1972, at seventy, he received the IEEE Lamme Medal, a major honor in power and electrical machine engineering, for his “outstanding contributions to the analysis of AC machines and power systems.” Coincidentally, another scholar receiving the Lamme Medal that year was Yu Hsiu Ku, a Chinese scholar born in the same year as Park, also a graduate of MIT, whose paper on AC machine transient analysis had appeared alongside Park's in the same July 1929 issue of the *Transactions of the AIEE*.

In 1986, at the age of eighty-four, Park was elected to the National Academy of Engineering (NAE).

<a id="conclusion"></a>

## VII. Conclusion

Park settled in Providence, Rhode Island, in his later years and continued working as an independent consulting engineer until the age of ninety. On February 18, 1994, this engineer and inventor, whose life had spanned almost the entire twentieth century, died at the age of ninety-one. He was survived by a daughter, three sons, and a niece or nephew.

Looking back over Robert Hiram Park's life, the celebrated paper he wrote at twenty-seven was only one stage in a long creative career. In dye laboratories, the Naval Ordnance Laboratory, and plastic-bottle factories, he repeatedly turned mathematics and physics into practical technologies. In his seventies, he was still making battery plates by hand and investigating charging and discharging in hybrid vehicles. His late work on fast valving brought him back to the field of power system stability that he had helped establish in his youth.

If Park had remained in power engineering as a young man and devoted the following decades of his talent to power system research, might he have become the greatest scholar in the history of the discipline? I believe most engineers would answer yes. On the strength of the work he did leave behind, many already regard him as one of the most influential figures in power system history.

In fairness, the dozens of chemical, military, and mechanical patents Park produced after thirty, inventive though many were, did not repeat the theoretical achievement of his twenty-seventh year: reshaping the language of an entire discipline. This may be one of the regrets that history leaves us. From another perspective, however, Park himself may never have regretted his path. He was not a scholar content to spend a lifetime guarding a monument to his own theory. He was a pioneer who remained endlessly curious about the concrete problem in front of him.

The historical stature of an engineering scientist depends not only on how many particular problems he solves, but also on how many paths his ideas and tools open for those who follow. Park's equations still help engineers understand electrical machines and power networks, and his influence continues to grow through new engineering applications.

---

> This article draws on the National Academy of Engineering memorial tribute, IEEE engineering history archives, contemporary technical papers, original United States patent documents, university archival collections, and family historical materials. Appendices I–III use modern mathematical notation to derive the Park transformation, the equivalence between Yu Hsiu Ku's transformation and the Park transformation, and the equal-area criterion and critical clearing angle formulas in the 1929 Park–Bancker paper. Appendix IV uses renewable-energy grid-connected converters to explain briefly why the Park transformation remains applicable even without a physically rotating mechanical rotor.

<a id="appendix-i"></a>

## Appendix I. Core Derivations of Park's Theory

> **Scope and conventions.** This appendix uses the amplitude-invariant transformation common in modern electrical machine theory to derive the essential mathematical structure of Park's equations and explain how a rotating reference frame simplifies the dynamic equations of a synchronous machine. Throughout, the motor (passive) sign convention is used: stator current is positive when flowing into the machine, electrical angle increases in the positive direction, the rotor direct axis is the $d$ axis, and the orthogonal axis leading it is the $q$ axis.

### Starting from the Three-Phase Circuit Equations

Let the stator phase terminal voltages, currents, and flux linkages be

$$
\boldsymbol{u}_{abc}=\begin{bmatrix}u_a\\u_b\\u_c\end{bmatrix},\quad
\boldsymbol{i}_{abc}=\begin{bmatrix}i_a\\i_b\\i_c\end{bmatrix},\quad
\boldsymbol{\psi}_{abc}=\begin{bmatrix}\psi_a\\\psi_b\\\psi_c\end{bmatrix}.
$$

For symmetrical stator windings with the same phase resistance $R_s$, the voltage equation is

$$
\boldsymbol{u}_{abc}=R_s\boldsymbol{i}_{abc}
+\frac{\mathrm d\boldsymbol{\psi}_{abc}}{\mathrm dt}.
\tag{A1-1}
$$

The main difficulty in synchronous machine analysis lies in the relationship between flux linkages and currents. In an ideal linear model, the coupling between stator and rotor can be written as

$$
\boldsymbol{\psi}_{abc}=\boldsymbol{L}_{abc}(\theta)\boldsymbol{i}_{abc}
+\boldsymbol{\psi}^{(f)}_{abc}(\theta),
\tag{A1-2}
$$

where $\theta$ is the rotor electrical angle. Because the phase windings are fixed to the stator while the rotor magnetic axis rotates, some elements of $\boldsymbol{L}_{abc}(\theta)$ vary with $\theta$. The differential equations to be solved directly therefore have periodically varying coefficients.

### Constructing Two Stationary Axes, Then Rotating Them with the Rotor

The first step uses the amplitude-invariant Clarke transformation to convert the three-phase quantities into two stationary orthogonal components and a zero-sequence component:

$$
\begin{bmatrix}x_\alpha\\x_\beta\\x_0\end{bmatrix}
=\frac{2}{3}
\begin{bmatrix}
1&-\frac12&-\frac12\\
0&\frac{\sqrt3}{2}&-\frac{\sqrt3}{2}\\
\frac12&\frac12&\frac12
\end{bmatrix}
\begin{bmatrix}x_a\\x_b\\x_c\end{bmatrix}.
\tag{A1-3}
$$

Here, $x$ may represent voltage, current, or flux linkage. With the zero-sequence component retained, the transformation is invertible for arbitrary instantaneous three-phase quantities. When $x_a+x_b+x_c=0$, the zero-sequence channel may be omitted.

The second step rotates the stationary $\alpha\beta$ coordinates into $dq$ coordinates rotating synchronously with the rotor:

$$
\begin{bmatrix}x_d\\x_q\end{bmatrix}
=\underbrace{
\begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix}
}_{\boldsymbol{R}(-\theta)}
\begin{bmatrix}x_\alpha\\x_\beta\end{bmatrix}.
\tag{A1-4}
$$

Combining these two steps gives the commonly used Park transformation:

$$
\boxed{
\begin{bmatrix}x_d\\x_q\\x_0\end{bmatrix}
=\frac{2}{3}
\begin{bmatrix}
\cos\theta&\cos(\theta-\frac{2\pi}{3})&\cos(\theta+\frac{2\pi}{3})\\
-\sin\theta&-\sin(\theta-\frac{2\pi}{3})&-\sin(\theta+\frac{2\pi}{3})\\
\frac12&\frac12&\frac12
\end{bmatrix}
\begin{bmatrix}x_a\\x_b\\x_c\end{bmatrix}}
\tag{A1-5}
$$

Its inverse is

$$
\begin{bmatrix}x_a\\x_b\\x_c\end{bmatrix}
=
\begin{bmatrix}
\cos\theta&-\sin\theta&1\\
\cos(\theta-\frac{2\pi}{3})&-\sin(\theta-\frac{2\pi}{3})&1\\
\cos(\theta+\frac{2\pi}{3})&-\sin(\theta+\frac{2\pi}{3})&1
\end{bmatrix}
\begin{bmatrix}x_d\\x_q\\x_0\end{bmatrix}.
\tag{A1-6}
$$

**The essential intuition:** The stator windings do not physically rotate; we change the reference frame in which we observe the electromagnetic quantities. The rotor magnetic axis, which rotates continuously relative to the stator, becomes fixed in the rotor reference frame. Consequently, many coupling relationships that rotate with time in the original description of an ideal machine become relationships along fixed axes.

### The Crucial Step: Differentiating a Rotating Transformation

The rotating transformation matrix varies with time, so its derivative must account for the rotation of the coordinate axes. Let

$$
\omega_e=\frac{\mathrm d\theta}{\mathrm dt},\qquad
\boldsymbol{x}_{dq}=\boldsymbol{R}(-\theta)\boldsymbol{x}_{\alpha\beta}.
$$

The product rule gives

$$
\frac{\mathrm d\boldsymbol{x}_{dq}}{\mathrm dt}
=\boldsymbol{R}(-\theta)
\frac{\mathrm d\boldsymbol{x}_{\alpha\beta}}{\mathrm dt}
+\omega_e
\begin{bmatrix}0&1\\-1&0\end{bmatrix}
\boldsymbol{x}_{dq}.
\tag{A1-7}
$$

Rearranging yields

$$
\boldsymbol{R}(-\theta)
\frac{\mathrm d\boldsymbol{x}_{\alpha\beta}}{\mathrm dt}
=\frac{\mathrm d\boldsymbol{x}_{dq}}{\mathrm dt}
-\omega_e\begin{bmatrix}0&1\\-1&0\end{bmatrix}
\boldsymbol{x}_{dq}.
\tag{A1-8}
$$

The speed terms that appear here arise from the rotation of the reference frame and couple the flux linkages and voltages on the two orthogonal axes.

Applying Eq. (A1-8) to the flux-linkage vector and substituting into the three-phase voltage equation gives

$$
\boxed{
\begin{aligned}
u_d&=R_s i_d+\frac{\mathrm d\psi_d}{\mathrm dt}-\omega_e\psi_q,\\
u_q&=R_s i_q+\frac{\mathrm d\psi_q}{\mathrm dt}+\omega_e\psi_d,\\
u_0&=R_s i_0+\frac{\mathrm d\psi_0}{\mathrm dt}.
\end{aligned}}
\tag{A1-9}
$$

The terms $\omega_e\psi_q$ and $\omega_e\psi_d$ are the speed-dependent cross-coupling terms in the rotating reference frame. Their signs must be adjusted if a different orientation of the $q$ axis is adopted, or if the generator convention of positive current flowing out of the machine is used.

### Why the Synchronous Machine Model Becomes Much Simpler

For a linear, symmetrical salient-pole synchronous machine model with idealized magnetic parameters, and neglecting complex damper circuits, we may write

$$
\psi_d=L_d i_d+\psi_{\mathrm{exc}},\qquad
\psi_q=L_q i_q,
\tag{A1-10}
$$

where $L_d$ and $L_q$ are the equivalent inductances along the two magnetic axes, and $\psi_{\mathrm{exc}}$ is the equivalent direct-axis flux linkage produced by rotor excitation. Unlike the original three-phase mutual inductance coefficients, which vary with $\theta$, $L_d$ and $L_q$ are constant parameters in the ideal case once the axes have been fixed to the rotor.

Substitution into Eq. (A1-9) gives

$$
\begin{aligned}
u_d&=R_s i_d+L_d\dot{i}_d+\dot\psi_{\mathrm{exc}}-\omega_e L_q i_q,\\
u_q&=R_s i_q+L_q\dot{i}_q+\omega_e(L_d i_d+\psi_{\mathrm{exc}}).
\end{aligned}
\tag{A1-11}
$$

This reveals the source of the simplification: periodic parameter variations caused by rotating magnetic axes are converted into explicit speed-coupling terms and more readily identifiable axis parameters, giving the machine's dynamic relationships a clearer structure.

For a synchronous machine with field and damper windings, we may further write

$$
\begin{bmatrix}\psi_d\\\lambda_f\\\lambda_{kd}\end{bmatrix}
=\boldsymbol{L}_d
\begin{bmatrix}i_d\\i_f\\i_{kd}\end{bmatrix},\qquad
\begin{bmatrix}\psi_q\\\lambda_{kq}\end{bmatrix}
=\boldsymbol{L}_q
\begin{bmatrix}i_q\\i_{kq}\end{bmatrix},
\tag{A1-12}
$$

where $\lambda_f$, $\lambda_{kd}$, and $\lambda_{kq}$ denote the flux linkages of the field and damper windings themselves, while $\psi_{\mathrm{exc}}$ in Eq. (A1-10) denotes the equivalent stator flux linkage produced by excitation. After the rotor quantities have been referred consistently using the selected turns ratios and base values, the corresponding $\boldsymbol{L}_d$ and $\boldsymbol{L}_q$ are constant matrices in the ideal linear model. Combining these relations with the individual voltage equations of the rotor windings describes the dynamics of the field and damper circuits. Park's generalized analysis of 1929 followed precisely this approach, applying the two-axis concept throughout calculations of machine transients, electromagnetic torque, and multiple rotor circuits; see Reference 6.

### Obtaining Electromagnetic Torque from the Two-Axis Equations

Under the amplitude-invariant coordinate transformation, the full expression for instantaneous three-phase electrical power is

$$
P_e=u_ai_a+u_bi_b+u_ci_c
=\frac32(u_di_d+u_qi_q)+3u_0i_0.
\tag{A1-13}
$$

The last term is omitted when zero-sequence power is zero. Substituting Eq. (A1-9) separates the expression into resistive losses, terms containing flux-linkage derivatives, and terms proportional to speed. When field and damper circuits participate in the dynamic process, electrical power on both the stator and rotor sides jointly determines total magnetic energy storage and electromechanical energy conversion. In the fundamental-wave machine model described here, the electromechanical conversion power is

$$
P_{\mathrm{em}}=\frac32\omega_e(\psi_di_q-\psi_qi_d).
\tag{A1-14}
$$

The coordinate frame is fixed to the rotor. If the machine has $n_p$ pole pairs and mechanical angular speed $\omega_m=\omega_e/n_p$, then $P_{\mathrm{em}}=T_e\omega_m$ gives the electromagnetic torque as

$$
\boxed{T_e=\frac32 n_p(\psi_di_q-\psi_qi_d).}
\tag{A1-15}
$$

Here, $T_e>0$ means that the electromagnetic system drives the rotor in the positive direction of rotation. Dividing power by speed is valid at nonzero speed; the final torque expression can also be obtained by differentiating magnetic coenergy with respect to mechanical angle, and remains valid at zero speed. Substituting Eq. (A1-10) gives the familiar excitation-torque and reluctance-torque form:

$$
T_e=\frac32 n_p\left[\psi_{\mathrm{exc}} i_q+(L_d-L_q)i_di_q\right].
\tag{A1-16}
$$

This simplified expression applies to models satisfying Eq. (A1-10), such as a permanent-magnet synchronous machine with $\psi_{\mathrm{exc}}$ taken as the permanent-magnet flux linkage. The flux-linkage–current form in Eq. (A1-15) has wider applicability. When dynamic field and damper circuits are included, the corresponding complete flux-linkage model should be used.

### From a Single-Machine Model to Numerical Analysis of Large Power Systems

To remain consistent with the passive current convention above, first treat both electromagnetic torque and externally applied mechanical torque as signed quantities measured in the specified positive direction of rotation. The mechanical equations are then

$$
J\dot\omega_m=T_e+T_{\mathrm{ext}}-D(\omega_m-\omega_{m0}),
\qquad
\dot\delta=\omega_e-\omega_{\mathrm{ref}},
\tag{A1-17}
$$

where $J$ is the moment of inertia, $T_{\mathrm{ext}}$ is the externally applied mechanical torque, $D$ is the equivalent damping coefficient associated with speed deviation from the operating point, and $\delta$ is the rotor electrical angle relative to the reference frame. During generator operation, prime-mover torque is normally positive, while $T_e$ as defined here is negative. Defining the generator braking torque as $T_g=-T_e$ and writing $T_{\mathrm{ext}}=T_m$ gives the familiar equation $J\dot\omega_m=T_m-T_g-D(\omega_m-\omega_{m0})$. The two formulations are connected by $T_g=-T_e$.

Combining the equations of each synchronous machine with the excitation-system, governor-system, and network algebraic equations produces a differential-algebraic system:

$$
\dot{\boldsymbol{x}}=\boldsymbol{f}(\boldsymbol{x},\boldsymbol{y},\boldsymbol{u}),
\qquad
\boldsymbol{0}=\boldsymbol{g}(\boldsymbol{x},\boldsymbol{y},\boldsymbol{u}).
\tag{A1-18}
$$

Linearization about an operating point then yields

$$
\Delta\dot{\boldsymbol{x}}=\boldsymbol{A}\Delta\boldsymbol{x}
+\boldsymbol{B}\Delta\boldsymbol{u}.
\tag{A1-19}
$$

This connects the early problem of machine transients to modern multimachine stability simulation, eigenvalue analysis, control design, and numerical integration on computers.

The Park transformation provides a clear model structure for numerical computation. Building on this foundation, later researchers progressively refined the methods for coupling machines to networks, solving initial conditions, identifying parameters, and performing numerical integration. They incorporated saturation, harmonics, and practical control characteristics into the models, ultimately developing today's framework for dynamic simulation of large power systems.

---

<a id="appendix-ii"></a>

## Appendix II. Deriving the Park Transformation Step by Step from the Ku Transformation

Yu Hsiu Ku (1902–2002) was born in the same year as Park. Between 1923 and 1928, he earned his bachelor's, master's, and doctoral degrees at the Massachusetts Institute of Technology; his doctoral thesis was entitled *Transient Analysis of A-C. Machinery*. In July 1929, Ku's paper (pp. 707–714) and Part I of Park's two-reaction theory (pp. 716–727) appeared close together in Volume 48, Issue 3 of the *Transactions of the AIEE*. In 1951, Ku published another paper on rotating reference frames, further explaining the underlying relationship between forward and backward components and direct- and quadrature-axis components. In 1972, both men received the IEEE Lamme Medal.

### Introducing the Ku Transformation

In his research on AC machine transients, Ku developed a method based on complex variables. What is now generally called the Ku transformation combines three-phase voltages, currents, or flux linkages into forward, backward, and zero-sequence coordinates. It uses complex exponentials to represent the phase relationships among the three phases, then applies rotation factors to move the observation coordinates into a specified reference frame. The real and imaginary parts of a complex number can represent information along two orthogonal directions in a plane, so coordinate rotation becomes complex multiplication.

For real instantaneous three-phase waveforms, the forward and backward complex variables are conjugates: once one is specified, the other is determined. Their sum, and their difference multiplied by the appropriate coefficient, extract real components along two orthogonal directions. This is the starting point for deriving the Park transformation from the Ku transformation. Following this reasoning, we first write the Ku transformation, then derive the $d$-axis, $q$-axis, and zero-sequence components step by step, checking the consistency of the voltage equations, power, and torque.

### Consistent Conventions and Normalization

We retain the conventions of Appendix I: the phase axes and angles are ordered according to the positive phase sequence $a\to b\to c$, the $q$ axis leads the $d$ axis by $90^\circ$ in the positive direction of rotation, and the reference-frame angle is $\theta$. This convention fixes the coordinate directions consistently and applies to three-phase waveforms containing positive-, negative-, and zero-sequence components. Define

$$
a=\mathrm e^{\mathrm j2\pi/3},\qquad
a^2=\mathrm e^{-\mathrm j2\pi/3},\qquad
1+a+a^2=0,\qquad \mathrm j^2=-1.
\tag{A2-1}
$$

Here, the coefficient $a$ is a unit complex number, distinct from the phase label in $x_a$, whose subscript identifies phase $a$. Let

$$
\gamma_a=\theta,\qquad
\gamma_b=\theta-\frac{2\pi}{3},\qquad
\gamma_c=\theta+\frac{2\pi}{3}.
$$

The **power-invariant** Ku transformation commonly used in modern literature can be written, with rows ordered as $(f,b,0)$, as

$$
\boldsymbol{x}_{K,p}=\boldsymbol K_p(\theta)\boldsymbol{x}_{abc},\qquad
\boldsymbol K_p(\theta)=\frac1{\sqrt3}
\begin{bmatrix}
\mathrm e^{-\mathrm j\theta}&a\mathrm e^{-\mathrm j\theta}&a^2\mathrm e^{-\mathrm j\theta}\\
\mathrm e^{\mathrm j\theta}&a^2\mathrm e^{\mathrm j\theta}&a\mathrm e^{\mathrm j\theta}\\
1&1&1
\end{bmatrix}.
\tag{A2-2}
$$

The subscripts $f$, $b$, and $0$ denote forward, backward, and zero-sequence coordinates, respectively. Some publications use the order $(0,f,b)$ or denote the inverse transformation by $K$. These formulations correspond once the row and column ordering and the transformation direction have been aligned; see Reference 25.

To connect directly with the amplitude-invariant $dq0$ quantities of Appendix I, this appendix scales the entire set of Ku coordinates down by a factor of $\sqrt3$, defining

$$
\boldsymbol{x}_K=
\begin{bmatrix}x_f\\x_b\\x_0\end{bmatrix}
=\boldsymbol K(\theta)\boldsymbol{x}_{abc},\qquad
\boldsymbol K(\theta)=\frac1{\sqrt3}\boldsymbol K_p(\theta).
\tag{A2-3}
$$

Thus, the prefactor of $K$ in this appendix is $1/3$, and $x_0=(x_a+x_b+x_c)/3$. The scaled transformation remains invertible, with the coefficients in the power expressions adjusted accordingly. Under this normalization, $\lvert x_f\rvert$ for a balanced set of three-phase sinusoidal quantities equals half the phase peak value.

To avoid confusing phase $b$ with backward coordinate $b$, $x_\ell$ in the sums below always denotes an original three-phase variable, whereas $x_b$ appearing by itself in $(x_f,x_b,x_0)$ denotes the backward coordinate. Where necessary, the two are written as $x_b^{abc}$ and $x_b^K$, respectively.

### Step 1: Expressing the Ku Transformation as a Sum of Phase-by-Phase Complex Exponentials

Using Eq. (A2-1), Eq. (A2-3) is equivalent to

$$
\boxed{
\begin{aligned}
x_f&=\frac13\sum_{\ell\in\{a,b,c\}}
x_\ell^{abc}\mathrm e^{-\mathrm j\gamma_\ell},\\
x_b^K&=\frac13\sum_{\ell\in\{a,b,c\}}
x_\ell^{abc}\mathrm e^{\mathrm j\gamma_\ell},\\
x_0&=\frac13(x_a^{abc}+x_b^{abc}+x_c^{abc}).
\end{aligned}}
\tag{A2-4}
$$

First set $\theta=0$. Combining this with the Clarke transformation in Appendix I gives directly

$$
x_f^{(s)}=\frac12(x_\alpha+\mathrm jx_\beta),\qquad
x_b^{(s)}=\frac12(x_\alpha-\mathrm jx_\beta).
\tag{A2-5}
$$

Now rotate the observation coordinates through $\theta$:

$$
x_f=\mathrm e^{-\mathrm j\theta}x_f^{(s)},\qquad
x_b^K=\mathrm e^{\mathrm j\theta}x_b^{(s)}.
\tag{A2-6}
$$

The two opposite phase factors in the forward and backward coordinates therefore represent the same planar rotation in a complex basis.

### Step 2: Combining the Forward and Backward Coordinates into Direct- and Quadrature-Axis Coordinates

Define the constant matrix

$$
\boldsymbol H=
\begin{bmatrix}
1&1&0\\
-\mathrm j&\mathrm j&0\\
0&0&1
\end{bmatrix},\qquad
\begin{bmatrix}x_d\\x_q\\x_0\end{bmatrix}
=\boldsymbol H\begin{bmatrix}x_f\\x_b^K\\x_0\end{bmatrix}.
\tag{A2-7}
$$

In other words,

$$
x_d=x_f+x_b^K,\qquad
x_q=-\mathrm j(x_f-x_b^K).
\tag{A2-8}
$$

For the direct axis, substitute Eq. (A2-4) and apply Euler's formula term by term:

$$
\begin{aligned}
x_d
&=\frac13\sum_\ell x_\ell^{abc}
\left(\mathrm e^{-\mathrm j\gamma_\ell}+\mathrm e^{\mathrm j\gamma_\ell}\right)\\
&=\frac23\sum_\ell x_\ell^{abc}\cos\gamma_\ell.
\end{aligned}
\tag{A2-9}
$$

Similarly, for the quadrature axis,

$$
\begin{aligned}
x_q
&=-\frac{\mathrm j}{3}\sum_\ell x_\ell^{abc}
\left(\mathrm e^{-\mathrm j\gamma_\ell}-\mathrm e^{\mathrm j\gamma_\ell}\right)\\
&=-\frac{\mathrm j}{3}\sum_\ell x_\ell^{abc}(-2\mathrm j\sin\gamma_\ell)\\
&=-\frac23\sum_\ell x_\ell^{abc}\sin\gamma_\ell.
\end{aligned}
\tag{A2-10}
$$

Because $(-\mathrm j)(-2\mathrm j)=-2$, the quadrature-axis row contains negative sine terms. Combining the direct-axis, quadrature-axis, and zero-sequence rows gives

$$
\boxed{
\begin{bmatrix}x_d\\x_q\\x_0\end{bmatrix}
=\frac23
\begin{bmatrix}
\cos\theta&\cos(\theta-\frac{2\pi}{3})&\cos(\theta+\frac{2\pi}{3})\\
-\sin\theta&-\sin(\theta-\frac{2\pi}{3})&-\sin(\theta+\frac{2\pi}{3})\\
\frac12&\frac12&\frac12
\end{bmatrix}
\begin{bmatrix}x_a^{abc}\\x_b^{abc}\\x_c^{abc}\end{bmatrix}.}
\tag{A2-11}
$$

This agrees term by term with the Park transformation in Eq. (A1-5) of Appendix I. Hence, denoting its matrix by $\boldsymbol P(\theta)$ gives the exact identity

$$
\boxed{\boldsymbol P(\theta)=\boldsymbol H\boldsymbol K(\theta).}
\tag{A2-12}
$$

This relationship applies to arbitrary instantaneous three-phase quantities. Using the three-phase values at the same instant and the same reference angle, and retaining the zero-sequence channel, the two coordinate systems can be converted completely into one another.

### Step 3: Writing the Inverse Transformation

The inverse of the matrix in Eq. (A2-7) is

$$
\boldsymbol H^{-1}
=\begin{bmatrix}
\frac12&\frac{\mathrm j}{2}&0\\
\frac12&-\frac{\mathrm j}{2}&0\\
0&0&1
\end{bmatrix}.
\tag{A2-13}
$$

Therefore,

$$
\boxed{x_f=\frac12(x_d+\mathrm jx_q),\qquad
x_b^K=\frac12(x_d-\mathrm jx_q).}
\tag{A2-14}
$$

The Ku transformation itself is also invertible:

$$
\boldsymbol K^{-1}(\theta)=
\begin{bmatrix}
\mathrm e^{\mathrm j\theta}&\mathrm e^{-\mathrm j\theta}&1\\
a^2\mathrm e^{\mathrm j\theta}&a\mathrm e^{-\mathrm j\theta}&1\\
a\mathrm e^{\mathrm j\theta}&a^2\mathrm e^{-\mathrm j\theta}&1
\end{bmatrix}.
\tag{A2-15}
$$

Substituting Eq. (A2-14) into Eq. (A2-15), each phase satisfies

$$
\begin{aligned}
x_\ell^{abc}
&=\mathrm e^{\mathrm j\gamma_\ell}x_f
+\mathrm e^{-\mathrm j\gamma_\ell}x_b^K+x_0\\
&=x_d\cos\gamma_\ell-x_q\sin\gamma_\ell+x_0.
\end{aligned}
\tag{A2-16}
$$

This is precisely the inverse Park transformation of Appendix I. The complete relationship is

$$
\boxed{\boldsymbol K=\boldsymbol H^{-1}\boldsymbol P,\qquad
\boldsymbol P^{-1}=\boldsymbol K^{-1}\boldsymbol H^{-1}.}
\tag{A2-17}
$$

For example, set $\theta=\pi/6$, $x_d=2$, $x_q=-1$, and $x_0=0.2$. Then

$$
x_f=1-0.5\mathrm j,\qquad x_b^K=1+0.5\mathrm j,
$$

and both inverse transformations give the same set of instantaneous three-phase values:

$$
\boldsymbol{x}_{abc}
=\begin{bmatrix}\sqrt3+0.7\\-0.8\\-\sqrt3+0.7\end{bmatrix}.
$$

The example retains a nonzero zero-sequence component, and both inverse transformations still recover the same instantaneous three-phase values.

### Why Different Normalizations Produce Different-Looking Formulas

The power-invariant Park variables and the amplitude-invariant variables of Appendix I satisfy

$$
\begin{bmatrix}x_{d,p}\\x_{q,p}\\x_{0,p}\end{bmatrix}
=\operatorname{diag}\!\left(\sqrt{\frac32},\sqrt{\frac32},\sqrt3\right)
\begin{bmatrix}x_d\\x_q\\x_0\end{bmatrix}.
\tag{A2-18}
$$

For the power-invariant Ku variables in Eq. (A2-2), the corresponding constant change of basis is

$$
\begin{bmatrix}x_{d,p}\\x_{q,p}\\x_{0,p}\end{bmatrix}
=\underbrace{\begin{bmatrix}
\frac1{\sqrt2}&\frac1{\sqrt2}&0\\
-\frac{\mathrm j}{\sqrt2}&\frac{\mathrm j}{\sqrt2}&0\\
0&0&1
\end{bmatrix}}_{\boldsymbol H_p}
\begin{bmatrix}x_{f,p}\\x_{b,p}\\x_{0,p}\end{bmatrix}.
\tag{A2-19}
$$

Thus, for real instantaneous quantities, the relations
$x_{d,p}=\sqrt2\,\operatorname{Re}x_{f,p}$ and
$x_{q,p}=\sqrt2\,\operatorname{Im}x_{f,p}$ found in the literature are fully consistent with
$x_d=2\operatorname{Re}x_f$ and $x_q=2\operatorname{Im}x_f$ in this appendix; see Reference 25.

The matrices also satisfy $\boldsymbol K_p^{\mathrm H}\boldsymbol K_p=\boldsymbol I$ and $\boldsymbol H_p^{\mathrm H}\boldsymbol H_p=\boldsymbol I$, where the superscript $\mathrm H$ denotes the conjugate transpose. Thus, for real three-phase voltages and currents, $p=\boldsymbol u_{K,p}^{\mathrm H}\boldsymbol i_{K,p}=\boldsymbol u_{dq0,p}^{\mathrm T}\boldsymbol i_{dq0,p}$; power in complex coordinates uses the corresponding conjugate inner product.

Each normalization, paired with its corresponding power formula, gives the same physical result. A different coordinate order or $q$-axis orientation is handled by the appropriate permutation or sign change.

### The Dynamic Voltage Equations Also Correspond Term by Term

Let $\omega_e=\dot\theta$, and assume equal stator phase resistances. Because the Ku matrix contains time-varying phase factors,

$$
\dot{\boldsymbol K}\boldsymbol K^{-1}
=\operatorname{diag}(-\mathrm j\omega_e,\mathrm j\omega_e,0).
\tag{A2-20}
$$

For any flux-linkage vector, the product rule gives

$$
\boldsymbol K\dot{\boldsymbol\psi}_{abc}
=\dot{\boldsymbol\psi}_K
+\operatorname{diag}(\mathrm j\omega_e,-\mathrm j\omega_e,0)
\boldsymbol\psi_K.
\tag{A2-21}
$$

Transforming the three-phase voltage equation
$\boldsymbol u_{abc}=R_s\boldsymbol i_{abc}+\dot{\boldsymbol\psi}_{abc}$
into Ku coordinates gives

$$
\begin{aligned}
u_f&=R_si_f+\dot\psi_f^K+\mathrm j\omega_e\psi_f^K,\\
u_b^K&=R_si_b^K+\dot\psi_b^K-\mathrm j\omega_e\psi_b^K,\\
u_0&=R_si_0+\dot\psi_0.
\end{aligned}
\tag{A2-22}
$$

Here, in $\psi_f^K$, $u_f$, and $i_f$, the subscript $f$ denotes the forward coordinate; in Appendix I, $i_f$ instead denotes the rotor field-winding current, following the usual convention in electrical machine theory. Adding the first two equations, or subtracting them and multiplying by $-\mathrm j$, and using Eq. (A2-8), gives

$$
\boxed{
\begin{aligned}
u_d&=R_si_d+\dot\psi_d-\omega_e\psi_q,\\
u_q&=R_si_q+\dot\psi_q+\omega_e\psi_d,\\
u_0&=R_si_0+\dot\psi_0.
\end{aligned}}
\tag{A2-23}
$$

The result agrees exactly with Eq. (A1-9). The terms $\pm\mathrm j\omega_e$ in the complex equations become precisely the speed-dependent cross-coupling terms between the $d,q$ axes in real coordinates. This step remains valid even when rotational speed varies with time.

### Equivalence of Flux Linkages, Power, and Torque

Now take the simplified synchronous machine model of Appendix I, denoting the equivalent stator flux linkage produced by excitation as $\psi_{\mathrm{exc}}$:

$$
\psi_d=L_di_d+\psi_{\mathrm{exc}},\qquad \psi_q=L_qi_q.
$$

Define $\overline L=(L_d+L_q)/2$ and $\Delta L=(L_d-L_q)/2$. Equation (A2-14) gives directly

$$
\begin{aligned}
\psi_f^K&=\overline L i_f+\Delta L i_b^K+\frac{\psi_{\mathrm{exc}}}{2},\\
\psi_b^K&=\Delta L i_f+\overline L i_b^K+\frac{\psi_{\mathrm{exc}}}{2}.
\end{aligned}
\tag{A2-24}
$$

In the $dq$ representation, saliency appears as $L_d\ne L_q$; in the Ku representation, it appears as coupling through $\Delta L$ between the two complex coordinates. Both describe the same physical property.

For real instantaneous three-phase voltages and currents, three-phase power satisfies

$$
\begin{aligned}
p&=u_ai_a+u_b^{abc}i_b^{abc}+u_ci_c\\
&=3\left(u_fi_b^K+u_b^Ki_f+u_0i_0\right)\\
&=\frac32(u_di_d+u_qi_q)+3u_0i_0.
\end{aligned}
\tag{A2-25}
$$

Using $i_b^K=i_f^{\ast}$ and $u_b^K=u_f^{\ast}$, this can also be written as

$$
p=6\operatorname{Re}(u_fi_f^*)+3u_0i_0.
\tag{A2-26}
$$

Electromagnetic torque likewise satisfies

$$
\boxed{
T_e=\frac32n_p(\psi_di_q-\psi_qi_d)
=6n_p\operatorname{Im}\!\left[(\psi_f^K)^*i_f\right].}
\tag{A2-27}
$$

The coordinate transformations, voltage equations, instantaneous power, and electromagnetic torque thus correspond one to one. The torque retains the signed convention of Appendix I: a positive value drives the rotor in the positive direction of rotation, while generator braking torque is denoted by $T_g=-T_e$.

### How the Forward and Backward Coordinates Represent Positive and Negative Sequences

When the original three-phase quantities are real instantaneous values, the first two rows of the Ku matrix are conjugates, so

$$
x_b^K=x_f^*.
\tag{A2-28}
$$

Together, the two coordinates represent two real degrees of freedom, with $x_d=2\operatorname{Re}x_f$ and $x_q=2\operatorname{Im}x_f$. For general complex phasors, the full relations in Eq. (A2-8) should be used.

For example, a purely positive-sequence set of three-phase sinusoidal quantities,

$$
\begin{aligned}
x_a^{abc}&=X\cos(\omega t+\varphi),\\
x_b^{abc}&=X\cos(\omega t+\varphi-2\pi/3),\\
x_c^{abc}&=X\cos(\omega t+\varphi+2\pi/3)
\end{aligned}
$$

gives, in a reference frame with $\theta=\omega t$,

$$
x_f=\frac X2\mathrm e^{\mathrm j\varphi},\qquad
x_b^K=\frac X2\mathrm e^{-\mathrm j\varphi},\qquad
x_d=X\cos\varphi,\quad x_q=X\sin\varphi.
\tag{A2-29}
$$

These purely positive-sequence waveforms produce a pair of nonzero conjugate coordinates. Here, “backward” describes how the complex coordinates are organized; a negative-sequence component in the supply must still be identified from the direction in which the waveform rotates.

If the space vector expressed in the stationary reference frame contains components rotating in both directions, write

$$
z_s(t)=A\mathrm e^{\mathrm j\omega t}+B\mathrm e^{-\mathrm j\omega t},
$$

so that, in the positively rotating synchronous reference frame,

$$
z_r(t)=\mathrm e^{-\mathrm j\omega t}z_s(t)
=A+B\mathrm e^{-2\mathrm j\omega t}.
\tag{A2-30}
$$

The negative-sequence component therefore appears as a double-frequency variation in the positively rotating synchronous frame. Ku coordinates and $dq$ coordinates give the same result.

### The Relationship Between the Two Coordinate Systems

Starting from the Ku transformation, we have obtained the Park transformation through a constant change of basis independent of the angle $\theta$, represented by the invertible matrix $\boldsymbol H$. The two transformations are coordinate representations of the same space of three-phase variables. Their most concise relationship is

$$
\boxed{\boldsymbol P=\boldsymbol H\boldsymbol K,\qquad
\boldsymbol K=\boldsymbol H^{-1}\boldsymbol P.}
$$

With zero sequence retained, this equivalence applies to balanced and unbalanced instantaneous three-phase quantities, in both steady state and transients, and rotational speed may vary with time. Under ideal assumptions such as symmetrical windings, a fundamental air-gap field, and a linear magnetic circuit, both representations also make the machine inductance parameters constant, greatly simplifying dynamic analysis.

One might ask: from the basic principles of linear algebra, any invertible constant matrix $\boldsymbol H$ can be used to derive a transformation equivalent to the Park transformation. What, then, is the particular significance of the Ku transformation?

The key is that $\boldsymbol H$ in Eq. (A2-7) is not an arbitrarily chosen invertible matrix. It is the basis transformation connecting two-dimensional orthogonal real coordinates with conjugate complex coordinates. A general invertible matrix would only increase the coupling among channels in the differentiation operation. This particular $\boldsymbol H$, however, diagonalizes the planar rotation operator, reducing the rotational derivative terms to the purely diagonal matrix $\dot{\boldsymbol K}\boldsymbol K^{-1}=\operatorname{diag}(-\mathrm j\omega_e,\mathrm j\omega_e,0)$; see Eq. (A2-20). Consequently, the speed-dependent cross-coupling terms between the $d$ and $q$ axes in Park's equations ($-\omega_e\psi_q$ and $+\omega_e\psi_d$) become separate scalar multipliers $\pm\mathrm j\omega_e$ in Ku coordinates; see Eqs. (A2-22) and (A2-23).

The Ku transformation also connects instantaneous symmetrical components with space-vector theory, offering a particularly intuitive treatment of three-phase unbalance and the separation of positive and negative sequences. Equations (A2-2) and (A2-5) show that, in the stationary reference frame $\theta=0$, the Ku transformation is precisely an instantaneous symmetrical-component transformation built from the unit complex operator $a=\mathrm e^{\mathrm j2\pi/3}$. Its forward component, $x_f^{(s)}=\frac12(x_\alpha+\mathrm jx_\beta)$, directly represents the complex space vector in the stationary $\alpha\beta$ plane, consistent with the voltage space vector $\underline u=u_\alpha+\mathrm ju_\beta$ in Appendix IV. On moving to the synchronously rotating frame ($\theta=\omega t$), Eqs. (A2-29) and (A2-30) show that the forward- and backward-rotating electromagnetic components map directly to a constant complex phasor and a double-frequency rotating term $B\mathrm e^{-2\mathrm j\omega t}$. This representation can make formulation and analytical calculation more convenient in specific problems, such as unsymmetrical fault analysis in AC machines and positive- and negative-sequence analysis of modern renewable-energy grid-connected converters under three-phase unbalance.

### Why Park's Theory Achieved Broader Influence

In my view, the broader engineering influence that Park's theory later attained owes much to the intuitive nature of real $dq$ coordinates. The direct axis follows the rotor magnetic pole, and the quadrature axis is perpendicular to it, allowing the relationships among current, flux linkage, and torque to be understood directly along these two directions. With the advent of computers and automatic control, these real variables also connected naturally to state equations, control block diagrams, and signal channels in software, making them convenient both for teaching and for computer implementation.

A deeper reason is that, from an early age, Park placed machine dynamics within the problem of power-system stability. His paper “System Stability as a Design Problem,” presented in 1928, already connected generator parameters, excitation control, fault clearing, and transmission networks, discussing how they jointly determine transfer capability and synchronous operation. Machine equations thus became a fundamental tool linking equipment performance to grid behavior. Ku's early research focused principally on AC machine transient analysis, extending to networks and interconnected machines in 1951. Park, however, had already closely integrated machine modeling with power-system stability design while still in his twenties.

This system-wide perspective, looking beyond an individual machine to the entire grid, brought Park's theory directly to bear on electrical power engineering's most urgent problems. As interconnected grids expanded, it continually found new applications in stability calculations, simulation software, and control design, gradually becoming a shared language for generations of engineers.

---

<a id="appendix-iii"></a>

## Appendix III. The Equal-Area Method in the Park–Bancker Paper: From the Swing Equation to the Critical Clearing Angle

> Based on Park and Bancker’s “System Stability as a Design Problem,” this appendix uses modern notation to derive the swing equation, the equal-area criterion, and the critical clearing angle relationship presented in that paper. The original paper is listed as Reference 28.

### The Rotor Swing Equation and the Energy Integral

Consider a classical single-machine–infinite-bus system, or a lossless two-machine system reduced using an equivalent inertia. Let $\delta$ be the rotor’s electrical angle relative to the synchronous reference frame, in radians; $\omega_s$ the synchronous electrical angular velocity; and $H$ the inertia constant. (The inertia constant defined on page 175 of the original paper is twice the kinetic energy at rated speed divided by the base power, corresponding to $2H$ in modern notation.) Denote the prime mover’s mechanical input power by $P_m$ and the generator’s electromagnetic power output by $P_{\mathrm{out}}(\delta)$, with all powers expressed in per unit on the same base. Neglecting damping, the classical swing equation is

$$
\mathcal M=\frac{2H}{\omega_s},
\qquad
\mathcal M\ddot\delta=P_m-P_{\mathrm{out}}(\delta).
\tag{A3-1}
$$

(For two machines with finite inertias $\mathcal M_1, \mathcal M_2$, take the relative angle $\delta=\delta_1-\delta_2$ and replace the inertia and mechanical power in the equation with the equivalent inertia $\mathcal M_{\mathrm{rel}}=\frac{\mathcal M_1\mathcal M_2}{\mathcal M_1+\mathcal M_2}$ and equivalent driving power $P_{m,\mathrm{rel}}=\frac{\mathcal M_2P_{m1}-\mathcal M_1P_{m2}}{\mathcal M_1+\mathcal M_2}$ given on page 177 of the original paper.)

Multiplying both sides of Equation (A3-1) by the relative angular velocity $\dot\delta$ and integrating from the initial steady-state condition $(\delta_0, \dot\delta_0=0)$ yields the energy integral identity

$$
\boxed{
\frac12\mathcal M\dot\delta^2
=\int_{\delta_0}^{\delta}
[P_m-P_{\mathrm{out}}(\alpha)]\,\mathrm d\alpha
}.
\tag{A3-2}
$$

When the rotor reaches its maximum angle $\delta_{\max}$ at the peak of the first swing, its relative velocity is $\dot\delta=0$. The left-hand side of Equation (A3-2) is therefore zero, and the net integrated area on the right must also be zero: the accelerating area accumulated during the fault must equal the net decelerating area after fault clearing.

### Deriving the Critical Clearing Angle from the Equal-Area Criterion

Let the sinusoidal power–angle characteristics before, during, and after the fault be

$$
P_{\mathrm{out}}^{\mathrm{pre}}=P_0\sin\delta,\qquad
P_{\mathrm{out}}^{\mathrm F}=P_F\sin\delta,\qquad
P_{\mathrm{out}}^{\mathrm{post}}=P_C\sin\delta.
\tag{A3-3}
$$

Before the fault, the system operates at the stable equilibrium point $\delta_0=\arcsin(P_m/P_0)$.

After a short circuit occurs, the rotor accelerates while $P_m > P_F\sin\delta$, until the circuit breaker trips and clears the fault at the clearing angle $\delta_c$.

The accelerating area accumulated during the fault is

$$
A_{\mathrm{acc}}
=\int_{\delta_0}^{\delta_c}
(P_m-P_F\sin\delta)\,\mathrm d\delta
=P_m(\delta_c-\delta_0)
+P_F(\cos\delta_c-\cos\delta_0).
\tag{A3-4}
$$

Assuming that the post-fault system satisfies $0 < P_m < P_C$, the new stable equilibrium angle and the adjacent unstable equilibrium angle—the saddle point associated with loss of synchronism—are

$$
\delta_s=\arcsin\frac{P_m}{P_C},
\qquad
\delta_u=\pi-\arcsin\frac{P_m}{P_C}.
\tag{A3-5}
$$

From the clearing angle $\delta_c$ to the loss-of-synchronism boundary angle $\delta_u$, the maximum signed net decelerating area available from the post-fault network is

$$
A_{\mathrm{dec,net}}
=\int_{\delta_c}^{\delta_u}
(P_C\sin\delta-P_m)\,\mathrm d\delta
=P_C(\cos\delta_c-\cos\delta_u)
-P_m(\delta_u-\delta_c).
\tag{A3-6}
$$

At the critical condition, set $A_{\mathrm{acc}}=A_{\mathrm{dec,net}}$ and denote the critical clearing angle by $\delta_c=\delta_{\mathrm{cr}}$:

$$
P_m(\delta_{\mathrm{cr}}-\delta_0)
+P_F(\cos\delta_{\mathrm{cr}}-\cos\delta_0)
=P_C(\cos\delta_{\mathrm{cr}}-\cos\delta_u)
-P_m(\delta_u-\delta_{\mathrm{cr}}).
\tag{A3-7}
$$

Canceling the $P_m\delta_{\mathrm{cr}}$ terms on both sides and rearranging gives the critical clearing angle formula commonly used in modern textbooks:

$$
\boxed{
\cos\delta_{\mathrm{cr}}
=\frac{
P_m(\delta_u-\delta_0)
+P_C\cos\delta_u-P_F\cos\delta_0
}{P_C-P_F}
}.
\tag{A3-8}
$$

Introduce the amplitude ratios defined by Park and Bancker on page 190 of the original paper:

$$
r_1=\frac{P_F}{P_0},\qquad
r_2=\frac{P_C}{P_0},\qquad
\frac{P_m}{P_0}=\sin\delta_0,
$$

Dividing the numerator and denominator of Equation (A3-8) by $P_0$ immediately gives an expression identical to that in Appendix VIII of the 1929 paper:

$$
\boxed{
\cos\delta_{\mathrm{cr}}
=\frac{
\sin\delta_0(\delta_u-\delta_0)
-r_1\cos\delta_0+r_2\cos\delta_u
}{r_2-r_1}
}.
\tag{A3-9}
$$

### Critical Clearing Time and Fast Valving

Solving Equation (A3-2) for the fault-on angular velocity $\dot\delta(\delta)$ and integrating using $\mathrm dt=\mathrm d\delta/\dot\delta$ gives the circuit breaker’s critical clearing time $t_{\mathrm{cr}}$, corresponding to Appendices IV and VIII of the original paper:

$$
\boxed{
t_{\mathrm{cr}}
=\int_{\delta_0}^{\delta_{\mathrm{cr}}}
\frac{\mathrm d\delta}{
\sqrt{\dfrac{2}{\mathcal M}
\displaystyle\int_{\delta_0}^{\delta}
[P_m-P_{\mathrm{out}}^{\mathrm F}(\alpha)]
\,\mathrm d\alpha}}
}.
\tag{A3-10}
$$

In the special case of a bolted three-phase short circuit at the generator terminals, for which $P_{\mathrm{out}}^{\mathrm F}=0$, the rotor has constant angular acceleration, $\delta(t)-\delta_0=\frac{P_m}{2\mathcal M}t^2$. Equation (A3-10) then reduces to the explicit square-root formula

$$
\boxed{
t_{\mathrm{cr}}
=\sqrt{\frac{2\mathcal M(\delta_{\mathrm{cr}}-\delta_0)}{P_m}}
=\sqrt{\frac{4H(\delta_{\mathrm{cr}}-\delta_0)}
{\omega_sP_m}}
}.
\tag{A3-11}
$$

If excitation control, flux-linkage decay, governor action, or the fast turbine valving promoted by Park in his later years are also included, with their states collected in the vector $\boldsymbol z$, together with a damping term $D_\delta\dot\delta$, the system dynamics are described by coupled differential equations:

$$
\begin{aligned}
\mathcal M\ddot\delta+D_\delta\dot\delta
&=P_m(t,\boldsymbol z,\dot\delta)
-P_{\mathrm{out}}(\delta,t,\boldsymbol z),\\
\dot{\boldsymbol z}
&=\boldsymbol f(\delta,\dot\delta,\boldsymbol z,t),
\end{aligned}
\tag{A3-12}
$$

The energy balance along the actual trajectory then generalizes to

$$
\frac12\mathcal M
\bigl[\dot\delta(t_2)^2-\dot\delta(t_1)^2\bigr]
=\int_{t_1}^{t_2}\bigl[P_m(t,\boldsymbol z,\dot\delta)-P_{\mathrm{out}}(\delta,t,\boldsymbol z)\bigr]
\dot\delta\,\mathrm dt
-\int_{t_1}^{t_2}D_\delta\dot\delta^2\,\mathrm dt.
\tag{A3-13}
$$

Equation (A3-13) makes the physical basis of Park’s later work on fast valving readily apparent. Rapidly reducing the steam-valve opening after a fault forces $P_m(t,\boldsymbol z,\dot\delta)$ to fall quickly during the first swing. This directly reduces the net accelerating work in the first integral on the right-hand side and thereby substantially increases the transient stability margin of the interconnected grid.

---

<a id="appendix-iv"></a>

## Appendix IV. Why Converters Can Still Use the Park Transformation Without a Rotor


> **Conventions.** This appendix uses the amplitude-invariant transformation from Appendix I, with the $q$ axis leading the $d$ axis. For balanced sinusoidal quantities, the amplitude in synchronous coordinates corresponds to the phase peak value. Grid current is positive from the converter toward the grid. The analysis uses a switching-period-averaged model of a three-phase, three-wire system with a symmetrical linear RL filter; the power-control relationships apply to the balanced fundamental component.

Photovoltaic inverters and energy-storage converters use semiconductor devices such as IGBTs and SiC MOSFETs to convert electrical energy. Their main power circuits do not depend on mechanical rotation, yet they can still use the Park transformation. The reason is that **the Park transformation rotates the reference coordinates used to observe three-phase electrical quantities; it does not require a mechanical rotor to exist.**

### An Intuitive View: The “Virtual Rotor” and Rotating Voltage Produced by High-Speed Power-Electronic Switching

Begin by recalling the stator of an induction motor. Its three-phase windings are stationary, with their magnetic axes successively displaced by $120^\circ$ electrical in space. When balanced three-phase AC currents flow through them, the currents are also successively displaced by $120^\circ$ in time phase. Under the ideal assumptions of symmetrical windings and fundamental components only, the pulsating magnetomotive forces produced by the three windings add to form a resultant magnetomotive force of constant magnitude and continuously rotating direction, establishing a rotating magnetic field in the air gap. The coils do not rotate, but the resultant magnetic field does. The key is the coordination between the spatial distribution of the windings and the time variation of the currents.

This phenomenon offers an intuitive route to understanding converters: “rotation” can also describe the combined effect of several time-varying quantities. In a machine, that effect takes the form of a physical rotating magnetic field; in a converter, it can first be understood through the rotating vector formed from the three-phase output voltages.

The converter’s DC bus supplies electrical energy. High-speed switching of the semiconductor devices connects each phase leg to different DC-bus potentials as required by the controller. By arranging the switching sequence and duty ratios, the controller can make the three-phase output voltages, after removal of zero sequence, follow prescribed sinusoidal trajectories in a switching-period-averaged sense, within the modulation range. In a conventional two-level, three-phase bridge, for example, the switching states correspond to six nonzero voltage vectors and two zero vectors. Space-vector pulse-width modulation (SVPWM) synthesizes the required average voltage vector by allocating the time spent in each state during a switching period.

Denote the average three-phase voltages by $u_a,u_b,u_c$. When they are balanced sinusoidal quantities with phase peak value $U$ and positive-sequence phase $\phi$, they can be represented together by a single “voltage arrow”:

$$
\underline u=u_\alpha+j u_\beta
=\frac23\left(u_a+u_b e^{j2\pi/3}+u_c e^{-j2\pi/3}\right)
=Ue^{j\phi}.
$$

Here, $j$ is the imaginary unit. The arrow’s length represents the voltage magnitude, and its direction represents the common phase of the three-phase voltages. As $\phi$ advances, the arrow rotates in the $\alpha\beta$ plane. Through controlled switching modulation, DC electrical energy produces a three-phase AC output that can be described by a rotating voltage vector. This continuous rotation refers to the fundamental or switching-period-averaged quantities; the actual bridge-terminal voltages still contain switching pulses and ripple.

The “space vector” is a unified mathematical representation of three-phase electrical quantities. For a typical grid-connected converter, using this representation requires only the phase relationships among the three-phase quantities. If the converter is connected to a motor’s three-phase windings, the output currents also establish a physical rotating magnetic field in the air gap through the spatial distribution of those windings. This connects the “rotating voltage vector synthesized by the circuit” with the “rotating magnetic field synthesized by the windings.”

In a synchronous generator, DC excitation establishes a magnetic field on the rotor. Rotation of the rotor moves this field relative to the stator windings, changing their flux linkages and inducing three-phase electromotive forces. This is what is commonly meant by the rotor field “cutting” the stator coils. The three-phase fundamental internal electromotive forces can likewise be represented by a rotating voltage vector.

Through switching modulation, a converter can also synthesize three-phase fundamental voltages with the required magnitude, frequency, and phase, within its permissible voltage range. Thus, at the level of the fundamental voltage at the AC port, the converter can be pictured as using electronic switches to perform the role of the excited rotor in establishing three-phase electromotive forces. Modulation control determines the magnitude of the synthesized voltage and the law governing its phase advance, while the DC-side energy source supplies the actual electrical energy. Together with a filter or equivalent impedance, these elements form an appropriate port circuit model. Care is also needed when comparing phases: in sinusoidal steady state, a synchronous machine’s induced electromotive force differs from its rotor excitation flux linkage by $90^\circ$ electrical, so the voltage-vector phase cannot be treated directly as the rotor magnetic-axis angle.

This analogy explains how the voltage is produced. To emulate a synchronous machine’s rotor swing and inertial response, however, the converter also needs appropriate dynamic control, with actual reserve generation or energy storage supporting the required energy exchange. Using the Park transformation in a control strategy does not, by itself, give a converter mechanical inertia or the characteristics of a virtual synchronous machine.

### Three-Phase AC Quantities Can Become “Stationary” in the Reference Frame

For the real instantaneous values $x_a,x_b,x_c$ of three-phase voltages or currents, the Park transformation can be written directly as

$$
\begin{bmatrix}x_d\\x_q\end{bmatrix}
=\frac23
\begin{bmatrix}
\cos\theta&\cos(\theta-\frac{2\pi}{3})&\cos(\theta+\frac{2\pi}{3})\\
-\sin\theta&-\sin(\theta-\frac{2\pi}{3})&-\sin(\theta+\frac{2\pi}{3})
\end{bmatrix}
\begin{bmatrix}x_a\\x_b\\x_c\end{bmatrix}.
\tag{A4-1}
$$

For balanced three-phase sinusoidal quantities, let $x_a=X\cos\phi$, $x_b=X\cos(\phi-2\pi/3)$, and $x_c=X\cos(\phi+2\pi/3)$. Choosing the reference angle $\theta=\phi$ and substituting gives $x_d=X$ and $x_q=0$: with constant amplitude, the three-phase AC quantities become constants in synchronous coordinates. This operation simply projects three real signals. It requires neither a rotating shaft in the circuit nor a machine-like rotating magnetic field produced by the filter inductors.

In terms of the “voltage arrow” introduced above, this projection can also be written as $u_d+j u_q=\underline u\,e^{-j\theta}=Ue^{j(\phi-\theta)}$. When the coordinates follow the voltage vector at the same angular velocity and phase, $\phi-\theta=0$, and the observed components are $u_d=U$ and $u_q=0$. The Park transformation can therefore treat both electromotive forces produced by a mechanical rotor and voltages synthesized by semiconductor switches through the same method of observation: rotating together with the vector.

The choice of reference angle $\theta$ depends on the control approach. Grid-following control often uses a phase-locked loop (PLL) to estimate the grid-voltage phase, effectively locking the observation frame to the grid-voltage vector to regulate grid current. Grid-forming control with $dq$ inner loops instead generates the angle by integrating an internal controller frequency state, effectively constructing “virtual rotor” coordinates within the algorithm. Angles from either source can be used in the same Park transformation.

### Where the “Angular-Velocity Terms” in a Stationary Circuit Come From

Let $\boldsymbol u_{abc}$ and $\boldsymbol v_{abc}$ be the equivalent phase voltages at the converter bridge terminals and the point of grid connection, respectively, with zero sequence removed, and let $\boldsymbol i_{abc}$ be the grid current. The three-phase filter circuit satisfies

$$
\boldsymbol u_{abc}-\boldsymbol v_{abc}
=R\boldsymbol i_{abc}
+L\frac{\mathrm d\boldsymbol i_{abc}}{\mathrm dt}.
\tag{A4-2}
$$

Denote the transformation matrix in Equation (A4-1) by $\boldsymbol T(\theta)$, so that $\boldsymbol i_{dq}=\boldsymbol T\boldsymbol i_{abc}$. Differentiating this product and then differentiating the sine and cosine entries of the matrix term by term gives

$$
\begin{aligned}
\dot{\boldsymbol i}_{dq}
&=\dot{\boldsymbol T}\boldsymbol i_{abc}
+\boldsymbol T\dot{\boldsymbol i}_{abc},\\
\dot{\boldsymbol T}
&=\omega
\begin{bmatrix}0&1\\-1&0\end{bmatrix}
\boldsymbol T,\qquad \omega=\dot\theta.
\end{aligned}
\tag{A4-2a}
$$

Substituting the second line into the first and moving the coordinate-rotation term to the right gives

$$
\boldsymbol T\dot{\boldsymbol i}_{abc}
=\dot{\boldsymbol i}_{dq}
-\omega\begin{bmatrix}i_q\\-i_d\end{bmatrix}
=\begin{bmatrix}
\dot i_d-\omega i_q\\
\dot i_q+\omega i_d
\end{bmatrix}.
\tag{A4-2b}
$$

Now premultiply both sides of Equation (A4-2) by $\boldsymbol T$. The voltages and currents become their $dq$ components. Because $R,L$ are identical constants in all three phases, the resistive term becomes $R\boldsymbol i_{dq}$, while the inductive term is replaced using Equation (A4-2b). Expanding row by row yields

$$
\boxed{
\begin{aligned}
u_d-v_d&=Ri_d+L\dot i_d-\omega Li_q,\\
u_q-v_q&=Ri_q+L\dot i_q+\omega Li_d.
\end{aligned}}
\tag{A4-3}
$$

The $\omega Li$ terms arise from the time derivative of the coordinate transformation. To examine power, multiply the two axis equations by $3i_d/2$ and $3i_q/2$, respectively, and add them. The cross-coupling terms cancel exactly:

$$
\frac32\left[i_d(-\omega Li_q)+i_q(\omega Li_d)\right]=0.
\tag{A4-4}
$$

Thus, in this averaged model, the active-power difference between the bridge terminals and the point of grid connection comprises only resistive losses and changes in the energy stored in the inductors. There is no mechanical-power term, even though coordinate angular-velocity terms appear in the equations.

### Why This Simplifies Grid-Connected Control

Aligning the $d$ axis with the positive-sequence grid voltage gives $v_d=V>0$ and $v_q=0$. Under the coordinate and current-direction conventions used here, the three-phase active and reactive powers are

$$
\boxed{
P=\frac32Vi_d,\qquad
Q=-\frac32Vi_q.}
\tag{A4-5}
$$

The active-power command can therefore be converted into a $d$-axis current command, and the reactive-power command into a $q$-axis current command. This is the direct reason many grid-following converters use synchronous-frame current control. The minus sign is tied to the selected $q$-axis direction and must not be mixed with other sign conventions.

Let $w_d,w_q$ be the outputs of the two axis PI controllers acting on the current errors $i_k^\star-i_k$ ($k=d,q$). Adding grid-voltage feedforward and cross-coupling compensation gives

$$
\begin{aligned}
u_d^\star&=v_d-\omega Li_q+w_d,\\
u_q^\star&=v_q+\omega Li_d+w_q.
\end{aligned}
\tag{A4-6}
$$

Under the ideal assumptions of accurate parameters, an output voltage that follows its command, and negligible delay, substituting these expressions into Equation (A4-3) reduces the two axes to $L\dot i_d+Ri_d=w_d$ and $L\dot i_q+Ri_q=w_q$. The original task of tracking three-phase sinusoids becomes two regulation problems whose steady-state references are constants. When the loops are stable and unsaturated, the integral action of the PI controllers can achieve zero steady-state error for constant commands.

### How the Calculated Commands Become IGBT Switching Actions

After calculating the $dq$ voltage commands, the controller can use the inverse Park transformation to recover the three-phase voltage references directly. With the zero-sequence voltage reference set to $u_0^\star=0$, the inverse transformation corresponding to Equation (A4-1) is

$$
\begin{bmatrix}u_a^\star\\u_b^\star\\u_c^\star\end{bmatrix}
=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\cos(\theta-\frac{2\pi}{3})&-\sin(\theta-\frac{2\pi}{3})\\
\cos(\theta+\frac{2\pi}{3})&-\sin(\theta+\frac{2\pi}{3})
\end{bmatrix}
\begin{bmatrix}u_d^\star\\u_q^\star\end{bmatrix}.
\tag{A4-7}
$$

On the measurement side, the forward transformation sends the three-phase quantities into the $dq$ controller. On the actuation side, the inverse transformation converts the $dq$ commands back into three-phase references, and PWM then calculates the phase-leg duty ratios. In practice, the inverse transformation can also be split into an inverse rotation from $dq\rightarrow\alpha\beta$ and an inverse Clarke transformation from $\alpha\beta\rightarrow abc$; together, these two steps give Equation (A4-7). With SVPWM, the modulator can also use the $\alpha\beta$ voltage commands directly.

When the DC-bus voltage and modulation range permit, the semiconductor devices switch on and off in sequence so that the average output voltage follows the desired three-phase AC trajectory. What changes is the time waveform of each phase voltage; the devices themselves need not rotate.

The Park transformation selects coordinates that are convenient for control. Semiconductor devices and circuit topologies continue to evolve, but the phase relationships among three-phase AC quantities remain. This is the fundamental reason the Park transformation continues to be effective in grid-connection control for renewable-energy resources.

---

<a id="references"></a>

## References and Index of Original Sources

1. **Official National Academy of Engineering memorial tribute.** Charles Concordia, “Robert H. Park,” in *Memorial Tributes: Volume 8* (1996), pp. 174–177. <https://www.nationalacademies.org/read/5427/chapter/34> . Scans of the original volume: [page 175](https://nap.nationalacademies.org/books/5427/gif/175.gif), [page 176](https://nap.nationalacademies.org/books/5427/gif/176.gif), [page 177](https://nap.nationalacademies.org/books/5427/gif/177.gif).
2. **IEEE engineering-history biography.** “Robert H. Park,” Engineering and Technology History Wiki (ETHW). <https://ethw.org/Robert_H._Park> . Includes a career chronology covering MIT, his studies in Sweden, GE, the chemical industry, the Navy, Emhart, and Fast Load Control.
3. **University of Chicago Library historical materials.** “Robert E. Park (1864–1944): Sociology.” <https://www.lib.uchicago.edu/collex/exhibits/university-chicago-centennial-catalogues/university-chicago-faculty-centennial-view/robert-e-park-1864-1944-sociology/> .
4. **University of Chicago family-archive finding aid.** *Park Family Collection, 1894–1951*, biographical note and correspondence inventory. <https://www.lib.uchicago.edu/e/scrc/findingaids/view.php?eadid=ICU.SPCL.PARKFAMILY> . Identifies family members, nicknames, and archived letters.
5. **Family recollections.** Donald Breed Jr. and Sylvia Breed Vaterlaus, “Portrait Painter Theodosia Breed,” submitted 2009, Illinois Women Artists. <https://illinoiswomenartists.org/theodosia-breed/> . Includes recollections of the 1917 journey as recounted by descendants of the brother and sister.
6. **Original paper.** R. H. Park, “Two-Reaction Theory of Synchronous Machines: Generalized Method of Analysis—Part I,” *Transactions of the AIEE*, 48(3), 716–727, July 1929. <https://doi.org/10.1109/T-AIEE.1929.5055275> .
7. **Original paper.** R. H. Park and B. L. Robertson, “The Reactances of Synchronous Machines,” *Transactions of the AIEE*, 47(2), 514–535, 1928. <https://doi.org/10.1109/T-AIEE.1928.5055010> .
8. **Original paper.** R. H. Park, “Two-Reaction Theory of Synchronous Machines—II,” *Transactions of the AIEE*, 52(2), 352–354, June 1933. <https://doi.org/10.1109/T-AIEE.1933.5056309> .
9. **Family-history material.** David L. Parke, “Robert Hiram Park—Inventor,” *Newsletter of the Parke Society*, Vol. XXIII, No. 3, 1986, pp. 33, 45. Scan of the issue: <https://parkesociety.org/wp-content/uploads/2022/04/Vol.-23-No.-3.pdf> .
10. **Original patent.** W. R. Maltby and R. H. Park, *Magnetic Detector*, US 2,436,394, filed June 6, 1941; patented February 24, 1948. <https://patents.google.com/patent/US2436394A/en> .
11. **Official U.S. Navy operational history.** Naval History and Heritage Command, “Operation Starvation: The Aerial Mine Campaign Against Japan, March–August 1945,” in *H-Gram 053*. <https://www.history.navy.mil/content/history/nhhc/about-us/leadership/director/directors-corner/h-grams/h-gram-053/h-053-1.html> . Provides statistics on mines laid and shipping losses during the campaign.
12. **Original patents.** R. H. Park, *Method for Blow Molding Hollow Articles*, US 3,008,191, filed July 14, 1954, patented Nov. 14, 1961; and *Apparatus for Blow Molding Hollow Articles*, US 3,089,186, patented May 14, 1963. <https://patents.google.com/patent/US3008191A/en> ; <https://patents.google.com/patent/US3089186A/en> .
13. **Original patent.** R. H. Park, *Method of Charge Control for Vehicle Hybrid Drive Batteries*, US 4,313,080, filed May 22, 1978, patented Jan. 26, 1982. <https://patents.google.com/patent/US4313080A/en> .
14. **Original patents.** R. H. Park, *Method of Improving the Stability of Interconnected Power Systems*, US 3,515,893, filed Feb. 7, 1966, patented June 2, 1970; *Method of Effecting Fast Turbine Valving for Improvement of Power System Stability*, US 3,848,138, patented 1974. <https://patents.google.com/patent/US3515893A/en> ; the subsequent reissue, <https://patents.google.com/patent/USRE27842E/en> , explicitly discusses an alternative implementation using digital signals and storage devices; <https://patents.google.com/patent/US3848138A/en> .
15. **Conference and journal papers.** R. H. Park, “Improved Reliability of Bulk Power Supply by Fast Load Control,” *Proceedings of the American Power Conference*, vol. 30 (1968), pp. 1128–1141; “Fast Turbine Valving,” *IEEE Transactions on Power Apparatus and Systems*, PAS-92 (1973), pp. 1065–1073. Bibliographic information used to check Park’s scholarly publications after his return to the power industry.
16. **Contemporary paper and discussion.** B. M. Pasternack and N. B. Bhatt, “The Rockport Plant—Analysis of Temporary Fast Turbine Valving Tests,” *IEEE Transactions on Power Systems*, 3(2), 1988, pp. 529–540, including a discussion signed by R. H. Park. Paper retrieval link: <https://home.engineering.iastate.edu/~jdm/ee554/FastValvingRockport1988paper1.pdf> .
17. **Historical list of IEEE Lamme Medal recipients.** Engineering and Technology History Wiki, “IEEE Lamme Medal,” listing Robert H. Park and Yu H. Ku for 1972. <https://ethw.org/IEEE_Lamme_Medal> .
18. **Bibliographic lead for a contemporary obituary.** “In Memory of. Robert H. Park. Inventor, Engineer,” *IEEE Power Engineering Review*, 14(5), May 1994, p. 26. [DOI: 10.1109/MPER.1994.279095](https://doi.org/10.1109/MPER.1994.279095).
19. **MIT historical project.** “Ku Yu Hsiu—Polymath,” *Early Chinese Students at MIT*. <https://earlychinesemit.mit.edu/student-profiles/ku-yu-hsiu-polymath/> . Used to check Ku’s degrees and the title of his 1928 doctoral dissertation.
20. **IEEE engineering-history biography.** “Yu Hsiu Ku,” ETHW. <https://ethw.org/Yu_Hsiu_Ku> . Used to check Ku’s employment at GE, his academic career after 1950, and his 1972 award.
21. **Chinese-language historical study.** Yang Huizhong, Fang Guanghui, and Ji Zhicheng, “Mr. Ku Yu Hsiu’s Innovations in Science and Technology,” *Journal of Jiangnan University (Humanities & Social Sciences)*, vol. 2, no. 1, 2003, reprinted by the Ku Yu Hsiu Memorial Hall: <https://guyx.org/index.php?a=memory&id=226&m=article> . The article provides a historical overview of “Ku variables.”
22. **Original paper.** Y. H. Ku, “Transient Analysis of A-C. Machinery,” *Transactions of the AIEE*, 48(3), 707–714, 1929. <https://doi.org/10.1109/T-AIEE.1929.5055273> .
23. **Original paper.** Y. H. Ku, “Transient Analysis of Rotating Machines and Stationary Networks by Means of Rotating Reference Frames,” *Transactions of the AIEE*, 70(1), 943–957, 1951. <https://doi.org/10.1109/T-AIEE.1951.5060505> . The original abstract explicitly discusses the relationship between forward and backward components and direct- and quadrature-axis components.

24. **Modern original research: the complex–real relationship between Ku and Park quantities.** M. Bakkar, S. Bogarra, A. Rolán, F. Córcoles, J. Saura, “Voltage sag influence on controlled three-phase grid-connected inverters according to the Spanish grid code,” *IET Generation, Transmission & Distribution*, 14(10), 1882–1892, 2020. [DOI: 10.1049/iet-gtd.2019.1496](https://doi.org/10.1049/iet-gtd.2019.1496). Section 3.1 explicitly describes the Ku transformation as the complex form of the Park transformation and explains that the forward and backward components of real instantaneous quantities are complex conjugates.
25. **Modern original research: explicit matrices and normalization.** A. Rolán, S. Bogarra, M. Bakkar, “Integration of Distributed Energy Resources to Unbalanced Grids Under Voltage Sags With Grid Code Compliance,” *IEEE Transactions on Smart Grid*, 13(1), 355–366, January 2022. [DOI: 10.1109/TSG.2021.3107984](https://doi.org/10.1109/TSG.2021.3107984). Equation (21) in Appendix B gives the power-invariant Ku matrix, and Equation (26) gives its relationship to Park quantities. [University repository record](https://upcommons.upc.edu/handle/2117/361578).
26. **Original municipal record.** City of Quincy, *Inaugural Address of the Mayor, with the Annual Report of the Officers of the City of Quincy for the Year 1923*, p. 154, “Marriages Recorded in Quincy in 1923.” The entry for January 13 records Robert Hiram Park and Miriam Elizabeth Helenius. [Digitized collection](https://archive.org/details/inauguraladdress1923quin).
27. **Original patent: a kitchen-appliance invention.** R. H. Park, *Electric Cooking Device*, US 2,233,485, filed September 29, 1938; patented March 4, 1941. [Full patent](https://patents.google.com/patent/US2233485A/en). Used to illustrate the vessel-heating arrangement, clamping and energization interlock, and thermal-protection design.
28. **Original paper: system stability and the equal-area method.** R. H. Park and E. H. Bancker, “System Stability as a Design Problem,” *Transactions of the American Institute of Electrical Engineers*, 48(1), January 1929, pp. 170–193. [DOI: 10.1109/T-AIEE.1929.5055195](https://doi.org/10.1109/T-AIEE.1929.5055195).
