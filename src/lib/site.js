import { SITE_URL } from '$app/env/public';

export const site = {
  name: 'Platinum Choice Consulting',
  // Set SITE_URL in the environment when the domain changes
  url: SITE_URL,
  phone: '(813) 683-2995',
  phoneHref: 'tel:+18136832995',
  mobile: '(443) 766-9087',
  mobileHref: 'tel:+14437669087',
  email: 'PlatinumChoiceConsulting@gmail.com',
  altSite: 'https://www.platinumchoiceconsulting.net/',
  serviceAreas: ['Washington, DC', 'Virginia', 'Maryland', 'Tampa']
};

export const nav = [
  { href: '/', label: 'Home' },
  { href: '/about', label: 'About Us' },
  { href: '/mission', label: 'Mission' },
  { href: '/services', label: 'Services' },
  { href: '/government-entity', label: 'Government Entity' },
  { href: '/capability-statement', label: 'Capability Statement' }
];

/** Registration details, certifications and codes, as listed on the Government Entity page */
export const credentials = {
  certifications: ['HUBZone', 'EDWOSB', 'WOSB', 'WBE', 'MBE', 'AABE'],
  certificationNames: /** @type {Record<string, string>} */ ({
    HUBZone: 'SBA: Historically Underutilized Business Zones',
    EDWOSB: 'SAM: Economically Disadvantaged Women-Owned Small Business',
    WOSB: 'SAM: Women-Owned Small Business',
    WBE: 'SAM: Women Business Enterprise',
    MBE: 'SAM: Minority Business Enterprise',
    AABE: 'SAM: African American Business Enterprise'
  }),
  legalName: 'Platinum Choice Consulting, Inc.',
  address: ['4825 Sevilla Shores Drive', 'Wimauma, FL 33598'],
  contacts: 'Desiree L. Watkins & LaMont Flanagan',
  ein: '84-5094283',
  uei: 'ZEJBM3DSLF58',
  cage: '8UAV4',
  naics: ['541410', '541611', '541612', '541613', '561311', '561320', '611430', '621999'],
  psc: ['U001', 'R607', 'R431', 'R408'],
  incorporated: 'Florida'
};
