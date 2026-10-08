<script>
  import { nav, site, credentials } from '#lib/site.js';
  import Facets from './Facets.svelte';

  const year = new Date().getFullYear();
</script>

<footer class="relative isolate overflow-hidden bg-ink text-paper/75 print:hidden">
  <Facets
    class="absolute inset-0 -z-10 h-full w-full opacity-[0.12]"
    seed={23}
    cols={12}
    rows={5}
  />
  <div class="h-1 w-full bg-brand"></div>

  <div class="mx-auto grid max-w-7xl gap-14 px-5 py-16 sm:px-8 lg:grid-cols-12 lg:py-20">
    <div class="lg:col-span-5">
      <p class="font-display text-3xl leading-tight text-paper sm:text-4xl">
        Helping organizations achieve success
        <em class="text-brand not-italic">through people.</em>
      </p>
      <p class="mt-6 max-w-md text-sm leading-relaxed">
        A woman-owned, minority-owned small business providing HR, workforce and management support
        to government, corporate, nonprofit and community clients.
      </p>
      <ul class="mt-8 flex flex-wrap gap-2" aria-label="Certifications">
        {#each credentials.certifications as cert (cert)}
          <li
            class="rounded-full border border-paper/20 px-3 py-1 text-xs font-semibold tracking-wider text-paper/90"
          >
            {cert}
          </li>
        {/each}
      </ul>
    </div>

    <nav aria-label="Footer" class="lg:col-span-2 lg:col-start-7">
      <h2 class="text-xs font-semibold tracking-[0.2em] text-gold uppercase">Explore</h2>
      <ul class="mt-5 space-y-3">
        {#each [...nav, { href: '/contact', label: 'Contact' }] as item (item.href)}
          <li><a href={item.href} class="transition hover:text-paper">{item.label}</a></li>
        {/each}
      </ul>
    </nav>

    <div class="lg:col-span-4">
      <h2 class="text-xs font-semibold tracking-[0.2em] text-gold uppercase">Get in touch</h2>
      <ul class="mt-5 space-y-3">
        <li><a href={site.phoneHref} class="transition hover:text-paper">{site.phone}</a></li>
        <li>
          <a href="mailto:{site.email}" class="break-all transition hover:text-paper"
            >{site.email}</a
          >
        </li>
        <li>
          <a href={site.altSite} class="transition hover:text-paper" rel="noopener">
            PlatinumChoiceConsulting.net
          </a>
        </li>
      </ul>
      <p class="mt-6 text-sm">Serving {site.serviceAreas.join(', ')}.</p>
    </div>
  </div>

  <div class="border-t border-paper/10">
    <div
      class="mx-auto flex max-w-7xl flex-col gap-2 px-5 py-6 text-xs sm:flex-row sm:items-center sm:justify-between sm:px-8"
    >
      <p>© {year} Platinum Choice Consulting. All rights reserved.</p>
      <p>CAGE {credentials.cage} · Incorporated in {credentials.incorporated}</p>
    </div>
  </div>
</footer>
