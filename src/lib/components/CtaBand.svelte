<script>
  import { reveal } from '#lib/actions/reveal.js';
  import { site } from '#lib/site.js';

  /** @type {{ title?: string, text?: string }} */
  let {
    title = 'Let’s work together',
    text = 'Tell us what your organization needs. We’ll help you find the right people and the right plan.'
  } = $props();
</script>

<section class="px-5 py-20 sm:px-8 sm:py-28">
  <div
    use:reveal
    class="relative isolate mx-auto max-w-7xl overflow-hidden rounded-[2rem] bg-paper-deep px-6 py-14 sm:px-14 sm:py-20"
  >
    <div
      class="absolute -top-24 -right-24 -z-10 size-72 rounded-full bg-brand opacity-30 blur-3xl"
    ></div>
    <div class="grid items-end gap-10 lg:grid-cols-[1.4fr_1fr]">
      <div>
        <h2 class="font-display text-4xl leading-tight text-ink sm:text-6xl">{title}</h2>
        <p class="mt-5 max-w-xl text-lg leading-relaxed">{text}</p>
      </div>
      <div class="flex flex-col gap-3 sm:flex-row lg:justify-end">
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
