<script>
  import '../app.css';
  import SiteHeader from '#lib/components/SiteHeader.svelte';
  import SiteFooter from '#lib/components/SiteFooter.svelte';
  import OrganizationSchema from '#lib/components/OrganizationSchema.svelte';

  let { children } = $props();
</script>

<OrganizationSchema />

<div class="flex min-h-screen flex-col">
  <SiteHeader />
  <main id="main" class="flex-1">
    {@render children()}
  </main>
  <SiteFooter />
</div>
