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
      const url = new URL(value || 'https://www.platinumchoiceconsultants.com');
      return url.origin;
    }
  },
  MAIL_HOST: {
    description: 'SMTP server used to deliver contact form messages',
    schema: (value) => value || 'smtp.gmail.com'
  },
  MAIL_PORT: {
    description: 'SMTP port; 465 connects over TLS, other ports upgrade with STARTTLS',
    schema: (value) => Number(value || 465)
  },
  GOOGLE_EMAIL: {
    description: 'SMTP login, and the address contact form messages are sent from',
    schema: optional
  },
  GOOGLE_EMAIL_PASSWORD: {
    description: 'SMTP password; for Gmail, an app password rather than the account password',
    schema: optional
  }
});
