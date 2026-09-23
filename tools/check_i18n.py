#!/usr/bin/env python3
"""Проверки для миграции i18n. См. TZ-i18n-migration-v1.1.md, раздел 4 (описание check_i18n.py) и 5.

Режимы:
  --report   отчёт о полноте словарей T по всем HTML-страницам репозитория
             (без сборки, читает только текущие файлы) — используется в батче 0.
  (без флага) проверка уже собранных страниц из i18n_pages.json: hreflang,
             canonical, отсутствие T/localStorage.getItem, битые внутренние ссылки.

Код выхода != 0 при любой ошибке.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_i18n import (  # noqa: E402
    ROOT, LANGS, PAGES_JSON, extract_dict, find_t_block, output_path,
    load_pages_config, StopCondition, page_url,
)

DATA_I18N_KEY_RE = re.compile(r'data-i18n(?:-html)?="([^"]+)"')


def discover_source_pages() -> list:
    pages = []
    for p in sorted(ROOT.glob("*.html")):
        if p.name == "404.html":
            continue
        pages.append(p)
    articles_dir = ROOT / "articles"
    if articles_dir.exists():
        pages.extend(sorted(articles_dir.glob("*.html")))
    return pages


def report_page(path: Path) -> list:
    problems = []
    src = path.read_text(encoding="utf-8")
    try:
        find_t_block(src)
    except StopCondition:
        print(f"[{path.relative_to(ROOT)}] нет словаря T — пропущена (см. ТЗ: статьи переводят только обвязку либо страница вне миграции)")
        return problems

    try:
        data = extract_dict(src)
    except StopCondition as e:
        problems.append(f"{path.relative_to(ROOT)}: словарь T не читается — {e}")
        return problems

    used_keys = set(DATA_I18N_KEY_RE.findall(src))
    key_sets = {lang: set(data.get(lang, {}).keys()) for lang in LANGS}
    all_keys = set().union(*key_sets.values()) if key_sets else set()

    print(f"[{path.relative_to(ROOT)}]")
    for lang in LANGS:
        missing = all_keys - key_sets[lang]
        if missing:
            problems.append(f"{path.relative_to(ROOT)} [{lang}]: нет ключей {sorted(missing)}")
            print(f"  {lang}: НЕ ХВАТАЕТ {sorted(missing)}")
        else:
            print(f"  {lang}: {len(key_sets[lang])} ключей, полный")

    referenced_missing = used_keys - all_keys
    if referenced_missing:
        problems.append(f"{path.relative_to(ROOT)}: в разметке есть data-i18n без записи в словаре: {sorted(referenced_missing)}")
        print(f"  разметка ссылается на отсутствующие в словаре ключи: {sorted(referenced_missing)}")

    unused = all_keys - used_keys - {"page_title", "meta_desc", "meta.title", "meta.description", "mailto_subject"}
    if unused:
        print(f"  в словаре есть, но не используются в разметке (может быть намеренно): {sorted(unused)}")

    return problems


def cmd_report() -> int:
    pages = discover_source_pages()
    problems = []
    for path in pages:
        problems.extend(report_page(path))
        print()
    if problems:
        for p in problems:
            print(f"ОШИБКА: {p}")
        print(f"ИТОГО проблем: {len(problems)}")
        return 1
    print("ИТОГО: словари полные, разметка согласована с ключами.")
    return 0


def cmd_verify_build() -> int:
    configured = load_pages_config()
    if not configured:
        print("i18n_pages.json пуст — собранных страниц для проверки нет.")
        return 0

    problems = []
    for page in configured:
        for lang in LANGS:
            path = output_path(page, lang)
            if not path.exists():
                problems.append(f"{page} [{lang}]: файл {path} не собран")
                continue
            src = path.read_text(encoding="utf-8")

            hreflang_count = len(re.findall(r'rel="alternate" hreflang="', src))
            if hreflang_count != len(LANGS) + 1:  # +x-default
                problems.append(f"{page} [{lang}]: hreflang-ссылок {hreflang_count}, ожидалось {len(LANGS) + 1}")

            if 'rel="canonical"' not in src:
                problems.append(f"{page} [{lang}]: нет canonical")

            if re.search(r"(?:var|const|let)\s+T\s*=\s*\{", src):
                problems.append(f"{page} [{lang}]: словарь T остался в собранном файле")

            if "localStorage.getItem" in src:
                problems.append(f"{page} [{lang}]: остался автовыбор языка через localStorage.getItem (запрещено INV-04)")

            expected_url = page_url(page, lang)
            if f'href="{expected_url}"' not in src:
                problems.append(f"{page} [{lang}]: canonical/hreflang не совпадает с ожидаемым url {expected_url}")

            for m in re.finditer(r'href="(/[^"]*)"', src):
                href = m.group(1)
                if href.startswith("//") or "@" in href:
                    continue
                clean = href.split("#")[0].split("?")[0]
                if not clean or clean == "/":
                    continue
                rel = clean[1:] + ("index.html" if clean.endswith("/") else "")
                if not (ROOT / rel).exists():
                    problems.append(f"{page} [{lang}]: битая внутренняя ссылка {href}")

    if problems:
        for p in problems:
            print(f"ОШИБКА: {p}")
        print(f"ИТОГО проблем: {len(problems)}")
        return 1
    print(f"ИТОГО: {len(configured)} страниц x {len(LANGS)} языков — без ошибок.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true", help="отчёт о полноте словарей по текущим страницам (без сборки)")
    args = ap.parse_args()
    if args.report:
        return cmd_report()
    return cmd_verify_build()


if __name__ == "__main__":
    sys.exit(main())
