/** Helpers shared by pages and components. */

/** Link to a page or file inside this site, respecting the deploy base path. */
export function url(path: string = ''): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${path.replace(/^\//, '')}`;
}

/** Image hosted on the original Wix media CDN. */
export const wix = (path: string): string => `https://static.wixstatic.com/media/${path}`;

/** Full page title, e.g. "About us | We Stand 4 Something". */
export const pageTitle = (title?: string): string =>
  title ? `${title} | We Stand 4 Something` : 'We Stand 4 Something';
