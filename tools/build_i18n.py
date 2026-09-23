#!/usr/bin/env python3
"""Собирает языковые версии страниц (en/pl/ru) из шаблонов в src/.
См. TZ-i18n-migration-v1.1.md, раздел 4. Только stdlib (INV-08)."""
import argparse
import html as html_lib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "src"
TOOLS_DIR = ROOT / "tools"
PAGES_JSON = TOOLS_DIR / "i18n_pages.json"
SITEMAP = ROOT / "sitemap.xml"
SITE_URL = "https://kholomyanskiy.com"
LANGS = ["en", "pl", "ru"]

BREADCRUMB_PARENT = {
    "audit": "services",
    "spec": "services",
    "metodichka": "products",
}
PARENT_NAV_KEY = {"services": "nav.services", "products": "nav.products", "articles": "nav.articles"}
PARENT_PAGE = {"services": "services", "products": "products", "articles": "articles"}


class StopCondition(Exception):
    """Соответствует разделу 9 ТЗ — требует решения Артёма, сборка не продолжается."""


# ---------- извлечение словаря T ----------

def find_t_block(src: str) -> str:
    """Вырезает блок `{...}` словаря T. Учитывает оба варианта кавычек в
    строках ('audit.html: "..."' и 'metodichka.html: \'...\''), в том числе
    "сырые" двойные кавычки внутри одинарных строк (SVG-атрибуты в fig*_svg)."""
    m = re.search(r"(?:var|const|let)\s+T\s*=\s*\{", src)
    if not m:
        raise StopCondition("Словарь T не найден в шаблоне")
    start = m.end() - 1
    depth = 0
    quote = None  # None | '"' | "'"
    esc = False
    i = start
    while i < len(src):
        c = src[i]
        if quote:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == quote:
                quote = None
        else:
            if c in "\"'":
                quote = c
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return src[start:i + 1]
        i += 1
    raise StopCondition("Не нашёл закрывающую скобку словаря T (не хватает '}' или разбалансированы кавычки)")


def js_obj_to_json(js_text: str) -> str:
    """Токенайзер JS-объекта -> JSON-текст. Работает посимвольно, чтобы
    запятые/двоеточия/скобки ВНУТРИ строковых значений (включая сырые "
    внутри '...'-строк) не путались со структурой объекта."""
    out = []
    i, n = 0, len(js_text)
    while i < n:
        c = js_text[i]
        if c == '"':
            j = i + 1
            while j < n:
                if js_text[j] == "\\" and j + 1 < n:
                    j += 2
                    continue
                if js_text[j] == '"':
                    j += 1
                    break
                j += 1
            out.append(js_text[i:j])
            i = j
            continue
        if c == "'":
            j = i + 1
            buf = []
            while j < n:
                ch = js_text[j]
                if ch == "\\" and j + 1 < n:
                    nxt = js_text[j + 1]
                    buf.append("'" if nxt == "'" else ("\\" if nxt == "\\" else nxt))
                    j += 2
                    continue
                if ch == "'":
                    j += 1
                    break
                buf.append(ch)
                j += 1
            out.append(json.dumps("".join(buf), ensure_ascii=False))
            i = j
            continue
        if c.isalpha() or c == "_":
            j = i
            while j < n and (js_text[j].isalnum() or js_text[j] == "_"):
                j += 1
            ident = js_text[i:j]
            k = j
            while k < n and js_text[k] in " \t\r\n":
                k += 1
            out.append(json.dumps(ident) if k < n and js_text[k] == ":" else ident)
            i = j
            continue
        out.append(c)
        i += 1
    text = "".join(out)
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    return text


def extract_dict(src: str) -> dict:
    block = find_t_block(src)
    try:
        data = json.loads(js_obj_to_json(block))
    except json.JSONDecodeError as e:
        raise StopCondition(f"Словарь T не парсится как JSON после нормализации: {e}")
    missing = [l for l in LANGS if l not in data]
    if missing:
        raise StopCondition(f"В словаре T нет языков: {missing}")
    return data


