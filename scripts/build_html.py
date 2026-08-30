#!/usr/bin/env python3
"""Build a deterministic standalone HTML reading/print artifact from a Markdown manuscript.

Supported M1 subset:
- `#` title
- `##` section headings
- blank-line separated prose paragraphs

No Markdown library or external dependency is required. The builder changes only
presentation markup; manuscript wording remains the source of truth.
"""

from __future__ import annotations

import argparse
import html
from pathlib import Path

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #f2f1ed;
  color: #191919;
  font-family: Georgia, 'Times New Roman', serif;
  line-height: 1.62;
}
.book {
  width: min(44rem, calc(100% - 2rem));
  margin: 3rem auto;
  background: #fff;
  padding: 4rem 5rem 5rem;
  box-shadow: 0 0.5rem 2rem rgba(0,0,0,.08);
}
h1 {
  min-height: 55vh;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  font-size: clamp(2.5rem, 8vw, 5rem);
  letter-spacing: .08em;
  font-weight: 700;
  text-transform: uppercase;
  page-break-after: always;
}
h2 {
  margin: 5rem 0 2rem;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 1rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  page-break-before: always;
}
p { margin: 0 0 1.05em; }
@media (max-width: 640px) {
  .book { width: 100%; margin: 0; padding: 2rem 1.35rem 3rem; box-shadow: none; }
  h1 { min-height: 45vh; }
}
@media print {
  @page { size: A5; margin: 18mm 16mm 20mm; }
  body { background: #fff; font-size: 10.5pt; }
  .book { width: auto; margin: 0; padding: 0; box-shadow: none; }
  h1 { min-height: 80vh; }
  h2 { margin-top: 0; }
}
""".strip()


def render_markdown_subset(text: str) -> tuple[str, str]:
    title = "Manuskript"
    blocks: list[str] = []

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            title = line[2:].strip()
            blocks.append(f"<h1>{html.escape(title)}</h1>")
        elif line.startswith("## "):
            blocks.append(f"<h2>{html.escape(line[3:].strip())}</h2>")
        else:
            blocks.append(f"<p>{html.escape(line, quote=False)}</p>")

    return title, "\n".join(blocks)


def build_document(markdown_text: str) -> str:
    title, body = render_markdown_subset(markdown_text)
    return (
        "<!doctype html>\n"
        '<html lang="de">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"  <title>{html.escape(title)}</title>\n"
        "  <style>\n"
        f"{CSS}\n"
        "  </style>\n"
        "</head>\n"
        "<body>\n"
        '  <main class="book">\n'
        f"{body}\n"
        "  </main>\n"
        "</body>\n"
        "</html>\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build standalone HTML from the framework manuscript Markdown subset.")
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    source = args.manuscript.read_text(encoding="utf-8")
    result = build_document(source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
