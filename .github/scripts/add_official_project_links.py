from pathlib import Path

ZRTDB = "https://github.com/zoudehupowersystem/ZRTDB"
POWERTOOL = "https://github.com/zoudehupowersystem/power_tool"


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f"Required anchor not found: {label}")
    return text.replace(old, new, 1)


# Chinese homepage
p = Path("index.html")
zh = p.read_text(encoding="utf-8")

zh = zh.replace(
    '<title>邹德虎（Dehu Zou）｜电力系统仿真、调度自动化与工业软件研发</title>',
    '<title>邹德虎（Dehu Zou）｜电力系统仿真、调度自动化、ZRTDB 与 PowerTool</title>'
)
zh = zh.replace(
    '<meta name="description" content="邹德虎（Dehu Zou），高级工程师、电力系统研发架构师。长期从事电力系统建模仿真、实时电磁暂态仿真（EMT）、电网调度自动化与工业软件研发，ADS-RTSim 实时仿真平台负责人，OPSEN 开源项目发起人。" />',
    '<meta name="description" content="邹德虎（Dehu Zou），高级工程师、电力系统研发架构师。长期从事电力系统建模仿真、实时电磁暂态仿真（EMT）、电网调度自动化与工业软件研发；公开维护 ZRTDB 零拷贝实时数据总线与 PowerTool 电力系统工程计算工具。" />'
)
zh = zh.replace(
    '<meta property="og:title" content="邹德虎（Dehu Zou）｜电力系统仿真、调度自动化与工业软件研发" />',
    '<meta property="og:title" content="邹德虎（Dehu Zou）｜电力系统研发 · ZRTDB · PowerTool" />'
)
zh = zh.replace(
    '<meta property="og:description" content="邹德虎（Dehu Zou），高级工程师、电力系统研发架构师。长期从事电力系统建模仿真、实时电磁暂态仿真（EMT）、电网调度自动化与工业软件研发。" />',
    '<meta property="og:description" content="电力系统建模仿真、实时 EMT、调度自动化与工业软件研发；ZRTDB 与 PowerTool 官方主页入口。" />'
)
zh = zh.replace(
    '<meta name="twitter:title" content="邹德虎（Dehu Zou）｜电力系统仿真、调度自动化与工业软件研发" />',
    '<meta name="twitter:title" content="邹德虎（Dehu Zou）｜ZRTDB · PowerTool · Power Systems" />'
)
zh = zh.replace(
    '<meta name="twitter:description" content="电力系统建模仿真、实时 EMT、调度自动化与工业软件研发。" />',
    '<meta name="twitter:description" content="电力系统建模仿真、实时 EMT、调度自动化与工业软件研发；ZRTDB 与 PowerTool 官方 GitHub 项目。" />'
)
zh = zh.replace('"dateModified": "2026-09-15T09:55:00+08:00"', '"dateModified": "2026-09-17T17:00:00+08:00"')

old_actions = '''            <div class="quick-actions">
              <a class="btn primary" href="blog.html"><strong>文章</strong><span class="mono">Blog</span></a>
              <a class="btn" href="#experience"><strong>履历</strong><span class="mono">Experience</span></a>
              <a class="btn" href="#papers"><strong>代表成果</strong><span class="mono">Work</span></a>
              <a class="btn" href="#contact"><strong>联系</strong><span class="mono">Contact</span></a>
            </div>'''
new_actions = f'''            <div class="quick-actions">
              <a class="btn primary" href="blog.html"><strong>文章</strong><span class="mono">Blog</span></a>
              <a class="btn" href="{ZRTDB}" target="_blank" rel="noopener noreferrer"><strong>ZRTDB</strong><span class="mono">GitHub ↗</span></a>
              <a class="btn" href="{POWERTOOL}" target="_blank" rel="noopener noreferrer"><strong>PowerTool</strong><span class="mono">GitHub ↗</span></a>
              <a class="btn" href="#experience"><strong>履历</strong><span class="mono">Experience</span></a>
              <a class="btn" href="#papers"><strong>代表成果</strong><span class="mono">Work</span></a>
              <a class="btn" href="#contact"><strong>联系</strong><span class="mono">Contact</span></a>
            </div>'''
if f'href="{ZRTDB}"' not in zh:
    zh = replace_once(zh, old_actions, new_actions, "Chinese hero actions")

