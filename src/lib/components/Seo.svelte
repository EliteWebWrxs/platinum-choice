<script>
  import { page } from '$app/state';
  import { site } from '#lib/site.js';

  /**
   * @type {{
   *   title?: string,
   *   description: string,
   *   image?: { src: string, width: number, height: number, alt: string }
   * }}
   */
  let {
    title,
    description,
    image = {
      src: '/images/og-default.jpg',
      width: 1200,
      height: 630,
      alt: 'Platinum Choice Consulting: helping organizations succeed through people'
    }
  } = $props();

  const fullTitle = $derived(title ? `${title} | ${site.name}` : site.name);
  const canonical = $derived(new URL(page.url.pathname, site.url).href);
  const imageUrl = $derived(new URL(image.src, site.url).href);
</script>

<svelte:head>
  <title>{fullTitle}</title>
  <meta name="description" content={description} />
  <link rel="canonical" href={canonical} />

  <meta property="og:type" content="website" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:site_name" content={site.name} />
  <meta property="og:title" content={fullTitle} />
  <meta property="og:description" content={description} />
  <meta property="og:url" content={canonical} />
  <meta property="og:image" content={imageUrl} />
  <meta property="og:image:width" content={String(image.width)} />
  <meta property="og:image:height" content={String(image.height)} />
  <meta property="og:image:alt" content={image.alt} />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content={fullTitle} />
  <meta name="twitter:description" content={description} />
  <meta name="twitter:image" content={imageUrl} />
  <meta name="twitter:image:alt" content={image.alt} />
</svelte:head>
