from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = '/* SCHENGEN REDESIGN 2026-09-01 */'
if marker in s:
    raise SystemExit(0)

css = r'''
/* SCHENGEN REDESIGN 2026-09-01 */
:root{--ink:#1C1C1C;--ink-soft:#8C877E;--paper:#F9F5EB;--line:#F0EBDD;--red:#8C4A3B;--red-bg:#FFF0E3;--green:#2E6B3A;--green-bg:#EAF5EC;--a:#2D4A6B;--a-bg:#EEF3F8;--b:#8C4A3B;--b-bg:#FFF0E3;--both:#3BA44B;--gap:#C96B5A;--radius:18px;--radius-lg:24px;--serif:Georgia,'Times New Roman',serif;--mono:'SFMono-Regular',Consolas,'Liberation Mono',monospace;--sans:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;--shadow:0 1px 2px rgba(0,0,0,.04),0 12px 32px rgba(0,0,0,.05);--shadow-lg:0 1px 2px rgba(0,0,0,.04),0 16px 40px rgba(0,0,0,.05)}
body{background:#F9F5EB;color:#1C1C1C;font-family:var(--sans)}
.wrap{max-width:1200px;padding:40px 32px 64px}
.masthead{border-bottom:0;padding-bottom:28px;margin-bottom:0;align-items:flex-start}
.masthead h1{font-size:56px;line-height:.95;letter-spacing:-.035em;font-weight:500;color:#1C1C1C}
.masthead h1 small{font-family:var(--sans);font-size:14px;letter-spacing:.02em;color:#8C877E;margin-top:12px;font-weight:400}
.masthead .sub{display:none}.controls-top{gap:12px;align-items:center}
.today-box{border:1px solid #EEE9DC;border-radius:999px;padding:7px 14px;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.04),0 8px 24px rgba(0,0,0,.04);font-family:var(--sans);color:#6B6760}
.today-box input{font-family:var(--sans);font-size:13px;font-weight:500;color:#1C1C1C}
.badge-v2{background:#F2EFE7;color:#8A857A;border:1px solid #EDE8DC;border-radius:999px;font-size:10px;padding:6px 10px;font-family:var(--sans);font-weight:500}
.backup-bar{background:transparent;margin:0 0 24px;gap:8px}.backup-bar .plan-btn{padding:9px 14px;font-size:12px}.backup-status{font-family:var(--sans);font-size:11px;color:#9A958B}
.cloud-pill{font-family:var(--sans);border-radius:999px;background:#fff;border:1px solid #EDE8DC;padding:6px 10px;font-size:10px;box-shadow:0 1px 2px rgba(0,0,0,.03)}.cloud-pill.ok{color:#2E6B3A;border-color:#D6EAD9;background:#EAF5EC}
.people{gap:24px;margin-bottom:32px}.person-card{background:#fff;border:1px solid #F0EBDD;border-radius:22px;padding:28px;box-shadow:0 1px 2px rgba(0,0,0,.04),0 12px 32px rgba(0,0,0,.05);overflow:visible}.person-card::before{display:none}
.name-row{margin:0 0 24px;gap:12px;position:relative}.name-row::before{width:36px;height:36px;border-radius:999px;display:grid;place-items:center;color:#fff;font-family:var(--serif);font-size:16px;flex:0 0 auto}.person-card.a .name-row::before{content:'Л';background:#2D4A6B}.person-card.b .name-row::before{content:'С';background:#8C4A3B}
.name-row input{font-family:var(--serif);font-size:20px;font-weight:500;color:#1C1C1C;border:0;padding:0;width:auto;min-width:90px}.badge{margin-left:auto;border-radius:999px;font-family:var(--sans);font-size:10px;letter-spacing:.12em;padding:6px 9px;font-weight:600}.a .badge{background:#2D4A6B;color:#fff}.b .badge{background:#8C4A3B;color:#fff}
.trips{max-height:310px;margin-bottom:18px;padding-right:2px}.trip-row{gap:7px;margin-bottom:9px}.trip-row input{font-family:var(--sans);font-size:13px;border:1px solid #EDE8DC;border-radius:999px;padding:9px 13px;background:#FDFCF8;min-height:40px;color:#1C1C1C}.trip-row input:focus{outline:none;border-color:#2D4A6B;background:#fff}.b .trip-row input:focus{border-color:#8C4A3B}.trip-row input.empty{border-style:solid;color:#9A958B;background:#FBF8F1}.trip-row .rm{width:30px;height:30px;border:1px solid #EDE8DC;border-radius:999px;background:#fff;color:#8C877E;font-size:15px;padding:0;align-self:center}.trip-row .hint{font-family:var(--sans);font-size:11px;color:#9A958B;padding-left:5px;margin-top:-2px}
.add-trip{border:1px dashed #E2DDD0;border-radius:999px;background:#fff;color:#8C877E;padding:11px 14px;font-family:var(--sans);font-size:13px;text-transform:none;font-weight:500}.add-trip:hover{background:#FDFCF8;border-color:#CFC8B6}
.stats{margin-top:22px;padding-top:20px;border-top:1px solid #F1EDE3;gap:16px}.stat .label{font-family:var(--sans);font-size:10px;color:#9A958B;letter-spacing:.09em}.stat .value{font-family:var(--serif);font-size:22px;font-weight:500;color:#1C1C1C}.stat .value.ok{color:#2E6B3A}.stat .value.warn{color:#8C4A3B}.stat .hint{font-family:var(--sans);font-size:11px;color:#8C877E}
.section-title{font-family:var(--serif);font-size:26px;font-weight:500;letter-spacing:-.02em;border:0;margin:32px 0 14px;padding:0}.section-title .icon{display:none}.panel{background:#fff;border:1px solid #F0EBDD;border-radius:24px;padding:32px;margin-bottom:20px;box-shadow:0 1px 2px rgba(0,0,0,.04),0 16px 40px rgba(0,0,0,.05)}
.ai-header{gap:14px;align-items:flex-end;margin-bottom:18px}.field label{font-family:var(--sans);font-size:10px;color:#8C877E;letter-spacing:.09em;margin-bottom:6px}.field select,.field input{font-family:var(--sans);font-size:13px;border:1px solid #F1EDE3;border-radius:999px;padding:9px 13px;background:#FBF8F1;color:#1C1C1C}
.plan-btn{font-family:var(--sans);font-size:13px;font-weight:600;background:#1C1C1C;color:#fff;border-radius:999px;padding:10px 16px;box-shadow:none}.plan-btn:hover{transform:none;background:#000;box-shadow:none}.plan-btn.secondary{background:#fff;color:#1C1C1C;border:1px solid #EDE8DC}.plan-btn.secondary:hover{background:#FDFCF8}
.timeline-wrap{background:#FBF8F1;border:1px solid #F1EDE3;border-radius:18px;padding:20px;margin:20px 0}.timeline-row{background:#fff;border:1px solid #F1EDE3;border-radius:10px}.timeline-row .row-label{font-family:var(--sans);font-size:10px;background:rgba(255,255,255,.92)}.timeline-legend,.timeline-axis{font-family:var(--sans);color:#8C877E}.human-result{background:#FDFCF8;border:1px solid #EDE8DC;border-radius:18px;padding:18px;font-family:var(--sans);font-size:13px;color:#444}
.warn-box,.ok-box,.info-box{border-radius:16px;font-family:var(--sans)}.ok-box{background:#EAF5EC;border-color:#D6EAD9;color:#2E6B3A}.warn-box{background:#FFF0E3;border-color:#F6DCC2}.info-box{background:#FDFCF8;border-color:#F0EBDD;color:#6B6760;padding:18px}
.pin-gate{background:rgba(28,28,28,.72);backdrop-filter:blur(8px)}.pin-card{background:#FDFCF8;border:1px solid #F0EBDD;border-radius:24px;padding:28px;box-shadow:0 12px 40px rgba(0,0,0,.12)}.pin-card h2{font-size:28px;font-weight:500}.pin-card input{border-radius:999px;border-color:#EDE8DC;padding:12px 15px}
@media(max-width:800px){.wrap{padding:28px 16px 56px}.masthead{padding-bottom:22px}.masthead h1{font-size:42px}.controls-top{width:100%;justify-content:flex-start}.today-box{padding:6px 12px}.person-card{padding:22px 18px;border-radius:20px}.panel{padding:22px 18px;border-radius:20px}.section-title{font-size:22px;margin-top:28px}.backup-status{width:100%}.trip-row{grid-template-columns:minmax(0,1fr) minmax(0,1fr) auto}}
'''

s = s.replace('</style>', css + '\n</style>', 1)
p.write_text(s, encoding='utf-8')

sw = Path('sw.js')
w = sw.read_text(encoding='utf-8')
if 'schengen-pwa-v3' in w:
    w = w.replace('schengen-pwa-v3', 'schengen-pwa-v4', 1)
elif 'schengen-pwa-v4' not in w:
    raise SystemExit('Unexpected service worker cache version')
sw.write_text(w, encoding='utf-8')
