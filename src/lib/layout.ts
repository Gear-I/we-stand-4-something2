/**
 * Layout helpers.
 *
 * Every element is placed with the coordinates measured on the original Wix site:
 * a 980px-wide canvas centred in a 1265px window, so the canvas starts at page x = 142.
 * Page content starts below the 354px header; the footer is 236px tall.
 * Below 1000px wide the CSS ignores these positions and stacks everything in one column.
 */
export const CANVAS_LEFT = 142;
export const HEADER_H = 354;
export const FOOTER_H = 236;

/** Inline `left/top/width/height` for an element at page coordinates (x, y). */
export function pos(x: number, y: number, w?: number, h?: number, originY: number = HEADER_H): string {
  let s = `left:${Math.round(x - CANVAS_LEFT)}px;top:${Math.round(y - originY)}px;`;
  if (w !== undefined) s += `width:${Math.round(w)}px;`;
  if (h !== undefined) s += `height:${Math.round(h)}px;`;
  return s;
}

/** Height of the content area for a page whose original total height was `total`. */
export const contentHeight = (total: number): number => total - HEADER_H - FOOTER_H;

/** Link to a page or file inside this site, respecting the deploy base path. */
export function url(path: string = ''): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${path.replace(/^\//, '')}`;
}

/** Image hosted on the original Wix media CDN. */
export const wix = (path: string): string => `https://static.wixstatic.com/media/${path}`;

/** Stepped "3D" shadow used on the home page buttons. */
export const stackShadow = (color: string): string =>
  [1, 3, 5, 7, 9].map((n) => `${color} ${n}px ${n}px 0 0`).join(', ');

export const FONTS = {
  os: "'Open Sans',sans-serif",
  enr: "'Enriqueta',serif",
  lb: "'Libre Baskerville',serif",
  pop: "'Poppins',sans-serif",
  jost: "'Jost','Futura',sans-serif",
  lulo: "'Montserrat',sans-serif",
  trend: "'Archivo Black',sans-serif",
  cinzel: "'Cinzel',serif",
  pf: "'Playfair Display',serif",
  amatic: "'Amatic SC',cursive",
  din: "'Barlow',sans-serif",
  helv: "'Helvetica Neue',Helvetica,Arial,sans-serif",
  avenir: "'Nunito Sans',sans-serif",
  bree: "'Bree Serif',serif",
  script: "'Lobster',cursive",
  georgia: 'Georgia,serif',
} as const;

export type FontKey = keyof typeof FONTS;

export const COLORS = {
  light: '#F0FAFF',
  blueGrey: '#CADDE6',
  text: '#515E65',
  heading: '#292F33',
  bright: '#00E689',
  green: '#00995B',
  darkGreen: '#004D2E',
  teal: '#01B1AF',
  navy: '#221F7B',
} as const;