zh_projects = f'''        <!-- OPEN SOURCE PROJECTS -->
        <div class="section" id="opensource">
          <h2>已发布开源项目</h2>
          <div class="section-note">以下 GitHub 仓库为项目官方发布源，可直接查看源码、README、版本历史与更新记录。</div>
          <div class="two-col">
            <div class="card">
              <h3 style="margin:0 0 8px;color:rgba(255,255,255,.94);font-size:18px;">ZRTDB <span class="mono" style="font-size:12px;color:var(--faint);">Zero-copy Real-Time Data Bus</span></h3>
              <p style="margin:0 0 12px;">面向实时控制、SCADA 与工业边缘计算的零拷贝实时数据总线。采用共享内存、静态建模与固定偏移访问，强调确定性时延和工程可运维性。</p>
              <a class="btn primary" href="{ZRTDB}" target="_blank" rel="noopener noreferrer"><strong>访问 ZRTDB 官方 GitHub</strong><span class="mono">zoudehupowersystem/ZRTDB ↗</span></a>
            </div>
            <div class="card">
              <h3 style="margin:0 0 8px;color:rgba(255,255,255,.94);font-size:18px;">PowerTool <span class="mono" style="font-size:12px;color:var(--faint);">power_tool</span></h3>
              <p style="margin:0 0 12px;">面向电力系统工程近似计算、参数换算、波形分析、稳定性分析与快速校核的轻量桌面工具，提供中英文 GUI。</p>
              <a class="btn primary" href="{POWERTOOL}" target="_blank" rel="noopener noreferrer"><strong>访问 PowerTool 官方 GitHub</strong><span class="mono">zoudehupowersystem/power_tool ↗</span></a>
            </div>
          </div>
        </div>

'''
if 'id="opensource"' not in zh:
    zh = replace_once(
        zh,
        '      <div class="main">\n        <!-- ARTICLES -->',
        '      <div class="main">\n' + zh_projects + '        <!-- ARTICLES -->',
        "Chinese main/projects insertion",
    )

old_service = '<li>OPSEN 开源项目发起人与维护者（GitHub：zoudehupowersystem，2025–至今），围绕电力系统建模、仿真、分析与应用构建开源工具生态。</li>'
new_service = f'''<li>公开发布并维护 <a href="{ZRTDB}" target="_blank" rel="noopener noreferrer"><strong>ZRTDB</strong></a>（零拷贝实时数据总线）与 <a href="{POWERTOOL}" target="_blank" rel="noopener noreferrer"><strong>PowerTool</strong></a>（电力系统工程计算工具），GitHub 账号 zoudehupowersystem 为官方发布源。</li>
              <li>OPSEN 开源项目发起人与维护者（GitHub：zoudehupowersystem，2025–至今），围绕电力系统建模、仿真、分析与应用构建开源工具生态。</li>'''
if '公开发布并维护 <a href="https://github.com/zoudehupowersystem/ZRTDB"' not in zh:
    zh = replace_once(zh, old_service, new_service, "Chinese open-source service")

p.write_text(zh, encoding="utf-8")


# English homepage
p = Path("en.html")
en = p.read_text(encoding="utf-8")

en = en.replace(
    '<title>Dehu Zou | Power-System Simulation, Grid Automation and Industrial Software R&D</title>',
    '<title>Dehu Zou | Power-System R&D, ZRTDB & PowerTool</title>'
)
en = en.replace(
    '<meta name="description" content="Dehu Zou is a senior engineer and power-system R&D architect working on power-system modelling and simulation, real-time electromagnetic-transient simulation, grid dispatch automation, high-performance C++, and industrial software engineering." />',
    '<meta name="description" content="Dehu Zou is a senior engineer and power-system R&D architect working on power-system modelling, real-time EMT simulation, grid dispatch automation, and industrial software. Official open-source projects include ZRTDB and PowerTool." />'
)
en = en.replace(
    '<meta property="og:title" content="Dehu Zou | Power-System Simulation, Grid Automation and Industrial Software R&D" />',
    '<meta property="og:title" content="Dehu Zou | Power-System R&D · ZRTDB · PowerTool" />'
)
en = en.replace(
    '<meta property="og:description" content="Senior engineer and power-system R&D architect focused on real-time EMT simulation, grid automation, numerical computing, software architecture, and industrial product development." />',
    '<meta property="og:description" content="Power-system R&D, real-time EMT simulation, grid automation, and industrial software; official links to ZRTDB and PowerTool." />'
)
en = en.replace(
    '<meta name="twitter:title" content="Dehu Zou | Power Systems · Real-Time EMT · Industrial Software" />',
    '<meta name="twitter:title" content="Dehu Zou | ZRTDB · PowerTool · Power Systems" />'
)
en = en.replace(
    '<meta name="twitter:description" content="Power-system modelling and simulation, real-time EMT, grid dispatch automation, high-performance C++, and industrial software R&D." />',
    '<meta name="twitter:description" content="Power-system modelling, real-time EMT, grid automation and industrial software; official GitHub projects ZRTDB and PowerTool." />'
)
en = en.replace('"dateModified": "2026-09-15T09:55:00+08:00"', '"dateModified": "2026-09-17T17:00:00+08:00"')

