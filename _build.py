import os, json, datetime
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://hopalongbooks.github.io"
PUB = "Hop Along Books"
TODAY = "2026-10-08"

BOOKS = [
 dict(slug="trucks-trains-rockets", key="book1", topic="things-that-go", age="3-5", color="#1F75FE",
      title="Trucks, Trains, Rockets & Things That Go",
      short="Things That Go",
      sub="Color by Number for Kids Ages 3-5",
      amazon="https://www.amazon.com/dp/B0HMHYR6GY",
      isbn="", status="Available on Amazon",
      blurb="45 big, friendly vehicles: cars, fire trucks, diggers, school buses, trains, boats, planes and rockets, plus busy scenes like the airport and the construction site.",
      inside="cars, trucks, diggers, trains, rockets, boats, planes, buses, space and construction scenes",
      levels=["Car", "Steam Train", "Construction Site"], sample="Fire Truck", fact="a read-aloud vehicle fact"),
 dict(slug="cute-animals", key="book2", topic="animals", age="3-5", color="#1CAC78",
      title="Cute Animals Color by Number for Kids Ages 3-5",
      short="Cute Animals",
      sub="Pets, Farm, Zoo & Dinosaurs",
      amazon="https://www.amazon.com/dp/B0HMJBBSST",
      isbn="9798160782225", status="Available on Amazon",
      blurb="45 big, friendly animals: cats, dogs, ducks, lions, elephants, penguins, dolphins, dinosaurs and busy scenes like the farm, the jungle and under the sea.",
      inside="pets, farm animals, zoo animals, sea creatures, dinosaurs and big scenes",
      levels=["Cat", "Lion", "Farm"], sample="Elephant", fact="a read-aloud animal fact"),
 dict(slug="dinosaurs", key="book3", topic="dinosaurs", age="3-5", color="#6A4BB0",
      title="Dinosaurs Color by Number for Kids Ages 3-5",
      short="Dinosaurs",
      sub="A Day in the Life of Silly Dinos",
      amazon="https://www.amazon.com/dp/B0HMRJ8KRW",
      isbn="9798161871522", status="Available on Amazon",
      blurb="45 pictures starring 8 dino friends - T-Rex, Triceratops, Stegosaurus, Brachiosaurus, Ankylosaurus, Parasaurolophus, Pteranodon and Baby Dino - brushing their teeth, baking cakes, driving trucks and flying rockets.",
      inside="8 recurring dinosaur characters in everyday life, jobs, vehicles and big scenes",
      levels=["T-Rex Eats an Apple", "Brachiosaurus Pulls a Carrot", "A Dinosaur Birthday Party"], sample="T-Rex Brushes His Teeth", fact="a read-aloud dinosaur fact"),
]

TOPICS = [
 dict(slug="things-that-go", name="Things That Go", blurb="Trucks, trains, diggers, boats and rockets.", color="#C9DCEB", img="hero_truck.jpg", numbered="free_fire-truck.jpg"),
 dict(slug="animals", name="Animals", blurb="Pets, farm friends, zoo animals and sea creatures.", color="#D6E3CF", img="hero_cat.jpg", numbered="free_cat.jpg"),
 dict(slug="dinosaurs", name="Dinosaurs", blurb="Silly dinos brushing teeth, baking cakes and driving trucks.", color="#EED7D3", img="hero_trex.jpg", numbered="free_trex-apple.jpg"),
]
SOON = ["Ocean", "Space", "Holidays", "Bugs & Garden"]
# Grown-up line (bold & easy, no numbers, no key) - kept apart from BOOKS so the kids' level/key logic never touches it
GROWNUP = dict(slug="fireside-and-flurries", key="book4", short="Fireside & Flurries",
    title="Fireside & Flurries: Bold and Easy Christmas Coloring Book for Adults and Kids",
    sub="50 Cozy Fall, Winter and Holiday Designs", amazon="https://www.amazon.com/dp/B0HMWDQG8B", asin="B0HMWDQG8B",
    isbn="9798162146315", price="9.99", status="Available on Amazon", pages=108, size="8.5 x 8.5 in",
    blurb="Hot cocoa, crackling fireplaces, snowy cabins, gingerbread houses and Christmas morning: 50 cozy scenes drawn with thick, bold lines and big, simple spaces. No tiny details. Relaxing coloring you can finish in one sitting.")
AGES = [dict(slug="3-5", name="Ages 3-5", blurb="Big shapes, 3 to 8 colors, color names on every key.", live=True),
        dict(slug="5-7", name="Ages 5-7", blurb="Smaller spaces and more colors.", live=False)]
FREE = [dict(slug="trex-apple", name="T-Rex Eats an Apple", book="dinosaurs", level="Level 1, 3 colors"),
        dict(slug="cat", name="Cat", book="cute-animals", level="Level 1, 3 colors"),
        dict(slug="fire-truck", name="Fire Truck", book="trucks-trains-rockets", level="Level 2, 4 colors")]

