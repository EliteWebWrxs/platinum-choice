<script>
  import Seo from '#lib/components/Seo.svelte';
  import PageHero from '#lib/components/PageHero.svelte';
  import CtaBand from '#lib/components/CtaBand.svelte';
  import { reveal } from '#lib/actions/reveal.js';
  import { site } from '#lib/site.js';

  const expertise = [
    'Human Resources Management',
    'Leadership/Team Development',
    'Workforce Development & Coaching',
    'Diversity & Inclusion Strategic Planning',
    'Employer-Employee Relations',
    'Financial Management & Budgeting Skills',
    'Organizational Skills'
  ];
</script>

<Seo
  title="About Us"
  description="Meet CEO Desiree L. Watkins and the team behind Platinum Choice Consulting, a woman-owned, minority-owned provider of HR and human capital professionals."
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
            src="/images/desiree-watkins.jpg"
            alt="Portrait of Desiree L. Watkins"
            width="761"
            height="1000"
            class="aspect-[4/5] w-full rounded-[2rem] object-cover object-top"
          />
        </div>

        <div class="mt-8 hidden lg:block">{@render contactCard()}</div>
      </div>
    </div>

    <div class="lg:col-span-7 lg:pl-6" use:reveal={120}>
      <div class="hidden lg:block">{@render ownerHeading()}</div>

      <div class="mt-8 space-y-6 text-lg leading-relaxed">
        <p>
          Desiree L. Watkins possesses 31 years of Federal Government experience directly supporting
          Federal Government programming, serving in leadership and advisory roles in executive
          management, human capital, managerial, operational, financial, workforce
          development/coaching and administrative issues. She has also served in the Executive and
          Legislative branches of the federal government.
        </p>
        <p>
          She possesses direct experience overseeing government contracts as a Contracting Officer
          Representative, acting as the business communications liaison between the Government and
          the private sector monitoring contract performance. Her experience includes providing
          technical expertise necessary to convey and meet the technical requirements of the
          Government.
        </p>
        <p>
          During her tenure as a Human Resources Executive at the Administrative Office of the U.S.
          Courts in Washington, DC, she was responsible for the implementation, management and
          enhancement of the agency’s Special Recruitment and Staffing Programs. She also
          established a Workforce Investment Program partnering with private sector companies
          enabling women entering/reentering the workforce with federal contract opportunities, many
          of whom successfully transitioned to permanent federal employment.
        </p>
        <p>
          Through this program she provided Career Development and Coaching, training, and mentoring
          to staff to guarantee smooth operations between participants and hiring managers. She
          developed comprehensive life skills modules in an academic environment, such as financial
          planning, employment readiness, preparation, retention and career development.
        </p>
        <p>
          She sits on the Board of the National Association of Women Business Owners (NAWBO), Tampa
          Lakeland Chapter.
        </p>
      </div>

      <h3 class="mt-14 text-xs font-semibold tracking-[0.25em] text-ink-muted uppercase">
        Expertise
      </h3>
      <ul class="mt-6 grid gap-3 sm:grid-cols-2">
        {#each expertise as item (item)}
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
