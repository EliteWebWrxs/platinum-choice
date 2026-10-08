<script>
  import { enhance } from '$app/forms';
  import Seo from '#lib/components/Seo.svelte';
  import Facets from '#lib/components/Facets.svelte';
  import { site } from '#lib/site.js';

  /** @type {import('./$types').PageProps} */
  let { form } = $props();

  let sending = $state(false);

  const values = $derived(form && 'values' in form ? form.values : undefined);

  const input =
    'mt-2 block w-full rounded-xl border border-line bg-paper px-4 py-3.5 text-ink transition placeholder:text-ink-muted/60 focus:border-flame focus:ring-4 focus:ring-flame/15 focus:outline-none';
  const label = 'text-sm font-semibold text-ink';
</script>

<Seo
  title="Contact"
  description="Contact Platinum Choice Consulting to request staff or discuss workforce solutions. Call (813) 683-2995 or email PlatinumChoiceConsulting@gmail.com."
/>

<section class="relative isolate overflow-hidden">
  <div class="absolute inset-0 -z-10 grain"></div>
  <div class="mx-auto grid max-w-7xl gap-14 px-5 py-16 sm:px-8 sm:py-24 lg:grid-cols-12">
    <!-- Details -->
    <div class="lg:col-span-5">
      <p
        class="text-xs font-semibold tracking-[0.25em] text-flame-dark uppercase motion-safe:animate-rise"
      >
        Contact us
      </p>
      <h1
        class="mt-5 font-display text-6xl leading-[0.98] font-medium text-ink motion-safe:animate-rise sm:text-7xl"
        style="animation-delay: 80ms"
      >
        Let’s start a <em class="text-brand font-normal">conversation.</em>
      </h1>
      <p
        class="mt-7 max-w-md text-lg leading-relaxed motion-safe:animate-rise"
        style="animation-delay: 160ms"
      >
        Request staff, ask about our services, or tell us about your next project. We’ll be in touch
        soon.
      </p>

      <dl class="mt-12 space-y-7 motion-safe:animate-rise" style="animation-delay: 240ms">
        <div>
          <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">Phone</dt>
          <dd class="mt-1.5">
            <a href={site.phoneHref} class="font-display text-3xl text-ink hover:text-flame-dark"
              >{site.phone}</a
            >
          </dd>
        </div>
        <div>
          <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">Email</dt>
          <dd class="mt-1.5">
            <a
              href="mailto:{site.email}"
              class="font-display text-xl break-all text-ink hover:text-flame-dark sm:text-2xl"
              >{site.email}</a
            >
          </dd>
        </div>
        <div>
          <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">Serving</dt>
          <dd class="mt-1.5 text-lg">{site.serviceAreas.join(' · ')}</dd>
        </div>
      </dl>
    </div>

    <!-- Form -->
    <div class="lg:col-span-7">
      <div class="relative motion-safe:animate-rise" style="animation-delay: 160ms">
        <div
          class="absolute -inset-1 -z-10 rounded-[2.15rem] bg-brand opacity-70 sm:-inset-2 sm:rotate-1"
        ></div>
        <div
          class="relative overflow-hidden rounded-[2rem] border border-line bg-paper p-7 shadow-xl shadow-ink/5 sm:p-10"
        >
          {#if form?.success}
            <div class="py-16 text-center" role="status">
              <Facets class="mx-auto h-24 w-36 rounded-xl" seed={4} cols={4} rows={3} />
              <h2 class="mt-8 font-display text-4xl text-ink">Thanks for submitting!</h2>
              <p class="mt-4 text-lg">We’ve received your message and will be in touch soon.</p>
              <a href="/" class="mt-8 inline-flex font-semibold text-flame-dark hover:text-ink"
                >Back to home →</a
              >
            </div>
          {:else}
            <form
              method="post"
              use:enhance={() => {
                sending = true;
                return async ({ update }) => {
                  await update();
                  sending = false;
                };
              }}
              class="grid gap-6 sm:grid-cols-2"
            >
              <label class="sm:col-span-2">
                <span class={label}>Company / Organization</span>
                <input
                  name="organization"
                  autocomplete="organization"
                  value={values?.organization ?? ''}
                  class={input}
                />
              </label>

              <label>
                <span class={label}>Contact name</span>
                <input name="name" autocomplete="name" value={values?.name ?? ''} class={input} />
              </label>

              <label>
                <span class={label}
                  >Email <span class="text-flame-dark" aria-hidden="true">*</span></span
                >
                <input
                  name="email"
                  type="email"
                  required
                  autocomplete="email"
                  value={values?.email ?? ''}
                  class={input}
                />
              </label>

              <label class="sm:col-span-2">
                <span class={label}
                  >Message <span class="text-flame-dark" aria-hidden="true">*</span></span
                >
                <textarea name="message" rows="6" required class="{input} resize-y"
                  >{values?.message ?? ''}</textarea
                >
              </label>

              <!-- Honeypot: hidden from people, filled in by bots -->
              <div class="hidden" aria-hidden="true">
                <label>Website <input name="website" tabindex="-1" autocomplete="off" /></label>
              </div>

              {#if form && 'error' in form && form.error}
                <p
                  class="rounded-xl bg-ember/10 px-4 py-3 text-sm font-medium text-ember sm:col-span-2"
                  role="alert"
                >
                  {form.error}
                </p>
              {/if}

              <div class="flex items-center justify-between gap-4 sm:col-span-2">
                <p class="text-xs text-ink-muted">
                  <span class="text-flame-dark">*</span> Required
                </p>
                <button
                  type="submit"
                  disabled={sending}
                  class="inline-flex items-center gap-2 rounded-full bg-ink px-8 py-4 font-semibold text-paper transition hover:bg-flame-dark disabled:cursor-wait disabled:opacity-60"
                >
                  {sending ? 'Sending…' : 'Send message'}
                  <span aria-hidden="true">→</span>
                </button>
              </div>
            </form>
          {/if}
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Affiliations -->
<section class="border-t border-line bg-paper-deep/60">
  <div
    class="mx-auto flex max-w-7xl flex-col gap-8 px-5 py-14 sm:px-8 md:flex-row md:items-center md:justify-between"
  >
    <h2 class="text-xs font-semibold tracking-[0.25em] text-ink-muted uppercase">Affiliations</h2>
    <div class="flex flex-wrap items-center gap-10">
      <img
        src="/images/nawbo-lakeland.png"
        alt="National Association of Women Business Owners, Lakeland Metro"
        width="341"
        height="100"
        loading="lazy"
        class="h-14 w-auto"
      />
      <img
        src="/images/aacc-central-florida.png"
        alt="African American Chamber of Commerce of Central Florida"
        width="290"
        height="85"
        loading="lazy"
        class="h-14 w-auto"
      />
    </div>
  </div>
</section>
