import { credentials, site } from '#lib/site.js';

export const prerender = true;

/** @param {string} path */
const url = (path) => new URL(path, site.url).href;

export function GET() {
  const body = `# ${site.name}

> ${site.name} (PCC) is a woman-owned, minority-owned small business providing HR, staffing, workforce development and management support services to government agencies, corporate clients, nonprofits and community organizations.

- Legal name: ${credentials.legalName}, incorporated in ${credentials.incorporated}
- Leadership: Desiree L. Watkins (Chief Executive Officer, 31 years of federal government experience) and LaMont Flanagan Esq. (President, 40-year local, state and federal executive)
- Service areas: ${site.serviceAreas.join(', ')} metropolitan areas; serves the entire US
- Certifications: ${credentials.certifications.join(', ')}
- Federal registration: UEI ${credentials.uei}, CAGE ${credentials.cage}
- NAICS codes: ${credentials.naics.join(', ')}
- PSC codes: ${credentials.psc.join(', ')}
- Memberships: National Association of Women Business Owners (NAWBO), African American Chamber of Commerce of Central Florida
- Contact: ${site.phone}, ${site.email}

## Pages

- [Home](${url('/')}): Overview of PCC, service areas, memberships and client testimonials
- [About Us](${url('/about')}): Company background and the biography and expertise of CEO Desiree L. Watkins
- [Mission](${url('/mission')}): PCC's mission to help organizations achieve success through people
- [Services](${url('/services')}): Workforce solutions, direct hire, customized solutions, introductory consultation, health care administration and non-profit HR consulting
- [Government Entity](${url('/government-entity')}): HUBZone status, workforce development programs and full company registration data for contracting officers
- [Capability Statement](${url('/capability-statement')}): Full capability statement with differentiators, pertinent codes and past performance
- [Contact](${url('/contact')}): Contact form, phone and email for staffing requests and enquiries
`;

  return new Response(body, {
    headers: { 'content-type': 'text/plain; charset=utf-8' }
  });
}