CSS = r"""
:root{--paper:#FFF8EC;--ink:#2B2A4C;--mut:#6B6A85;--butter:#FFD166;--sky:#7FD3F0;--coral:#FF7B6B;--leaf:#5BC98A;--line:#EADFC8}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:Nunito,system-ui,sans-serif;color:var(--ink);background:var(--paper);line-height:1.6;font-size:17px}
a{color:var(--ink)}img{max-width:100%}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:72px}
.brand{font-family:Fredoka,sans-serif;font-weight:700;font-size:24px;color:var(--ink);text-decoration:none;display:flex;align-items:center;gap:10px}
.brand i{width:34px;height:34px;border-radius:50% 50% 50% 8px;background:var(--butter);display:inline-block}
nav a{margin-left:22px;text-decoration:none;color:var(--ink);font-weight:700;font-size:16px}
h1,h2,h3{font-family:Fredoka,sans-serif;font-weight:600;line-height:1.15;margin:0}
h1{font-size:clamp(34px,5.2vw,56px)}h2{font-size:clamp(26px,3.4vw,36px);margin:64px 0 18px}h3{font-size:20px;margin:0 0 6px}
.hero{position:relative;background:var(--sky);overflow:hidden}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:32px;align-items:center;padding-top:40px;padding-bottom:70px}
.hero p{font-size:19px;max-width:30em;margin:14px 0 24px}
.hero img{width:100%;border-radius:28px;background:#fff;padding:14px;transform:rotate(-2deg)}
.wave{display:block;width:100%;height:40px;margin-top:-1px}
.btn{display:inline-block;background:var(--coral);color:#fff;text-decoration:none;padding:14px 24px;border-radius:999px;font-weight:800;font-size:17px;border:0}
.btn.soft{background:#fff;color:var(--ink);border:2px solid var(--ink)}
.btn:focus-visible,a:focus-visible{outline:3px solid var(--coral);outline-offset:3px}
.shelf{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:26px;max-width:860px}
.book{display:block;text-decoration:none;color:var(--ink)}
.book img{width:100%;border-radius:14px;box-shadow:0 10px 0 var(--line);transition:transform .15s}
.book:hover img{transform:translateY(-4px)}
.book h3{margin-top:16px}.book p{margin:2px 0;color:var(--mut);font-size:15px}
.book .tag{display:inline-block;background:var(--butter);border-radius:999px;padding:2px 10px;font-size:13px;font-weight:800;margin-top:8px}
.promise{display:grid;grid-template-columns:1fr 1.2fr;gap:28px;align-items:center;margin:28px 0 44px}
.promise:nth-child(even){direction:rtl}.promise:nth-child(even)>*{direction:ltr}
.promise img{border-radius:22px;background:#fff;padding:12px;width:100%;max-height:360px;object-fit:contain}
.promise p{font-size:18px;max-width:28em;color:#3a3958}
.spec{width:100%;border-collapse:collapse;margin:16px 0;background:#fff;border-radius:16px;overflow:hidden}
.spec th,.spec td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}.spec th{width:32%;color:var(--mut);font-weight:700}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.three img{width:100%;border-radius:16px;background:#fff;padding:8px}.three figcaption{font-size:15px;color:var(--mut);margin-top:6px}figure{margin:0}
.guides{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}
.guide{background:#fff;border-radius:18px;padding:22px;text-decoration:none;color:var(--ink);border:2px solid transparent}
.guide:hover{border-color:var(--butter)}.guide p{color:var(--mut);font-size:15px;margin:6px 0 0}
.hero img.hero-art{width:100%;display:block;background:none;padding:0;transform:none;border-radius:0}
.topics{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:20px}
.topic{display:block;border-radius:24px;padding:18px 18px 22px;text-decoration:none;color:var(--ink);transition:transform .15s}
.topic:hover{transform:translateY(-3px)}
.topic img{width:100%;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:16px;padding:10px}
.topic h3{margin:14px 0 2px}.topic p{margin:0;font-size:15px;color:#3a3958}.topic .count{font-weight:800;font-size:14px;margin-top:8px;display:block}
.soon{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}.soon span{border:2px dashed var(--line);border-radius:999px;padding:6px 14px;color:var(--mut);font-weight:700;font-size:15px}
.ages{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}
.age{display:block;background:#fff;border-radius:20px;padding:20px 22px;text-decoration:none;color:var(--ink);border:3px solid var(--butter)}
.age.off{border-style:dashed;border-color:var(--line);color:var(--mut)}
.age b{font-family:Fredoka,sans-serif;font-size:26px;font-weight:600;display:block}
.freebie{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:stretch}
.fcard{display:flex;flex-direction:column;background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 8px 0 var(--line)}
.fcard .top{padding:18px 18px 0;border-top:8px solid var(--c)}
.fcard .pill{display:inline-block;background:var(--c);color:#fff;border-radius:999px;padding:3px 12px;font-size:13px;font-weight:800}
.fcard .art{display:block;width:100%;aspect-ratio:1/1;object-fit:contain;background:var(--paper);border-radius:18px;padding:14px;margin:14px 0 0}
.fcard h3{margin:16px 18px 2px}.fcard .from{margin:0 18px;color:var(--mut);font-size:15px}
.fcard .inside{margin:16px 18px 0;padding:14px;border:2px dashed var(--line);border-radius:16px}
.fcard .inside b{display:block;font-size:13px;letter-spacing:.04em;text-transform:uppercase;color:var(--mut);margin-bottom:10px}
.fcard .pair{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.fcard .pair img{width:100%;aspect-ratio:8.5/11;object-fit:cover;border:1px solid var(--line);border-radius:6px;background:#fff}
.fcard .pair span{display:block;font-size:13px;text-align:center;margin-top:4px;color:var(--mut)}
.fcard .go{margin:auto 18px 18px;padding-top:18px}.fcard .go .btn{display:block;text-align:center}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:26px 0 0;padding:0;list-style:none;counter-reset:s}
.steps li{background:#fff;border-radius:18px;padding:16px 18px;font-weight:700;counter-increment:s;display:flex;gap:12px;align-items:center}
.steps li:before{content:counter(s);flex:none;width:34px;height:34px;border-radius:50%;background:var(--coral);color:#fff;display:grid;place-items:center;font-family:Fredoka,sans-serif}
.signup{background:var(--ink);color:#fff;border-radius:28px;padding:28px 30px;margin-top:28px;display:grid;grid-template-columns:1.1fr 1fr;gap:24px;align-items:center}
.signup h2{margin:0 0 6px;color:#fff}.signup p{margin:0;color:#d9d8ef}
.signup form{display:flex;gap:10px;flex-wrap:wrap}.signup input[type=email]{flex:1 1 220px;padding:14px 18px;border-radius:999px;border:0;font:inherit;font-size:17px}
.signup small{display:block;width:100%;color:#b9b8d6;font-size:13px}
.signup.done form{display:none}.signup .ok{display:none;font-weight:800;color:var(--butter)}.signup.done .ok{display:block}
@media(max-width:860px){.freebie{grid-template-columns:1fr;max-width:420px;margin:0 auto}.steps,.signup{grid-template-columns:1fr}}
.band{background:var(--butter);border-radius:28px;padding:30px;margin-top:64px;display:grid;grid-template-columns:1.3fr 1fr;gap:24px;align-items:center}
.band h2{margin:0 0 8px}.band img{width:100%;border-radius:18px;background:#fff;padding:10px}
@media(max-width:720px){.band{grid-template-columns:1fr}}
.faq{max-width:760px}.faq details{background:#fff;border-radius:16px;padding:16px 20px;margin:0 0 10px}.faq summary{font-weight:800;cursor:pointer;font-size:17px}.faq details p{margin:10px 0 2px;color:#3a3958}
.post{max-width:680px}.post p,.post li{font-size:18px}.post h2{font-size:26px;margin-top:40px}
.newsletter{background:var(--butter);border-radius:24px;padding:28px;margin-top:70px}
footer{margin-top:70px;padding:30px 0;color:var(--mut);font-size:15px;border-top:2px dashed var(--line)}
@media(max-width:720px){.hero .wrap{grid-template-columns:1fr;padding-bottom:40px}.hero img{transform:none}.promise,.promise:nth-child(even){grid-template-columns:1fr;direction:ltr}.three{grid-template-columns:1fr 1fr}nav a{margin-left:10px;font-size:14px;white-space:nowrap}nav a[href$="about.html"],nav a[href*="/blog/"]{display:none}.topics{grid-template-columns:1fr 1fr;gap:12px}.topic{padding:10px 10px 14px;border-radius:18px}.topic p{display:none}.topic h3{font-size:17px;margin-top:8px}header .wrap{height:60px}.brand{font-size:19px;white-space:nowrap}.brand i{width:26px;height:26px}}
@media(prefers-reduced-motion:reduce){.book img{transition:none}html{scroll-behavior:auto}}

.cbn{background:#fff;border-radius:28px;padding:16px;box-shadow:0 10px 0 rgba(43,42,76,.12);min-width:0}
.cbn-tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px}
.cbn-tabs button{font:inherit;font-weight:800;font-size:14px;border:2px solid var(--line);background:var(--paper);color:var(--ink);border-radius:999px;padding:6px 12px;cursor:pointer}
.cbn-tabs button[aria-pressed=true]{background:var(--ink);border-color:var(--ink);color:#fff}
.cbn-meta{font-size:13px;color:var(--mut);font-weight:700;margin:0 2px 6px}
.cbn-art{position:relative;background:#fff;border:2px solid var(--line);border-radius:18px;overflow:hidden}
.cbn-art svg{display:block;width:100%;height:auto;touch-action:manipulation}
.cbn-art .s{cursor:pointer;transition:fill .25s}
.cbn-art .s:hover{stroke-width:2}
.cbn-art .nums text{font-family:Fredoka,Nunito,sans-serif;font-weight:600;font-size:7px;fill:#2B2A4C;text-anchor:middle;dominant-baseline:central;pointer-events:none;transition:opacity .2s}
.cbn-art .s.pop{animation:pop .35s ease}
.cbn-art .s.no{animation:no .3s ease}
@keyframes pop{50%{transform:scale(1.04)}}@keyframes no{25%{transform:translateX(-1.5px)}75%{transform:translateX(1.5px)}}
.cbn-art .s{transform-box:fill-box;transform-origin:center}
.cbn-key{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.cbn-key button{display:flex;align-items:center;gap:8px;font:inherit;font-weight:800;font-size:15px;color:var(--ink);background:#fff;border:2px solid var(--line);border-radius:14px;padding:6px 12px 6px 6px;cursor:pointer}
.cbn-key button i{width:28px;height:28px;border-radius:8px;border:1.5px solid #1b1b1b;display:grid;place-items:center;font-style:normal;font-family:Fredoka,sans-serif;font-size:15px}
.cbn-key button[aria-pressed=true]{border-color:var(--ink);box-shadow:0 0 0 3px var(--butter)}
.cbn-foot{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:10px;min-height:34px}
.cbn-msg{font-size:15px;font-weight:700;color:var(--ink);min-width:0}
.cbn-tools{display:flex;gap:6px;flex:none}
.cbn-tools button{font:inherit;font-size:13px;font-weight:800;color:var(--mut);background:none;border:0;cursor:pointer;text-decoration:underline;padding:4px}
.cbn-done{position:absolute;inset:auto 10px 10px 10px;background:var(--ink);color:#fff;border-radius:16px;padding:12px 14px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between;transform:translateY(130%);transition:transform .35s cubic-bezier(.3,1.4,.6,1)}
.cbn-done.on{transform:none}
.cbn-done b{font-family:Fredoka,sans-serif;font-weight:600;font-size:17px}
.cbn-done a{color:var(--ink);background:var(--butter);text-decoration:none;font-weight:800;border-radius:999px;padding:7px 14px;font-size:14px}
.cbn button:focus-visible{outline:3px solid var(--coral);outline-offset:2px}
@media(prefers-reduced-motion:reduce){.cbn-art .s,.cbn-done{transition:none}.cbn-art .s.pop,.cbn-art .s.no{animation:none}}

.quiz{background:#fff;border-radius:28px;padding:22px;box-shadow:0 10px 0 rgba(43,42,76,.12);min-width:0}
.quiz .dots{display:flex;gap:6px;margin-bottom:14px}.quiz .dots i{height:6px;flex:1;border-radius:6px;background:var(--line)}.quiz .dots i.on{background:var(--coral)}
.quiz .q{font-family:Fredoka,sans-serif;font-weight:600;font-size:22px;line-height:1.2;margin:0 0 14px}
.quiz .opts{display:grid;gap:10px}
.quiz .opts button{display:flex;align-items:center;gap:12px;text-align:left;font:inherit;font-weight:700;font-size:16px;background:var(--paper);border:2px solid var(--line);border-radius:16px;padding:10px 14px;cursor:pointer;color:var(--ink);transition:transform .12s,border-color .12s}
.quiz .opts button:hover{border-color:var(--ink);transform:translateX(3px)}
.quiz .opts img{width:58px;height:58px;object-fit:contain;background:#fff;border-radius:10px;flex:none}
.quiz .opts small{display:block;font-weight:600;color:var(--mut);font-size:13px}
.quiz .back{font:inherit;font-size:13px;font-weight:800;color:var(--mut);background:none;border:0;cursor:pointer;margin-top:12px;text-decoration:underline;padding:0}
.res{display:grid;grid-template-columns:110px 1fr;gap:16px;align-items:start}
.res img{width:100%;border-radius:10px;border:1px solid var(--line)}
.res h3{font-size:22px}.res p{font-size:15px;margin:6px 0 12px;color:#3a3958}
.res .why{grid-column:1/-1;background:var(--paper);border-radius:14px;padding:12px 14px;font-size:15px;margin:0}
.res .acts{grid-column:1/-1;display:flex;gap:10px;flex-wrap:wrap}
.res .btn{padding:11px 18px;font-size:15px}
.quiz button:focus-visible{outline:3px solid var(--coral);outline-offset:2px}
.ladder{background:#fff;border-radius:28px;padding:22px;display:grid;grid-template-columns:1fr 1.1fr;gap:26px;align-items:center}
.ladder .seg{display:inline-flex;background:var(--paper);border-radius:999px;padding:4px;gap:4px;flex-wrap:wrap}
.ladder .seg button{font:inherit;font-weight:800;font-size:14px;border:0;background:none;border-radius:999px;padding:7px 14px;cursor:pointer;color:var(--ink)}
.ladder .seg button[aria-pressed=true]{background:var(--ink);color:#fff}
.ladder .lv{display:flex;gap:8px;margin:14px 0}
.ladder .lv button{flex:1;font:inherit;font-weight:800;border:2px solid var(--line);background:#fff;border-radius:14px;padding:10px 6px;cursor:pointer;color:var(--ink)}
.ladder .lv button[aria-pressed=true]{border-color:var(--coral);background:#FFF1EE}
.ladder .stat{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ladder .stat div{background:var(--paper);border-radius:14px;padding:10px 14px}
.ladder .stat b{display:block;font-family:Fredoka,sans-serif;font-size:28px;font-weight:600;line-height:1.1;font-variant-numeric:tabular-nums}
.ladder .stat span{font-size:13px;color:var(--mut);font-weight:700}
.ladder .pic{position:relative;aspect-ratio:1;background:var(--paper);border-radius:20px;overflow:hidden}
.ladder .pic img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;transition:opacity .3s,transform .3s}
.ladder .pic img.out{opacity:0;transform:scale(.96)}
.tryit{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
.tryit .cbn{max-width:460px}
@media(max-width:720px){.ladder,.tryit{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){.ladder .pic img,.quiz .opts button{transition:none}}

/* layout: big-scene hero (book on the table + character stickers), moving character strip, living page, sticky reasons, shelf */
:root{--paper:#F4F1EC;--ink:#1F2A44;--mut:#646B7A;--line:#E2DCD2;--card:#fff;
 --hero:#DCE6EE;--hero-ink:#1F2A44;--a1:#C9DCEB;--a2:#D6E3CF;--a3:#F2D9A0;--a4:#EED7D3;--cta:#2E46C9;--cta-ink:#fff;--strip:#2E46C9;--strip-ink:#fff;
 --disp:'Fraunces',Georgia,serif;--body:'Figtree',system-ui,sans-serif;--dw:500;--track:-1px;--r:24px;
 --butter:var(--a3);--coral:var(--cta);--sky:var(--a1);--leaf:var(--a2);color-scheme:light}
html,body{overflow-x:clip}body{background:var(--paper);color:var(--ink);font-family:var(--body);font-size:17px}
h1,h2,h3,.brand{font-family:var(--disp);font-weight:var(--dw);letter-spacing:var(--track);text-wrap:balance}
.home h2{font-size:clamp(30px,4.4vw,52px);margin:0 0 18px}h3{font-weight:var(--dw)}
.brand i{background:var(--a3);border:2.5px solid var(--ink)}
main.home{max-width:none;padding:0}
.in{max-width:1120px;margin:0 auto;padding-inline:20px}
.home section{padding-block:72px}
.btn{background:var(--cta);color:var(--cta-ink);border-radius:999px;transition:transform .15s}.btn:hover{transform:translateY(-2px) rotate(-1deg)}
.btn.soft{background:var(--card);color:var(--ink);border:2px solid var(--ink)}
.topbar{background:var(--strip);color:var(--strip-ink);text-align:center;font-weight:700;font-size:14px;padding:8px 16px}.topbar a{color:inherit}
header{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:color-mix(in srgb,var(--paper) 88%,transparent);backdrop-filter:blur(10px)}
.sticker{filter:drop-shadow(3px 0 0 #fff) drop-shadow(-3px 0 0 #fff) drop-shadow(0 3px 0 #fff) drop-shadow(0 -3px 0 #fff) drop-shadow(0 8px 10px rgba(0,0,0,.18))}
/* HERO */
.hero{background:var(--hero);color:var(--hero-ink);position:relative;overflow:hidden;padding-block:56px 90px}
.hero::before{content:"";position:absolute;inset:0;background-image:radial-gradient(color-mix(in srgb,var(--hero-ink) 14%,transparent) 1.5px,transparent 1.6px);background-size:22px 22px;opacity:.6;pointer-events:none}
.hero .in{display:grid;grid-template-columns:1.05fr 1fr;gap:30px;align-items:center;position:relative}
.eyebrow{display:inline-flex;gap:8px;align-items:center;background:var(--card);color:var(--ink);border-radius:999px;padding:6px 14px;font-weight:800;font-size:13px;letter-spacing:.06em;text-transform:uppercase}
.hero h1{font-size:clamp(42px,6.4vw,84px);line-height:.98;margin:18px 0 18px}
.hero p.lede{font-size:19px;max-width:30em;margin:0 0 26px;opacity:.92}
.hero .ctas{display:flex;gap:12px;flex-wrap:wrap}
.proof{display:flex;gap:10px;flex-wrap:wrap;margin-top:26px;padding:0;list-style:none}
.proof li{background:color-mix(in srgb,var(--card) 18%,transparent);border:1.5px solid color-mix(in srgb,var(--hero-ink) 35%,transparent);border-radius:999px;padding:5px 12px;font-weight:700;font-size:14px}
.scene{position:relative;aspect-ratio:1/1;max-width:560px;width:100%;justify-self:center}
.table{position:absolute;left:-8%;right:-8%;bottom:4%;height:30%;background:color-mix(in srgb,var(--ink) 10%,transparent);border-radius:50%;filter:blur(18px)}
.scene .bk3{position:absolute;width:44%;height:auto;aspect-ratio:440/569;object-fit:cover;border-radius:4px 10px 10px 4px;box-shadow:7px 0 0 #e9e4dc,14px 18px 0 rgba(0,0,0,.16);transform-origin:50% 100%}
.scene .bk3.b1{left:30%;top:18%;transform:rotate(4deg);z-index:3}.scene .bk3.b2{left:10%;top:22%;transform:rotate(-9deg);z-index:2}.scene .bk3.b3{left:50%;top:24%;transform:rotate(14deg);z-index:1}
.scene:hover .bk3.b2{transform:rotate(-14deg) translateX(-12px)}.scene:hover .bk3.b3{transform:rotate(19deg) translateX(12px)}.scene .bk3{transition:transform .5s cubic-bezier(.3,1.4,.5,1)}
.crayon{position:absolute;height:14px;width:34%;border-radius:3px 0 0 3px;background:var(--c);z-index:4;box-shadow:inset 0 -4px 0 rgba(0,0,0,.15)}
.crayon::before{content:"";position:absolute;right:-16px;top:0;border-left:16px solid var(--c);border-top:7px solid transparent;border-bottom:7px solid transparent}
.crayon::after{content:"";position:absolute;left:18%;width:30%;top:0;bottom:0;border-left:2px solid rgba(255,255,255,.5);border-right:2px solid rgba(255,255,255,.5)}
.st{position:absolute;z-index:5;animation:bob 5s ease-in-out infinite;will-change:transform}
.st img{display:block;width:100%}
@keyframes bob{0%,100%{translate:0 0}50%{translate:0 -12px}}
.bubble{position:absolute;z-index:6;background:var(--card);color:var(--ink);border:2.5px solid var(--ink);border-radius:20px;padding:8px 14px;font-weight:800;font-size:14px;line-height:1.2;rotate:-6deg}
.bubble::after{content:"";position:absolute;left:22px;bottom:-11px;width:16px;height:16px;background:var(--card);border-right:2.5px solid var(--ink);border-bottom:2.5px solid var(--ink);rotate:45deg}
.badge{position:absolute;z-index:6;width:118px;height:118px;right:-2%;top:-2%;animation:spin 18s linear infinite}
.badge text{font:800 11.5px var(--body);letter-spacing:2.6px;fill:var(--ink)}
@keyframes spin{to{rotate:360deg}}
.hero img{background:none;padding:0;border-radius:0;transform:none;width:100%}
.wavy{display:block;width:100%;height:46px;margin-top:-46px;position:relative}
/* STRIP */
.strip{background:var(--strip);color:var(--strip-ink);overflow:hidden;padding-block:16px;rotate:-1.6deg;margin:-8px -20px 0;position:relative;z-index:2}
.strip .row{display:flex;gap:34px;align-items:center;width:max-content;animation:slide 32s linear infinite}
.strip span{font-family:var(--disp);font-weight:var(--dw);font-size:30px;white-space:nowrap}
.strip img{height:58px;width:auto}
@keyframes slide{to{transform:translateX(-50%)}}
/* LIVING PAGE */
.live{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.livecard{position:relative;background:var(--card);border-radius:var(--r);padding:16px;border:2.5px solid var(--ink);box-shadow:10px 10px 0 var(--a1)}
.livecard svg{display:block;width:100%;height:auto}
.livecard .nums text{font-family:Fredoka,sans-serif;font-weight:600;font-size:7px;fill:#2B2A4C;text-anchor:middle;dominant-baseline:central;transition:opacity .2s}
.livecard .s{transition:fill .35s}
.pen{position:absolute;left:0;top:0;width:76px;z-index:3;pointer-events:none;transition:transform .45s cubic-bezier(.5,0,.3,1);transform-origin:0 100%}
.livekey{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.livekey span{display:flex;gap:6px;align-items:center;font-weight:800;font-size:14px;border:2px solid var(--line);border-radius:12px;padding:4px 10px 4px 4px;transition:border-color .2s,background .2s}
.livekey span.on{border-color:var(--ink);background:var(--paper)}
.livekey i{width:24px;height:24px;border-radius:7px;border:1.5px solid #1b1b1b;display:grid;place-items:center;font-style:normal;font-weight:800;font-size:13px}
.tag{display:inline-block;background:var(--a3);color:var(--ink);border-radius:999px;padding:3px 12px;font-weight:800;font-size:13px}
.live .copy p{font-size:18px;color:var(--mut);max-width:30em}
.live .copy h3{font-size:24px;margin:22px 0 6px}
.yourturn{margin-top:14px}
/* QUIZ panel */
.qpanel{background:var(--a4);border-radius:calc(var(--r) + 10px);padding:44px;display:grid;grid-template-columns:.9fr 1.1fr;gap:34px;align-items:center;position:relative;overflow:visible}
.qpanel .st{position:absolute}
.quiz{border:2.5px solid var(--ink);box-shadow:8px 8px 0 var(--ink);border-radius:var(--r)}
.quiz .dots i.on{background:var(--cta)}
.quiz .q{font-family:var(--disp);font-weight:var(--dw)}
/* TOPICS */
.topics{grid-template-columns:repeat(3,1fr);gap:22px}
.topic{border:2.5px solid var(--ink);border-radius:var(--r);transition:transform .25s cubic-bezier(.3,1.5,.6,1)}
.topic:nth-child(1){background:var(--a1)!important}.topic:nth-child(2){background:var(--a2)!important}.topic:nth-child(3){background:var(--a3)!important}
.topic:hover{transform:translateY(-8px) rotate(-1.5deg)}.topic:nth-child(2):hover{transform:translateY(-8px) rotate(1.5deg)}
.topic .pair{position:relative;display:block}.topic .pair img{border:2px solid var(--ink)}
.topic .pair img.c{position:absolute;inset:0;opacity:0;transition:opacity .45s}
.topic:hover .pair img.c,.topic:focus-visible .pair img.c{opacity:1}
.topic h3{font-size:24px}
.soon span{border-color:var(--ink);color:var(--ink);background:var(--card);transition:transform .2s}.soon span:hover{transform:rotate(-4deg)}
/* REASONS: sticky picture */
.reasons{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start}
.reasons .pin{position:sticky;top:110px;aspect-ratio:1;background:var(--card);border:2.5px solid var(--ink);border-radius:var(--r);overflow:hidden;box-shadow:10px 10px 0 var(--a2)}
.reasons .pin img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:18px;opacity:0;transition:opacity .4s,transform .4s;transform:scale(.97)}
.reasons .pin img.on{opacity:1;transform:none}
.reason{min-height:62vh;display:flex;flex-direction:column;justify-content:center;padding-block:20px}
.reason:first-child{min-height:auto;padding-top:120px}
.reason .ico{width:64px;height:64px;margin-bottom:14px}
.reason h3{font-size:clamp(26px,3vw,36px);margin-bottom:10px}.reason p{font-size:19px;color:var(--mut);max-width:28em}
.reason img.m{display:none}
/* LADDER + stats */
.ladder{border:2.5px solid var(--ink);border-radius:var(--r);background:var(--card)}
.ladder .seg button[aria-pressed=true]{background:var(--ink)}
.ladder .lv button[aria-pressed=true]{border-color:var(--ink);background:var(--a3)}
.ladder .stat b{font-family:var(--disp);font-weight:var(--dw)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:22px}
.stats div{background:var(--ink);color:var(--paper);border-radius:var(--r);padding:20px}
.stats b{display:block;font-family:var(--disp);font-weight:var(--dw);font-size:clamp(34px,4vw,52px);line-height:1;font-variant-numeric:tabular-nums}
.stats span{font-size:14px;opacity:.8;font-weight:700}
/* FREE */
.free{background:var(--a3);border-radius:calc(var(--r) + 10px);padding:44px;display:grid;grid-template-columns:1fr 1fr;gap:30px;align-items:center;position:relative;color:var(--ink)}
.free h2{color:var(--ink)}.free p{font-size:18px}
.free .cbn{border:2.5px solid var(--ink)}
.free .mascot{position:absolute;width:150px;left:-30px;top:-70px;rotate:-10deg}
/* SHELF */
.shelf{display:flex;gap:34px;align-items:flex-start;justify-content:flex-start;flex-wrap:wrap;max-width:none;position:relative}
.book{width:250px;position:relative;z-index:1}
.book img{border-radius:4px 10px 10px 4px;box-shadow:inset 6px 0 0 rgba(0,0,0,.12),8px 0 0 #e9e4dc,10px 10px 0 rgba(0,0,0,.15);transition:transform .35s cubic-bezier(.3,1.4,.5,1)}
.book:hover img{transform:translateY(-16px) rotate(-3deg)}
.book .tag2{display:inline-block;margin-top:10px;background:var(--a3);color:var(--ink);border-radius:999px;padding:3px 10px;font-weight:800;font-size:13px}
.book h3{font-size:22px;margin-top:14px}.book p{color:var(--mut)}
.faq details{border:2px solid var(--ink);border-radius:14px}.faq summary{list-style:none}.faq summary::after{content:"+";float:right;font-weight:800;font-size:22px;line-height:1}.faq details[open] summary::after{content:"\2212"}
.guide{border:2px solid var(--ink);border-radius:var(--r);transition:transform .2s,background .2s}.guide:hover{transform:translateY(-4px);background:var(--a1)}
.bigmark{font-family:var(--disp);font-weight:var(--dw);font-size:clamp(64px,15vw,210px);line-height:.85;letter-spacing:var(--track);text-align:center;color:var(--ink);margin:70px 0 0;position:relative}
.bigmark img{position:absolute;width:12%;bottom:30%;animation:bob 4s ease-in-out infinite}
footer{margin-top:0}
.reveal{transition:transform .7s cubic-bezier(.2,.9,.3,1)}.reveal.pre{transform:translateY(26px)}
@media(max-width:860px){.hero .in,.live,.qpanel,.free,.reasons{grid-template-columns:1fr}.scene{max-width:440px}
 .reasons .pin{display:none}.reason,.reason:first-child{min-height:auto;padding-top:10px}.reason img.m{display:block;width:100%;max-width:420px;border:2.5px solid var(--ink);border-radius:var(--r);background:var(--card);padding:12px;margin-top:14px}
 .topics{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px;padding-bottom:10px;margin-inline:-20px;padding-inline:20px}.topics .topic{flex:0 0 74%;scroll-snap-align:center}.topics .topic p{display:block}.stats{grid-template-columns:1fr 1fr}.brand{font-size:18px}.brand i{width:24px;height:24px}nav a{margin-left:12px}.qpanel,.free{padding:26px}.qpanel .st{display:none}.free .mascot{width:96px;left:auto;right:-6px;top:-50px}
 .home section{padding-block:52px}.book{width:200px}}
@media(prefers-reduced-motion:reduce){.st,.badge,.strip .row,.bigmark img{animation:none}.reveal.pre{transform:none}.pen{transition:none}}

/* ---- hero, 2026-10 v2: headline colors itself in, books rise, characters pop ---- */
.cw .w{position:relative;display:inline-block;white-space:nowrap;isolation:isolate}
.cw .hl{position:absolute;left:-4%;width:108%;top:34%;height:60%;z-index:-1;overflow:visible}
.cw .hl path{fill:none;stroke:var(--c);stroke-width:clamp(16px,2.8vw,38px);stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:100;animation:draw .6s cubic-bezier(.4,0,.2,1) backwards;animation-delay:calc(var(--i)*.5s + .65s)}
.cw .w::before{content:attr(data-n);position:absolute;right:-.5em;top:-.35em;font:800 .22em/1 var(--body);letter-spacing:0;color:var(--ink);background:var(--card);border:2px solid var(--ink);border-radius:50%;width:1.9em;height:1.9em;display:grid;place-items:center;opacity:0;animation:badge 1.5s ease forwards;animation-delay:calc(var(--i)*.5s + .3s)}
@keyframes draw{from{stroke-dashoffset:100}to{stroke-dashoffset:0}}
@keyframes badge{0%{opacity:0;transform:scale(0)}18%{opacity:1;transform:scale(1.2)}28%{transform:scale(1)}72%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(.3)}}
.pop{position:absolute;animation:popin .7s cubic-bezier(.3,1.7,.5,1) backwards;animation-delay:var(--dl)}
@keyframes popin{from{transform:scale(0) rotate(-25deg);opacity:0}}
.hA{padding-block:28px 0}
.hA .in{display:flex;flex-direction:column;align-items:center;text-align:center}
.hA h1{font-size:clamp(44px,7.4vw,104px);line-height:1;max-width:12ch;margin:16px 0 22px}
.hA .ctas{justify-content:center}
.hA .stage{position:relative;width:min(920px,100%);height:clamp(210px,25vw,320px);margin-top:26px}
.hero .fan{position:absolute;width:27%;height:auto;bottom:-34%;border-radius:4px 10px 10px 4px;box-shadow:7px 0 0 #e9e4dc,0 16px 34px rgba(31,42,68,.22);transform:none;padding:0;background:none;animation:rise 1s cubic-bezier(.2,.9,.3,1.15) backwards;transition:translate .4s cubic-bezier(.3,1.4,.5,1)}
.hero .fan.f1{left:36.5%;z-index:3;animation-delay:.25s}.hero .fan.f2{left:16%;bottom:-42%;rotate:-11deg;z-index:2;animation-delay:.45s}.hero .fan.f3{left:57%;bottom:-42%;rotate:11deg;z-index:2;animation-delay:.6s}
.stage:hover .fan.f1{translate:0 -18px}.stage:hover .fan.f2{translate:-14px -8px}.stage:hover .fan.f3{translate:14px -8px}
@keyframes rise{from{transform:translateY(60%);opacity:0}}
.hA .stage .bubble{rotate:5deg}
.hB{padding-block:60px 90px}
.hB .in{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}
.hB h1{font-size:clamp(44px,6.6vw,96px);line-height:1;margin:18px 0 28px}
.hstage{position:relative;max-width:520px;width:100%;justify-self:center}
.hB .livecard{rotate:1.5deg;animation:popin .8s cubic-bezier(.3,1.5,.5,1) backwards .2s}
.hB .yourturn{display:block;margin:22px auto 0;font:inherit;font-weight:800;font-size:16px;background:none;border:0;color:var(--ink);text-decoration:underline;text-underline-offset:4px;cursor:pointer}
.intro{font-size:20px;max-width:34em;color:var(--mut);margin:-4px 0 34px}
@media(max-width:860px){.hB .in{grid-template-columns:1fr}.hA .stage{height:56vw;margin-top:28px}.hero .fan{width:34%}.hero .fan.f1{left:33%}.hero .fan.f2{left:8%}.hero .fan.f3{left:58%}.hA .stage .bubble{display:none}}
@media(prefers-reduced-motion:reduce){.cw .hl path,.cw .w::before,.pop,.hero .fan,.hB .livecard{animation:none}.cw .w::before{opacity:0}}

/* ---- 2026-10 v4: clay. Every block looks pressed out of soft clay: light from top-left, shade bottom-right, soft drop shadow.
   V picked "clay + tilt" (2026-10-13). Hard ink borders are dropped on blocks; light and shade carry the depth. ---- */
:root{--clay:inset 10px 10px 22px rgba(255,255,255,.62),inset -12px -14px 26px rgba(31,42,68,.12),22px 30px 50px -18px rgba(31,42,68,.30);
 --clay-sm:inset 6px 6px 12px rgba(255,255,255,.72),inset -8px -10px 16px rgba(31,42,68,.13),12px 16px 28px -10px rgba(31,42,68,.30);
 --clay-in:inset 4px 5px 12px rgba(31,42,68,.18),inset -3px -3px 8px rgba(255,255,255,.7);
 --rc:40px;--rs:28px}
.home section:not(.hero){padding-block:26px}
.home #finder{padding-top:60px}
.slab,.qpanel,.free{position:relative;border:0;border-radius:var(--rc);padding:46px;box-shadow:var(--clay)}
.slab>h2:first-child{margin-top:0}.slab h2.h2b{margin-top:46px}
.t-card{background:#FBF9F5}.t-a1{background:var(--a1)}.t-a2{background:var(--a2)}.t-a3{background:var(--a3)}.t-a4{background:var(--a4)}
/* small clay pieces */
.topic,.age,.guide,.faq details,.ladder,.quiz,.reason,.livecard,.free .cbn{border:0!important;box-shadow:var(--clay-sm);border-radius:var(--rs)}
.topic:nth-child(1){background:#DCE9F3!important}.topic:nth-child(2){background:#E3EEDC!important}.topic:nth-child(3){background:#F8E6BC!important}
.topic .pair img{border:0;border-radius:18px;box-shadow:var(--clay-in);background:#fff}
.age,.guide,.reason,.quiz,.ladder,.faq details,.livecard,.free .cbn{background:#fff}
.age.off{box-shadow:var(--clay-in);background:transparent}
.topic,.age,.guide,.reason{transition:transform .35s cubic-bezier(.3,1.6,.5,1)}
.age:hover,.guide:hover,.reason:hover{transform:translateY(-6px) scale(1.02)}
.guide:hover{background:#fff}
.faq details{margin-bottom:12px}
.quiz .opts button{border:0;background:var(--paper);box-shadow:inset 4px 4px 8px rgba(255,255,255,.8),inset -5px -6px 10px rgba(31,42,68,.1),6px 8px 14px -6px rgba(31,42,68,.25)}
.quiz .opts img{box-shadow:var(--clay-in)}
.ladder .lv button,.ladder .seg button{border:0!important;box-shadow:inset 3px 3px 6px rgba(255,255,255,.8),inset -4px -5px 8px rgba(31,42,68,.12),4px 6px 10px -5px rgba(31,42,68,.25)}
.ladder .lv button[aria-pressed=true],.ladder .seg button[aria-pressed=true]{box-shadow:var(--clay-in)}
.ladder .stat>div{box-shadow:var(--clay-in)}
.stats div{background:var(--ink);border-radius:var(--rs);box-shadow:inset 6px 6px 12px rgba(255,255,255,.14),inset -8px -10px 16px rgba(0,0,0,.35),12px 16px 28px -10px rgba(31,42,68,.45)}
.reasons3{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.reason{padding:18px 20px 24px;display:block;min-height:0}
.reason .rpic{aspect-ratio:1;border-radius:20px;background:#fff;overflow:hidden;margin-bottom:16px;box-shadow:var(--clay-in)}
.reason .rpic img{width:100%;height:100%;object-fit:contain;padding:10px}
.reason .ico{width:44px;height:44px;margin-bottom:8px}
.reason h3{font-size:22px;margin:0 0 6px}.reason p{font-size:16px;margin:0;color:var(--mut)}
.slab .intro{margin-bottom:28px}
/* puffy buttons */
.btn{border:0!important;box-shadow:inset 4px 4px 8px rgba(255,255,255,.35),inset -5px -6px 10px rgba(0,0,0,.22),8px 12px 20px -8px rgba(46,70,201,.55)}
.btn.soft{box-shadow:inset 4px 4px 8px rgba(255,255,255,.9),inset -5px -6px 10px rgba(31,42,68,.12),8px 12px 20px -8px rgba(31,42,68,.3)}
.btn:active{box-shadow:var(--clay-in)}
/* books: real covers, lifted with a soft shadow; tilt is added by home.js */
.book img{display:block;width:100%;height:auto;aspect-ratio:800/1035;object-fit:cover;border-radius:6px 16px 16px 6px;box-shadow:inset 6px 0 0 rgba(0,0,0,.12),18px 26px 36px -14px rgba(31,42,68,.45)}
/* tilt (pointer devices only, set by home.js) */
.tilt{transform-style:preserve-3d;will-change:transform}
.tilt.tilting{transition:transform .12s ease-out!important}
.topic.tilt .pair,.book.tilt img{transform:translateZ(36px)}
.topics,.shelf{perspective:1000px}
.bigmark{margin-top:64px}
.grown{display:grid;grid-template-columns:.9fr 1.1fr;gap:40px;align-items:center;background:#EAD9CF}
.gpic{position:relative;max-width:420px;justify-self:center;width:100%}
.gpic img:first-child{display:block;width:78%;border-radius:8px 16px 16px 8px;box-shadow:inset 6px 0 0 rgba(0,0,0,.12),18px 26px 36px -14px rgba(31,42,68,.45);rotate:-4deg}
.gpic .gpage{position:absolute;right:0;bottom:-6%;width:52%;border-radius:14px;background:#fff;padding:6px;box-shadow:var(--clay-sm);rotate:5deg}
@media(max-width:860px){.grown{grid-template-columns:1fr}}
@media(max-width:860px){.slab,.qpanel,.free{padding:24px;border-radius:30px}.reasons3{grid-template-columns:1fr}.home section:not(.hero){padding-block:14px}.slab h2.h2b{margin-top:30px}}
"""

FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,500,100;9..144,600,100&family=Figtree:wght@400;500;700;800&family=Fredoka:wght@600&display=swap"
def page(title, desc, body, path, jsonld=None, canonical=None, main_class="wrap", tail=""):
    can = canonical or f"{SITE}/{path}"
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j)}</script>' for j in (jsonld if isinstance(jsonld, list) else [jsonld])) if jsonld else ""
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{can}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:image" content="{SITE}/img/hero_group.png"><meta property="og:url" content="{can}">
<meta name="p:domain_verify" content="dbc56bd2b5ac3a820feb8a26e39030c8"><link rel="icon" type="image/png" href="{SITE}/img/favicon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="{FONTS}">
<style>{CSS}</style>{ld}</head><body>
<div class="topbar">20 free cozy Christmas coloring pages for grown-ups &middot; <a href="{SITE}/xmas/">Print them here</a> &middot; Kids pages: <a href="{SITE}/free.html">here</a></div>
<header><div class="wrap"><a class="brand" href="{SITE}/"><i></i>Hop Along Books</a><nav><a href="{SITE}/#topics">Books</a><a href="{SITE}/free.html">Free pages</a><a href="{SITE}/xmas/">Christmas pages</a><a href="{SITE}/blog/">Guides</a><a href="{SITE}/about.html">About</a></nav></div></header>
<main class="{main_class}">{body}</main>
<footer><div class="wrap">&copy; 2026 Hop Along Books. Color by number books for ages 3-5. Available on Amazon. &middot; <a href="{SITE}/about.html">About</a> &middot; <a href="{SITE}/blog/">Guides for parents</a></div></footer>
{tail}</body></html>"""
    full = os.path.join(ROOT, path); os.makedirs(os.path.dirname(full), exist_ok=True); open(full, "w").write(html)

def book_card(b):
    return f"""<a class="book" href="{SITE}/books/{b['slug']}.html"><img src="{SITE}/img/{b['key']}_cover.jpg" alt="{b['title']} cover" loading="lazy" width="800" height="1035">
