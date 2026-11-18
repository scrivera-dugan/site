# sarahdocs.com

Source for [sarahdocs.com](https://sarahdocs.com), a one-page Jekyll site served by GitHub Pages.

## Layout

| Path | What it holds |
| --- | --- |
| `index.md` | The page: selected work, writing, speaking, newsletter, timeline, about |
| `_layouts/default.html` | Page shell, hero, navigation, and the small scripts |
| `_includes/` | Section headings and the logo tiles (`logos/*.svg`) |
| `_data/work.yml` | Selected work, writing, and speaking |
| `_data/resume.yml` | The "Where I've been" timeline: titles, companies, years |
| `_data/substack.json` | Latest newsletter posts, refreshed daily by `.github/workflows/substack-feed.yml` |
| `styles.css` | All styles, including light and dark themes |
| `images/` | The owl, the ivy divider, the Stellic mark, and the link-preview photo |

## Run it locally

```bash
bundle exec jekyll serve
```
