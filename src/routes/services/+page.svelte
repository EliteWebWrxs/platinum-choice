<script>
  import Seo from '#lib/components/Seo.svelte';
  import PageHero from '#lib/components/PageHero.svelte';
  import CtaBand from '#lib/components/CtaBand.svelte';
  import { reveal } from '#lib/actions/reveal.js';

  const placements = [
    'Human Resources',
    'Office Support',
    'Executive/Administrative Assistants',
    'Financial',
    'Legal',
    'Editorial',
    'Accounting',
    'Marketing',
    'Graphic Design',
    'Social Media'
  ];

  const focusAreas = [
    'Workforce & Leadership Development',
    'Emotional Management',
    'Communication',
    'Training the Trainer',
    'Coaching & Mentoring'
  ];
</script>

<Seo
  title="Services"
  description="Workforce solutions, direct hire, customized staffing and consulting from Platinum Choice Consulting, backed by 60+ years of professional experience."
/>

<PageHero
  eyebrow="Services"
  title="Team Platinum Choice Consultants"
  intro="Team PCC possesses more than 60 years of professional experience and demonstrated ability to effectively and efficiently provide consultative, developmental, and facilitative support."
  seed={31}
>
  <ul class="mt-10 flex flex-wrap gap-2 motion-safe:animate-rise" style="animation-delay: 240ms">
    {#each focusAreas as area (area)}
      <li class="rounded-full border border-paper/20 bg-paper/5 px-4 py-2 text-sm text-paper/90">
        {area}
      </li>
    {/each}
  </ul>
  <p class="mt-8 max-w-2xl text-paper/70 motion-safe:animate-rise" style="animation-delay: 300ms">
    Team PCC served as a Training Facilitator for Supervisory Development Programs under contract
    with federal government agencies.
  </p>
</PageHero>

<!-- 01 Workforce Solutions -->
<section class="mx-auto max-w-7xl px-5 py-24 sm:px-8 sm:py-32">
  <div class="grid gap-12 lg:grid-cols-12">
    <header class="lg:col-span-4" use:reveal>
      <span class="text-brand font-display text-7xl leading-none">01</span>
      <h2 class="mt-4 font-display text-5xl leading-tight text-ink">Workforce Solutions</h2>
    </header>

    <div class="lg:col-span-8" use:reveal={120}>
      <p class="font-display text-2xl leading-snug text-ink sm:text-3xl">
        Platinum Choice Consulting is an emerging leader in the Workforce Solutions industry.
      </p>
      <p class="mt-6 text-lg leading-relaxed">
        We recruit and place candidates in a variety of positions, including:
      </p>
      <ul class="mt-6 flex flex-wrap gap-2.5">
        {#each placements as p (p)}
          <li
            class="rounded-full border border-line bg-paper-deep/60 px-4 py-2 font-medium text-ink"
          >
            {p}
          </li>
        {/each}
      </ul>

      <div class="mt-12 grid gap-5 md:grid-cols-2">
        <article class="rounded-[1.75rem] border border-line bg-paper p-8">
          <h3 class="font-display text-3xl text-ink">Health Care Administration</h3>
          <p class="mt-4 leading-relaxed">
            Providing a full spectrum of health care services, including highly qualified
            professionals providing primary care, mental and behavioral health care in challenging
            work environments.
          </p>
        </article>
        <article class="rounded-[1.75rem] border border-line bg-paper p-8">
          <h3 class="font-display text-3xl text-ink">Commercial Interior Design</h3>
          <p class="mt-4 leading-relaxed">
            Consultations in creating and directing the construction of commercial spaces. Our
            designers guide clients to select materials, colors, and furnishings that align with the
            company’s brand aesthetic.
          </p>
          <p class="mt-4 leading-relaxed">
            Interior designers and interior design consultants work in areas such as hospitality,
            healthcare, commercial and corporate design.
          </p>
        </article>
      </div>
    </div>
  </div>
</section>

<!-- 02 Direct Hire -->
<section class="relative isolate overflow-hidden bg-ink text-paper/80">
  <div
    class="mx-auto grid max-w-7xl items-center gap-12 px-5 py-24 sm:px-8 sm:py-32 lg:grid-cols-12"
  >
    <div class="lg:col-span-6" use:reveal>
      <span class="text-brand font-display text-7xl leading-none">02</span>
      <h2 class="mt-4 font-display text-5xl leading-tight text-paper">Direct Hire</h2>
      <p class="mt-7 text-lg leading-relaxed">
        Recruiters in our Direct Hire division have decades of experience placing applicants in
        roles across Human Resources, Office Support, Executive/Administrative Assistants,
        Marketing, and more. They work in conjunction with our sourcing team to identify the most
        qualified candidates to meet the demanding needs of our clients.
      </p>
    </div>
    <div class="lg:col-span-5 lg:col-start-8" use:reveal={120}>
      <img
        src="/images/hiring-professionals.jpg"
        alt="Professionals in conversation during an interview"
        width="1200"
        height="628"
        loading="lazy"
        class="aspect-[4/3] w-full rounded-[2rem] object-cover"
      />
    </div>
  </div>
  <div class="h-1 w-full bg-brand"></div>
</section>

<!-- 03 + 04 -->
<section class="mx-auto max-w-7xl px-5 py-24 sm:px-8 sm:py-32">
  <div class="grid gap-6 lg:grid-cols-2">
    <article class="rounded-[2rem] bg-paper-deep/70 p-9 sm:p-12" use:reveal>
      <span class="text-brand font-display text-7xl leading-none">03</span>
      <h2 class="mt-4 font-display text-4xl leading-tight text-ink sm:text-5xl">
        Customized Solutions
      </h2>
      <p class="mt-6 text-lg leading-relaxed">
        We will assist you in designing a customized workforce solution that reduces costs, enhances
        productivity, and streamlines the requisition process.
      </p>
    </article>

    <article class="rounded-[2rem] bg-paper-deep/70 p-9 sm:p-12" use:reveal={120}>
      <span class="text-brand font-display text-7xl leading-none">04</span>
      <h2 class="mt-4 font-display text-4xl leading-tight text-ink sm:text-5xl">
        Introductory Consultation
      </h2>
      <p class="mt-6 text-lg leading-relaxed">
        Looking to develop your business but not sure where to turn? Need help planning or executing
        your next project? Let us guide you.
      </p>
      <p class="mt-4 text-lg leading-relaxed">
        Any organization can move forward with small incremental changes, but building for the
        future in today’s rapidly evolving environment means taking bold chances and making
        insightful decisions.
      </p>
    </article>
  </div>
</section>

<CtaBand title="Ready to build your team?" />
