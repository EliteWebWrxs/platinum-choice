<script>
  import Seo from '#lib/components/Seo.svelte';
  import PageHero from '#lib/components/PageHero.svelte';
  import CtaBand from '#lib/components/CtaBand.svelte';
  import { reveal } from '#lib/actions/reveal.js';
  import { credentials, site } from '#lib/site.js';

  const pdf = '/files/pcc-capability-statement.pdf';

  // Content from the current capability statement
  const whatWeDo = [
    'Platinum Choice Consulting, Inc. provides professional services focusing on human resources consulting, change management, and strategic organizational development. The firm delivers workforce restructuring, talent management, healthcare staffing, business process improvement, and performance management solutions to federal and state agencies.',
    'We possess SMEs and consultants that provide a full range of HR and management support services personnel to provide strategic and operational administrative support to a variety of clients and the communities that we serve.',
    'We excel in recruiting, identifying and providing short- and long-term temporary personnel to assist companies with workload fluctuations and unexpected or temporary demands.',
    'Our corporate focus is delivering expert people, ensuring each business has knowledgeable, experienced, and innovative people to carry them into the future.',
    'We provide business support to commercial, nonprofit and public sectors.'
  ];

  const differentiators = [
    'Combined 60 years of seasoned leadership in judicial, legislative, and executive branches of government, including state and local.',
    'In-depth knowledge of federal acquisition strategies.',
    'Functional expertise of operational areas.',
    'Seasoned, certified and pre-screened technical personnel.',
    'Intimate knowledge of Federal PII and security processes.',
    'Works shoulder to shoulder with clients, meeting temporary and short-term staffing needs cost-effectively, works within budget and delivers work on time.'
  ];

  const pastPerformance = [
    'Past performance encompasses a subcontractor relationship with prime healthcare contractor STG International, managing a National Institutes of Health staffing contract.',
    'Qualified senior-level executive with over thirty-five years of professional experience serving in leadership and advisory roles to senior executives on administrative, financial, operational, and managerial issues.',
    'Managed over one billion dollars of health and detention services contracts per year for the federal government.',
    'Supervised federal and contract employees performing work at the GS 15, 14, 13, and 12 levels who perform broad/extensive assignments related to government programs that are of significant interest to the public and Congress.',
    'Served as a COR for the judiciary’s temporary help services contract for professional and executive-administrative support personnel, including monitoring financial management controls and contractor performance within the scope of the contractual order.',
    'Provided reporting updates on contractor’s technical performance on a semi-annual basis.',
    'Maintained contract administration and policy for judicial program offices and worked in collaboration with the Office of Procurement.'
  ];

  const codes = [
    { label: 'State of incorporation', value: credentials.incorporated },
    { label: 'EIN', value: credentials.ein },
    { label: 'UEI (SAM)', value: credentials.uei },
    { label: 'CAGE code', value: credentials.cage }
  ];

  // Second statement: Workforce Development Training (page 2 of the PDF)
  const training = [
    'Platinum Choice Consulting specializes in delivering comprehensive and innovative workforce development training solutions tailored to meet the evolving needs of businesses and organizations across various industries.',
    'Committed to excellence and focused on empowering individuals with the skills necessary for success in today’s dynamic workforce.',
    'Offer a range of training programs designed to enhance productivity, efficiency, and overall performance.',
    'PCC also provides contractual human resources services, including a job board and talent management, to the private non-profit Damien Ministries. Certified as a WOSB small business, the company uses NAICS codes 541612 and 541613 to support government initiatives that require specialized human capital and management consulting expertise.'
  ];

  const competencies = [
    {
      lead: 'Customized Training Programs',
      text: 'Experienced trainers work closely with clients to develop customized training programs that address specific needs, goals, and objectives.'
    },
    {
      lead: 'Industry Expertise',
      text: 'Our trainers possess extensive industry experience and stay updated on the latest trends, regulations, and best practices to deliver impactful and actionable training.'
    },
    {
      lead: 'Innovative Training Methods',
      text: 'We leverage cutting-edge instructional design techniques, interactive workshops, simulations, and e-learning platforms to deliver engaging and immersive training experiences.'
    },
    {
      lead: 'Innovative Approach',
      text: 'Ensures maximum retention and application of knowledge, fostering a culture of continuous learning and improvement within your organization.'
    },
    {
      lead: 'Flexible Delivery Options',
      text: 'Our scalable training solutions can be adapted to meet the needs of individuals, small groups, or large organizations.'
    },
    {
      lead: 'Measurable Results',
      text: 'Through pre- and post-assessments, participant feedback surveys, and performance metrics analysis, we evaluate the effectiveness of our training interventions and make data-driven adjustments to optimize outcomes and drive continuous improvement.'
    }
  ];

  const keyDifferentiators = [
    { text: 'Prioritize building strong relationships with our clients.' },
    {
      text: 'Trusted partner with a solid and proven track record of success and a portfolio of satisfied clients, such as the University of Maryland Global, National Institutes of Health, Virginia State University, and STG International.'
    },
    {
      text: 'Commitment to quality, integrity, and professionalism that sets us apart and makes us the preferred choice for organizations.'
    },
    {
      lead: 'Sustainability and Scalability',
      text: 'We design our training programs with sustainability and scalability in mind, ensuring they can adapt and evolve alongside your organization’s changing needs and priorities.'
    },
    {
      text: 'Dedicated to empowering individuals and organizations with the knowledge, skills, and confidence needed to thrive in today’s competitive landscape.'
    },
    {
      text: 'Through our comprehensive workforce development training programs, we help unlock human potential, drive performance improvement, and achieve sustainable success. Partner with us to unlock your workforce’s full potential and take your organization to new heights.'
    }
  ];

  const tabs = [
    { id: 'hr-services', label: 'HR & Management Services' },
    { id: 'workforce-development', label: 'Workforce Development Training' }
  ];
  let active = $state(tabs[0].id);

  // Open the tab named in the URL hash, so each statement can be linked directly
  $effect(() => {
    const fromHash = tabs.find((t) => `#${t.id}` === window.location.hash);
    if (fromHash) active = fromHash.id;
  });

  /** @param {string} id */
  function select(id) {
    active = id;
    history.replaceState(history.state, '', id === tabs[0].id ? location.pathname : `#${id}`);
  }

  /** Arrow keys move between tabs, per the WAI-ARIA tabs pattern @param {KeyboardEvent} e */
  function onTabKey(e) {
    const step = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
    if (!step) return;
    const i = tabs.findIndex((t) => t.id === active);
    const next = tabs[(i + step + tabs.length) % tabs.length];
    select(next.id);
    document.getElementById(`tab-${next.id}`)?.focus();
  }

  const heading = 'font-display text-3xl text-ink sm:text-4xl print:text-2xl';
  const sideHeading = 'font-display text-3xl text-ink print:text-2xl';
