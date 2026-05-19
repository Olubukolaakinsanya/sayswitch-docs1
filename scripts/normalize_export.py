#!/usr/bin/env python3
from pathlib import Path
import re


PROJECT_ROOT = Path(__file__).resolve().parents[1]

SCRIPT_TAG_RE = re.compile(r'<script[^>]+src="/_next/static/[^"]+"[^>]*></script>')
NEXT_DATA_RE = re.compile(
    r'<script id="__NEXT_DATA__" type="application/json">.*?</script>',
    re.DOTALL,
)
FEEDBACK_LINK_RE = re.compile(
    r'<a[^>]+href="https://github\.com/shuding/nextra/issues/new[^"]*"[^>]*>Question\? Give us feedback →</a>'
)
EDIT_LINK_RE = re.compile(
    r'<a[^>]+href="https://github\.com/shuding/nextra/pages/[^"]*"[^>]*>Edit this page</a>'
)


def normalize_html(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    original = html

    html = SCRIPT_TAG_RE.sub("", html)
    html = NEXT_DATA_RE.sub("", html)
    html = FEEDBACK_LINK_RE.sub("", html)
    html = EDIT_LINK_RE.sub("", html)
    html = re.sub(
        r'\s+srcSet="/_next/image\?url=%2Fassets%2Fimg%2Fsay-switchlogo\.png&amp;w=\d+&amp;q=\d+\s+1x,\s+/_next/image\?url=%2Fassets%2Fimg%2Fsay-switchlogo\.png&amp;w=\d+&amp;q=\d+\s+2x"',
        "",
        html,
    )
    html = re.sub(
        r'src="/_next/image\?url=%2Fassets%2Fimg%2Fsay-switchlogo\.png&amp;w=\d+&amp;q=\d+"',
        'src="/assets/img/say-switchlogo.png"',
        html,
    )
    html = html.replace("MIT 2026 © Nextra.", "Recovered Sayswitch documentation archive.")

    if html != original:
        path.write_text(html, encoding="utf-8")


def main() -> None:
    for html_file in PROJECT_ROOT.rglob("*.html"):
        normalize_html(html_file)


if __name__ == "__main__":
    main()
