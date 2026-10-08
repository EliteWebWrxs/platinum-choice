<script>
  import { page } from '$app/state';
  import { nav } from '#lib/site.js';

  let open = $state(false);
  let scrollY = $state(0);
  const scrolled = $derived(scrollY > 8);

  // Close the mobile menu whenever the route changes
  $effect(() => {
    page.url.pathname;
    open = false;
  });

  /** @param {string} href */
  const isActive = (href) =>
    href === '/' ? page.url.pathname === '/' : page.url.pathname.startsWith(href);
</script>

<svelte:window bind:scrollY />

<header
  class={[
    'sticky top-0 z-50 border-b transition-colors duration-300 print:hidden',
    'bg-paper/90 backdrop-blur-md',
    scrolled || open ? 'border-line' : 'border-transparent'
  ]}
>
  <a
    href="#main"
    class="sr-only rounded-full bg-ink px-4 py-2 text-paper focus:not-sr-only focus:absolute focus:top-3 focus:left-3"
  >
    Skip to main content
  </a>

  <div class="mx-auto flex h-20 max-w-7xl items-center justify-between gap-6 px-5 sm:px-8">
    <a href="/" class="shrink-0" aria-label="Platinum Choice Consulting home">
      <img src="/images/logo.png" alt="" width="640" height="296" class="h-13 w-auto sm:h-16" />
    </a>

    <nav aria-label="Main" class="hidden xl:block">
      <ul class="flex items-center gap-1">
        {#each nav as item (item.href)}
          <li>
            <a
              href={item.href}
              aria-current={isActive(item.href) ? 'page' : undefined}
              class={[
                'relative rounded-full px-3.5 py-2 text-[0.94rem] font-medium transition-colors',
                isActive(item.href) ? 'text-ink' : 'text-ink-muted hover:text-ink'
              ]}
            >
              {item.label}
              {#if isActive(item.href)}
                <span class="absolute inset-x-3.5 -bottom-0.5 h-0.5 rounded-full bg-brand"></span>
              {/if}
            </a>
          </li>
        {/each}
      </ul>
    </nav>

    <div class="flex items-center gap-3">
      <a
        href="/contact"
        class="hidden rounded-full bg-ink px-5 py-2.5 text-sm font-semibold text-paper transition hover:bg-flame-dark sm:inline-flex"
      >
        Contact Us
      </a>

      <button
        type="button"
        class="inline-flex size-11 items-center justify-center rounded-full border border-line text-ink transition hover:border-ink xl:hidden"
        aria-expanded={open}
        aria-controls="mobile-menu"
        aria-label={open ? 'Close menu' : 'Open menu'}
        onclick={() => (open = !open)}
      >
        <svg
          viewBox="0 0 24 24"
          class="size-5"
          fill="none"
          stroke="currentColor"
          stroke-width="1.8"
          aria-hidden="true"
        >
          {#if open}
            <path d="M6 6l12 12M18 6L6 18" stroke-linecap="round" />
          {:else}
            <path d="M4 7h16M4 12h16M4 17h10" stroke-linecap="round" />
          {/if}
        </svg>
      </button>
    </div>
  </div>

  {#if open}
    <nav id="mobile-menu" aria-label="Main" class="border-t border-line bg-paper xl:hidden">
      <ul class="mx-auto max-w-7xl px-5 py-4 sm:px-8">
        {#each [...nav, { href: '/contact', label: 'Contact' }] as item, i (item.href)}
          <li class="motion-safe:animate-rise" style="animation-delay: {i * 40}ms">
            <a
              href={item.href}
              aria-current={isActive(item.href) ? 'page' : undefined}
              class={[
                'flex items-center justify-between border-b border-line py-4 font-display text-2xl',
                isActive(item.href) ? 'text-flame-dark' : 'text-ink'
              ]}
            >
              {item.label}
              <span aria-hidden="true" class="text-base text-ink-muted">→</span>
            </a>
          </li>
        {/each}
      </ul>
    </nav>
  {/if}
</header>
