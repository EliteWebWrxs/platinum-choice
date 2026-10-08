<script>
  import { page } from '$app/state';
  import { site } from '#lib/site.js';

  /** @type {{ title?: string, description: string, image?: string }} */
  let { title, description, image = '/images/hero-federal.jpg' } = $props();

  const fullTitle = $derived(title ? `${title} | ${site.name}` : site.name);
  const canonical = $derived(new URL(page.url.pathname, site.url).href);
</script>

<svelte:head>
  <title>{fullTitle}</title>
  <meta name="description" content={description} />
  <link rel="canonical" href={canonical} />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content={site.name} />
  <meta property="og:title" content={fullTitle} />
  <meta property="og:description" content={description} />
  <meta property="og:url" content={canonical} />
  <meta property="og:image" content={new URL(image, site.url).href} />
  <meta name="twitter:card" content="summary_large_image" />
</svelte:head>
