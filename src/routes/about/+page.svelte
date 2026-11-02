<script>
  import Seo from '#lib/components/Seo.svelte';
  import PageHero from '#lib/components/PageHero.svelte';
  import CtaBand from '#lib/components/CtaBand.svelte';
  import { reveal } from '#lib/actions/reveal.js';
  import { site } from '#lib/site.js';

  const competencies = [
    'Executive Leadership',
    'Human Capital Strategy',
    'Workforce Development',
    'Federal Contract Oversight and Administration',
    'Government & Private Sector Partnership Development',
    'Program Management',
    'Career Coaching & Executive Coaching',
    'Recruitment & Staffing',
    'Organizational Development',
    'Board Governance',
    'Training & Mentoring',
    'Stakeholder Relations'
  ];
</script>

<Seo
  title="About Us"
  description="Meet CEO Desiree L. Watkins and the team behind Platinum Choice Consulting, a woman-owned, minority-owned provider of HR and human capital professionals."
  image="/images/og/about.jpg"
  imageAlt="Small, but mighty: CEO Desiree L. Watkins of Platinum Choice Consulting"
/>

<PageHero
  eyebrow="About us"
  title="Small, but mighty."
  intro="Platinum Choice Consulting, Inc. (PCC) is a woman-owned, minority-owned small business established to provide business support and human capital professionals."
  seed={9}
/>

<!-- Company -->
<section class="mx-auto max-w-7xl px-5 py-24 sm:px-8 sm:py-32">
  <div class="grid gap-14 lg:grid-cols-12">
    <div class="space-y-6 text-lg leading-relaxed lg:col-span-7" use:reveal>
      <p class="font-display text-3xl leading-snug text-ink sm:text-4xl">
        PCC focuses on providing expert people, processes, and solutions to ensure each business has
        knowledgeable, experienced, and innovative people to carry them into the future.
      </p>
      <p>
        Small, but mighty, PCC stands head and shoulders above the competition. PCC builds on the
        experience of President, LaMont Flanagan Esq., a 40-year Local, State, and Federal
        executive, and Desiree Watkins, a 30-year State and Federal executive.
      </p>
      <p>
        PCC has assembled a cadre of subject matter experts, consultants, and administrative
        personnel to provide strategic, operational, and administrative support to a variety of
        clients, including community associations and non-profit organizations.
      </p>
      <p class="font-display text-2xl text-ink italic">
        Platinum Choice Consulting is <span class="text-brand not-italic">the solution.</span>
      </p>
    </div>

    <dl
      class="grid grid-cols-2 gap-px self-start overflow-hidden rounded-[2rem] border border-line bg-line lg:col-span-4 lg:col-start-9"
      use:reveal={120}
    >
      <div class="bg-paper p-7">
        <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
          Combined leadership
        </dt>
        <dd class="mt-3 font-display text-5xl text-ink">60<span class="text-brand">+</span></dd>
        <dd class="mt-1 text-sm">years of professional experience</dd>
      </div>
      <div class="bg-paper p-7">
        <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
          Federal experience
        </dt>
        <dd class="mt-3 font-display text-5xl text-ink">31</dd>
        <dd class="mt-1 text-sm">years, CEO Desiree L. Watkins</dd>
      </div>
      <div class="col-span-2 bg-paper p-7">
        <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">Ownership</dt>
        <dd class="mt-3 font-display text-xl text-ink sm:text-2xl">
          Woman-owned · <span class="whitespace-nowrap">Minority-owned</span>
        </dd>
      </div>
    </dl>
  </div>
</section>

