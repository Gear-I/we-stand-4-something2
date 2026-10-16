// @ts-check
import { defineConfig } from 'astro/config';

// The deploy workflow sets SITE_URL/BASE_PATH from the repository it runs in
// (https://<owner>.github.io/<repo>/). These defaults are for local builds.
// When a custom domain (e.g. westand4something.org) is set up, build with
// SITE_URL=https://www.westand4something.org BASE_PATH=/ (see README).
// `||` (not `??`) so empty values from unset CI variables fall back to the defaults.
const site = process.env.SITE_URL || 'https://westand4.github.io';
const base = process.env.BASE_PATH || '/we-stand-4-something';

export default defineConfig({
  site,
  base,
  trailingSlash: 'always',
  build: { format: 'directory' },
});
