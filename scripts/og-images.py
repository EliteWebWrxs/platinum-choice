"""
Generates the social share cards (Open Graph / Twitter) in static/images/og/.

Run from the project root after changing card copy, certifications or photos:
    python3 scripts/og-images.py

Needs Pillow (pip install pillow) and the fontsource packages from node_modules.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / 'static/images'
OUT = IMAGES / 'og'
FONTS = ROOT / 'node_modules/@fontsource-variable'

W, H = 1200, 630
BAR = 10

# Palette, matching src/app.css
PAPER = (251, 247, 241)
PAPER_DEEP = (243, 235, 223)
INK = (29, 22, 19)
INK_MUTED = (110, 97, 90)
LINE = (230, 218, 203)
GOLD = (247, 181, 43)
FLAME_DARK = (194, 65, 12)
BRAND = [(0, (232, 67, 47)), (0.35, (240, 90, 40)), (0.7, (247, 181, 43)), (1, (214, 36, 110))]
BRAND_TEXT = [(0, (232, 67, 47)), (0.4, (240, 90, 40)), (1, (247, 181, 43))]

CERTS = ['Woman-owned', 'Minority-owned', 'HUBZone', 'WOSB']
DOMAIN = 'platinumchoice.consulting'


def font(family, size, weight=400, italic=False):
    name = {
        'serif': f"eb-garamond/files/eb-garamond-latin-wght-{'italic' if italic else 'normal'}.woff2",
        'sans': 'hanken-grotesk/files/hanken-grotesk-latin-wght-normal.woff2'
    }[family]
    f = ImageFont.truetype(str(FONTS / name), size)
    f.set_variation_by_axes([weight])
    return f


def lerp(stops, t):
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if t <= t1:
            k = (t - t0) / (t1 - t0) if t1 > t0 else 0
            return tuple(round(a + (b - a) * k) for a, b in zip(c0, c1))
    return stops[-1][1]


def gradient(size, stops):
    """Left-to-right gradient, slightly tilted like the CSS 100deg one"""
    w, h = size
    row = Image.new('RGB', (w, 1))
    row.putdata([lerp(stops, x / max(w - 1, 1)) for x in range(w)])
    return row.resize((w, h))


def rng(s):
    def next_():
        nonlocal s
        s = (s * 16807) % 2147483647
        return (s - 1) / 2147483646

    return next_


def facets(size, seed, cols, rows, line_alpha, fill_alpha):
    """Port of Facets.svelte: a seeded low-poly mesh in the brand gradient"""
    w, h = size
    rand = rng(seed)
    cw, ch = w / cols, h / rows
    pts = []
    for r in range(rows + 1):
        pts.append([])
        for c in range(cols + 1):
            edge = r in (0, rows) or c in (0, cols)
            jx = 0 if edge else (rand() - 0.5) * cw * 0.7
            jy = 0 if edge else (rand() - 0.5) * ch * 0.7
            pts[r].append((c * cw + jx, r * ch + jy))

    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    tris = []
    for r in range(rows):
        for c in range(cols):
            a, b, d, e = pts[r][c], pts[r][c + 1], pts[r + 1][c], pts[r + 1][c + 1]
            pair = [(a, b, e), (a, e, d)] if rand() > 0.5 else [(a, b, d), (b, e, d)]
            for t in pair:
                fill = rand() * 0.14 if rand() > 0.82 else 0
                tris.append((t, fill))
    for t, fill in tris:
        if fill:
            draw.polygon(t, fill=round(255 * fill * fill_alpha))
    for t, _ in tris:
        draw.line([*t, t[0]], fill=round(255 * line_alpha), width=1, joint='curve')

    layer = gradient(size, BRAND).convert('RGBA')
    layer.putalpha(mask)
    return layer


def text_width(f, s):
    return f.getlength(s)


def draw_text(img, xy, s, f, fill):
    """Draws text; a list fill means the brand text gradient"""
    if isinstance(fill, tuple):
        ImageDraw.Draw(img).text(xy, s, font=f, fill=fill)
        return
    x, y = xy
    left, top, right, bottom = f.getbbox(s)
    box = (int(x + left), int(y + top), int(x + right) + 1, int(y + bottom) + 1)
    mask = Image.new('L', (box[2] - box[0], box[3] - box[1]), 0)
    ImageDraw.Draw(mask).text((x - box[0], y - box[1]), s, font=f, fill=255)
    img.paste(gradient(mask.size, fill), box[:2], mask)


def headline(img, x, y, lines, size, max_width, color, weight=500):
    """
    lines: list of lines, each a list of (text, emphasis) runs.
    Emphasised runs are italic with the brand gradient, like the site's <em class="text-brand">.
    Shrinks to fit max_width and returns the y below the block.
    """
    while True:
        regular, italic = font('serif', size, weight), font('serif', size, 400, italic=True)
        widest = max(
            sum(text_width(italic if em else regular, t) for t, em in line) for line in lines
        )
        if widest <= max_width or size <= 40:
            break
        size -= 2
    lead = round(size * 1.04)
    for line in lines:
        cx = x
        for t, em in line:
            f = italic if em else regular
            draw_text(img, (cx, y), t, f, BRAND_TEXT if em else color)
            cx += text_width(f, t)
        y += lead
    return y


def eyebrow(img, x, y, s, color):
    f = font('sans', 20, 650)
    cx = x
    for ch in s.upper():
        ImageDraw.Draw(img).text((cx, y), ch, font=f, fill=color)
        cx += text_width(f, ch) + 4.5


def pills(img, x, y, labels, dark):
    f = font('sans', 21, 600)
    draw = ImageDraw.Draw(img)
    for label in labels:
        w = text_width(f, label) + 38
        draw.rounded_rectangle(
            (x, y, x + w, y + 46),
            radius=23,
            fill=None if dark else PAPER,
            outline=(90, 78, 72) if dark else LINE,
            width=2
        )
        draw.text((x + 19, y + 11), label, font=f, fill=PAPER if dark else INK)
        x += w + 12


def brand_bar(img):
    img.paste(gradient((W, BAR), BRAND), (0, H - BAR))


def logo(height):
    im = Image.open(IMAGES / 'logo.png').convert('RGBA')
    return im.resize((round(im.width * height / im.height), height), Image.LANCZOS)


def logo_card(img, x, y, height=72):
    mark = logo(height)
    pad = 16
    card = (x, y, x + mark.width + pad * 2, y + mark.height + pad * 2)
    ImageDraw.Draw(img).rounded_rectangle(card, radius=18, fill=PAPER)
    img.alpha_composite(mark, (x + pad, y + pad))


def photo_panel(img, src, width, focus=(0.5, 0.5)):
    photo = ImageOps.exif_transpose(Image.open(IMAGES / src)).convert('RGB')
    photo = ImageOps.fit(photo, (width, H - BAR), Image.LANCZOS, centering=focus)
    img.paste(photo, (W - width, 0))
    # Brand edge between text column and photo
    img.paste(gradient((6, H - BAR), BRAND).rotate(0), (W - width - 6, 0))


def dark_base(seed):
    img = Image.new('RGBA', (W, H), INK)
    # Warm glow in the top-right corner, as on the site's dark sections
    glow = Image.new('L', (W, H), 0)
    ImageDraw.Draw(glow).ellipse((W * 0.45, -H * 0.9, W * 1.5, H * 0.7), fill=70)
    glow = glow.filter(ImageFilter.GaussianBlur(160))
    warm = Image.new('RGBA', (W, H), (110, 40, 22, 255))
    warm.putalpha(glow)
    img.alpha_composite(warm)
    img.alpha_composite(facets((W, H), seed, 11, 6, 0.22, 1))
    return img


def inner_card(slug, eyebrow_text, lines, sub=None, photo=None, focus=(0.5, 0.5), seed=7):
    img = dark_base(seed)
    panel = 430 if photo else 0
    if photo:
        photo_panel(img, photo, panel, focus)

    x = 72
    logo_card(img, x, 64)
    # Cards without a photo have room for bigger type, so start the block higher
    top = 248 if photo else 212
    eyebrow(img, x, top, eyebrow_text, GOLD)
    y = headline(img, x, top + 42, lines, 76 if photo else 96, W - panel - x - 70, PAPER)
    if sub:
        ImageDraw.Draw(img).text((x, y + 40), sub, font=font('sans', 26, 450), fill=(205, 196, 188))
    ImageDraw.Draw(img).text(
        (x, H - BAR - 56), f'{DOMAIN}/{slug}', font=font('sans', 21, 500), fill=(150, 138, 130)
    )
    brand_bar(img)
    save(img, slug)


def home_card():
    img = Image.new('RGBA', (W, H), PAPER)
    img.alpha_composite(facets((W, H), 3, 11, 6, 0.28, 0.5))
    # Soft paper wash behind the logo so the mesh doesn't fight with it
    wash = Image.new('L', (W, H), 0)
    ImageDraw.Draw(wash).ellipse((180, -40, 1020, 560), fill=235)
    wash = wash.filter(ImageFilter.GaussianBlur(70))
    paper = Image.new('RGBA', (W, H), PAPER)
    paper.putalpha(wash)
    img.alpha_composite(paper)

    mark = logo(296)
    img.alpha_composite(mark, ((W - mark.width) // 2, 40))

    regular, italic = font('serif', 52, 500), font('serif', 52, 400, italic=True)
    a, b = 'Helping organizations succeed ', 'through people.'
    x = (W - text_width(regular, a) - text_width(italic, b)) / 2
    draw_text(img, (x, 370), a, regular, INK)
    draw_text(img, (x + text_width(regular, a), 370), b, italic, BRAND_TEXT)

    f = font('sans', 21, 600)
    total = sum(text_width(f, c) + 38 for c in CERTS) + 12 * (len(CERTS) - 1)
    pills(img, (W - total) / 2, 470, CERTS, dark=False)

    brand_bar(img)
    save(img, 'home')


def save(img, slug):
    OUT.mkdir(exist_ok=True)
    img.convert('RGB').save(OUT / f'{slug}.jpg', quality=88, optimize=True, progressive=True)
    print(f'static/images/og/{slug}.jpg')


home_card()
inner_card(
    'about',
    'About us',
    [[('Small, but', False)], [('mighty.', True)]],
    sub='Meet CEO Desiree L. Watkins and Team PCC',
    photo='desiree-watkins-headshot.jpg',
    focus=(0.5, 0.25),
    seed=9
)
inner_card(
    'mission',
    'Our mission',
    [[('Success', False)], [('through people.', True)]],
    sub='Quality professionals and solutions for the communities we serve',
    seed=17
)
inner_card(
    'services',
    'Services',
    [[('Workforce solutions', False)], [('that ', False), ('deliver.', True)]],
    sub='Direct hire · Staffing · HR & non-profit consulting',
    photo='hiring-professionals.jpg',
    focus=(0.6, 0.5),
    seed=31
)
inner_card(
    'government-entity',
    'Government entity',
    [[('A workforce', False)], [('that ', False), ('stays.', True)]],
    sub='HUBZone & WOSB certified · CAGE 8UAV4',
    photo='hero-federal.jpg',
    focus=(0.75, 0.5),
    seed=53
)
inner_card(
    'capability-statement',
    'Capability statement',
    [[('Built for government.', False)], [('Ready for business.', True)]],
    sub='UEI ZEJBM3DSLF58 · CAGE 8UAV4 · NAICS 541612',
    photo='government-team.jpg',
    focus=(0.6, 0.5),
    seed=41
)
inner_card(
    'contact',
    'Contact',
    [[('Let’s start a', False)], [('conversation.', True)]],
    sub='(813) 683-2995 · PlatinumChoiceConsulting@gmail.com',
    seed=23
)
