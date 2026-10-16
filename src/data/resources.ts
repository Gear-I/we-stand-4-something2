/**
 * Partner resources listed on the Resources page, grouped by topic.
 * Descriptions are based on each organisation's own website (checked October 2026).
 */
export interface Resource {
  name: string;
  /** One plain-language sentence: what it is and who it helps. */
  description: string;
  url: string;
  /** True when the link opens a PDF document. */
  pdf?: boolean;
  /** Wix media path for the organisation's logo. */
  logo: string;
}

export interface ResourceGroup {
  id: string;
  title: string;
  resources: Resource[];
}

export const RESOURCE_GROUPS: ResourceGroup[] = [
  {
    id: 'guides',
    title: 'Guides and directories',
    resources: [
      {
        name: 'Delaware Disability Hub',
        description:
          'Information and connections on education, employment, health, housing, legal issues and transportation, for young people moving into adult life, their families and the professionals who support them.',
        url: 'https://deldhub.gacec.delaware.gov/',
        logo: 'f45d39_92794a9a269a4f4b9a09152d51dafb81~mv2.png/v1/fill/w_562,h_450,al_c,lg_1,q_85/DDH_edited.png',
      },
      {
        name: 'Guide to Services for Older Delawareans and Persons with Disabilities',
        description:
          'A directory of state services from the Division of Services for Aging and Adults with Physical Disabilities.',
        url: 'https://dhss.delaware.gov/dhss/dsaapd/files/aging_and_disabilities_guide.pdf',
        pdf: true,
        logo: 'f45d39_ea356b7e1af94a81817b2c9fc5f79e69~mv2.png/v1/fill/w_324,h_422,al_c,lg_1,q_85/DHSS_edited.png',
      },
    ],
  },
  {
    id: 'housing-transport',
    title: 'Housing and getting around',
    resources: [
      {
        name: 'Handbook for Renters',
        description:
          'A guide to renting a home, from Delaware’s Division of Developmental Disabilities Services.',
        url: 'https://docs.wixstatic.com/ugd/1829a9_888cd069874748a98f5e40334c013705.pdf',
        pdf: true,
        logo: 'f45d39_c14795d3ad5b49e6a1c885f660148fe7~mv2.png/v1/fill/w_510,h_380,al_c,lg_1,q_85/House-removebg-preview.png',
      },
      {
        name: 'DART Paratransit',
        description:
          'Delaware’s paratransit bus service for people with disabilities and older adults. Apply online through DART.',
        url: 'https://dartfirststate.com/services/para_services.shtml',
        logo: 'f45d39_3c9f6a123f204a3c8ac51008f288276d~mv2.jpg/v1/fill/w_450,h_450,al_c,lg_1,q_80/DART.jpg',
      },
    ],
  },
  {
    id: 'rights',
    title: 'Rights and advocacy',
    resources: [
      {
        name: 'Mid-Atlantic ADA Center',
        description:
          'Answers questions and offers training about the Americans with Disabilities Act (ADA) for people, businesses and public agencies in Delaware and nearby states.',
        url: 'https://www.adainfo.org/',
        logo: 'f45d39_f53e48d8dab143ca8cc233664f037c2d~mv2.png/v1/fill/w_320,h_320,al_c,q_85,usm_0.66_1.00_0.01/ADA.png',
      },
      {
        name: 'Delaware Developmental Disabilities Council (DDC)',
        description:
          'A state council that works to change laws, systems and policies so people with developmental disabilities and their families can take part fully in their communities.',
        url: 'https://ddc.delaware.gov/',
        logo: 'f45d39_db45f4c8bf184859bf41cbad3e4db663~mv2.png/v1/fill/w_474,h_284,al_c,lg_1,q_85/agency-logo.png',
      },
    ],
  },
  {
    id: 'support',
    title: 'Support and community',
    resources: [
      {
        name: 'Traumatic Brain Injury Fund',
        description:
          'Helps Delaware residents with a traumatic brain injury pay for things like home changes, assistive technology and medical equipment that other agencies don’t cover. Run by the State Council for Persons with Disabilities.',
        url: 'https://scpd.delaware.gov/brain-injury-funds.shtml',
        logo: 'f45d39_e219687224c343498d0e3be8ca6d015d~mv2.jpg/v1/fill/w_346,h_346,al_c,lg_1,q_80/SCPD-Logo.jpg',
      },
      {
        name: 'Autism Delaware',
        description: 'A nonprofit supporting people with autism and their families across Delaware.',
        url: 'https://www.autismdelaware.org/about/autism-in-delaware/',
        logo: 'f45d39_953c5bcfa6284d16a500b58d8295ff76~mv2.png/v1/fill/w_302,h_302,al_c,q_85,usm_0.66_1.00_0.01/Autism-Delaware_edited.png',
      },
      {
        name: 'EPIC (Endless Possibilities in the Community)',
        description:
          'Inclusive fitness and social programs in Newark for adults with intellectual, developmental or physical disabilities.',
        url: 'https://www.epicdelaware.org/',
        logo: 'f45d39_069b81adcc4f4094aec4c3efb5d0905d~mv2.png/v1/fill/w_316,h_230,al_c,q_85,usm_0.66_1.00_0.01/EPIC-Logo_edited.png',
      },
    ],
  },
];

/** The website's address without "https://www." — shown so people know where a link goes. */
export const displayHost = (url: string): string => new URL(url).hostname.replace(/^www\./, '');