</script>

<Seo
  title="Capability Statement"
  description="Capability statements for HR and management services and workforce development training. HUBZone and WOSB certified. UEI ZEJBM3DSLF58, CAGE 8UAV4."
  image="/images/og/capability-statement.jpg"
  imageAlt="Built for government, ready for business: PCC capability statement"
/>

<div class="print:hidden">
  <PageHero
    eyebrow="Capability statement"
    title="Built for government. Ready for business."
    intro="Expert people, processes and solutions for commercial, nonprofit and public sector clients."
    seed={41}
  >
    <div
      class="mt-10 flex flex-col gap-3 motion-safe:animate-rise sm:flex-row"
      style="animation-delay: 240ms"
    >
      <a
        href={pdf}
        download
        class="inline-flex items-center justify-center gap-2 rounded-full bg-paper px-7 py-4 font-semibold text-ink transition hover:bg-gold"
      >
        Download PDF <span aria-hidden="true">↓</span>
      </a>
      <button
        type="button"
        onclick={() => window.print()}
        class="inline-flex items-center justify-center rounded-full border border-paper/30 px-7 py-4 font-semibold text-paper transition hover:border-paper"
      >
        Print this page
      </button>
    </div>
  </PageHero>
</div>

<!-- The statement, laid out as a single document -->
<section class="mx-auto max-w-7xl py-0 sm:px-8 sm:py-24 print:max-w-none print:p-0">
  <div
    role="tablist"
    aria-label="Capability statements"
    class="mx-5 my-8 flex flex-col gap-1 rounded-[1.75rem] border border-line bg-paper-deep/70 p-1.5 sm:mx-auto sm:mt-0 sm:mb-10 sm:w-fit sm:flex-row sm:rounded-full print:hidden"
  >
    {#each tabs as tab (tab.id)}
      <button
        type="button"
        role="tab"
        id="tab-{tab.id}"
        aria-controls="panel-{tab.id}"
        aria-selected={active === tab.id}
        tabindex={active === tab.id ? 0 : -1}
        onclick={() => select(tab.id)}
        onkeydown={onTabKey}
        class={[
          'rounded-full px-6 py-3 text-sm font-semibold transition sm:text-base',
          active === tab.id ? 'bg-ink text-paper shadow-md' : 'text-ink-soft hover:text-ink'
        ]}
      >
        {tab.label}
      </button>
    {/each}
  </div>

  <article
    use:reveal
    class="overflow-hidden border-y border-line bg-paper sm:rounded-[2rem] sm:border sm:shadow-2xl sm:shadow-ink/10 print:rounded-none print:border-0 print:text-[9.5pt] print:shadow-none"
  >
    <!-- Letterhead -->
    <header class="relative">
      <div
        class="flex flex-col items-center gap-6 px-6 pt-10 pb-8 sm:flex-row sm:justify-between sm:px-12"
      >
        <img
          src="/images/logo.png"
          alt="Platinum Choice Consulting"
          width="640"
          height="296"
          class="h-20 w-auto sm:h-24"
        />
        <p class="text-center text-sm text-ink-muted sm:text-right">
          {credentials.legalName}<br />
          {credentials.address[0]}, {credentials.address[1]}
        </p>
      </div>
      <div class="bg-brand px-6 py-5 sm:px-12 print:[print-color-adjust:exact]">
        <h2
          class="text-center font-display text-4xl font-medium text-paper [font-variant:small-caps] sm:text-6xl"
        >
          Capability Statement
        </h2>
        {#if active === 'workforce-development'}
          <p
            class="mt-1 text-center text-xs font-semibold tracking-[0.25em] text-paper uppercase sm:text-sm"
          >
            Workforce development training
          </p>
        {/if}
      </div>
    </header>

    <div
      role="tabpanel"
      id="panel-hr-services"
      aria-labelledby="tab-hr-services"
      hidden={active !== 'hr-services'}
      class="grid lg:grid-cols-[1fr_24rem] print:grid-cols-[1fr_17rem]"
    >
      <!-- Main column -->
      <div class="space-y-14 px-6 py-12 sm:px-12 print:space-y-8 print:py-8">
        <section>
          <h3 class={heading}>Who we are</h3>
          <dl class="mt-6 grid gap-x-8 gap-y-5 sm:grid-cols-2">
            <div>
              <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
                Company
              </dt>
              <dd class="mt-1 font-medium text-ink">{credentials.legalName}</dd>
            </div>
            <div>
              <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
                Contacts
              </dt>
              <dd class="mt-1 font-medium text-ink">{credentials.contacts}</dd>
            </div>
            <div>
              <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">Phone</dt>
              <dd class="mt-1">
                <a href={site.phoneHref} class="font-medium text-ink hover:text-flame-dark"
                  >{site.phone}</a
                >
              </dd>
            </div>
            <div>
              <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">Email</dt>
              <dd class="mt-1">
                <a
                  href="mailto:{site.email}"
                  class="font-medium break-all text-ink hover:text-flame-dark">{site.email}</a
                >
              </dd>
            </div>
            <div>
              <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
                Website
              </dt>
              <dd class="mt-1">
                <a
                  href={site.altSite}
                  rel="noopener"
                  class="font-medium [overflow-wrap:anywhere] text-ink hover:text-flame-dark"
                  >www.PlatinumChoiceConsulting.net</a
                >
              </dd>
            </div>
            <div>
              <dt class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
                Coverage
              </dt>
              <dd class="mt-1 font-medium text-ink">
                Currently serving the Washington, DC, metropolitan areas. Serves the entire US.
              </dd>
            </div>
          </dl>
        </section>

        <section>
          <h3 class={heading}>What we do</h3>
          <ul class="mt-6 space-y-4 leading-relaxed">
            {#each whatWeDo as item (item)}
              <li class="flex gap-4">
                <span
                  class="mt-2 size-2.5 shrink-0 rounded-full bg-gold print:[print-color-adjust:exact]"
                ></span>
                {item}
              </li>
            {/each}
          </ul>
        </section>

        <section>
          <h3 class={heading}>Differentiators</h3>
          <ul class="mt-6 space-y-4 leading-relaxed">
            {#each differentiators as item (item)}
              <li class="flex gap-4">
                <span
                  class="mt-2 size-2.5 shrink-0 rounded-full bg-gold print:[print-color-adjust:exact]"
                ></span>
                {item}
              </li>
            {/each}
          </ul>
        </section>

        <section class="print:hidden">
          <h3 class="text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
            SBA certified
          </h3>
          <div class="mt-5 flex flex-wrap items-center gap-8">
            <img
              src="/images/sba-wosb.png"
              alt="SBA certified Woman Owned Small Business (WOSB)"
              width="650"
              height="135"
              loading="lazy"
              class="h-9 w-auto sm:h-11"
            />
            <img
              src="/images/sba-hubzone.jpg"
              alt="SBA HUBZone certified"
              width="160"
              height="200"
              loading="lazy"
              class="h-16 w-auto"
            />
          </div>
        </section>
      </div>

      <!-- Side column -->
      <aside
        class="space-y-12 border-t border-line bg-gold/15 px-6 py-12 sm:px-12 lg:border-t-0 lg:border-l lg:px-9 print:space-y-8 print:border-t-0 print:border-l print:px-6 print:py-8 print:[print-color-adjust:exact]"
      >
        <section>
          <h3 class={sideHeading}>Pertinent codes</h3>
          <dl class="mt-6 divide-y divide-ink/10">
            {#each codes as row (row.label)}
              <div class="flex items-baseline justify-between gap-4 py-2.5">
                <dt class="text-sm text-ink-muted">{row.label}</dt>
                <dd class="font-mono font-medium tracking-wide text-ink">{row.value}</dd>
              </div>
            {/each}
          </dl>

          <h4 class="mt-8 text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
            Special certifications
          </h4>
          <ul class="mt-3 flex flex-wrap gap-2">
            {#each credentials.certifications as cert (cert)}
              <li
                class="rounded-full bg-paper px-3 py-1 font-display text-lg text-ink"
                title={credentials.certificationNames[cert]}
              >
                {cert}
              </li>
            {/each}
          </ul>

          <h4 class="mt-8 text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
            NAICS codes
          </h4>
          <p class="mt-3 font-mono text-ink">{credentials.naics.join(', ')}</p>

          <h4 class="mt-6 text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
            PSC codes
          </h4>
          <p class="mt-3 font-mono text-ink">{credentials.psc.join(', ')}</p>
        </section>

        <section>
          <h3 class={sideHeading}>Past performance</h3>
          <ul class="mt-6 space-y-5 text-[0.95rem] leading-relaxed">
            {#each pastPerformance as item (item)}
              <li class="flex gap-3.5">
                <span
                  class="mt-2 size-2.5 shrink-0 rounded-full bg-ember print:[print-color-adjust:exact]"
                ></span>
                {item}
              </li>
            {/each}
          </ul>
        </section>
      </aside>
    </div>

    <div
      role="tabpanel"
      id="panel-workforce-development"
      aria-labelledby="tab-workforce-development"
      hidden={active !== 'workforce-development'}
      class="grid lg:grid-cols-[1fr_24rem] print:grid-cols-[1fr_17rem]"
    >
      <!-- Main column -->
      <div class="space-y-14 px-6 py-12 sm:px-12 print:space-y-8 print:py-8">
        <section>
          <h3 class={heading}>Workforce development training</h3>
          <ul class="mt-6 space-y-4 leading-relaxed">
            {#each training as item (item)}
              <li class="flex gap-4">
                <span
                  class="mt-2 size-2.5 shrink-0 rounded-full bg-gold print:[print-color-adjust:exact]"
                ></span>
                {item}
              </li>
            {/each}
          </ul>
        </section>

        <section>
          <h3 class={heading}>Key differentiators</h3>
          <h4 class="mt-6 text-xs font-semibold tracking-[0.2em] text-ink-muted uppercase">
            Client-centric approach
          </h4>
          <ul class="mt-4 space-y-4 leading-relaxed">
            {#each keyDifferentiators as item (item.text)}
              <li class="flex gap-4">
                <span
                  class="mt-2 size-2.5 shrink-0 rounded-full bg-gold print:[print-color-adjust:exact]"
                ></span>
                <span>
                  {#if item.lead}<strong class="font-semibold text-ink">{item.lead}:</strong>{/if}
                  {item.text}
                </span>
              </li>
            {/each}
          </ul>
        </section>
      </div>

      <!-- Side column -->
      <aside
        class="border-t border-line bg-gold/15 px-6 py-12 sm:px-12 lg:border-t-0 lg:border-l lg:px-9 print:border-t-0 print:border-l print:px-6 print:py-8 print:[print-color-adjust:exact]"
      >
        <section>
          <h3 class={sideHeading}>Core competencies</h3>
          <ul class="mt-6 space-y-5 text-[0.95rem] leading-relaxed">
            {#each competencies as item (item.lead)}
              <li class="flex gap-3.5">
                <span
                  class="mt-2 size-2.5 shrink-0 rounded-full bg-ember print:[print-color-adjust:exact]"
                ></span>
                <span>
                  <strong class="block font-semibold text-ink">{item.lead}</strong>
                  {item.text}
                </span>
              </li>
            {/each}
          </ul>
        </section>
      </aside>
    </div>

    <!-- Footer strip -->
    <footer
      class="flex flex-col items-center justify-center gap-x-6 gap-y-1 border-t border-line px-6 py-5 text-center font-display text-lg text-flame-dark [font-variant:small-caps] sm:flex-row"
    >
      <a href={site.phoneHref} class="hover:text-ink">{site.phone}</a>
      <span class="hidden text-line sm:inline" aria-hidden="true">|</span>
      <a href={site.altSite} rel="noopener" class="hover:text-ink"
        >www.platinumchoiceconsulting.net</a
      >
      <span class="hidden text-line sm:inline" aria-hidden="true">|</span>
      <a href="mailto:{site.email}" class="break-all hover:text-ink">{site.email.toLowerCase()}</a>
    </footer>
  </article>
</section>

<div class="print:hidden">
  <CtaBand
    title="Partner with PCC"
    text="Contracting officers and primes: reach out to discuss staffing, HR and management support for your next requirement."
  />
</div>
