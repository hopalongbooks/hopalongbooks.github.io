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
      amazon="https://www.amazon.com/s?k=Trucks+Trains+Rockets+Things+That+Go+Hop+Along+Books",
      isbn="", status="Published October 2026",
      blurb="45 big, friendly vehicles: cars, fire trucks, diggers, school buses, trains, boats, planes and rockets, plus busy scenes like the airport and the construction site.",
      inside="cars, trucks, diggers, trains, rockets, boats, planes, buses, space and construction scenes",
      levels=["Car", "Steam Train", "Construction Site"], sample="Fire Truck", fact="a read-aloud vehicle fact"),
 dict(slug="cute-animals", key="book2", topic="animals", age="3-5", color="#1CAC78",
      title="Cute Animals Color by Number for Kids Ages 3-5",
      short="Cute Animals",
      sub="Pets, Farm, Zoo & Dinosaurs",
      amazon="https://www.amazon.com/s?k=Cute+Animals+Color+by+Number+Hop+Along+Books",
      isbn="9798160782225", status="Published October 2026",
      blurb="45 big, friendly animals: cats, dogs, ducks, lions, elephants, penguins, dolphins, dinosaurs and busy scenes like the farm, the jungle and under the sea.",
      inside="pets, farm animals, zoo animals, sea creatures, dinosaurs and big scenes",
      levels=["Cat", "Lion", "Farm"], sample="Elephant", fact="a read-aloud animal fact"),
 dict(slug="dinosaurs", key="book3", topic="dinosaurs", age="3-5", color="#6A4BB0",
      title="Dinosaurs Color by Number for Kids Ages 3-5",
      short="Dinosaurs",
      sub="A Day in the Life of Silly Dinos",
      amazon="https://www.amazon.com/s?k=Dinosaurs+Color+by+Number+Silly+Dinos+Hop+Along+Books",
      isbn="", status="Coming October 2026",
      blurb="45 pictures starring 8 dino friends - T-Rex, Triceratops, Stegosaurus, Brachiosaurus, Ankylosaurus, Parasaurolophus, Pteranodon and Baby Dino - brushing their teeth, baking cakes, driving trucks and flying rockets.",
      inside="8 recurring dinosaur characters in everyday life, jobs, vehicles and big scenes",
      levels=["T-Rex Eats an Apple", "Brachiosaurus Pulls a Carrot", "A Dinosaur Birthday Party"], sample="T-Rex Brushes His Teeth", fact="a read-aloud dinosaur fact"),
]

TOPICS = [
 dict(slug="things-that-go", name="Things That Go", blurb="Trucks, trains, diggers, boats and rockets.", color="#7FD3F0", img="hero_truck.jpg"),
 dict(slug="animals", name="Animals", blurb="Pets, farm friends, zoo animals and sea creatures.", color="#5BC98A", img="hero_cat.jpg"),
 dict(slug="dinosaurs", name="Dinosaurs", blurb="Silly dinos brushing teeth, baking cakes and driving trucks.", color="#C7B6F2", img="hero_trex.jpg"),
]
SOON = ["Ocean", "Space", "Holidays", "Bugs & Garden"]
AGES = [dict(slug="3-5", name="Ages 3-5", blurb="Big shapes, 3 to 8 colors, color names on every key.", live=True),
        dict(slug="5-7", name="Ages 5-7", blurb="Smaller spaces and more colors.", live=False)]
