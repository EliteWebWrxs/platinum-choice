<!--
  Low-poly line mesh echoing the faceted heads in the logo.
  Deterministic (seeded) so server and client render identically.
-->
<script>
  /** @type {{ class?: string, cols?: number, rows?: number, seed?: number }} */
  let { class: className = '', cols = 9, rows = 6, seed = 7 } = $props();

  const W = 900;
  const H = 600;

  /** @param {number} s */
  function rng(s) {
    return () => {
      s = (s * 16807) % 2147483647;
      return (s - 1) / 2147483646;
    };
  }

  const mesh = $derived.by(() => {
    const rand = rng(seed);
    const cw = W / cols;
    const ch = H / rows;

    /** @type {[number, number][][]} */
    const pts = [];
    for (let r = 0; r <= rows; r++) {
      pts[r] = [];
      for (let c = 0; c <= cols; c++) {
        const edge = r === 0 || c === 0 || r === rows || c === cols;
        const jx = edge ? 0 : (rand() - 0.5) * cw * 0.7;
        const jy = edge ? 0 : (rand() - 0.5) * ch * 0.7;
        pts[r][c] = [c * cw + jx, r * ch + jy];
      }
    }

    /** @type {{ d: string, fill: number }[]} */
    const tris = [];
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const a = pts[r][c];
        const b = pts[r][c + 1];
        const d = pts[r + 1][c];
        const e = pts[r + 1][c + 1];
        const pair =
          rand() > 0.5
            ? [
                [a, b, e],
                [a, e, d]
              ]
            : [
                [a, b, d],
                [b, e, d]
              ];
        for (const t of pair) {
          tris.push({
            d: `M${t.map(([x, y]) => `${x.toFixed(1)},${y.toFixed(1)}`).join('L')}Z`,
            fill: rand() > 0.82 ? rand() * 0.14 : 0
          });
        }
      }
    }
    return tris;
  });

  const id = $derived(`facets-${seed}`);
</script>

<svg
  class={className}
  viewBox="0 0 {W} {H}"
  preserveAspectRatio="xMidYMid slice"
  aria-hidden="true"
  focusable="false"
>
  <defs>
    <linearGradient {id} x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="var(--color-ember)" />
      <stop offset="0.45" stop-color="var(--color-flame)" />
      <stop offset="0.75" stop-color="var(--color-gold)" />
      <stop offset="1" stop-color="var(--color-rose)" />
    </linearGradient>
  </defs>
  <g stroke="url(#{id})" stroke-width="1" stroke-linejoin="round">
    {#each mesh as t, i (i)}
      <path d={t.d} vector-effect="non-scaling-stroke" fill="url(#{id})" fill-opacity={t.fill} />
    {/each}
  </g>
</svg>
