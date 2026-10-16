/** Board members, in the order the bio pages link to each other. */
import { wix } from '../lib/site';

export interface Member {
  name: string;
  role: string;
  /** Page path, kept from the old Wix site. */
  href: string;
  photo: string;
  /** Square-cropped photo for the About page grid. */
  thumb: string;
}

export const TEAM: Member[] = [
  {
    name: 'Emmanuel Jenkins',
    role: 'Founder and Director',
    href: 'emmanuel/',
    photo: wix('f45d39_0f746333cff946bda5b82c822bd27a7e~mv2.jpeg/v1/fill/w_654,h_634,al_c,lg_1,q_85/Emmanuel%20Jenkins.jpeg'),
    thumb: wix('0bae78_65688fe79512416aabb7ebcc737b1519~mv2_d_1440_1440_s_2.jpg/v1/fill/w_480,h_480,al_c,q_80,usm_0.66_1.00_0.01/emmanuel.jpg'),
  },
  {
    name: 'Marissa Castello',
    role: 'Administrative Support and Secretary',
    href: 'marissa/',
    photo: wix('b08a92_e0b91d78637244ef8ad543b47224477c~mv2.jpeg/v1/fill/w_520,h_520,al_c,q_80,usm_0.66_1.00_0.01/Marissa.jpeg'),
    thumb: wix('b08a92_e0b91d78637244ef8ad543b47224477c~mv2.jpeg/v1/fill/w_480,h_480,al_c,q_80,usm_0.66_1.00_0.01/Marissa.jpeg'),
  },
  {
    name: 'Dielle De Noon',
    role: 'Board member and Website Manager',
    href: 'dielle/',
    photo: wix('f45d39_2e77752fec1347b1b50ddb302f678ce0~mv2.jpeg/v1/fill/w_520,h_520,al_c,q_80,usm_0.66_1.00_0.01/dielle.jpeg'),
    thumb: wix('f45d39_1f23f76352474dd3b8ddf23fa1303ab4~mv2.jpg/v1/crop/x_0,y_505,w_3024,h_3022/fill/w_480,h_480,al_c,q_80,usm_0.66_1.00_0.01/dielle.jpg'),
  },
];
