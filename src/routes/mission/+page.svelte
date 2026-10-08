<script>
  import Seo from '#lib/components/Seo.svelte';
  import Facets from '#lib/components/Facets.svelte';
  import { reveal } from '#lib/actions/reveal.js';
  import { site } from '#lib/site.js';
</script>

<Seo
  title="Mission"
  description="Our mission is simple: to help organizations achieve success through people by providing quality professionals and solutions to our clients and the populations we serve."
/>

<section class="relative isolate overflow-hidden bg-ink text-paper">
  <Facets class="absolute inset-0 -z-10 h-full w-full opacity-25" seed={17} cols={11} rows={7} />
  <div
    class="absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_bottom_left,rgba(214,36,110,0.3),transparent_55%),radial-gradient(ellipse_at_top_right,rgba(247,181,43,0.22),transparent_50%)]"
  ></div>

  <div class="mx-auto max-w-6xl px-5 py-28 sm:px-8 sm:py-40">
    <p class="text-xs font-semibold tracking-[0.25em] text-gold uppercase motion-safe:animate-rise">
      Our mission is simple
    </p>
    <h1
      class="mt-8 font-display text-[2.6rem] leading-[1.08] font-normal text-balance text-paper motion-safe:animate-rise sm:text-7xl"
      style="animation-delay: 100ms"
    >
      To help organizations achieve success
      <em class="text-brand">through people</em>, by providing quality professionals and solutions
      to our clients and the populations that we serve.
    </h1>
  </div>
  <div class="h-1 w-full bg-brand"></div>
</section>

<section class="mx-auto max-w-7xl px-5 py-24 sm:px-8 sm:py-32">
  <div class="grid items-center gap-14 lg:grid-cols-2">
    <div class="relative" use:reveal>
      <div class="absolute -top-3 -left-3 -z-10 h-3/4 w-3/4 rounded-[2rem] bg-brand"></div>
      <img
        src="/images/work-together.jpg"
        alt="Colleagues shaking hands across a meeting table"
        width="508"
        height="339"
        loading="lazy"
        class="aspect-[3/2] w-full rounded-[2rem] object-cover"
      />
    </div>

    <div use:reveal={120}>
      <h2 class="font-display text-5xl leading-tight text-ink sm:text-7xl">Let’s work together</h2>
      <p class="mt-6 max-w-lg text-lg leading-relaxed">
        Whether you need staff for a short-term project, a long-term placement, or a partner to plan
        your workforce, we’re ready to help.
      </p>
      <div class="mt-10 flex flex-col gap-3 sm:flex-row">
        <a
          href="/contact"
          class="inline-flex items-center justify-center gap-2 rounded-full bg-ink px-7 py-4 font-semibold text-paper transition hover:bg-flame-dark"
        >
          Contact us <span aria-hidden="true">→</span>
        </a>
        <a
          href={site.phoneHref}
          class="inline-flex items-center justify-center rounded-full border border-ink/20 px-7 py-4 font-semibold text-ink transition hover:border-ink"
        >
          {site.phone}
        </a>
      </div>
    </div>
  </div>
</section>
