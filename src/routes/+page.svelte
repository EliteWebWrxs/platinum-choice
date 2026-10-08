<script>
  import Seo from '#lib/components/Seo.svelte';
  import Facets from '#lib/components/Facets.svelte';
  import CtaBand from '#lib/components/CtaBand.svelte';
  import { reveal } from '#lib/actions/reveal.js';
  import { credentials, site } from '#lib/site.js';

  const services = [
    {
      title: 'Workforce Solutions',
      text: 'We recruit and place candidates across HR, office support, finance, legal, marketing, health care administration and more.'
    },
    {
      title: 'Direct Hire',
      text: 'Recruiters with decades of experience, working with our sourcing team to find the most qualified candidates.'
    },
    {
      title: 'Customized Solutions',
      text: 'A workforce plan designed around you that reduces costs, enhances productivity and streamlines requisitions.'
    },
    {
      title: 'Introductory Consultation',
      text: 'Not sure where to turn next? We help you plan and execute with bold, insightful decisions.'
    }
  ];

  /** @param {string} name */
  const initials = (name) =>
    name
      .split(/\s+/)
      .map((part) => part[0])
      .join('')
      .toUpperCase();

  // Add `photo: '/images/...'` to an entry to show a real headshot instead of initials
  /** @type {{ quote: string, name: string, photo?: string }[]} */
  const testimonials = [
    {
      quote:
        'PCC is an amazing company to work for! They understand their clients & have helped me establish my career!',
      name: 'Rhonda Smith'
    },
    {
      quote:
        'PCC has helped me build a great company by sending me professional, ready to work, experienced staff!',
      name: 'Johnathan McInnis'
    },
    {
      quote:
        'PCC helped me grow my company with high quality staff and significant resource skills.',
      name: 'Mariah Bowens'
    }
  ];
</script>

<Seo
  description="Platinum Choice Consulting is a woman-owned, minority-owned HR and workforce solutions firm serving government, corporate and nonprofit clients in Washington DC, Virginia, Maryland and Tampa."
/>

