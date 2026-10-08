import { fail } from '@sveltejs/kit';
import { CONTACT_FROM_EMAIL, CONTACT_TO_EMAIL, RESEND_API_KEY } from '$app/env/private';
import { site } from '#lib/site.js';

export const prerender = false;

/** @satisfies {import('./$types').Actions} */
export const actions = {
  default: async ({ request }) => {
    const form = await request.formData();

    /** @param {string} key */
    const field = (key) => String(form.get(key) ?? '').trim();

    const values = {
      organization: field('organization'),
      name: field('name'),
      email: field('email'),
      message: field('message')
    };

    // Bots fill in the hidden field; pretend it worked
    if (field('website')) return { success: true };

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(values.email)) {
      return fail(400, { values, error: 'Please enter a valid email address.' });
    }
    if (!values.message) {
      return fail(400, { values, error: 'Please include a message.' });
    }

    if (!RESEND_API_KEY) {
      console.error('Contact form: RESEND_API_KEY is not set, message not delivered');
      return fail(503, {
        values,
        error: `Our form is temporarily unavailable. Please email us at ${site.email} or call ${site.phone}.`
      });
    }

    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        authorization: `Bearer ${RESEND_API_KEY}`,
        'content-type': 'application/json'
      },
      body: JSON.stringify({
        from: CONTACT_FROM_EMAIL,
        to: [CONTACT_TO_EMAIL],
        reply_to: values.email,
        subject: `Website enquiry${values.organization ? ` from ${values.organization}` : ''}`,
        text: [
          `Organization: ${values.organization || '-'}`,
          `Contact name: ${values.name || '-'}`,
          `Email: ${values.email}`,
          '',
          values.message
        ].join('\n')
      })
    });

    if (!response.ok) {
      console.error('Contact form: Resend error', response.status, await response.text());
      return fail(502, {
        values,
        error: `Sorry, something went wrong sending your message. Please email us at ${site.email}.`
      });
    }

    return { success: true };
  }
};
