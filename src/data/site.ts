/** Site-wide content: navigation, contact details, social links, blog posts. */

export interface NavItem {
  label: string;
  /** Page path relative to the site root, e.g. "about/". */
  href?: string;
  /** Items shown in a drop-down group instead of a single link. */
  children?: { label: string; href: string }[];
}

export const NAV: NavItem[] = [
  { label: 'Home', href: '' },
  { label: 'About us', href: 'about/' },
  { label: 'Services', href: 'services/' },
  { label: 'Events', href: 'events/' },
  {
    label: 'Resources',
    children: [
      { label: 'Resources for Delawareans', href: 'resources/' },
      { label: 'Local legislation', href: 'legislation/' },
      { label: 'Give us feedback', href: 'feedback/' },
    ],
  },
  {
    label: 'More',
    children: [
      { label: 'Friday Feast', href: 'friday-feast/' },
      { label: 'Photo gallery', href: 'photo-gallery/' },
      { label: 'Blog', href: 'blog-1/' },
      { label: 'Shop', href: 'shop/' },
      { label: 'Support us', href: 'blank/' },
    ],
  },
];

export const CONTACT = {
  name: 'We Stand 4 Something',
  motto: 'Education, Advocacy, Empowerment',
  tagline: 'Enhancing independence for people with disabilities',
  address: ['PO Box 207', 'Greenwood, Delaware 19950'],
  phoneDisplay: '302-669-9747',
  phoneVanity: '302-669-WS4S',
  phone: '+13026699747',
  email: 'info@westand4something.org',
  volunteerEmail: 'volunteer@westand4something.org',
  copyright: '© 2025 We Stand 4 Something',
} as const;

/**
 * Online donations. The old Wix site's PayPal button pointed nowhere this site can reproduce,
 * so the Friday Feast donation form is used until a general donation link is added here.
 */
export const DONATE = {
  url: 'https://www.zeffy.com/en-US/donation-form/3036b57a-b266-4240-97ab-7b99843ce6d8',
  label: 'Donate online through Zeffy',
} as const;

export const SOCIAL = [
  { name: 'Instagram', href: 'https://www.instagram.com/westand4somthing/', icon: '8d6893330740455c96d218258a458aa4.png' },
  { name: 'X (Twitter)', href: 'https://twitter.com/4Westand', icon: '9c4b521dd2404cd5a05ed6115f3a0dc8.png' },
  { name: 'Facebook', href: 'https://www.facebook.com/westand4something', icon: 'e316f544f9094143b9eac01f1f19e697.png' },
] as const;

export const LOGO = '996292_c27297a55ebd4707ba1e7e31cc39572e~mv2.png';

export interface Post {
  /** URL path under /post/, kept identical to the old Wix blog. */
  slug: string;
  title: string;
  author: string;
  /** ISO date, e.g. 2016-07-20 */
  date: string;
  readTime: string;
  youtube?: string;
  image?: string;
  imageAlt?: string;
  excerpt?: string;
  body?: string;
}

export const POSTS: Post[] = [
  {
    slug: '2016/07/20/for-those-of-you-who-missed-emmanuel-on-delmarva-life-check-the-video-out-here',
    title: 'For those of you, who missed Emmanuel on Delmarva life. Check the video out here',
    author: 'intern679',
    date: '2016-07-20',
    readTime: 'Video',
    youtube: '37wSDJ7Un_U',
    excerpt: 'Watch Emmanuel Jenkins on WBOC’s Delmarva Life.',
  },
  {
    slug: '2016/06/23/emmanuel-is-live-on-wboc-tv',
    title: 'Emmanuel is Live on WBOC TV!',
    author: 'intern679',
    date: '2016-06-23',
    readTime: '1 minute read',
    image: '996292_9dae49e74efe4d098adb14ae92d754fa~mv2.jpg',
    imageAlt: 'Emmanuel Jenkins',
    excerpt:
      'Congratulations to We Stand 4 Something Inc. Owner Emmanuel Jenkins! Watch him on WBOC Delmarva Life June 30th at 5:00pm.',
    body:
      "Congratulations to We Stand 4 Something Inc. Owner Emmanuel Jenkins! Watch him on WBOC Delmarva Life June 30th @ 5:00pm. He will be talking about his nonprofit and what it has to offer to our community, as well as the 3rd Annual Friday Feast for people with disabilities and their family's. DON'T FORGET TO TUNE IN!",
  },
];

/** Format an ISO date (YYYY-MM-DD) as e.g. "June 23, 2016" without time-zone drift. */
export function formatDate(iso: string): string {
  const [y, m, d] = iso.split('-').map(Number);
  return new Date(Date.UTC(y, m - 1, d)).toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric', timeZone: 'UTC' });
}