def detect_pattern(src: str) -> str:
    if "function setLang" in src:
        return "setLang"
    if "function applyLang" in src:
        return "applyLang"
    raise StopCondition("Не нашёл ни applyLang(), ни setLang() в шаблоне")


# ---------- подстановка текста ----------

DATA_I18N_RE = re.compile(r'(<[^>]+?\sdata-i18n="([^"]+)"[^>]*>)([^<]*)')
DATA_I18N_HTML_RE = re.compile(r'(<[^>]+?\sdata-i18n-html="([^"]+)"[^>]*>)(.*?)(?=</)', re.DOTALL)


def substitute_text(page_html: str, lang_dict: dict, lang: str) -> str:
    def sub_text(m):
        tag, key = m.group(1), m.group(2)
        if key not in lang_dict:
            raise StopCondition(f"Нет ключа '{key}' для языка '{lang}' (data-i18n)")
        return tag + html_lib.escape(lang_dict[key])

    def sub_html(m):
        tag, key = m.group(1), m.group(2)
        if key not in lang_dict:
            raise StopCondition(f"Нет ключа '{key}' для языка '{lang}' (data-i18n-html)")
        return tag + lang_dict[key]

    page_html = DATA_I18N_RE.sub(sub_text, page_html)
    page_html = DATA_I18N_HTML_RE.sub(sub_html, page_html)
    return page_html


# ---------- head: html lang / title / meta / canonical / hreflang ----------

def meta_title_desc(lang_dict: dict, page: str) -> tuple:
    if "page_title" in lang_dict and "meta_desc" in lang_dict:
        return lang_dict["page_title"], lang_dict["meta_desc"]
    if "meta.title" in lang_dict and "meta.description" in lang_dict:
        return lang_dict["meta.title"], lang_dict["meta.description"]
    raise StopCondition(f"Нет page_title/meta_desc (или meta.title/meta.description) для страницы '{page}'")


def page_url(page: str, lang: str) -> str:
    if page == "index":
        path = "/" if lang == "en" else f"/{lang}/"
    else:
        path = f"/{page}.html" if lang == "en" else f"/{lang}/{page}.html"
    return SITE_URL + path


def set_head(page_html: str, lang: str, page: str, title: str, desc: str) -> str:
    page_html = re.sub(r'<html lang="[^"]*"', f'<html lang="{lang}"', page_html, count=1)
    page_html = re.sub(r"<title>.*?</title>", f"<title>{html_lib.escape(title)}</title>", page_html, count=1, flags=re.DOTALL)
    page_html = re.sub(
        r'(<meta name="description" content=")[^"]*(")',
        lambda m: m.group(1) + html_lib.escape(desc) + m.group(2),
        page_html, count=1,
    )
    page_html = re.sub(
        r'(<meta property="og:locale" content=")[^"]*(")',
        lambda m: m.group(1) + {"en": "en_US", "pl": "pl_PL", "ru": "ru_RU"}[lang] + m.group(2),
        page_html, count=1,
    )
    url = page_url(page, lang)
    page_html = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), page_html, count=1)

    page_html = re.sub(r'\s*<link rel="canonical"[^>]*>\n?', "\n", page_html, count=1)
    page_html = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*"[^>]*>\n?', "", page_html)
    hreflang_block = "".join(
        f'<link rel="alternate" hreflang="{hl}" href="{page_url(page, hl)}">\n'
        for hl in LANGS
    ) + f'<link rel="alternate" hreflang="x-default" href="{page_url(page, "en")}">\n'
    canonical_and_hreflang = f'<link rel="canonical" href="{url}">\n{hreflang_block}'
    page_html = page_html.replace("</head>", canonical_and_hreflang + "</head>", 1)
    return page_html


# ---------- удаление старого кода переключения языков ----------

