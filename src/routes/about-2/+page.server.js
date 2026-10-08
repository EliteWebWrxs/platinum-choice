import { redirect } from '@sveltejs/kit';

// The old Wix site served the Government Entity page at /about-2
export const prerender = false;

export function load() {
  redirect(308, '/government-entity');
}
