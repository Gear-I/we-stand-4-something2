# We Stand 4 Something — website

Recreation of [westand4something.org](https://www.westand4something.org/) built with **Astro**, **TypeScript** and **CSS**, deployed to GitHub Pages.
On desktop it reproduces the original Wix layout; on phones the same content stacks into a single column.

## Develop

Requires Node.js 22.12 or newer.

```sh
npm install
npm run dev      # local preview at http://localhost:4321/we-stand-4-something/
npm run build    # production build into dist/
npm run check    # type-check .astro and .ts files
```

## Project layout

```
src/
  pages/          one .astro file per page; URLs match the old Wix site
    post/[...slug].astro   blog posts (data in src/data/site.ts)
  layouts/Base.astro       <head>, header, content canvas, footer
  components/     Header, Footer and building blocks:
                  Text, Img, Box, Abs (positioned elements), StackButton,
                  ContactForm, Popup, Calendar, PhotoSlider, Band, Icon, PostMeta
  data/           site.ts (menu, contact details, blog posts), resources.ts,
                  gallery.ts (photo IDs), icons.ts (SVG icons)
  lib/layout.ts   positioning helpers, fonts, colours, url() for links
  scripts/        client-side TypeScript (form → email)
  styles/site.css all site styles, including the phone layout
```

### How positioning works

Elements take the coordinates measured on the original site, e.g.

```astro
<Text x={918} y={374} w={194} font="os" size={25}>Leave Your Mark</Text>
```

`x`/`y` are page coordinates (the 980px canvas starts at x = 142; content starts below the 354px header).
Below 1000px wide, `site.css` ignores the positions and stacks elements in source order, so keep elements
in reading order inside each page.

Always build internal links with `url('about/')` so they work under the GitHub Pages base path.

## Deploying

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and publishes it to GitHub Pages.
One-time setup: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
(GitHub Pages on a private repository requires a paid GitHub plan.)

The site is served at `https://gear-i.github.io/we-stand-4-something/`.

### Custom domain

To serve it at westand4something.org:
1. **Settings → Pages → Custom domain**, and point the domain's DNS at GitHub Pages.
2. **Settings → Secrets and variables → Actions → Variables**: add `SITE_URL` = `https://www.westand4something.org` and `BASE_PATH` = `/`.
3. Re-run the deploy workflow.

## Notes

- Images still load from the Wix image CDN (`static.wixstatic.com`). If the Wix site is closed, download them into `public/` and update the paths.
- Forms (Feedback, Events registration, Services group sign-ups) open the visitor's email app with a message to info@westand4something.org, since GitHub Pages can't process form submissions.
- The Events calendar is a simple month view (the original Wix calendar had no events listed).