def strip_lang_switch_code(page_html: str, pattern: str) -> str:
    page_html = re.sub(r"<script>\s*(?:var|const|let)\s+T\s*=\s*\{.*?</script>", "", page_html, flags=re.DOTALL, count=1)
    if pattern == "applyLang":
        page_html = re.sub(r"function applyLang\(.*?\n\}\n", "", page_html, flags=re.DOTALL, count=1)
        page_html = re.sub(r"const saved = localStorage\.getItem\('site-lang'\);\s*\nif\(saved.*?\n", "", page_html)
    else:
        page_html = re.sub(r"function setLang\(.*?\n\}\n", "", page_html, flags=re.DOTALL, count=1)
    return page_html


LANG_SWITCH_SCRIPT = """<script>
document.querySelectorAll('[data-lang]').forEach(function(b){
  b.addEventListener('click', function(){ localStorage.setItem('site-lang', b.dataset.lang); });
});
</script>
"""


def inject_lang_switch_script(page_html: str) -> str:
    return page_html.replace("</body>", LANG_SWITCH_SCRIPT + "</body>", 1)


# ---------- ссылки ----------

HREF_SRC_RE = re.compile(r'(href|src)="([^"]*)"')


def classify_and_rewrite(url: str, lang: str, migrated: set) -> str:
    if url.startswith(("http://", "https://", "mailto:", "tel:", "//", "#")):
        return url
    if url.startswith("/"):
        return url  # уже корневой

    path, _, anchor = url.partition("#")
    anchor = f"#{anchor}" if anchor else ""

    if not path:
        return url  # чистый якорь, уже отфильтрован выше, но на всякий случай

    if "." not in path.rsplit("/", 1)[-1] or path.endswith(".html"):
        # это HTML-страница (или ссылка без расширения по недосмотру)
        page = path
        if page.endswith(".html"):
            page = page[:-5]
        page = page.split("?")[0]
        if page == "index":
            base = "/" if lang == "en" else f"/{lang}/"
        elif page in migrated:
            base = f"/{page}.html" if lang == "en" else f"/{lang}/{page}.html"
        else:
            base = f"/{page}.html" if lang == "en" else f"/{page}.html?lang={lang}"
        return base + anchor

    # статический ресурс (img/, files/, favicon.ico, apple-touch-icon.png, ...)
    return "/" + path.split("?")[0] + anchor


def rewrite_links(page_html: str, lang: str, migrated: set) -> str:
    def sub(m):
        attr, url = m.group(1), m.group(2)
        return f'{attr}="{classify_and_rewrite(url, lang, migrated)}"'

    return HREF_SRC_RE.sub(sub, page_html)


# ---------- JSON-LD: язык и url (INV-06), без изменения @id ----------

def update_jsonld_lang(page_html: str, lang: str, page: str) -> str:
    def walk(node):
        if isinstance(node, dict):
            if "inLanguage" in node:
                node["inLanguage"] = lang
            if "url" in node and isinstance(node["url"], str) and node["url"].startswith(SITE_URL):
                node["url"] = page_url(page, lang)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    def sub(m):
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError:
            return m.group(0)
        walk(data)
        return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>"

    return re.sub(
        r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
        sub, page_html, flags=re.DOTALL,
    )


# ---------- хлебные крошки (шаг 8) ----------

def strip_arrow(text: str) -> str:
    return re.sub(r"^[←\s]+", "", text).strip()


