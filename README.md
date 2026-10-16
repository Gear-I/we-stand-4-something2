# We Stand 4 Something — website

Website for [We Stand 4 Something](https://www.westand4something.org/), a Delaware nonprofit enhancing independence for
people with disabilities. Built with **Astro**, **TypeScript** and **CSS**, deployed to GitHub Pages.

The site is designed to be accessible first: it aims to meet WCAG 2.2 AA, and every page is tested with automated checks,
keyboard-only use and large text sizes. See the site's own [accessibility statement](src/pages/accessibility.astro).

## Two versions

| Version | Branch | What it is |
|---|---|---|
| **Accessible design** (live) | `main` | Responsive layout, high-contrast colours, display settings, labelled forms |
| **Classic design** | `classic-design` | The first version: a pixel-for-pixel copy of the old Wix site |

### Going back to the classic design

No code changes needed:

1. Open the repository's **Actions** tab, then **Deploy to GitHub Pages**.
2. Choose **Run workflow**, pick **classic-design** as the version, and run it.

The live site switches to the classic design in about a minute. To return, run the workflow again with **main**.

A normal push to `main` publishes the accessible design again. To keep the classic design live even after pushes, add a
repository variable `SITE_VERSION` = `classic-design` (**Settings → Secrets and variables → Actions → Variables**), and
delete it to switch back.

## Develop

Requires Node.js 22.12 or newer.

```sh
npm install
npm run dev      # local preview at http://localhost:4321/we-stand-4-something/
npm run build    # production build into dist/
npm run check    # type-check .astro and .ts files
```

## Editing content

Most everyday changes are in `src/data/`:

| File | Contains |
|---|---|
| `site.ts` | Menu, contact details, donation link, social links, blog posts |
| `events.ts` | Events. Add an entry and it appears under "Upcoming events" until its date passes |
| `team.ts` | Board members (name, role, photos) |
| `resources.ts` | Partner organisations on the Resources page |
| `gallery.ts` | Photo gallery images |

Page text is in `src/pages/` (one `.astro` file per page; URLs match the old Wix site).

## Design

- **Colours** come from the logo: teal (`--teal`) for links and buttons, lime (`--lime`) only *behind* dark text, deep teal
  for the footer. All are defined once at the top of `src/styles/global.css`. Every text colour meets WCAG AA contrast;
  body text meets AAA. If you change a colour, check it with a contrast checker (at least 4.5:1 for text).
- **Font:** Atkinson Hyperlegible, designed by the Braille Institute for readers with low vision.
- **Display settings:** visitors can choose larger text or a high-contrast (yellow and white on black) scheme. The site also
  follows the device's "increase contrast" and "reduce motion" settings.

### Accessibility checklist for new content

- One `<h1>` per page (the `PageIntro` component provides it); don't skip heading levels.
- Give every image an `alt` description, or `alt=""` if it is purely decorative or repeats nearby text.
- Link text should say where it goes ("Read Emmanuel's story", not "click here").
- Keep text left-aligned; avoid all-caps and justified paragraphs.
- Form fields need a visible `label` (use the `ContactForm` component).
- Always build internal links with `url('about/')` so they work under the GitHub Pages base path.

## Project layout

```
src/
  pages/        one .astro file per page; post/[...slug].astro renders blog posts
  layouts/      Base.astro: <head>, skip link, header, footer
  components/   Header (menus), DisplaySettings, Footer, PageIntro, ContactForm,
                SignupDialog, EventItem, BioPage, PostMeta, Icon
  data/         content (see above) and icons.ts
  lib/site.ts   url(), wix() image helper, page titles
  scripts/      form-to-email helper
  styles/       global.css: colours, type, layout, high contrast
```

## Deploying

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and publishes it to GitHub Pages.
One-time setup: **Settings → Pages → Build and deployment → Source: GitHub Actions**.

The site is served at `https://<owner>.github.io/<repo>/`. The workflow works out the address from the repository it runs
in, so forks deploy correctly too.

### Custom domain

To serve it at westand4something.org:
1. **Settings → Pages → Custom domain**, and point the domain's DNS at GitHub Pages.
2. **Settings → Secrets and variables → Actions → Variables**: add `SITE_URL` = `https://www.westand4something.org` and `BASE_PATH` = `/`.
3. Re-run the deploy workflow.

## Notes

- Images still load from the Wix image CDN (`static.wixstatic.com`). If the Wix site is closed, download them into `public/` and update the paths.
- Forms open the visitor's email app with a message to info@westand4something.org, since GitHub Pages can't process form submissions.
- The Donate button uses the Friday Feast donation form on Zeffy. Put a general donation link in `DONATE` in `src/data/site.ts` when you have one.
