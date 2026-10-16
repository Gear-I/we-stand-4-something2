/** Resource listings on the Resources page, with their original positions. */
export interface Resource {
  title: string;
  url: string;
  /** Wix media path for the logo. */
  image: string;
  titleY: number;
  img: { x: number; y: number; w: number; h: number };
  viewY: number;
}

export const RESOURCES: Resource[] = [
  {
    title: 'The Division of Developmental Disabilities Services Handbook for Renters',
    url: 'https://docs.wixstatic.com/ugd/1829a9_888cd069874748a98f5e40334c013705.pdf',
    image: 'f45d39_c14795d3ad5b49e6a1c885f660148fe7~mv2.png/v1/fill/w_510,h_380,al_c,lg_1,q_85/House-removebg-preview.png',
    titleY: 526, img: { x: 504, y: 601, w: 255, h: 190 }, viewY: 812,
  },
  {
    title: 'Delaware Disability Hub',
    url: 'https://deldhub.gacec.delaware.gov/',
    image: 'f45d39_92794a9a269a4f4b9a09152d51dafb81~mv2.png/v1/fill/w_562,h_450,al_c,lg_1,q_85/DDH_edited.png',
    titleY: 893, img: { x: 491, y: 947, w: 281, h: 225 }, viewY: 1201,
  },
  {
    title: 'Guide to Services For Delawareans and\nPersons with Disabilities',
    url: 'https://dhss.delaware.gov/dhss/dsaapd/files/aging_and_disabilities_guide.pdf',
    image: 'f45d39_ea356b7e1af94a81817b2c9fc5f79e69~mv2.png/v1/fill/w_324,h_422,al_c,lg_1,q_85/DHSS_edited.png',
    titleY: 1302, img: { x: 550, y: 1400, w: 162, h: 211 }, viewY: 1669,
  },
  {
    title: 'DART Paratransit',
    url: 'https://dartfirststate.com/services/para_services.shtml',
    image: 'f45d39_3c9f6a123f204a3c8ac51008f288276d~mv2.jpg/v1/fill/w_450,h_450,al_c,lg_1,q_80/DART.jpg',
    titleY: 1724, img: { x: 519, y: 1783, w: 225, h: 225 }, viewY: 2057,
  },
  {
    title: 'Traumatic brain injury (TBI)',
    url: 'https://scpd.delaware.gov/brain-injury-funds.shtml',
    image: 'f45d39_e219687224c343498d0e3be8ca6d015d~mv2.jpg/v1/fill/w_346,h_346,al_c,lg_1,q_80/SCPD-Logo.jpg',
    titleY: 2130, img: { x: 545, y: 2188, w: 173, h: 173 }, viewY: 2422,
  },
  {
    title: 'Mid-Atlantic ADA Center',
    url: 'https://www.adainfo.org/',
    image: 'f45d39_f53e48d8dab143ca8cc233664f037c2d~mv2.png/v1/fill/w_320,h_320,al_c,q_85,usm_0.66_1.00_0.01/ADA.png',
    titleY: 2495, img: { x: 551, y: 2552, w: 160, h: 160 }, viewY: 2770,
  },
  {
    title: 'Autism Delaware',
    url: 'https://www.autismdelaware.org/about/autism-in-delaware/',
    image: 'f45d39_953c5bcfa6284d16a500b58d8295ff76~mv2.png/v1/fill/w_302,h_302,al_c,q_85,usm_0.66_1.00_0.01/Autism-Delaware_edited.png',
    titleY: 2841, img: { x: 556, y: 2905, w: 151, h: 151 }, viewY: 3091,
  },
  {
    title: 'The Delaware Disabilities Council (DDC)',
    url: 'https://ddc.delaware.gov/',
    image: 'f45d39_db45f4c8bf184859bf41cbad3e4db663~mv2.png/v1/fill/w_474,h_284,al_c,lg_1,q_85/agency-logo.png',
    titleY: 3151, img: { x: 513, y: 3228, w: 237, h: 142 }, viewY: 3416,
  },
  {
    title: 'EPIC',
    url: 'https://www.epicdelaware.org/',
    image: 'f45d39_069b81adcc4f4094aec4c3efb5d0905d~mv2.png/v1/fill/w_316,h_230,al_c,q_85,usm_0.66_1.00_0.01/EPIC-Logo_edited.png',
    titleY: 3488, img: { x: 553, y: 3536, w: 158, h: 115 }, viewY: 3685,
  },
];