<h3>{b['short']}</h3><p>{b['sub']}</p><span class="tag">{b['status']}</span></a>"""


# ---------- FAQ (shown on home + book pages, marked up as FAQPage) ----------
# General questions: taken from real Google "People also ask" / AI Overview results (checked 2026-10-08)
FAQ = [
 ("What age is color by number appropriate for?",
  "Simple color by number pages can start around age 3, when many children are learning their first numbers and basic colors. Pages with only 2 or 3 colors and big spaces work best at first. By 4 and 5, most children can handle more colors and smaller spaces, often without help."),
 ("Can 3 year olds do color by number?",
  "Yes, if the page is simple. Look for pages that use only the numbers 1 to 3 and big shapes. Expect to help read the key at first (\"find all the 1s and color them red\"), and don't worry about coloring outside the lines; neatness isn't the goal at 3. Hop Along Level 1 pictures use only 3 colors and spaces about an inch wide for exactly this reason."),
 ("Does my child need to know numbers and colors before starting?",
  "No. A good key shows each number next to a swatch of the color and the color's name, so a child can match by color and learn the number and the word along the way. Color by number is one way to practice them, not a test."),
 ("Is color by number bad for creativity?",
  "It is a structured activity, so it is best mixed with free drawing rather than replacing it. Following the key builds number recognition, color names, focus and crayon control; free drawing builds imagination. Every Hop Along picture has a blank box on the back for your child to draw their own picture."),
 ("Where can I find free printable color by number pages for 3 year olds?",
  "You can print real pages from our books for free, each with its answer picture, on the Free pages section of this website (hopalongbooks.github.io/free.html)."),
]
# Product questions (book pages only)
BOOK_FAQ = [
 ("Which crayons do I need?",
  "Any ordinary box of crayons or colored pencils. The books use everyday colors such as Red, Blue, Yellow, Green, Orange, Brown and Pink, and every key writes the color name out. If a page asks for Sky Blue, any light blue crayon works; for Tan, a light brown or peach crayon is fine."),
 ("Will markers bleed through the pages?",
  "Each picture is printed on one side of the page only. The back of every picture is an activity page, not another picture, so a marker can't ruin the next one. Crayons and colored pencils work best; if you use markers, slip a sheet of scrap paper behind the page."),
 ("How many pages and pictures are in the book?",
  "102 pages: 45 pictures to color in 5 levels from easy to harder (3 to 8 colors), an activity page behind each picture, and full answer pictures at the back. 8.5 x 11 inch paperback."),
 ("What is on the back of each picture?",
  "A short fact to read aloud, a strip to test colors before you start, a \"How did you feel?\" face to circle, and a box for your child to draw their own picture."),
]
def faq_html(items):
    return '<div class="faq">' + "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items) + '</div>'
def faq_ld(items):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}

# ---------- home ----------
def topic_count(t): 
    n=len([b for b in BOOKS if b["topic"]==t["slug"]]); return f"{n} book" + ("" if n==1 else "s")
# Home layout (2026-10 redesign, chosen by V: "C+" layout with the C2 palette).
# Interactive parts (living page, quiz, level ladder, try-it colorer) live in assets/home.js;
# HAB below hands it the book data so prices/links/status stay in one place (BOOKS).
STICKERS = [("st_trex", "Silly dinos"), ("st_truck", "Fire trucks"), ("st_cat", "Kittens"), ("st_rocket", "Rockets"), ("st_penguin", "Penguins"), ("st_baby", "Baby dinos")]
strip_row = "".join(f'<img class="sticker" src="{SITE}/img/{i}.png" alt="" width="66" height="58"><span>{t}</span><span aria-hidden="true">&#10022;</span>' for i, t in STICKERS)
ICON_KEY = '<svg class="ico" viewBox="0 0 64 64" aria-hidden="true"><rect x="4" y="10" width="56" height="44" rx="10" fill="var(--a1)" stroke="var(--ink)" stroke-width="3"/><rect x="12" y="20" width="12" height="12" rx="3" fill="#EE204D" stroke="var(--ink)" stroke-width="2"/><path d="M30 26h22M12 42h40" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/></svg>'
ICON_HAND = '<svg class="ico" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="27" fill="var(--a2)" stroke="var(--ink)" stroke-width="3"/><path d="M14 32h36M14 32l7-6M14 32l7 6M50 32l-7-6M50 32l-7 6" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_FLIP = '<svg class="ico" viewBox="0 0 64 64" aria-hidden="true"><path d="M10 12h30l14 14v26H10z" fill="var(--a4)" stroke="var(--ink)" stroke-width="3" stroke-linejoin="round"/><path d="M40 12v14h14" fill="var(--card)" stroke="var(--ink)" stroke-width="3" stroke-linejoin="round"/><circle cx="24" cy="38" r="4" fill="var(--ink)"/><path d="M33 38h12" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/></svg>'
P_KEY = "<h3>They can read the key on their own</h3><p>Every number has a swatch and the color's name - Red, Blue, Green. No squinting at a tiny dot, and no shades you don't own. For Sky Blue, any light blue crayon works.</p>"
P_BIG = "<h3>Big enough for a fist full of crayon</h3><p>Level 1 spaces are about an inch wide. Even the busiest Level 5 scene keeps every space around half an inch. We measure every page so small hands stay inside the lines without help.</p>"
P_FLIP = "<h3>Flip it over, there's more</h3><p>Pictures are printed on one side, so markers can't ruin the next one. Behind each picture: a fact to read aloud, a strip to test colors, a face to circle, and a box to draw their own.</p>"
FREE_NAME = {"things-that-go": "Fire Truck", "animals": "Cat", "dinosaurs": "T-Rex Eats an Apple"}
HAB = dict(site=SITE, free=FREE_NAME,
           books={b["topic"]: dict(t=b["short"], sub=b["sub"], url=f"{SITE}/books/{b['slug']}.html", amz=b["amazon"], live=b["status"].startswith("Available"), status=b["status"], key=b["key"]) for b in BOOKS})
# ----- home hero (V: the old first screen was "a pile of text, no effect") -----
HERO = os.environ.get("HAB_HERO", "B")   # V chose B (2026-10-13)
SCRIBBLE = '<svg class="hl" viewBox="0 0 100 30" preserveAspectRatio="none" aria-hidden="true"><path d="M3 20 C16 10 26 25 40 15 S64 24 78 13 S92 18 97 11" pathLength="100" vector-effect="non-scaling-stroke"/></svg>'
def hw(word, n, color):
    return f'<span class="w" data-n="{n}" style="--c:{color};--i:{n-1}">{SCRIBBLE}{word}</span>'
H1_WORDS = f'{hw("Coloring", 1, "#F6B8C4")} books {hw("little hands", 2, "#9ED8F5")} can actually {hw("finish", 3, "#F7D774")}'
STICKER_POP = lambda f, style, delay: f'<div class="pop" style="{style};--dl:{delay}s"><div class="st"><img class="sticker" src="{SITE}/img/{f}.png" alt=""></div></div>'
if HERO == "A":
    HERO_HTML = f"""<section class="hero hA"><div class="in">
 <span class="eyebrow">Color by number &middot; Ages 3-5</span>
 <h1 class="cw">{H1_WORDS}</h1>
 <div class="ctas"><a class="btn" href="#finder">Find a book</a><a class="btn soft" href="{SITE}/free.html">Free pages to print</a></div>
 <div class="stage" role="img" aria-label="The three Hop Along books with characters from the books: a T-Rex, a rocket, a cat, a penguin and a baby dinosaur">
  <img class="fan f2" src="{SITE}/img/book2_cover_sm.jpg" alt="" width="440" height="569">
  <img class="fan f3" src="{SITE}/img/book3_cover_sm.jpg" alt="" width="440" height="569">
  <img class="fan f1" src="{SITE}/img/book1_cover_sm.jpg" alt="" width="440" height="569" fetchpriority="high">
  {STICKER_POP("st_trex", "width:17%;left:2%;top:18%", .9)}
  {STICKER_POP("st_rocket", "width:12%;left:20%;top:-4%", 1.05)}
  {STICKER_POP("st_cat", "width:15%;right:3%;top:22%", 1.2)}
  {STICKER_POP("st_baby", "width:12%;right:19%;top:-2%", 1.35)}
  {STICKER_POP("st_penguin", "width:12%;left:14%;bottom:-2%", 1.5)}
  <div class="bubble pop" style="right:6%;top:-14%;--dl:1.7s">Color names<br>on every key!</div>
 </div>