old_en_actions = '<div class="actions"><a class="btn primary" href="english.html">English Articles</a><a class="btn" href="#experience">Experience</a><a class="btn" href="#papers">Publications</a><a class="btn" href="#contact">Contact</a><a class="btn" href="/" hreflang="zh-CN" lang="zh-CN">中文</a></div>'
new_en_actions = f'<div class="actions"><a class="btn primary" href="english.html">English Articles</a><a class="btn" href="{ZRTDB}" target="_blank" rel="noopener noreferrer">ZRTDB · GitHub ↗</a><a class="btn" href="{POWERTOOL}" target="_blank" rel="noopener noreferrer">PowerTool · GitHub ↗</a><a class="btn" href="#experience">Experience</a><a class="btn" href="#papers">Publications</a><a class="btn" href="#contact">Contact</a><a class="btn" href="/" hreflang="zh-CN" lang="zh-CN">中文</a></div>'
if f'href="{ZRTDB}"' not in en:
    en = replace_once(en, old_en_actions, new_en_actions, "English hero actions")

en_projects = f'''        <section class="section" id="opensource"><h2>Published Open-Source Projects</h2><div class="section-note">These GitHub repositories are the official project sources for source code, README documentation, release history, and updates.</div><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px"><div class="card"><h3 style="margin:0 0 8px;color:rgba(255,255,255,.94);font-size:18px">ZRTDB <span class="mono" style="font-size:12px;color:var(--faint)">Zero-copy Real-Time Data Bus</span></h3><p style="margin:0 0 12px;line-height:1.75;color:rgba(255,255,255,.78)">A zero-copy real-time data bus for real-time control, SCADA, and industrial edge computing, built around shared memory, static modelling, deterministic fixed-offset access, and operational inspectability.</p><a class="btn primary" href="{ZRTDB}" target="_blank" rel="noopener noreferrer">Official ZRTDB GitHub · zoudehupowersystem/ZRTDB ↗</a></div><div class="card"><h3 style="margin:0 0 8px;color:rgba(255,255,255,.94);font-size:18px">PowerTool <span class="mono" style="font-size:12px;color:var(--faint)">power_tool</span></h3><p style="margin:0 0 12px;line-height:1.75;color:rgba(255,255,255,.78)">A lightweight desktop tool for power-system engineering approximations, parameter conversion, waveform analysis, stability-oriented checks, and rapid engineering validation, with Chinese and English GUIs.</p><a class="btn primary" href="{POWERTOOL}" target="_blank" rel="noopener noreferrer">Official PowerTool GitHub · zoudehupowersystem/power_tool ↗</a></div></div></section>
'''
if 'id="opensource"' not in en:
    en = replace_once(
        en,
        '      <main class="main">\n        <section class="section" id="articles">',
        '      <main class="main">\n' + en_projects + '        <section class="section" id="articles">',
        "English main/projects insertion",
    )

old_en_service = '<li>Founder and maintainer of the OPSEN open-source project (GitHub: zoudehupowersystem, 2025–present), building an open-source ecosystem for power-system modelling, simulation, analysis, and applications.</li>'
new_en_service = f'<li>Creator and maintainer of <a href="{ZRTDB}" target="_blank" rel="noopener noreferrer"><strong>ZRTDB</strong></a> (zero-copy real-time data bus) and <a href="{POWERTOOL}" target="_blank" rel="noopener noreferrer"><strong>PowerTool</strong></a> (power-system engineering calculation tool); the zoudehupowersystem GitHub account is the official publication source.</li>' + old_en_service
if 'Creator and maintainer of <a href="https://github.com/zoudehupowersystem/ZRTDB"' not in en:
    en = replace_once(en, old_en_service, new_en_service, "English open-source service")

p.write_text(en, encoding="utf-8")