FREE = [dict(slug="trex-apple", name="T-Rex Eats an Apple", book="dinosaurs", level="Level 1, 3 colors"),
        dict(slug="cat", name="Cat", book="cute-animals", level="Level 1, 3 colors"),
        dict(slug="fire-truck", name="Fire Truck", book="trucks-trains-rockets", level="Level 2, 4 colors")]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap');
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
.post{max-width:680px}.post p,.post li{font-size:18px}.post h2{font-size:26px;margin-top:40px}
.newsletter{background:var(--butter);border-radius:24px;padding:28px;margin-top:70px}
footer{margin-top:70px;padding:30px 0;color:var(--mut);font-size:15px;border-top:2px dashed var(--line)}
@media(max-width:720px){.hero .wrap{grid-template-columns:1fr;padding-bottom:40px}.hero img{transform:none}.promise,.promise:nth-child(even){grid-template-columns:1fr;direction:ltr}.three{grid-template-columns:1fr 1fr}nav a{margin-left:10px;font-size:14px;white-space:nowrap}nav a[href$="about.html"],nav a[href$="/blog/"]{display:none}.topics{grid-template-columns:1fr 1fr;gap:12px}.topic{padding:10px 10px 14px;border-radius:18px}.topic p{display:none}.topic h3{font-size:17px;margin-top:8px}header .wrap{height:60px}.brand{font-size:19px;white-space:nowrap}.brand i{width:26px;height:26px}}
@media(prefers-reduced-motion:reduce){.book img{transition:none}html{scroll-behavior:auto}}
"""

def page(title, desc, body, path, jsonld=None, canonical=None):
    can = canonical or f"{SITE}/{path}"
    ld = f'<script type="application/ld+json">{json.dumps(jsonld)}</script>' if jsonld else ""
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{can}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:image" content="{SITE}/img/hero_group.png"><meta property="og:url" content="{can}">
<style>{CSS}</style>{ld}</head><body>
<header><div class="wrap"><a class="brand" href="{SITE}/"><i></i>Hop Along Books</a><nav><a href="{SITE}/#topics">Books</a><a href="{SITE}/free.html">Free pages</a><a href="{SITE}/blog/">Guides</a><a href="{SITE}/about.html">About</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap">&copy; 2026 Hop Along Books. Color by number books for ages 3-5. Available on Amazon. &middot; <a href="{SITE}/about.html">About</a> &middot; <a href="{SITE}/blog/">Guides for parents</a></div></footer>
</body></html>"""
    full = os.path.join(ROOT, path); os.makedirs(os.path.dirname(full), exist_ok=True); open(full, "w").write(html)

def book_card(b):
    return f"""<a class="book" href="{SITE}/books/{b['slug']}.html"><img src="{SITE}/img/{b['key']}_cover.jpg" alt="{b['title']} cover">
<h3>{b['short']}</h3><p>{b['sub']}</p><span class="tag">{b['status']}</span></a>"""

# ---------- home ----------
def topic_count(t): 
    n=len([b for b in BOOKS if b["topic"]==t["slug"]]); return f"{n} book" + ("" if n==1 else "s")
home_body = f"""
<div class="hero" style="margin:0 -20px"><div class="wrap">
<div><h1>Coloring books little hands can actually finish</h1>
<p>Big shapes, color names written on every page, and pictures that still look like a fire truck or a kitten when they're done. Every page is measured for the age on the cover.</p>
<a class="btn" href="#topics">Find a book</a> <a class="btn soft" href="{SITE}/free.html" style="margin-left:8px">Free pages to print</a></div>
<img class="hero-art" src="{SITE}/img/hero_group.png" alt="Finished pages from Hop Along books: a T-Rex, a fire truck, a cat, a rocket, a penguin and a baby dinosaur">
</div><svg class="wave" viewBox="0 0 1200 40" preserveAspectRatio="none" aria-hidden="true"><path d="M0,20 C150,45 300,-5 450,20 C600,45 750,-5 900,20 C1050,45 1150,0 1200,20 L1200,40 L0,40 Z" fill="#FFF8EC"/></svg></div>

<h2 id="topics">What does your kid love?</h2>
<div class="topics">{''.join(f'<a class="topic" style="background:{t["color"]}" href="{SITE}/topics/{t["slug"]}.html"><img src="{SITE}/img/{t["img"]}" alt=""><h3>{t["name"]}</h3><p>{t["blurb"]}</p><span class="count">{topic_count(t)}</span></a>' for t in TOPICS)}</div>
<div class="soon" aria-label="Coming soon">{''.join(f'<span>{x} &middot; coming soon</span>' for x in SOON)}</div>

<h2>How old is your little one?</h2>
<div class="ages">{''.join((f'<a class="age" href="{SITE}/ages/{g["slug"]}.html"><b>{g["name"]}</b>{g["blurb"]}</a>' if g["live"] else f'<div class="age off"><b>{g["name"]}</b>{g["blurb"]} Coming next.</div>') for g in AGES)}</div>

<h2>Why moms keep these in the car</h2>
<div class="promise"><img src="{SITE}/img/book3_B3_key.jpg" alt="Color key with the color name next to each number"><div><h3>They can read the key on their own</h3><p>Every number has a swatch and the color's name - Red, Blue, Green. No squinting at a tiny dot, and no shades you don't own. For Sky Blue, any light blue crayon works.</p></div></div>
<div class="promise"><img src="{SITE}/img/hero_trex.jpg" alt="Level 1 page: a T-Rex with three big areas to color"><div><h3>Big enough for a fist full of crayon</h3><p>Level 1 spaces are about an inch wide. Even the busiest Level 5 scene keeps every space around half an inch. We measure every page so small hands stay inside the lines without help.</p></div></div>
<div class="promise"><img src="{SITE}/img/book3_B2_back.jpg" alt="The activity page behind each picture"><div><h3>Flip it over, there's more</h3><p>Pictures are printed on one side, so markers can't ruin the next one. Behind each picture: a fact to read aloud, a strip to test colors, a face to circle, and a box to draw their own.</p></div></div>

<div class="band"><div><h2>Try a page tonight, free</h2><p>Print a real page from each book, with its answer picture. See if the level is right before you buy.</p><a class="btn" href="{SITE}/free.html">Print free pages</a></div><img src="{SITE}/img/free_cat.jpg" alt="Free printable page: a cat to color by number"></div>

<h2>All books</h2>
<div class="shelf">{''.join(book_card(b) for b in BOOKS)}</div>

<h2>For parents</h2>
<div class="guides">
<a class="guide" href="{SITE}/blog/how-to-choose-a-color-by-number-book-for-a-3-year-old.html"><h3>How to choose a color by number book for a 3-year-old</h3><p>Five things to check before you buy, and the mistake most books make.</p></a>
<a class="guide" href="{SITE}/blog/why-color-names-matter-more-than-color-dots.html"><h3>Why color names beat color dots</h3><p>Dots are hard to match. Words aren't.</p></a>
<a class="guide" href="{SITE}/blog/markers-vs-crayons-for-toddler-coloring-books.html"><h3>Markers or crayons?</h3><p>What works at 3, at 5, and how to stop bleed-through.</p></a>
</div>
"""
page("Hop Along Books - Color by Number for Kids Ages 3-5", "Color by number books made for ages 3-5: big shapes, color names on every key, one picture per page, a fun activity page behind each. Trucks, animals and dinosaurs. On Amazon.", home_body, "index.html",
     jsonld={"@context":"https://schema.org","@type":"Organization","name":PUB,"url":SITE+"/","description":"Publisher of color by number books for children ages 3-5."}, canonical=SITE+"/")