</div></section>"""
    LIVE_HTML = f"""<section><div class="in live">
 <div class="livecard"><div id="livepage"><img src="{SITE}/img/hero_truck.jpg" alt="A finished Level 2 fire truck page" style="display:block;width:100%"></div><div class="livekey" id="livekey"></div></div>
 <div class="copy">
  <span class="tag">Real pages from the books</span>
  <h2 style="margin-top:14px">Watch a page come to life</h2>
  <p>Find the number, match it to the color on the key, fill it in. This fire truck is a Level 2 page: 4 colors, each one named on the key.</p>
  <button type="button" class="btn soft yourturn" id="yourturn">Your turn: color one here</button>
 </div>
</div></section>"""
else:
    HERO_HTML = f"""<section class="hero hB"><div class="in">
 <div class="hcopy">
  <span class="eyebrow">Color by number &middot; Ages 3-5</span>
  <h1 class="cw">{H1_WORDS}</h1>
  <div class="ctas"><a class="btn" href="#finder">Find a book</a><a class="btn soft" href="{SITE}/free.html">Free pages to print</a></div>
 </div>
 <div class="hstage">
  {STICKER_POP("st_trex", "width:30%;left:-14%;bottom:6%;z-index:4", 1.0)}
  {STICKER_POP("st_cat", "width:24%;right:-10%;top:-8%;z-index:4", 1.2)}
  {STICKER_POP("st_baby", "width:20%;right:-6%;bottom:-6%;z-index:4", 1.4)}
  <div class="livecard"><div id="livepage"><img src="{SITE}/img/hero_truck.jpg" alt="A finished Level 2 fire truck page from Things That Go" style="display:block;width:100%"></div><div class="livekey" id="livekey"></div></div>
  <button type="button" class="yourturn" id="yourturn">Your turn: tap to color one &rarr;</button>
 </div>
</div></section>"""
    LIVE_HTML = ""

home_body = f"""
{HERO_HTML}
<div class="strip" aria-hidden="true"><div class="row">{strip_row}{strip_row}</div></div>

{LIVE_HTML}

<section id="finder"><div class="in">
 <div class="qpanel">
  <img class="st sticker" src="{SITE}/img/st_penguin.png" alt="" style="width:120px;right:-20px;top:-60px;rotate:10deg">
  <div><span class="tag">Find their book in 3 taps</span><h2 style="margin-top:14px">Not sure which one?</h2><p style="font-size:18px;max-width:26em">Tell us what they love and how they color today. We'll point you to the book and the level to start on.</p></div>
  <div class="quiz" id="quiz" aria-live="polite"><p class="q">What does your child love most?</p><div class="opts">{''.join(f'<a class="btn soft" href="{SITE}/topics/{t["slug"]}.html">{t["name"]}</a>' for t in TOPICS)}</div></div>
 </div>
</div></section>

<section id="topics"><div class="in"><div class="slab t-card">
 <h2>What does your kid love?</h2>
 <div class="topics">{''.join(f'<a class="topic" style="background:{t["color"]}" href="{SITE}/topics/{t["slug"]}.html"><span class="pair"><img src="{SITE}/img/{t["numbered"]}" alt="{t["name"]} page with numbers, ready to color" loading="lazy"><img class="c" src="{SITE}/img/{t["img"]}" alt="" loading="lazy"></span><h3>{t["name"]}</h3><p>{t["blurb"]}</p><span class="count">{topic_count(t)}</span></a>' for t in TOPICS)}</div>
 <div class="soon" aria-label="Coming soon">{''.join(f'<span>{x} &middot; coming soon</span>' for x in SOON)}</div>
 <h2 class="h2b">How old is your little one?</h2>
 <div class="ages">{''.join((f'<a class="age" href="{SITE}/ages/{g["slug"]}.html"><b>{g["name"]}</b>{g["blurb"]}</a>' if g["live"] else f'<div class="age off"><b>{g["name"]}</b>{g["blurb"]} Coming next.</div>') for g in AGES)}</div>
</div></div></section>

<section><div class="in"><div class="slab t-a2">
 <h2>Why moms keep these in the car</h2>
 <p class="intro">Big shapes, color names written on every page, and pictures that still look like a fire truck or a kitten when they're done. Every page is measured for the age on the cover.</p>
 <div class="reasons3">
  <div class="reason"><div class="rpic"><img src="{SITE}/img/book3_B3_key.jpg" alt="Color key with the color name next to each number" loading="lazy"></div>{ICON_KEY}{P_KEY}</div>
  <div class="reason"><div class="rpic"><img src="{SITE}/img/hero_trex.jpg" alt="Level 1 page: a T-Rex with three big areas to color" loading="lazy"></div>{ICON_HAND}{P_BIG}</div>
  <div class="reason"><div class="rpic"><img src="{SITE}/img/book3_B2_back.jpg" alt="The activity page behind each picture" loading="lazy"></div>{ICON_FLIP}{P_FLIP}</div>
 </div>
</div></div></section>

<section><div class="in"><div class="slab t-a1">
 <h2>Watch it get harder, page by page</h2>
 <div class="ladder" id="ladder"><div><div class="seg" role="group" aria-label="Book"></div><div class="lv" role="group" aria-label="Level"></div><div class="stat"><div><b data-s="c">3</b><span>colors in the key</span></div><div><b data-s="w">1 in</b><span>smallest space, about</span></div></div><p style="font-size:15px;color:var(--mut);margin:14px 0 0">Every book has 45 pictures in 5 levels, so the same book still works as your child grows.</p></div><div class="pic"><img src="{SITE}/img/book1_A1_level.jpg" alt="Level 1 example page" loading="lazy"></div></div>
 <div class="stats"><div><b data-count="45">45</b><span>pictures in every book</span></div><div><b data-count="5">5</b><span>levels, easy to harder</span></div><div><b>3-8</b><span>colors per picture</span></div><div><b>102</b><span>pages, 8.5 x 11 in</span></div></div>
</div></div></section>

<section><div class="in">
 <div class="free"><img class="mascot sticker" src="{SITE}/img/st_cat.png" alt="" loading="lazy">
  <div><h2>Try a page tonight, free</h2><p>Color this one on screen first. Then print a real page from each book, with its answer picture, and see if the level is right before you buy.</p><a class="btn" href="{SITE}/free.html">Print free pages</a></div>
  <div class="cbn" id="mini-cbn"><img src="{SITE}/img/free_cat.jpg" alt="Free printable page: a cat to color by number" loading="lazy" style="width:100%"></div>
 </div>
</div></section>

<section id="books"><div class="in"><div class="slab t-card">
 <h2>All books</h2>
 <div class="shelf">{''.join(f'<a class="book" href="{SITE}/books/{b["slug"]}.html"><img src="{SITE}/img/{b["key"]}_cover.jpg" alt="{b["title"]} cover" loading="lazy" width="800" height="1035"><h3>{b["short"]}</h3><p>{b["sub"]}</p><span class="tag2">{b["status"]}</span></a>' for b in BOOKS)}<a class="book" href="{SITE}/books/{GROWNUP["slug"]}.html"><img src="{SITE}/img/book4_cover.jpg" alt="{GROWNUP["title"]} cover" loading="lazy" width="800" height="824"><h3>{GROWNUP["short"]}</h3><p>For grown-ups &middot; {GROWNUP["sub"]}</p><span class="tag2">{GROWNUP["status"]}</span></a></div>
</div></div></section>

<section id="grownups"><div class="in"><div class="slab t-a4 grown">
 <div class="gpic"><img src="{SITE}/img/book4_cover.jpg" alt="{GROWNUP['title']} cover" loading="lazy" width="800" height="824"><img class="gpage" src="{SITE}/img/book4_xmas.jpg" alt="A bold and easy gingerbread house coloring page" loading="lazy"></div>
 <div>
  <span class="tag">New &middot; for grown-ups</span>
  <h2 style="margin-top:14px">Your turn to color, mom</h2>
  <p class="intro" style="margin-bottom:18px">{GROWNUP['blurb']}</p>
  <p style="margin:0 0 22px;color:var(--mut)">50 designs &middot; bold lines, big spaces &middot; {GROWNUP['size']} &middot; ${GROWNUP['price']}</p>
  <div class="ctas"><a class="btn" href="{GROWNUP['amazon']}" rel="nofollow">Get it on Amazon</a><a class="btn soft" href="{SITE}/books/{GROWNUP['slug']}.html">See inside</a></div>
 </div>
</div></div></section>

<section><div class="in"><div class="slab t-a4"><h2>Questions parents ask</h2>{faq_html(FAQ)}</div></div></section>

