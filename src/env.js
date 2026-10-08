import { defineEnvVars } from '@sveltejs/kit/env';

/** @param {string | undefined} value */
const optional = (value) => value || undefined;

export const variables = defineEnvVars({
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
