# sarahdocs.com

Source for [sarahdocs.com](https://sarahdocs.com), a one-page Jekyll site served by GitHub Pages.

## Layout

| Path | What it holds |
| --- | --- |
| `index.md` | The page: selected work, writing, speaking, newsletter, resume, about |
| `_layouts/default.html` | Page shell, hero, navigation, and the small scripts |
| `_includes/` | Section headings and the logo tiles (`logos/*.svg`) |
| `_data/work.yml` | Selected work, writing, and speaking |
| `_data/resume.yml` | Experience and education, shared by the page and the PDF |
| `_data/substack.json` | Latest newsletter posts, refreshed daily by `.github/workflows/substack-feed.yml` |
| `_resume/build.py` | Builds `sarah-dugan-resume.pdf` from the data files |
| `styles.css` | All styles, including light and dark themes and print |
| `images/` | The owl, the ivy divider, the Stellic mark, and the link-preview photo |

## Run it locally

```bash
bundle exec jekyll serve
```

## Update the resume PDF

Edit `_data/resume.yml`, then rebuild the PDF (needs Python with PyYAML and Google Chrome):

```bash
python3 _resume/build.py
```