<section><div class="in"><div class="slab t-a3"><h2>For parents</h2>
<div class="guides">
<a class="guide" href="{SITE}/blog/can-a-3-year-old-do-color-by-number.html"><h3>Can a 3-year-old do color by number?</h3><p>Yes, with the right pages. What to expect and how to help.</p></a>
<a class="guide" href="{SITE}/blog/how-to-choose-a-color-by-number-book-for-a-3-year-old.html"><h3>How to choose a color by number book for a 3-year-old</h3><p>Five things to check before you buy, and the mistake most books make.</p></a>
<a class="guide" href="{SITE}/blog/why-color-names-matter-more-than-color-dots.html"><h3>Why color names beat color dots</h3><p>Dots are hard to match. Words aren't.</p></a>
<a class="guide" href="{SITE}/blog/markers-vs-crayons-for-toddler-coloring-books.html"><h3>Markers or crayons?</h3><p>What works at 3, at 5, and how to stop bleed-through.</p></a>
<a class="guide" href="{SITE}/blog/quiet-activities-for-a-3-year-old-on-a-plane-or-car-ride.html"><h3>Quiet activities for a plane or car ride</h3><p>What to pack for a 3-year-old, and what to leave at home.</p></a>
<a class="guide" href="{SITE}/blog/how-to-help-a-3-year-old-hold-a-crayon.html"><h3>Helping a 3-year-old hold a crayon</h3><p>The fist grip is normal. Small things that help it grow.</p></a>
</div></div>
<div class="bigmark" aria-hidden="true">Hop Along<img class="sticker" src="{SITE}/img/st_rocket.png" alt="" style="left:-2%;rotate:-12deg" loading="lazy"><img class="sticker" src="{SITE}/img/st_baby.png" alt="" style="right:0;animation-delay:-2s" loading="lazy"></div>
</div></section>
"""
HOME_TAIL = f'<script>window.HAB={json.dumps(HAB)};</script><script src="{SITE}/assets/home.js" defer></script>'
page("Hop Along Books - Color by Number for Kids Ages 3-5", "Color by number books made for ages 3-5: big shapes, color names on every key, one picture per page, a fun activity page behind each. Trucks, animals and dinosaurs. On Amazon.", home_body, "index.html",
     jsonld=[{"@context":"https://schema.org","@type":"Organization","name":PUB,"url":SITE+"/","email":"purevibe88@gmail.com","description":"Publisher of color by number books for children ages 3-5."}, faq_ld(FAQ)], canonical=SITE+"/", main_class="home", tail=HOME_TAIL)

# ---------- book pages ----------
for b in BOOKS:
    k = b["key"]
    ld = {"@context":"https://schema.org","@type":"Book","name":b["title"],"alternativeHeadline":b["sub"],"author":{"@type":"Organization","name":PUB},"publisher":{"@type":"Organization","name":PUB},
          "bookFormat":"https://schema.org/Paperback","numberOfPages":102,"inLanguage":"en","typicalAgeRange":"3-5","genre":"Children's activity book, color by number",
          "image":f"{SITE}/img/{k}_cover.jpg","url":f"{SITE}/books/{b['slug']}.html","offers":{"@type":"Offer","url":b["amazon"],"priceCurrency":"USD","price":"10.99","availability":"https://schema.org/InStock"}}
    if b["isbn"]: ld["isbn"] = b["isbn"]
    bfaq = [(f"What pictures are in {b['short']}?", f"45 pictures: {b['inside']}. They go from Level 1 (3 colors) to Level 5 (8 colors).")] + BOOK_FAQ + FAQ[:3]
    body = f"""
<div class="promise" style="margin-top:36px;grid-template-columns:1fr 1.4fr;align-items:start">
<div><img src="{SITE}/img/{k}_cover.jpg" alt="{b['title']} cover" style="width:100%;border-radius:14px;border:1px solid var(--line)"></div>
<div><h1 style="margin-top:0">{b['short']}</h1><p style="font-size:20px;color:var(--mut);margin:8px 0 14px">{b['sub']}</p><p style="font-size:18px">{b['blurb']}</p>
<a class="btn" href="{b['amazon']}" rel="nofollow">Get it on Amazon</a> <span style="color:var(--mut);margin-left:10px">{b['status']} &middot; $10.99</span></div>
</div>
<h2>What's in it</h2>
<table class="spec">
<tr><th>Age</th><td>3-5 (preschool and kindergarten)</td></tr>
<tr><th>Pictures</th><td>45, in 5 levels from easy to harder</td></tr>
<tr><th>Colors per picture</th><td>Level 1: 3 &middot; Level 2: 4 &middot; Level 3: 5 &middot; Level 4: 6 &middot; Level 5: 8</td></tr>
<tr><th>Smallest coloring space</th><td>Level 1 about 1 inch (25 mm) wide; Level 5 about half an inch (12 mm) wide. Every page is measured.</td></tr>
<tr><th>Color key</th><td>Number + color swatch + color name written out. Everyday colors such as Red, Blue, Yellow, Green, Orange, Brown and Pink. Sky Blue = any light blue crayon.</td></tr>
<tr><th>Printing</th><td>One picture per page, printed on one side. Behind each picture: {b['fact']}, a color test strip, a "How did you feel?" face to circle and a box to draw your own.</td></tr>
<tr><th>Pages / size</th><td>102 pages &middot; 8.5 x 11 in &middot; paperback, matte cover</td></tr>
<tr><th>What's inside</th><td>{b['inside']}; answer pictures at the back</td></tr>
<tr><th>Best with</th><td>Crayons or colored pencils. Markers work too - the back of each picture is an activity page, not another picture.</td></tr>
{f'<tr><th>ISBN</th><td>{b["isbn"]}</td></tr>' if b['isbn'] else ''}
</table>
<h2>Easy to harder</h2>
<div class="three">
<figure><img src="{SITE}/img/{k}_A1_level.jpg" alt="Level 1 example"><figcaption>Level 1 &middot; 3 colors</figcaption></figure>
<figure><img src="{SITE}/img/{k}_A2_level.jpg" alt="Level 3 example"><figcaption>Level 3 &middot; 5 colors</figcaption></figure>
<figure><img src="{SITE}/img/{k}_A3_level.jpg" alt="Level 5 example"><figcaption>Level 5 &middot; 8 colors</figcaption></figure>
</div>
<h2>More than a coloring page</h2>
<div class="three">
<figure><img src="{SITE}/img/{k}_B1_page.jpg" alt="A numbered coloring page"><figcaption>One picture per page</figcaption></figure>
<figure><img src="{SITE}/img/{k}_B2_back.jpg" alt="The activity page behind each picture"><figcaption>Flip the page: fact, color test, feelings</figcaption></figure>
<figure><img src="{SITE}/img/{k}_B3_key.jpg" alt="Color key with color names"><figcaption>A color key kids can read</figcaption></figure>
</div>
<h2>Questions parents ask</h2>
{faq_html(bfaq)}
<h2>More from Hop Along Books</h2>
<div class="shelf">{''.join(book_card(o) for o in BOOKS if o['key']!=k)}</div>
"""
    page(f"{b['title']} | Hop Along Books", f"{b['sub']}. 45 pictures in 5 levels for ages 3-5, color names on every key, one picture per page. 102 pages, 8.5 x 11 in.", body, f"books/{b['slug']}.html", jsonld=[ld, faq_ld(bfaq)])

# ---------- grown-up book page ----------
g = GROWNUP
gld = {"@context":"https://schema.org","@type":"Book","name":g["title"],"alternativeHeadline":g["sub"],"author":{"@type":"Organization","name":PUB},"publisher":{"@type":"Organization","name":PUB},
       "bookFormat":"https://schema.org/Paperback","numberOfPages":g["pages"],"inLanguage":"en","isbn":g["isbn"],"genre":"Adult coloring book, bold and easy, Christmas",
       "image":f"{SITE}/img/book4_cover.jpg","url":f"{SITE}/books/{g['slug']}.html","offers":{"@type":"Offer","url":g["amazon"],"priceCurrency":"USD","price":g["price"],"availability":"https://schema.org/InStock"}}
gfaq = [("Is Fireside & Flurries for adults or kids?", "Both. The designs are drawn for grown-ups who want relaxing, easy coloring: thick outlines and big spaces, no tiny details. Older kids enjoy them too. There are no numbers or color key in this book."),
        ("How many pages are there?", f"50 designs, one per page, printed on one side only, plus a color test page at the front. {g['pages']} pages, {g['size']} square paperback."),
        ("What's in it?", "5 autumn pages, 18 snowy winter pages and 27 Christmas pages: hot cocoa, fireplaces, snow globes, ice skating, gingerbread houses, Santa, stockings, ornaments and Christmas morning. Hop the bunny, Bramble the bear, Mitten the cat and Pip the fox appear throughout."),
        ("Can I use markers?", "Yes. Pages are printed on one side, so slip a sheet of paper behind the page and markers won't reach the next design."),
        ("Is it a good gift?", "It's made to be a stocking stuffer: square, cozy and easy enough that anyone can finish a page in one sitting.")]
gbody = f"""
<div class="promise" style="margin-top:36px;grid-template-columns:1fr 1.4fr;align-items:start">
<div><img src="{SITE}/img/book4_cover.jpg" alt="{g['title']} cover" style="width:100%;border-radius:14px;border:1px solid var(--line)"></div>
<div><span class="tag">For grown-ups</span><h1 style="margin-top:10px">{g['short']}</h1><p style="font-size:20px;color:var(--mut);margin:8px 0 14px">{g['sub']}</p><p style="font-size:18px">{g['blurb']}</p>
<a class="btn" href="{g['amazon']}" rel="nofollow">Get it on Amazon</a> <span style="color:var(--mut);margin-left:10px">{g['status']} &middot; ${g['price']}</span></div>
</div>
<h2>What's in it</h2>
<table class="spec">
<tr><th>For</th><td>Adults, teens and seniors. Older kids enjoy it too. No numbers, no color key.</td></tr>
<tr><th>Designs</th><td>50, one per page: 5 fall, 18 winter, 27 Christmas</td></tr>
<tr><th>Lines</th><td>Thick, bold outlines and big open spaces. Easy on the eyes, easy to finish.</td></tr>
<tr><th>The cast</th><td>Hop the bunny, Bramble the bear, Mitten the cat and Pip the fox: sipping cocoa, ice skating, wrapping gifts, baking cookies</td></tr>
<tr><th>Printing</th><td>One design per page, printed on one side. Color test page at the front.</td></tr>
<tr><th>Pages / size</th><td>{g['pages']} pages &middot; {g['size']} &middot; square paperback, matte cover</td></tr>
<tr><th>Best with</th><td>Markers, colored pencils, gel pens or crayons. Put a sheet of paper behind the page when using markers.</td></tr>
<tr><th>ISBN</th><td>{g['isbn']}</td></tr>
</table>
<h2>Fall, winter, Christmas</h2>
<div class="three">
<figure><img src="{SITE}/img/book4_fall.jpg" alt="Autumn porch coloring page" loading="lazy"><figcaption>Fall &middot; autumn porch</figcaption></figure>
<figure><img src="{SITE}/img/book4_winter.jpg" alt="Hop the bunny ice skating coloring page" loading="lazy"><figcaption>Winter &middot; Hop goes ice skating</figcaption></figure>
<figure><img src="{SITE}/img/book4_xmas.jpg" alt="Gingerbread house coloring page" loading="lazy"><figcaption>Christmas &middot; gingerbread house</figcaption></figure>
</div>
<h2>Cozy, not fiddly</h2>
<div class="three">
<figure><img src="{SITE}/img/book4_cast.jpg" alt="Bramble the bear drinking cocoa" loading="lazy"><figcaption>Bramble drinks cocoa</figcaption></figure>
<figure><img src="{SITE}/img/book4_fire.jpg" alt="Fireplace with socks and slippers" loading="lazy"><figcaption>Fireplace, socks and slippers</figcaption></figure>
<figure><img src="{SITE}/img/book4_morning.jpg" alt="Christmas morning scene" loading="lazy"><figcaption>Christmas morning</figcaption></figure>
</div>
<h2>All 50 designs</h2>
<p style="color:var(--mut)">Every page in the book, in order.</p>
<img src="{SITE}/img/book4_overview.jpg" alt="Overview of all 50 designs in Fireside & Flurries" loading="lazy" style="width:100%;border-radius:16px;background:#fff;padding:8px">
<h2>Questions</h2>
{faq_html(gfaq)}
<h2>For the kids</h2>
<div class="shelf">{''.join(book_card(b) for b in BOOKS)}</div>
"""
page(f"{g['title']} | Hop Along Books", f"{g['sub']}. Bold lines, big spaces, no tiny details. One design per page, printed one side. {g['pages']} pages, {g['size']}. ${g['price']} on Amazon.", gbody, f"books/{g['slug']}.html", jsonld=[gld, faq_ld(gfaq)])

# ---------- blog ----------
POSTS = [
 ("can-a-3-year-old-do-color-by-number", "Can a 3-year-old do color by number?",
  "Yes, with the right pages. What 3-year-olds can usually manage, what to expect, how to help, and when to wait a little longer.",
  f"""
