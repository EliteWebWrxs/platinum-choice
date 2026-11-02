import { fail } from '@sveltejs/kit';
import nodemailer from 'nodemailer';
import { GOOGLE_EMAIL, GOOGLE_EMAIL_PASSWORD, MAIL_HOST, MAIL_PORT } from '$app/env/private';
import { site } from '#lib/site.js';

export const prerender = false;

const recipients = ['platinumchoiceconsulting@gmail.com', 'dwatkinsplatinumchoice@gmail.com'];

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

    if (!GOOGLE_EMAIL || !GOOGLE_EMAIL_PASSWORD) {
      console.error(
        'Contact form: GOOGLE_EMAIL or GOOGLE_EMAIL_PASSWORD is not set, message not delivered'
      );
      return fail(503, {
        values,
        error: `Our form is temporarily unavailable. Please email us at ${site.email} or call ${site.phone}.`
      });
    }

    const transport = nodemailer.createTransport({
      host: MAIL_HOST,
      port: MAIL_PORT,
      secure: MAIL_PORT === 465,
      auth: { user: GOOGLE_EMAIL, pass: GOOGLE_EMAIL_PASSWORD }
    });

    try {
      await transport.sendMail({
        from: { name: 'PCC Website', address: GOOGLE_EMAIL },
        to: recipients,
        replyTo: { name: values.name, address: values.email },
        subject: `Website enquiry${values.organization ? ` from ${values.organization}` : ''}`,
        text: [
          `Organization: ${values.organization || '-'}`,
          `Contact name: ${values.name || '-'}`,
          `Email: ${values.email}`,
          '',
          values.message
        ].join('\n')
      });
    } catch (error) {
      console.error('Contact form: SMTP error', error);
      return fail(502, {
        values,
        error: `Sorry, something went wrong sending your message. Please email us at ${site.email}.`
      });
    }

    return { success: true };
  }
};
