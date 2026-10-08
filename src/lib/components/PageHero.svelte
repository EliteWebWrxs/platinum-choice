<script>
  import Facets from './Facets.svelte';

  /** @type {{ eyebrow: string, title: string, intro?: string, seed?: number, children?: import('svelte').Snippet }} */
  let { eyebrow, title, intro, seed = 3, children } = $props();
</script>

<section class="relative isolate overflow-hidden bg-ink text-paper">
  <Facets class="absolute inset-0 -z-10 h-full w-full opacity-25" {seed} />
  <div
    class="absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_top_right,rgba(240,90,40,0.35),transparent_55%)]"
  ></div>
  <div class="mx-auto max-w-7xl px-5 pt-20 pb-16 sm:px-8 sm:pt-28 sm:pb-24">
    <p class="text-xs font-semibold tracking-[0.25em] text-gold uppercase motion-safe:animate-rise">
      {eyebrow}
    </p>
    <h1
      class="mt-5 max-w-4xl font-display text-5xl leading-[1.02] font-medium tracking-tight text-balance text-paper motion-safe:animate-rise sm:text-7xl"
      style="animation-delay: 80ms"
    >
      {title}
    </h1>
    {#if intro}
      <p
        class="mt-7 max-w-2xl text-lg leading-relaxed text-paper/75 motion-safe:animate-rise"
        style="animation-delay: 160ms"
      >
        {intro}
      </p>
    {/if}
    {@render children?.()}
  </div>
  <div class="h-1 w-full bg-brand"></div>
</section>
