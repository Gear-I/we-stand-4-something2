/** Partner resources listed on the Resources page. */
export interface Resource {
  name: string;
  url: string;
  /** True when the link opens a PDF document. */
  pdf?: boolean;
  /** Wix media path for the organisation's logo. */
  logo: string;
}

export const RESOURCES: Resource[] = [
  {
    name: 'Division of Developmental Disabilities Services: Handbook for Renters',
    url: 'https://docs.wixstatic.com/ugd/1829a9_888cd069874748a98f5e40334c013705.pdf',
    pdf: true,
    logo: 'f45d39_c14795d3ad5b49e6a1c885f660148fe7~mv2.png/v1/fill/w_510,h_380,al_c,lg_1,q_85/House-removebg-preview.png',
  },
  {
    name: 'Delaware Disability Hub',
    url: 'https://deldhub.gacec.delaware.gov/',
    logo: 'f45d39_92794a9a269a4f4b9a09152d51dafb81~mv2.png/v1/fill/w_562,h_450,al_c,lg_1,q_85/DDH_edited.png',
  },
  {
    name: 'Guide to Services for Delawareans and Persons with Disabilities',
    url: 'https://dhss.delaware.gov/dhss/dsaapd/files/aging_and_disabilities_guide.pdf',
    pdf: true,
    logo: 'f45d39_ea356b7e1af94a81817b2c9fc5f79e69~mv2.png/v1/fill/w_324,h_422,al_c,lg_1,q_85/DHSS_edited.png',
  },
  {
    name: 'DART Paratransit',
    url: 'https://dartfirststate.com/services/para_services.shtml',
    logo: 'f45d39_3c9f6a123f204a3c8ac51008f288276d~mv2.jpg/v1/fill/w_450,h_450,al_c,lg_1,q_80/DART.jpg',
  },
  {
    name: 'Traumatic Brain Injury Fund (State Council for Persons with Disabilities)',
    url: 'https://scpd.delaware.gov/brain-injury-funds.shtml',
    logo: 'f45d39_e219687224c343498d0e3be8ca6d015d~mv2.jpg/v1/fill/w_346,h_346,al_c,lg_1,q_80/SCPD-Logo.jpg',
  },
  {
    name: 'Mid-Atlantic ADA Center',
    url: 'https://www.adainfo.org/',
    logo: 'f45d39_f53e48d8dab143ca8cc233664f037c2d~mv2.png/v1/fill/w_320,h_320,al_c,q_85,usm_0.66_1.00_0.01/ADA.png',
  },
  {
    name: 'Autism Delaware',
    url: 'https://www.autismdelaware.org/about/autism-in-delaware/',
    logo: 'f45d39_953c5bcfa6284d16a500b58d8295ff76~mv2.png/v1/fill/w_302,h_302,al_c,q_85,usm_0.66_1.00_0.01/Autism-Delaware_edited.png',
  },
  {
    name: 'Delaware Developmental Disabilities Council (DDC)',
    url: 'https://ddc.delaware.gov/',
    logo: 'f45d39_db45f4c8bf184859bf41cbad3e4db663~mv2.png/v1/fill/w_474,h_284,al_c,lg_1,q_85/agency-logo.png',
  },
  {
    name: 'EPIC',
    url: 'https://www.epicdelaware.org/',
    logo: 'f45d39_069b81adcc4f4094aec4c3efb5d0905d~mv2.png/v1/fill/w_316,h_230,al_c,q_85,usm_0.66_1.00_0.01/EPIC-Logo_edited.png',
  },
];
