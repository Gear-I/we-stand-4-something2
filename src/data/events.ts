/**
 * Events shown on the Events page. Add new events here; the page sorts them and splits
 * them into upcoming and past each time the site is rebuilt (every push to main).
 */
export interface SiteEvent {
  title: string;
  /** ISO date, e.g. 2026-11-20 */
  date: string;
  time?: string;
  location?: string;
  description: string;
  /** Page on this site with more details, e.g. "friday-feast/". */
  page?: string;
}

export const EVENTS: SiteEvent[] = [
  {
    title: 'The Friday Feast',
    date: '2025-11-21',
    description:
      'A free holiday celebration of food, fun and community, where people with and without disabilities share a seat at the table.',
    page: 'friday-feast/',
  },
];