def inject_breadcrumbs(page_html: str, page: str, lang: str, lang_dict: dict) -> str:
    parent = BREADCRUMB_PARENT.get(page)
    if not parent:
        return page_html
    if "nav_home" not in lang_dict:
        raise StopCondition("Нет ключа nav_home для хлебных крошек")
    nav_key = PARENT_NAV_KEY[parent]
    if nav_key not in lang_dict:
        raise StopCondition(f"Нет ключа {nav_key} для хлебных крошек")
    if "h1_title" not in lang_dict:
        raise StopCondition("Нет ключа h1_title для хлебных крошек")

    home_name = strip_arrow(lang_dict["nav_home"])
    parent_name = lang_dict[nav_key]
    page_name = re.sub(r"<[^>]+>", "", lang_dict["h1_title"]).strip()

    items = [
        {"@type": "ListItem", "position": 1, "name": home_name, "item": page_url("index", lang)},
        {"@type": "ListItem", "position": 2, "name": parent_name, "item": page_url(PARENT_PAGE[parent], lang)},
        {"@type": "ListItem", "position": 3, "name": page_name, "item": page_url(page, lang)},
    ]
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
    script = '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=2) + "\n</script>\n"
    return page_html.replace("</head>", script + "</head>", 1)


def inject_article_breadcrumb(page_html: str, slug: str, article_title: str, articles_label: str, home_label: str) -> str:
    items = [
        {"@type": "ListItem", "position": 1, "name": home_label, "item": page_url("index", "en")},
        {"@type": "ListItem", "position": 2, "name": articles_label, "item": page_url("articles", "en")},
        {"@type": "ListItem", "position": 3, "name": article_title, "item": f"{SITE_URL}/articles/{slug}.html"},
    ]
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
    script = '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=2) + "\n</script>\n"
    return page_html.replace("</head>", script + "</head>", 1)


# ---------- сборка одной страницы ----------

def render_page(template_src: str, page: str, lang: str, full_dict: dict, migrated: set) -> str:
    if lang not in full_dict:
        raise StopCondition(f"В словаре T нет языка '{lang}' для страницы '{page}'")
    lang_dict = full_dict[lang]
    pattern = detect_pattern(template_src)

    out = substitute_text(template_src, lang_dict, lang)
    title, desc = meta_title_desc(lang_dict, page)
    out = set_head(out, lang, page, title, desc)
    out = strip_lang_switch_code(out, pattern)
    out = inject_lang_switch_script(out)
    out = rewrite_links(out, lang, migrated)
    out = update_jsonld_lang(out, lang, page)
    out = inject_breadcrumbs(out, page, lang, lang_dict)

    banner = f"<!-- GENERATED by tools/build_i18n.py from src/{page}.template.html; do not edit -->\n"
    out = banner + out
    return out


def output_path(page: str, lang: str) -> Path:
    if page == "index":
        return ROOT / ("index.html" if lang == "en" else f"{lang}/index.html")
    return ROOT / (f"{page}.html" if lang == "en" else f"{lang}/{page}.html")


def load_pages_config() -> list:
    if not PAGES_JSON.exists():
        return []
    return json.loads(PAGES_JSON.read_text(encoding="utf-8"))


def build_page(page: str, migrated: set) -> None:
    tpl_path = SRC_DIR / f"{page}.template.html"
    if not tpl_path.exists():
        raise StopCondition(f"Нет шаблона {tpl_path}")
    template_src = tpl_path.read_text(encoding="utf-8")
    full_dict = extract_dict(template_src)
    for lang in LANGS:
        rendered = render_page(template_src, page, lang, full_dict, migrated)
        out_path = output_path(page, lang)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rendered, encoding="utf-8")
        print(f"  {page} [{lang}] -> {out_path.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser(description="Сборка языковых версий страниц из src/*.template.html")
    ap.add_argument("pages", nargs="*", help="имена страниц (без .html); по умолчанию все из i18n_pages.json")
    args = ap.parse_args()

    configured = load_pages_config()
    pages = args.pages or configured
    if not pages:
        print("i18n_pages.json пуст и страницы не указаны в аргументах — собирать нечего.")
        return 0

    migrated = set(configured)
    try:
        for page in pages:
            print(f"Сборка {page}...")
            build_page(page, migrated)
    except StopCondition as e:
        print(f"СТОП: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