<p>Short answer: yes, many 3-year-olds can do color by number, as long as the page is simple and an adult helps at first. Here is what that looks like in practice.</p>
<h2>What a 3-year-old can usually manage</h2>
<p>At 3, many children are learning their first numbers (1, 2, 3) and the basic colors like red, blue and yellow. That makes pages with <b>2 or 3 colors</b> and <b>only the numbers 1 to 3</b> a good fit. Pages with 8 colors and numbers up to 10 are usually too much for now.</p>
<h2>What to expect</h2>
<ul><li><b>They will need help reading the key.</b> Point to the number and say "find all the 1s and color them red." After a few pages, many children start doing it on their own.</li>
<li><b>They will color outside the lines.</b> That's normal. Grip and control are still developing, and neatness isn't the goal at 3.</li>
<li><b>Short sessions.</b> One picture, or even half of one, is a good sitting. Stop while it's still fun.</li></ul>
<h2>How to pick pages that work</h2>
<ul><li>Big spaces: about an inch wide for the first pages</li>
<li>Few colors: 2 or 3 to start</li>
<li>A key with the color <b>name written out</b> next to a swatch, not just a dot (<a href="{SITE}/blog/why-color-names-matter-more-than-color-dots.html">why that matters</a>)</li>
<li>A picture they love: a truck, a cat, a dinosaur</li></ul>
<h2>Is it bad for creativity?</h2>
<p>Color by number is a structured activity: it practices numbers, color names, focus and crayon control. It doesn't replace free drawing, so keep blank paper around too. Mixing both is the easy answer.</p>
<h2>When to wait a little</h2>
<p>If your child gets upset by the rules ("but I want it purple!"), let them color it their way and try again in a few months. There is no rush, and every child moves at their own pace.</p>
<h2>Try it free</h2>
<p>Our Level 1 pages use only 3 colors and the numbers 1 to 3, with spaces about an inch wide. <a href="{SITE}/free.html">Print a free page</a> and see how your child does before you buy a book.</p>
"""),
 ("how-to-choose-a-color-by-number-book-for-a-3-year-old", "How to choose a color by number book for a 3-year-old",
  "Five things to check before you buy a color by number book for a toddler or preschooler - and the one mistake most books make.",
  f"""
<p>Most color by number books say "for kids" on the cover. Very few are made for a 3-year-old. Here is what to look at before you buy, based on what parents complain about most in Amazon reviews.</p>
<h2>1. How big are the spaces?</h2>
<p>This is the whole game. A 3-year-old holds a crayon in a fist and colors in big scribbles. If the spaces are the size of a fingernail, the picture will look like a mess and your child will give up. Look for spaces at least <b>half an inch wide</b>, and for the first pages, closer to <b>an inch</b>. If the listing doesn't say, zoom in on the sample pages.</p>
<h2>2. How many colors per picture?</h2>
<p>Three or four is right for a first book. Eight colors is a lot of switching for a small child. The best books start with 3 colors and build up, so the same book still works at 5.</p>
<h2>3. Does the color key have words, or just dots?</h2>
<p>Many books show only colored dots next to the numbers. A child who can't tell light blue from blue, or a parent who is color blind, gets stuck. Look for the <b>color name written out</b> next to each number: "1 - Red", "2 - Blue". <a href="{SITE}/blog/why-color-names-matter-more-than-color-dots.html">More on why this matters</a>.</p>
<h2>4. Are the colors ones you actually own?</h2>
<p>"Tan", "Apricot" and "Cerulean" are real crayon colors, but not in every box. Books that stick to Red, Blue, Yellow, Green, Orange, Brown and a few more work with any crayons in the house.</p>
<h2>5. What is on the back of each page?</h2>
<p>If pictures are printed on both sides, a marker will bleed through and ruin the picture behind it. One-sided printing fixes that. The best books put something useful on the back - a fact to read aloud, a place to test colors, a box to draw.</p>
<h2>The mistake most books make</h2>
<p>They print the age range on the cover without ever measuring the pages. "Ages 3-8" usually means "fine for 6, frustrating for 3." A book really made for 3-5 will tell you the number of colors per level and how big the spaces are.</p>
<p>That is how we make <a href="{SITE}/">Hop Along Books</a>: 5 levels from 3 to 8 colors, spaces measured on every page, color names on every key, one picture per page. <a href="{SITE}/#books">See the books</a>.</p>
"""),
 ("why-color-names-matter-more-than-color-dots", "Why color names matter more than color dots",
  "Color by number keys that show only colored dots leave young children and color-blind parents guessing. Here's why written color names work better.",
  f"""
<p>Open most color by number books and the key looks like this: a number, then a small colored dot. Simple enough for an adult. For a 3-year-old, it often isn't.</p>
<h2>Dots are hard to match</h2>
<p>A printed dot is tiny, flat and lit by whatever lamp is on. A crayon is waxy, thicker and a slightly different shade. Asking a child to hold a crayon up to a dot and decide "is this the same?" is a real task. Light blue vs blue, orange vs red-orange, brown vs dark orange - these trip up small children constantly.</p>
<h2>Words remove the guessing</h2>
<p>When the key says <b>"2 - Blue"</b>, a child who knows the word blue (most 3-year-olds do) can pick the blue crayon, and a parent can say "find the blue one" without pointing. The crayon's own label says Blue too. Everything matches.</p>
<h2>It also helps color-blind parents</h2>
<p>About 1 in 12 men has some form of color blindness. A key with dots only is useless to them when their child asks for help. A key with names works for everyone.</p>
<h2>And it teaches color words</h2>
<p>Every page becomes a little lesson: the number, the swatch and the word, side by side. Children who color this way learn color names faster, because they read and use the word every time.</p>
<h2>What to look for</h2>
<p>A key that shows <b>number + swatch + name</b>, and uses everyday color names that match the crayons you own. If a book uses an unusual shade, it should tell you what to use instead ("Sky Blue - any light blue crayon").</p>
<p>Every <a href="{SITE}/">Hop Along</a> book is made this way. <a href="{SITE}/#books">See the books</a>.</p>
"""),
 ("markers-vs-crayons-for-toddler-coloring-books", "Markers vs crayons for toddler coloring books",
  "Markers bleed through thin paper and ruin the next page. Here's what works best for ages 3-5 and how to choose a book that survives markers.",
  f"""