{#snippet ownerHeading()}
  <p class="text-xs font-semibold tracking-[0.25em] text-flame-dark uppercase">Meet the owner</p>
  <h2 class="mt-5 font-display text-5xl leading-tight text-ink sm:text-6xl">Desiree L. Watkins</h2>
  <p class="mt-4 text-sm font-semibold tracking-[0.15em] text-ink-muted uppercase">
    Executive Leadership · Human Capital Management · Workforce Development · Organizational
    Excellence
  </p>
{/snippet}

{#snippet contactCard()}
  <div class="rounded-[1.5rem] border border-line bg-paper p-7">
    <p class="font-display text-2xl text-ink">Desiree L. Watkins</p>
    <p class="text-sm font-semibold tracking-[0.15em] text-flame-dark uppercase">
      Chief Executive Officer
    </p>
    <ul class="mt-5 space-y-2 text-[0.95rem]">
      <li>
        <span class="text-ink-muted">Phone</span>
        <a href={site.phoneHref} class="ml-2 font-medium text-ink hover:text-flame-dark"
          >{site.phone}</a
        >
      </li>
      <li>
        <span class="text-ink-muted">Mobile</span>
        <a href={site.mobileHref} class="ml-2 font-medium text-ink hover:text-flame-dark"
          >{site.mobile}</a
        >
      </li>
      <li>
        <a href="mailto:{site.email}" class="font-medium break-all text-ink hover:text-flame-dark"
          >{site.email}</a
        >
      </li>
    </ul>
  </div>
{/snippet}

<!-- Meet the owner -->
<section class="bg-paper-deep/60">
  <div class="mx-auto grid max-w-7xl gap-14 px-5 py-24 sm:px-8 sm:py-32 lg:grid-cols-12">
    <div class="lg:col-span-5" use:reveal>
      <div class="mb-10 lg:hidden">{@render ownerHeading()}</div>
      <div class="lg:sticky lg:top-28">
        <div class="relative">
          <div class="absolute -inset-2 -z-10 -rotate-2 rounded-[2.25rem] bg-brand"></div>
          <img
            src="/images/desiree-watkins-headshot.jpg"
            alt="Portrait of Desiree L. Watkins"
            width="1000"
            height="1500"
            class="aspect-[4/5] w-full rounded-[2rem] object-cover"
          />
        </div>

        <div class="mt-8 hidden lg:block">{@render contactCard()}</div>
      </div>
    </div>

    <div class="lg:col-span-7 lg:pl-6" use:reveal={120}>
      <div class="hidden lg:block">{@render ownerHeading()}</div>

      <div class="mt-8 space-y-6 text-lg leading-relaxed">
        <p>
          Desiree L. Watkins is a distinguished executive with more than 31 years of federal
          government experience, bringing extensive expertise in executive leadership, human capital
          management, workforce development, government contract oversight, and organizational
          effectiveness. A former Human Resources executive with the Administrative Office of the
          U.S. Courts in Washington, D.C., Ms. Watkins has built an accomplished career providing
          strategic leadership across the Executive, Judicial, and Legislative branches of the
          federal government. Her expertise includes strategic workforce planning, federal staffing
          and recruitment, career coaching, leadership development, government contract management,
          stakeholder engagement, and cultivating public-private partnerships.
        </p>
        <p>
          Throughout her career, Ms. Watkins has led initiatives that strengthen workforce
          readiness, enhance employee development, improve organizational performance, and advance
          operational excellence. Her leadership reflects a commitment to developing human capital
          strategies that align workforce capabilities with organizational goals and long-term
          institutional success.
        </p>
        <p>
          Beyond her federal service, Ms. Watkins has demonstrated a commitment to business
          leadership, professional development, and community engagement through her board service
          with the National Association of Women Business Owners (NAWBO), Tampa Lakeland Chapter.
          With a career distinguished by strategic vision, collaborative leadership, and a
          dedication to organizational excellence, Ms. Watkins brings valuable insight and
          executive-level expertise to initiatives focused on workforce innovation, talent
          development, and sustainable organizational growth.
        </p>
      </div>

      <h3 class="mt-14 text-xs font-semibold tracking-[0.25em] text-ink-muted uppercase">
        Core Competencies
      </h3>
      <ul class="mt-6 grid gap-3 sm:grid-cols-2">
        {#each competencies as item (item)}
          <li
            class="flex items-start gap-3 rounded-2xl border border-line bg-paper px-5 py-4 font-medium text-ink"
          >
            <span class="mt-2 size-2 shrink-0 rotate-45 bg-brand"></span>
            {item}
          </li>
        {/each}
      </ul>

      <div class="mt-12 lg:hidden">{@render contactCard()}</div>
    </div>
  </div>
</section>

<!-- Image band -->
<section class="mx-auto max-w-7xl px-5 pt-24 sm:px-8 sm:pt-32" use:reveal>
  <img
    src="/images/professional-women.jpg"
    alt="Diverse professional women working together"
    width="1200"
    height="800"
    loading="lazy"
    class="aspect-[4/3] w-full rounded-[2rem] object-cover sm:aspect-[21/9]"
  />
</section>

<CtaBand />
