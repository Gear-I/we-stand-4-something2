/** Site-wide content: navigation, contact details, social links, blog posts. */

export interface NavLink {
  label: string;
  /** Page path relative to the site root, e.g. "resources/". `null` = menu heading only. */
  href: string | null;
  children?: { label: string; href: string }[];
}

export const NAV: NavLink[] = [
  { label: 'Home', href: '' },
  {
    label: 'Resources',
    href: 'resources/',
    children: [
      { label: 'Local Legislation', href: 'legislation/' },
      { label: 'Feedback!', href: 'feedback/' },
    ],
  },
  { label: 'About/Board Members', href: 'about/' },
  {
    label: 'More',
    href: null,
    children: [
      { label: 'Services', href: 'services/' },
      { label: 'Events', href: 'events/' },
      { label: 'Support Us!', href: 'blank/' },
      { label: 'Photo Gallery', href: 'photo-gallery/' },
      { label: 'Shop', href: 'shop/' },
      { label: 'Blog', href: 'blog-1/' },
    ],
  },
];

export const CONTACT = {
  name: 'We Stand 4 Something',
  tagline: 'Education, Advocacy, Empowerment',
  address: ['PO Box 207, Greenwood,', 'Delaware 19950'],
  phoneDisplay: '302. 669 WS4S (9747)',
  phone: '+13026699747',
  email: 'info@westand4something.org',
  copyright: '© 2025 by We Stand 4 Something',
} as const;

export const SOCIAL = [
  { name: 'Instagram', href: 'https://www.instagram.com/westand4somthing/', icon: '8d6893330740455c96d218258a458aa4.png' },
  { name: 'Twitter', href: 'https://twitter.com/4Westand', icon: '9c4b521dd2404cd5a05ed6115f3a0dc8.png' },
  { name: 'Facebook', href: 'https://www.facebook.com/westand4something', icon: 'e316f544f9094143b9eac01f1f19e697.png' },
] as const;

export interface Post {
  /** URL path under /post/, kept identical to the old Wix blog. */
  slug: string;
  title: string;
  author: string;
  date: string;
  readTime: string;
  youtube?: string;
  image?: string;
  excerpt?: string;
  body?: string;
}

export const POSTS: Post[] = [
  {
    slug: '2016/07/20/for-those-of-you-who-missed-emmanuel-on-delmarva-life-check-the-video-out-here',
    title: 'For those of you, who missed Emmanuel on Delmarva life. Check the video out here',
    author: 'intern679',
    date: 'Jul 20, 2016',
    readTime: '0 min read',
    youtube: '37wSDJ7Un_U',
  },
  {
    slug: '2016/06/23/emmanuel-is-live-on-wboc-tv',
    title: 'Emmanuel is Live on WBOC TV!',
    author: 'intern679',
    date: 'Jun 23, 2016',
    readTime: '1 min read',
    image: '996292_9dae49e74efe4d098adb14ae92d754fa~mv2.jpg',
    excerpt:
      'Congratulations to We Stand 4 Something Inc. Owner Emmanuel Jenkins! Watch him on ➡WBOC Delmarva Life June 30th @ 5:00pm⬅ he will be...',
    body:
      "Congratulations to We Stand 4 Something Inc. Owner Emmanuel Jenkins! Watch him on ➡WBOC Delmarva Life June 30th @ 5:00pm⬅ he will be talking about his Nonporfit and what is has to offer to our community, as well as the 3rd Annual Friday Feast for people with disabilities and their family's. DON'T FORGET TO TUNE IN!",
  },
];