<p>The most common one-star review of children's coloring books is some version of "the marker bled through and ruined the next picture." Here's what is going on and what to do about it.</p>
<h2>Why it happens</h2>
<p>Print-on-demand paperbacks (which is most coloring books on Amazon now) use fairly thin paper. Markers, especially washable kids' markers, soak through. Crayons and colored pencils sit on top of the paper and don't.</p>
<h2>Crayons: the best choice for 3-5</h2>
<p>Thick crayons are easiest for small hands to grip, they don't bleed, and a 3-year-old can press hard without tearing the page. For a first color by number book, crayons win.</p>
<h2>Colored pencils: good for 4-5</h2>
<p>Finer control, no bleed, but they need a bit more hand strength. Nice for the harder levels.</p>
<h2>Markers: fun, but check the book first</h2>
<p>Kids love markers. If yours insists, pick a book where <b>pictures are printed on one side only</b>, so bleed-through lands on a blank or activity page instead of the next picture. Slip a sheet of scrap paper behind the page as well.</p>
<h2>What to look for in a book</h2>
<ul><li>One picture per page, one-sided printing</li><li>Something useful on the back of each picture (so the page isn't wasted)</li><li>Thick, clear outlines that are easy to see even if a marker spreads a little</li></ul>
<p><a href="{SITE}/">Hop Along</a> books are printed one picture per page; the back of each picture is an activity page with a fact, a color test strip and a drawing box. <a href="{SITE}/#books">See the books</a>.</p>
"""),
 ("quiet-activities-for-a-3-year-old-on-a-plane-or-car-ride", "Quiet activities for a 3-year-old on a plane or car ride",
  "What to pack to keep a 3-year-old busy on a flight or long drive without a screen: coloring, stickers, small toys, and a few tricks that make them last longer.",
  f"""
<p>A long flight or drive with a 3-year-old goes better with a small bag of things to do. Here is what tends to work, and a few tricks that make each activity last longer.</p>
<h2>Pack several small things, not one big thing</h2>
<p>Attention spans at 3 are short. Five activities that each hold attention for ten minutes beat one that is supposed to last an hour. Bring them out one at a time and put each away before the next comes out.</p>
<h2>Coloring that works on a tray table</h2>
<ul><li><b>Crayons, not markers.</b> No caps to lose, no stains on the seat, no bleed-through.</li>
<li><b>Fewer crayons.</b> A small pouch with the 6 to 10 colors the page needs is easier than a full box that spills.</li>
<li><b>Big, simple pictures.</b> Bumpy roads and small tray tables make fine coloring hard. Pages with big spaces and only a few colors are easier to finish on the move.</li>
<li><b>Tear out a page or two before you leave</b> so a whole book isn't sliding around.</li></ul>
<h2>Other quiet favorites</h2>
<ul><li><b>Sticker books</b> and reusable sticker scenes</li>
<li><b>A few small, new toys</b> wrapped in paper, opened one at a time</li>
<li><b>Picture books</b> to read together, or look-and-find books</li>
<li><b>Snacks in a container with several small compartments</b>, which doubles as an activity</li></ul>
<h2>Games that need nothing</h2>
<p>I spy with colors ("I spy something blue"), counting cars or clouds, and guessing animal sounds. These are good for the last half hour, when everything in the bag has been used.</p>
<h2>Keep one thing in reserve</h2>
<p>Save one new activity for the hardest moment: the delay, the descent, or the last stretch of the drive.</p>
<p><a href="{SITE}/">Hop Along</a> books are made for this: big spaces, 3 to 8 colors, one picture per page. <a href="{SITE}/free.html">Print a free page</a> to try before your trip.</p>
"""),
 ("how-to-help-a-3-year-old-hold-a-crayon", "How to help a 3-year-old hold a crayon",
  "Many 3-year-olds hold a crayon in their fist. That is a normal stage. Simple ways to build hand strength and a better grip through play, without forcing it.",
  f"""
<p>If your 3-year-old grabs a crayon in their whole fist, that is very common. Grips change gradually as small hand muscles get stronger, and many children are still working toward holding a crayon between thumb and fingers well into the preschool years.</p>
<h2>Don't force the grip</h2>
<p>Correcting the grip every few seconds makes coloring a chore. A child who enjoys coloring will color more, and practice is what changes the grip. Show, don't push.</p>
<h2>Use shorter, thicker crayons</h2>
<p>Short pieces of crayon are hard to hold in a fist, so small hands naturally switch to the fingertips. Breaking a few crayons in half is an easy trick. Chunky or triangular crayons are also easier to grip.</p>
<h2>Give them big spaces first</h2>
<p>When the space to color is tiny, a child grips harder and gets frustrated. Big shapes let them make big arm movements and still stay mostly inside the lines. That success keeps them coming back.</p>
<h2>Build hand strength through play</h2>
<ul><li>Play dough: rolling, squeezing and pinching</li>
<li>Peeling and placing stickers</li>
<li>Tearing paper into small pieces</li>
<li>Picking up small objects with fingers or tongs</li>
<li>Coloring on a vertical surface, like paper taped to a wall or an easel</li></ul>
<h2>When to ask for advice</h2>
<p>Every child moves at their own pace. If you are worried about your child's hand use or fine motor skills, talk to your pediatrician or your child's teacher.</p>
<p><a href="{SITE}/">Hop Along</a> books start with Level 1 pictures that have only 3 colors and spaces about an inch wide. <a href="{SITE}/free.html">Try a free page</a>.</p>
"""),
]
idx = "<h1>Guides for parents</h1><p class='lead'>Short, practical guides on choosing and using coloring books with 3-5 year olds.</p><ul>"
for slug, title, desc, body in POSTS:
    ld = {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"author":{"@type":"Organization","name":PUB},"publisher":{"@type":"Organization","name":PUB},"datePublished":TODAY,"url":f"{SITE}/blog/{slug}.html"}
    page(f"{title} | Hop Along Books", desc, f"<article class='post'><h1>{title}</h1><p style='color:var(--mut)'>Hop Along Books &middot; {TODAY}</p>{body}</article>", f"blog/{slug}.html", jsonld=ld)
    idx += f"<li><a href='{SITE}/blog/{slug}.html'>{title}</a><br><span style='color:var(--mut)'>{desc}</span></li>"
idx += "</ul>"
page("Guides for parents | Hop Along Books", "Practical guides on choosing and using color by number books with children ages 3-5.", idx, "blog/index.html")

# ---------- about ----------
page("About Hop Along Books", "Hop Along Books makes color by number books for ages 3-5, measured page by page so small hands can finish them.", f"""
<h1>About Hop Along Books</h1>
<p class="lead">We make color by number books for children ages 3-5 - and we measure every page.</p>
<p>Most coloring books put an age range on the cover and hope. We started Hop Along Books because the books we found for 3-year-olds had spaces too small, too many colors, and keys that showed only dots.</p>
<p>So every Hop Along book follows the same rules:</p>
<ul>
<li><b>5 levels, easy to harder</b> - from 3 colors and inch-wide shapes up to 8-color scenes.</li>
<li><b>Every space is measured.</b> Level 1 spaces are about an inch wide; even Level 5 keeps every space about half an inch or bigger.</li>
<li><b>Color names on every key</b>, in everyday colors you already own.</li>
<li><b>One picture per page</b>, with a fact, a color test strip, a feelings face and a drawing box on the back.</li>
<li><b>Answer pictures at the back</b>, and a small color example on every page.</li>
</ul>
<p>The books are published through Amazon KDP and printed on demand. Line art and text are produced with AI tools and checked by hand, page by page.</p>
<p>Questions? Write to <a href="mailto:purevibe88@gmail.com">purevibe88@gmail.com</a>.</p>
<h2>The books</h2><div class="shelf">{''.join(book_card(b) for b in BOOKS)}</div>
""", "about.html")


# ---------- topic pages ----------
for t in TOPICS:
    bs=[b for b in BOOKS if b["topic"]==t["slug"]]
    page(f"{t['name']} Color by Number Books for Kids | Hop Along Books", f"{t['name']} color by number books for ages 3-5: {t['blurb']} Big shapes and color names on every key.",
         f"""<div style="background:{t['color']};border-radius:28px;padding:30px;margin-top:28px"><h1>{t['name']}</h1><p style="font-size:19px;margin:10px 0 0">{t['blurb']}</p></div>
<h2>Books</h2><div class="shelf">{''.join(book_card(b) for b in bs)}</div>
<h2>Other topics</h2><div class="topics">{''.join(f'<a class="topic" style="background:{o["color"]}" href="{SITE}/topics/{o["slug"]}.html"><img src="{SITE}/img/{o["img"]}" alt=""><h3>{o["name"]}</h3><p>{o["blurb"]}</p></a>' for o in TOPICS if o["slug"]!=t["slug"])}</div>""",
         f"topics/{t['slug']}.html")
# ---------- age pages ----------
for g in [x for x in AGES if x["live"]]:
    bs=[b for b in BOOKS if b["age"]==g["slug"]]
    page(f"Color by Number Books for {g['name']} | Hop Along Books", f"Color by number books for kids {g['name'].lower()}: {g['blurb']}",
         f"""<div style="background:var(--butter);border-radius:28px;padding:30px;margin-top:28px"><h1>{g['name']}</h1><p style="font-size:19px;margin:10px 0 0">{g['blurb']} Five levels in every book, so the same book still works at 5.</p></div>
<h2>Books</h2><div class="shelf">{''.join(book_card(b) for b in bs)}</div>""", f"ages/{g['slug']}.html")
# ---------- free page ----------
# Email gate. Leave None until the email service form exists; then set e.g.
# GATE = dict(action="https://app.kit.com/forms/XXXX/subscriptions", field="email_address")
GATE = dict(action="https://docs.google.com/forms/d/e/1FAIpQLSdFdQJOMdebMGkeHOC5z1wK7ttsjFmdx__mjwwPk-WPauX6xw/formResponse", field="entry.19342081", page="entry.156612593")
bymap={b["slug"]:b for b in BOOKS}
def fcard(f):
    b=bymap[f["book"]]; pdf=f"{SITE}/free/hop-along-free-page-{f['slug']}.pdf"
    btn=(f'<a class="btn" href="{pdf}" download>Download free PDF</a>' if not GATE else
         f'<a class="btn gated" href="#signup" data-pdf="{pdf}">Get this page free</a>')
    return f"""<article class="fcard" style="--c:{b['color']}"><div class="top"><span class="pill">{f['level']}</span>
<img class="art" src="{SITE}/img/free_{f['slug']}.jpg" alt="{f['name']} color by number picture" loading="lazy"></div>
<h3>{f['name']}</h3><p class="from">From <a href="{SITE}/books/{b['slug']}.html">{b['short']}</a></p>
<div class="inside"><b>What you'll print</b><div class="pair">
<figure><img src="{SITE}/img/free_{f['slug']}_page.jpg" alt="Page 1: {f['name']} numbered page with color key" loading="lazy"><span>1. Page to color</span></figure>
<figure><img src="{SITE}/img/free_{f['slug']}_answer.jpg" alt="Page 2: {f['name']} answer picture" loading="lazy"><span>2. Answer picture</span></figure></div></div>
<div class="go">{btn}</div></article>"""
signup = "" if not GATE else f"""<section class="signup" id="signup"><div><h2>Get all 3 pages free</h2><p>Enter your email and the download buttons unlock right away. Now and then we'll send new free pages and news about new books.</p></div>
<div><form id="gate" action="{GATE['action']}" method="post"><input type="hidden" name="{GATE['page']}" id="gpage" value="all"><input type="email" name="{GATE['field']}" required placeholder="Your email" aria-label="Your email"><button class="btn" type="submit">Unlock pages</button>
<small>No spam. Unsubscribe any time with one click.</small></form><p class="ok">Thank you! Your pages are unlocked below.</p></div></section>
<script>document.addEventListener("DOMContentLoaded",function(){{var K="hab_free_ok",sec=document.getElementById("signup"),f=document.getElementById("gate");
function open(){{sec.classList.add("done");document.querySelectorAll("a.gated").forEach(function(a){{a.href=a.dataset.pdf;a.setAttribute("download","");a.textContent="Download free PDF";a.classList.remove("gated")}})}}
try{{if(localStorage.getItem(K))open()}}catch(e){{}}
document.querySelectorAll("a.gated").forEach(function(a){{a.addEventListener("click",function(){{document.getElementById("gpage").value=a.dataset.pdf.split("free-page-")[1].replace(".pdf","")}})}});
f.addEventListener("submit",function(e){{e.preventDefault();fetch(f.action,{{method:"POST",mode:"no-cors",body:new FormData(f)}}).finally(function(){{try{{localStorage.setItem(K,"1")}}catch(e){{}}open()}})}});}});</script>"""
steps = ("<li>Enter your email</li><li>Download and print</li><li>Color, then check the answer</li>" if GATE else
         "<li>Download and print</li><li>Grab the crayons</li><li>Color, then check the answer</li>")
page("Free Printable Color by Number for 3 Year Olds (PDF) | Hop Along Books", "Free printable color by number pages for 3, 4 and 5 year olds. Big shapes, 3 to 4 colors, color names on the key, answer picture included. PDF, print at home.",
     f"""<div style="background:var(--butter);border-radius:28px;padding:30px;margin-top:28px"><h1>Free printable color by number for 3 year olds</h1><p style="font-size:19px;margin:10px 0 0;max-width:36em">Real pages from our books for ages 3-5, each a PDF with its answer picture. Big shapes, only 3 or 4 colors, and the color names written on the key. Print on regular paper and see if the level is right for your child.</p>
<ol class="steps">{steps}</ol></div>{signup}
<h2>Pick a page</h2><div class="freebie">{''.join(fcard(f) for f in FREE)}</div>
<p style="margin-top:30px;color:var(--mut)">Free for personal and classroom use. Please don't resell.</p>
<div style="background:var(--butter);border-radius:28px;padding:26px;margin-top:36px"><h2 style="margin:0 0 8px">For grown-ups: 20 free cozy Christmas pages</h2><p style="margin:0 0 14px">Bold lines, big spaces, from <i>Fireside &amp; Flurries</i>. No sign-up needed.</p><a class="btn" href="{SITE}/xmas/">See the Christmas pages</a></div>""", "free.html")

# sitemap + robots
urls = [SITE+"/", SITE+"/about.html", SITE+"/blog/", SITE+"/free.html"] + [f"{SITE}/topics/{t['slug']}.html" for t in TOPICS] + [f"{SITE}/ages/{g['slug']}.html" for g in AGES if g["live"]] + [f"{SITE}/books/{b['slug']}.html" for b in BOOKS] + [f"{SITE}/books/{GROWNUP['slug']}.html"] + [f"{SITE}/blog/{p[0]}.html" for p in POSTS]
open(os.path.join(ROOT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)+"</urlset>")
llms = f"""# Hop Along Books

> Hop Along Books publishes color by number activity books for children ages 3 to 5, plus a bold-and-easy coloring book for grown-ups, sold as paperbacks on Amazon. Every book has 45 pictures in 5 levels (3 to 8 colors), a color key with the number, a swatch and the color name written out, spaces measured for small hands (about 1 inch at Level 1, at least about half an inch at Level 5), and one picture per page with an activity page on the back.

## Books
""" + "".join(f"- [{b['title']}]({SITE}/books/{b['slug']}.html): {b['sub']}. 102 pages, 8.5 x 11 in, $10.99." + "\n" for b in BOOKS) + f"""
## For grown-ups
- [{GROWNUP['title']}]({SITE}/books/{GROWNUP['slug']}.html): {GROWNUP['sub']}. Bold and easy, no numbers or color key. {GROWNUP['pages']} pages, {GROWNUP['size']}, ${GROWNUP['price']}.

## Key facts
- Age: 3-5 (preschool and kindergarten)
- Colors: everyday colors such as Red, Blue, Yellow, Green, Orange, Brown and Pink, each named in the key; for Sky Blue any light blue crayon works
- Printing: one picture per page, one-sided; markers won't ruin the next picture
- Back of each picture: a read-aloud fact, a color test strip, a "How did you feel?" face, a drawing box
- Answer pictures at the back of every book

## Free resources
- [Free printable pages]({SITE}/free.html): one real page from each book with its answer picture

## Guides for parents
""" + "".join(f"- [{t}]({SITE}/blog/{sl}.html): {d}" + "\n" for sl,t,d,_ in POSTS) + f"""
## Contact
- [About]({SITE}/about.html) - purevibe88@gmail.com
"""
open(os.path.join(ROOT,"llms.txt"),"w").write(llms)
open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(ROOT,".nojekyll"),"w").write("")

# ---------- free Christmas/cozy pages from Book 4 (Pinterest landing pages) ----------
import re as _re
XM = json.load(open(os.path.join(ROOT, "xmas.json")))   # [{slug,title,label,desc,alt}]
XCSS = """<style>.xp{display:grid;grid-template-columns:1.1fr .9fr;gap:32px;margin-top:28px;align-items:start}
.xp .sheet{background:#fff;border-radius:24px;padding:18px;box-shadow:0 8px 0 var(--line)}.xp .sheet img{display:block;width:100%;height:auto}
.xp .side h1{font-size:clamp(28px,4vw,42px)}.xp .side p{font-size:18px}.xp .btn{margin:6px 0 10px}
.xbook{display:flex;gap:16px;align-items:center;background:var(--butter);border-radius:22px;padding:18px;margin-top:22px}.xbook img{width:110px;border-radius:10px;background:#fff}
.xgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:16px;margin-top:16px}.xgrid a{background:#fff;border-radius:16px;padding:10px;text-decoration:none;font-size:14px;font-weight:700;box-shadow:0 5px 0 var(--line)}.xgrid img{width:100%;aspect-ratio:1;object-fit:contain;display:block;margin-bottom:6px}
@media(max-width:760px){.xp{grid-template-columns:1fr}}</style>"""
G = GROWNUP
def xbook():
    return f'<div class="xbook"><img src="{SITE}/img/book4_cover.jpg" alt="{G["short"]} coloring book cover" loading="lazy"><div><b>Like this page? There are 50 more.</b><p style="margin:4px 0 10px;font-size:16px">This page is from <i>{G["short"]}</i>, a cozy coloring book with 50 fall, winter and Christmas scenes, bold lines and big spaces. {G["size"]}, ${G["price"]} paperback.</p><a class="btn" href="{G["amazon"]}" rel="nofollow">See the book on Amazon</a></div></div>'
def xcard(x): return f'<a href="{SITE}/xmas/{x["slug"]}.html"><img src="{SITE}/img/xmas/{x["slug"]}.jpg" alt="{x["alt"]}" loading="lazy">{x["label"]}</a>'
for i, x in enumerate(XM):
    FR = [m for m in XM if m['free']]
    more = [m for m in FR if m is not x][i % 4:][:5]
    if x['free']:
        act = f"""<a class="btn" href="{SITE}/free/xmas/{x['slug']}.pdf" download>Download free PDF</a>
<p style="font-size:15px;color:var(--mut)">US Letter, prints on regular paper. Free for personal use, please don't resell.</p>"""
    else:
        act = f"""<p style="font-size:16px;background:#fff;border-radius:14px;padding:12px 14px">This page is one of the 50 in the book. Want to try one first? <a href="{SITE}/xmas/{more[0]['slug']}.html">Print a free page here</a>.</p>"""
    body = f"""{XCSS}<div class="xp"><div class="sheet"><img src="{SITE}/img/xmas/{x['slug']}.jpg" alt="{x['alt']}" width="900" height="900"></div>
<div class="side"><h1>{x['title']}</h1><p>{x['desc']}</p>{act}{xbook()}</div></div>
<h2>More free cozy coloring pages</h2><div class="xgrid">{''.join(xcard(m) for m in more)}</div>
<p style="margin-top:24px"><a href="{SITE}/xmas/">See all free Christmas coloring pages</a></p>"""
    page(f"{x['title']} | Hop Along Books", x['desc'][:155], body, f"xmas/{x['slug']}.html")
page("Free Christmas Coloring Pages for Adults: Cozy, Easy, Printable | Hop Along Books",
     "Free printable Christmas and cozy winter coloring pages for adults and kids. Easy bold lines, big spaces. Download the PDF and print at home.",
     f"""{XCSS}<div style="background:var(--butter);border-radius:28px;padding:30px;margin-top:28px"><h1>Free cozy Christmas coloring pages</h1><p style="font-size:19px;margin:10px 0 0;max-width:36em">Easy, relaxing pages with bold lines and big spaces, for grown-ups and kids. 20 free pages: tap one, download the PDF, print at home.</p></div>
<div class="xgrid">{''.join(xcard(x) for x in XM if x['free'])}</div>{xbook()}""", "xmas/index.html")
urls += [f"{SITE}/xmas/"] + [f"{SITE}/xmas/{x['slug']}.html" for x in XM]
open(os.path.join(ROOT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)+"</urlset>")

print("built", len(urls), "pages")
