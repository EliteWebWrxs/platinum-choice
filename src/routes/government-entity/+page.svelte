<script>
  import Seo from '#lib/components/Seo.svelte';
  import PageHero from '#lib/components/PageHero.svelte';
  import CtaBand from '#lib/components/CtaBand.svelte';
  import { reveal } from '#lib/actions/reveal.js';
  import { credentials, site } from '#lib/site.js';

  const registration = [
    { label: 'Corporate name', value: credentials.legalName },
    { label: 'State of incorporation', value: credentials.incorporated },
    { label: 'Unique Entity ID (SAM)', value: credentials.uei, mono: true },
    { label: 'CAGE code', value: credentials.cage, mono: true },
    { label: 'EIN', value: credentials.ein, mono: true }
  ];
</script>

<Seo
  title="Government Entity"
  description="Platinum Choice Consulting is a HUBZone-certified, woman minority-owned company providing workforce development consulting to government agencies. UEI ZEJBM3DSLF58, CAGE 8UAV4."
  image="/images/government-team.jpg"
/>

<PageHero
  eyebrow="Government entity"
  title="PCC Government Entity"
  intro="A HUBZone-certified, woman minority-owned company helping agencies build a workforce that stays."
  seed={53}
>
  <ul class="mt-10 flex flex-wrap gap-2 motion-safe:animate-rise" style="animation-delay: 240ms">
    {#each credentials.certifications as cert (cert)}
      <li
        class="rounded-full border border-paper/20 bg-paper/5 px-4 py-2 text-sm font-semibold tracking-wider text-paper/90"
      >
        {cert}
      </li>
    {/each}
  </ul>
</PageHero>

<!-- Overview -->
<section class="mx-auto max-w-7xl px-5 py-24 sm:px-8 sm:py-32">
  <div class="grid items-start gap-14 lg:grid-cols-12">
    <div class="space-y-6 text-lg leading-relaxed lg:col-span-6" use:reveal>
      <p class="font-display text-3xl leading-snug text-ink sm:text-4xl">
        PCC recognizes the cost benefits of recruiting a workforce that remains long-term employees.
      </p>
      <p>
        Our team has experience providing consultative services to build Workforce Development
        Programs that assist organizations in developing their workforce, and developing career
        training programs to leverage our clients’ ability to identify people with the essential
        skills for entry-level opportunities.
      </p>
      <p>
        We specialize in assisting clients with defining the capabilities essential for their
        current and future workforce.
      </p>
      <p class="border-l-2 border-flame pl-5 font-display text-2xl text-ink italic">
        We strive to meet our clients’ needs cost-effectively, work within budget and deliver
        punctually.
      </p>
    </div>

    <div class="lg:col-span-5 lg:col-start-8" use:reveal={120}>
      <div class="relative">
        <div class="absolute -inset-2 -z-10 rotate-2 rounded-[2.25rem] bg-brand"></div>
        <img
          src="/images/government-team.jpg"
          alt="A diverse team of professionals standing together in an office lobby"
          width="780"
          height="440"
          loading="lazy"
          class="aspect-[4/3] w-full rounded-[2rem] object-cover"
        />
      </div>

      <div class="mt-10 flex gap-5 rounded-[1.5rem] border border-line bg-paper-deep/60 p-6">
        <img
          src="/images/sba-hubzone.jpg"
          alt="SBA HUBZone certified"
          width="160"
          height="200"
          loading="lazy"
          class="h-20 w-auto shrink-0 rounded"
        />
        <p class="leading-relaxed">
          PCC is a HUBZone, woman minority-owned company, certified and entitled to all the
          provisions designed to promote economic development and employment opportunities in
          metropolitan or rural areas with low income, high poverty rates, and/or high unemployment
          rates.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Company data -->
<section class="relative isolate overflow-hidden bg-ink text-paper/80">
  <div class="mx-auto max-w-7xl px-5 py-24 sm:px-8 sm:py-32">
    <div class="flex flex-col justify-between gap-6 md:flex-row md:items-end" use:reveal>
      <div>
        <p class="text-xs font-semibold tracking-[0.25em] text-gold uppercase">
          For contracting officers
        </p>
        <h2 class="mt-5 font-display text-4xl leading-tight text-paper sm:text-6xl">
          Company data
        </h2>
      </div>
      <a
        href="/files/pcc-capability-statement.pdf"
        download
        class="inline-flex shrink-0 items-center gap-2 rounded-full bg-paper px-6 py-3.5 font-semibold text-ink transition hover:bg-gold"
      >
        Capability statement <span aria-hidden="true">↓</span>
      </a>
    </div>

    <div class="mt-14 grid gap-6 lg:grid-cols-2">
      <!-- Registration -->
      <dl
        class="divide-y divide-paper/10 rounded-[2rem] border border-paper/15 px-7 sm:px-9"
        use:reveal
      >
        {#each registration as row (row.label)}
          <div
            class="flex flex-col gap-1 py-5 sm:flex-row sm:items-baseline sm:justify-between sm:gap-6"
          >
            <dt class="text-sm text-paper/60">{row.label}</dt>
            <dd
              class={[
                'text-paper',
                row.mono ? 'font-mono text-lg tracking-wider' : 'font-display text-xl'
              ]}
            >
              {row.value}
            </dd>
          </div>
        {/each}
        <div
          class="flex flex-col gap-1 py-5 sm:flex-row sm:items-baseline sm:justify-between sm:gap-6"
        >
          <dt class="text-sm text-paper/60">Corporate address</dt>
          <dd class="font-display text-xl text-paper sm:text-right">
            {credentials.address[0]}<br />{credentials.address[1]}
          </dd>
        </div>
        <div
          class="flex flex-col gap-1 py-5 sm:flex-row sm:items-baseline sm:justify-between sm:gap-6"
        >
          <dt class="text-sm text-paper/60">Contact persons</dt>
          <dd class="font-display text-xl text-paper sm:text-right">{credentials.contacts}</dd>
        </div>
        <div
          class="flex flex-col gap-1 py-5 sm:flex-row sm:items-baseline sm:justify-between sm:gap-6"
        >
          <dt class="text-sm text-paper/60">Business contact</dt>
          <dd class="text-paper sm:text-right">
            <a href={site.phoneHref} class="font-display text-xl hover:text-gold">{site.phone}</a
            ><br />
            <a href="mailto:{site.email}" class="break-all hover:text-gold">{site.email}</a>
          </dd>
        </div>
      </dl>

      <div class="flex flex-col gap-6">
        <!-- Certifications -->
        <div class="rounded-[2rem] border border-paper/15 p-7 sm:p-9" use:reveal={100}>
          <h3 class="text-xs font-semibold tracking-[0.2em] text-gold uppercase">
            Special certifications
          </h3>
          <ul class="mt-6 space-y-4">
            {#each credentials.certifications as cert (cert)}
              <li class="grid grid-cols-[5.5rem_1fr] items-baseline gap-4">
                <span class="font-display text-xl text-paper">{cert}</span>
                <span class="text-sm">{credentials.certificationNames[cert]}</span>
              </li>
            {/each}
          </ul>
        </div>

        <!-- Codes -->
        <div class="rounded-[2rem] border border-paper/15 p-7 sm:p-9" use:reveal={200}>
          <h3 class="text-xs font-semibold tracking-[0.2em] text-gold uppercase">NAICS codes</h3>
          <ul class="mt-5 flex flex-wrap gap-2">
            {#each credentials.naics as code (code)}
              <li class="rounded-full bg-paper/10 px-3.5 py-1.5 font-mono text-paper">{code}</li>
            {/each}
          </ul>
          <h3 class="mt-8 text-xs font-semibold tracking-[0.2em] text-gold uppercase">PSC codes</h3>
          <ul class="mt-5 flex flex-wrap gap-2">
            {#each credentials.psc as code (code)}
              <li class="rounded-full bg-paper/10 px-3.5 py-1.5 font-mono text-paper">{code}</li>
            {/each}
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="h-1 w-full bg-brand"></div>
</section>

<CtaBand
  title="Partner with PCC"
  text="Contracting officers and primes: reach out to discuss workforce development, staffing and HR support for your next requirement."
/>