# ---------- book pages ----------
for b in BOOKS:
    k = b["key"]
    ld = {"@context":"https://schema.org","@type":"Book","name":b["title"],"alternativeHeadline":b["sub"],"author":{"@type":"Organization","name":PUB},"publisher":{"@type":"Organization","name":PUB},
          "bookFormat":"https://schema.org/Paperback","numberOfPages":102,"inLanguage":"en","typicalAgeRange":"3-5","genre":"Children's activity book, color by number",
          "image":f"{SITE}/img/{k}_cover.jpg","url":f"{SITE}/books/{b['slug']}.html","offers":{"@type":"Offer","url":b["amazon"],"priceCurrency":"USD","price":"10.99","availability":"https://schema.org/InStock"}}
    if b["isbn"]: ld["isbn"] = b["isbn"]
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
<tr><th>Color key</th><td>Number + color swatch + color name written out. Everyday colors only (Red, Blue, Yellow, Green, Orange, Brown, Violet, Gray, Pink, Sky Blue = any light blue).</td></tr>
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
<h2>More from Hop Along Books</h2>
<div class="shelf">{''.join(book_card(o) for o in BOOKS if o['key']!=k)}</div>
"""
    page(f"{b['title']} | Hop Along Books", f"{b['sub']}. 45 pictures in 5 levels for ages 3-5, color names on every key, one picture per page. 102 pages, 8.5 x 11 in.", body, f"books/{b['slug']}.html", jsonld=ld)

# ---------- blog ----------
POSTS = [
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
page("Free Color by Number Pages to Print | Hop Along Books", "Print free color by number pages for ages 3-5, each with its answer picture. Real pages from Hop Along books.",
     f"""<div style="background:var(--butter);border-radius:28px;padding:30px;margin-top:28px"><h1>Free pages to print</h1><p style="font-size:19px;margin:10px 0 0;max-width:36em">One real page from each book, plus its answer picture. Print on regular paper and see if the level is right for your child before you buy.</p>
<ol class="steps">{steps}</ol></div>{signup}
<h2>Pick a page</h2><div class="freebie">{''.join(fcard(f) for f in FREE)}</div>
<p style="margin-top:30px;color:var(--mut)">Free for personal and classroom use. Please don't resell.</p>""", "free.html")

# sitemap + robots
urls = [SITE+"/", SITE+"/about.html", SITE+"/blog/", SITE+"/free.html"] + [f"{SITE}/topics/{t['slug']}.html" for t in TOPICS] + [f"{SITE}/ages/{g['slug']}.html" for g in AGES if g["live"]] + [f"{SITE}/books/{b['slug']}.html" for b in BOOKS] + [f"{SITE}/blog/{p[0]}.html" for p in POSTS]
open(os.path.join(ROOT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)+"</urlset>")
open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(ROOT,".nojekyll"),"w").write("")
print("built", len(urls), "pages")
