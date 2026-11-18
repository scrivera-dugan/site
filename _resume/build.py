#!/usr/bin/env python3
"""Build the printable resume from _data/resume.yml and _data/work.yml.

The site's resume section is designed for the screen. This builds a separate,
print-first page with a conventional one-column resume layout, then prints it
to PDF with headless Chrome.

Usage:
    python3 _resume/build.py [output.pdf]

Writes _resume/resume.html next to this script, and the PDF to the given path
(default: sarah-dugan-resume.pdf at the site root, where the
"Full resume (PDF)" link points). Jekyll ignores folders that start
with an underscore, so nothing here is published with the site.
"""

import html
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

NAME = "Sarah C. Dugan"
CONTACT = [
    ("sarahcdugan@gmail.com", "mailto:sarahcdugan@gmail.com"),
    ("sarahdocs.com", "https://sarahdocs.com"),
    ("linkedin.com/in/scdugan", "https://www.linkedin.com/in/scdugan"),
    ("github.com/scrivera-dugan", "https://github.com/scrivera-dugan"),
]

CSS = """
@page { size: letter; margin: 0.55in 0.6in; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 9.6pt; line-height: 1.38; color: #1a1a1a;
}
a { color: inherit; text-decoration: none; }

header { margin-bottom: 12pt; }
h1 { font-size: 21pt; font-weight: 600; letter-spacing: -0.2pt; line-height: 1.1; }
.contact { margin-top: 4pt; font-size: 9pt; color: #555; }
.contact span + span::before { content: "·"; margin: 0 6pt; color: #999; }

h2 {
  font-size: 8.5pt; font-weight: 700; letter-spacing: 1.2pt; text-transform: uppercase;
  color: #1a1a1a; border-bottom: 0.75pt solid #1a1a1a;
  padding-bottom: 2pt; margin: 13pt 0 7pt;
}
.summary { font-size: 9.8pt; }

.job { margin-bottom: 9pt; }
/* A job may continue onto the next page, but never strands its heading,
   and a single bullet never splits across pages. */
.job-head, .org { break-after: avoid; }
li { break-inside: avoid; }
h2 { break-after: avoid; }
.edu { break-inside: avoid; }
.job-head { display: flex; justify-content: space-between; align-items: baseline; gap: 12pt; }
.job-title { font-weight: 600; font-size: 10.2pt; }
.dates { font-size: 9pt; color: #555; white-space: nowrap; font-variant-numeric: tabular-nums; }
.org { font-size: 9.2pt; color: #555; margin-top: 1pt; }
.org .co { color: #1a1a1a; font-weight: 500; }
ul { margin: 3.5pt 0 0 12pt; }
li { margin-bottom: 2.2pt; padding-left: 2pt; }
li::marker { color: #888; }

.work li { margin-bottom: 2.5pt; }
.work .t { font-weight: 600; }
.work .o { color: #555; }

.edu { display: flex; justify-content: space-between; align-items: baseline; gap: 12pt; }
.edu .deg { font-weight: 600; }
.edu .minor { font-size: 9.2pt; color: #555; }
"""


def e(text):
    return html.escape(str(text), quote=True)


def dates(job):
    start = job.get("start", "")
    end = job.get("end") or "Present"
    return f"{start} – {end}"


def job_html(job):
    org = [f'<span class="co">{e(job["company"])}</span>']
    org += [e(job[k]) for k in ("industry", "location") if job.get(k)]
    bullets = "".join(f"<li>{e(b)}</li>" for b in job.get("bullets") or [])
    return f"""
<div class="job">
  <div class="job-head"><span class="job-title">{e(job["title"])}</span><span class="dates">{e(dates(job))}</span></div>
  <div class="org">{" · ".join(org)}</div>
  {f"<ul>{bullets}</ul>" if bullets else ""}
</div>"""


def work_html(work):
    # The featured project is the current job, which the experience bullets
    # already cover, so the PDF lists only the docs sets.
    items = work.get("docs") or []
    rows = []
    for it in items:
        if it.get("gated"):
            continue
        rows.append(
            f'<li><a href="{e(it["url"])}"><span class="t">{e(it["title"])}</span></a>'
            f' <span class="o">({e(it["org"])})</span>. {e(it["summary"]).strip()}</li>'
        )
    return f'<ul class="work">{"".join(rows)}</ul>'


def speaking_html(work):
    rows = []
    for t in work.get("speaking") or []:
        when = t["date"].strftime("%b %Y") if hasattr(t["date"], "strftime") else str(t["date"])
        rows.append(
            f'<li><a href="{e(t["url"])}"><span class="t">{e(t["title"])}</span></a>'
            f' <span class="o">({e(t["event"])})</span>. {e(t["kind"])}, {e(when)}.</li>'
        )
    return f'<ul class="work">{"".join(rows)}</ul>' if rows else ""


def build():
    r = yaml.safe_load((ROOT / "_data/resume.yml").read_text())
    w = yaml.safe_load((ROOT / "_data/work.yml").read_text())
    contact = "".join(f'<span><a href="{e(u)}">{e(t)}</a></span>' for t, u in CONTACT)
    jobs = "".join(job_html(j) for j in r["experience"])
    edu = "".join(
        f'<div class="edu"><div><div class="deg">{e(s["degree"])}</div>'
        f'<div class="minor">{e(s["school"])}{" · " + e(s["minor"]) if s.get("minor") else ""}</div></div>'
        f'<span class="dates">{e(s["year"])}</span></div>'
        for s in r["education"]
    )
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{e(NAME)} – Resume</title>
<style>{CSS}</style></head><body>
<header><h1>{e(NAME)}</h1><div class="contact">{contact}</div></header>
<p class="summary">{e(r["summary"])}</p>
<h2>Experience</h2>{jobs}
<h2>Selected work</h2>{work_html(w)}
{"<h2>Speaking</h2>" + speaking_html(w) if w.get("speaking") else ""}
<h2>Education</h2>{edu}
</body></html>"""


def main():
    out_pdf = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "sarah-dugan-resume.pdf"
    page = HERE / "resume.html"
    page.write_text(build())
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={out_pdf}", page.as_uri()],
        check=True, capture_output=True,
    )
    print(out_pdf)


if __name__ == "__main__":
    main()
