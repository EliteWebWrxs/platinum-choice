import { defineEnvVars } from '@sveltejs/kit/env';

/** @param {string | undefined} value */
const optional = (value) => value || undefined;

export const variables = defineEnvVars({
  SITE_URL: {
    public: true,
    static: true,
    description:
      'Public origin of the production site, used for canonical links, social previews and the sitemap',
    schema: (value) => {
      const url = new URL(value || 'https://www.platinumchoice.consulting');
      return url.origin;
    }
  },
  RESEND_API_KEY: {
    description: 'API key for https://resend.com, used to deliver contact form messages',
    schema: optional
  },
  CONTACT_TO_EMAIL: {
    description: 'Inbox that receives contact form messages',
    schema: (value) => value || 'platinumchoiceconsulting@gmail.com'
  },
  CONTACT_FROM_EMAIL: {
    description: 'Verified Resend sender, e.g. "PCC Website <website@platinumchoice.consulting>"',
    schema: (value) => value || 'PCC Website <onboarding@resend.dev>'
  }
});
