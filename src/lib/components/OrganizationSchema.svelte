<!-- Schema.org structured data describing the business, for search engines -->
<script>
  import { credentials, site } from '#lib/site.js';

  const schema = {
    '@context': 'https://schema.org',
    '@type': 'ProfessionalService',
    '@id': `${site.url}/#organization`,
    name: site.name,
    legalName: credentials.legalName,
    url: site.url,
    logo: `${site.url}/images/logo.png`,
    image: `${site.url}/images/og-default.jpg`,
    description:
      'Woman-owned, minority-owned HR, staffing and workforce solutions firm serving government, corporate and nonprofit clients.',
    telephone: '+1-813-683-2995',
    email: site.email,
    address: {
      '@type': 'PostalAddress',
      streetAddress: credentials.address[0],
      addressLocality: 'Wimauma',
      addressRegion: 'FL',
      postalCode: '33598',
      addressCountry: 'US'
    },
    areaServed: [
      { '@type': 'City', name: 'Washington, DC' },
      { '@type': 'State', name: 'Virginia' },
      { '@type': 'State', name: 'Maryland' },
      { '@type': 'City', name: 'Tampa, FL' }
    ],
    founder: { '@type': 'Person', name: 'Desiree L. Watkins', jobTitle: 'Chief Executive Officer' },
    sameAs: [site.altSite],
    identifier: [
      { '@type': 'PropertyValue', propertyID: 'CAGE', value: credentials.cage },
      { '@type': 'PropertyValue', propertyID: 'UEI', value: credentials.uei }
    ],
    memberOf: [
      { '@type': 'Organization', name: 'National Association of Women Business Owners' },
      { '@type': 'Organization', name: 'African American Chamber of Commerce of Central Florida' }
    ]
  };

  // Escape "<" so the JSON can't close the script tag early
  const json = JSON.stringify(schema).replace(/</g, '\\u003c');
</script>

<svelte:head>
  {@html `<script type="application/ld+json">${json}</script>`}
</svelte:head>