<!-- Hero -->
<section class="relative isolate overflow-hidden">
  <div class="absolute inset-0 -z-10 grain"></div>
  <div
    class="mx-auto grid max-w-7xl items-center gap-12 px-5 pt-10 pb-20 sm:px-8 lg:grid-cols-[1.15fr_1fr] lg:gap-16 lg:pt-16 lg:pb-28"
  >
    <div>
      <p
        class="inline-flex items-center gap-2.5 rounded-full border border-line bg-paper px-4 py-1.5 text-sm font-medium text-ink motion-safe:animate-rise"
      >
        <span class="size-2 rounded-full bg-brand"></span>
        A Woman Owned Business
      </p>

      <h1
        class="mt-7 font-display text-[3.4rem] leading-[0.95] font-medium tracking-tight text-ink motion-safe:animate-rise sm:text-8xl"
        style="animation-delay: 80ms"
      >
        Helping you <br class="hidden sm:block" />become
        <em class="text-brand pr-2 font-normal">great.</em>
      </h1>

      <p
        class="mt-8 max-w-xl text-lg leading-relaxed motion-safe:animate-rise"
        style="animation-delay: 160ms"
      >
        Platinum Choice Consulting provides a full range of HR and management support services
        personnel to provide strategic and operational administrative support. We assist companies
        with workload fluctuations and ensure each business has knowledgeable, experienced, and
        innovative people to carry them into the future. We provide premium employment
        opportunities.
      </p>

      <div
        class="mt-10 flex flex-col gap-3 motion-safe:animate-rise sm:flex-row"
        style="animation-delay: 240ms"
      >
        <a
          href="/contact"
          class="inline-flex items-center justify-center gap-2 rounded-full bg-ink px-7 py-4 font-semibold text-paper transition hover:bg-flame-dark"
        >
          Request staff <span aria-hidden="true">→</span>
        </a>
        <a
          href="/services"
          class="inline-flex items-center justify-center rounded-full border border-ink/20 px-7 py-4 font-semibold text-ink transition hover:border-ink"
        >
          Explore services
        </a>
      </div>
    </div>

    <div class="relative motion-safe:animate-rise" style="animation-delay: 200ms">
      <div class="absolute -inset-3 -z-10 rotate-2 rounded-[2.25rem] bg-brand opacity-80"></div>
      <div class="relative overflow-hidden rounded-[2rem] bg-ink">
        <img
          src="/images/hero-federal.jpg"
          alt="Government office towers and an American flag against a blue sky"
          width="2000"
          height="1334"
          class="aspect-[4/3] w-full object-cover opacity-90 sm:aspect-[4/5]"
        />
        <Facets
          class="absolute inset-0 h-full w-full opacity-40 mix-blend-screen"
          seed={11}
          cols={6}
          rows={7}
        />
      </div>
      <div
        class="absolute -bottom-6 -left-4 max-w-[16rem] rounded-2xl border border-line bg-paper p-5 shadow-xl shadow-ink/10 sm:-left-10"
      >
        <p class="text-xs font-semibold tracking-[0.2em] text-flame-dark uppercase">Now serving</p>
        <p class="mt-2 font-display text-xl leading-snug text-ink">
          {site.serviceAreas.join(' · ')}
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Credentials -->
<section aria-label="Certifications" class="border-y border-line bg-paper-deep/60">
  <div
    class="mx-auto flex max-w-7xl flex-col gap-5 px-5 py-7 sm:px-8 md:flex-row md:items-center md:justify-between"
  >
    <p class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
      Certified &amp; registered
    </p>
    <ul class="flex flex-wrap gap-x-8 gap-y-3">
      {#each credentials.certifications as cert (cert)}
        <li class="font-display text-2xl text-ink">{cert}</li>
      {/each}
      <li class="font-display text-2xl text-ink-muted">CAGE {credentials.cage}</li>
    </ul>
  </div>
</section>

<!-- Who we are -->
<section class="mx-auto max-w-7xl px-5 py-24 sm:px-8 sm:py-32">
  <div class="grid gap-14 lg:grid-cols-12">
    <div class="lg:col-span-7" use:reveal>
      <p class="text-xs font-semibold tracking-[0.25em] text-flame-dark uppercase">Who we are</p>
      <p class="mt-6 font-display text-3xl leading-snug text-ink sm:text-[2.6rem] sm:leading-[1.2]">
        We are a business engaged in the mission of meeting the
        <span class="italic">human capital needs</span> of government, corporate clients, nonprofits,
        and the communities we serve.
      </p>
    </div>

    <div class="space-y-10 lg:col-span-4 lg:col-start-9 lg:pt-12" use:reveal={120}>
      <div>
        <h2 class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
          Service areas
        </h2>
        <p class="mt-3 text-lg leading-relaxed">
          PCC currently services the Washington, DC, Virginia, Maryland, and Tampa metropolitan
          areas.
        </p>
      </div>
      <div>
        <h2 class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">Memberships</h2>
        <p class="mt-3 text-lg leading-relaxed">
          We are members of the National Association of Women Business Owners and the African
          American Chamber of Commerce, Central Florida.
        </p>
        <div class="mt-6 flex flex-wrap items-center gap-6">
          <img
            src="/images/nawbo-lakeland.png"
            alt="National Association of Women Business Owners, Lakeland Metro"
            width="341"
            height="100"
            class="h-11 w-auto"
            loading="lazy"
          />
          <img
            src="/images/aacc-central-florida.png"
            alt="African American Chamber of Commerce of Central Florida"
            width="290"
            height="85"
            class="h-11 w-auto"
            loading="lazy"
          />
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Personalized client service -->
<section class="relative isolate overflow-hidden bg-ink text-paper/80">
  <Facets class="absolute inset-0 -z-10 h-full w-full opacity-15" seed={5} cols={10} rows={6} />
  <div
    class="mx-auto grid max-w-7xl items-center gap-14 px-5 py-24 sm:px-8 sm:py-32 lg:grid-cols-2"
  >
    <div class="relative" use:reveal>
      <img
        src="/images/professional-women.jpg"
        alt="Diverse professional women collaborating in an office"
        width="1200"
        height="800"
        loading="lazy"
        class="aspect-[4/3] w-full rounded-[2rem] object-cover"
      />
      <div class="absolute -right-3 -bottom-3 -z-10 h-2/3 w-2/3 rounded-[2rem] bg-brand"></div>
    </div>

    <div use:reveal={120}>
      <p class="text-xs font-semibold tracking-[0.25em] text-gold uppercase">Our approach</p>
      <h2 class="mt-5 font-display text-4xl leading-tight text-paper sm:text-6xl">
        Personalized client service
      </h2>
      <p class="mt-7 text-lg leading-relaxed">
        Platinum Choice Consulting is recognized for our outstanding service to each and every one
        of our clients.
      </p>
      <p class="mt-5 text-lg leading-relaxed">
        We specialize in short-term and long-term Workforce Solutions. Founded in Virginia as a
        female minority business, we have gained a deep knowledge of the intricacies of the local
        job market and the essential needs of government and corporate clients.
      </p>
      <a
        href="/about"
        class="mt-9 inline-flex items-center gap-2 font-semibold text-gold transition hover:text-paper"
      >
        Meet our team <span aria-hidden="true">→</span>
      </a>
    </div>
  </div>
</section>

<!-- Services preview -->
<section class="mx-auto max-w-7xl px-5 py-24 sm:px-8 sm:py-32">
  <div class="flex flex-col justify-between gap-6 md:flex-row md:items-end" use:reveal>
    <div>
      <p class="text-xs font-semibold tracking-[0.25em] text-flame-dark uppercase">What we do</p>
      <h2 class="mt-5 max-w-2xl font-display text-4xl leading-tight text-ink sm:text-6xl">
        Workforce solutions, built around you
      </h2>
    </div>
    <a
      href="/services"
      class="inline-flex shrink-0 items-center gap-2 font-semibold text-ink transition hover:text-flame-dark"
    >
      All services <span aria-hidden="true">→</span>
    </a>
  </div>

  <ol
    class="mt-14 grid gap-px overflow-hidden rounded-[2rem] border border-line bg-line sm:grid-cols-2"
  >
    {#each services as service, i (service.title)}
      <li use:reveal={i * 80}>
        <a
          href="/services"
          class="group relative flex h-full flex-col bg-paper p-8 transition-colors hover:bg-paper-deep sm:p-10"
        >
          <span class="font-display text-lg text-ink-muted">0{i + 1}</span>
          <h3 class="mt-8 font-display text-3xl text-ink">{service.title}</h3>
          <p class="mt-4 leading-relaxed">{service.text}</p>
          <span
            aria-hidden="true"
            class="absolute bottom-0 left-0 h-1 w-0 bg-brand transition-all duration-500 group-hover:w-full"
          ></span>
        </a>
      </li>
    {/each}
  </ol>
</section>

<!-- Testimonials -->
<section class="bg-paper-deep/60">
  <div class="mx-auto max-w-7xl px-5 py-24 sm:px-8 sm:py-32">
    <p class="text-xs font-semibold tracking-[0.25em] text-flame-dark uppercase" use:reveal>
      What people say
    </p>
    <div class="mt-12 grid gap-10 lg:grid-cols-3 lg:gap-12">
      {#each testimonials as t, i (t.name)}
        <figure class="flex flex-col border-t-2 border-ink pt-8" use:reveal={i * 100}>
          <span aria-hidden="true" class="text-brand font-display text-7xl leading-none">“</span>
          <blockquote class="-mt-4 flex-1 font-display text-2xl leading-snug text-ink">
            {t.quote}
          </blockquote>
          <figcaption class="mt-8 flex items-center gap-4">
            {#if t.photo}
              <img
                src={t.photo}
                alt=""
                width="56"
                height="56"
                loading="lazy"
                class="size-14 rounded-full object-cover ring-2 ring-flame/60 ring-offset-2 ring-offset-paper-deep"
              />
            {:else}
              <span
                aria-hidden="true"
                class="grid size-14 shrink-0 place-items-center rounded-full bg-brand p-0.5"
              >
                <span
                  class="grid size-full place-items-center rounded-full bg-ink font-display text-xl tracking-wide text-paper"
                >
                  {initials(t.name)}
                </span>
              </span>
            {/if}
            <span class="text-sm font-semibold tracking-[0.15em] text-ink-muted uppercase">
              {t.name}
            </span>
          </figcaption>
        </figure>
      {/each}
    </div>
  </div>
</section>

<CtaBand />
