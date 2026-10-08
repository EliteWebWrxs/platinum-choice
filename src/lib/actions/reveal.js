/**
 * Fades an element up into view the first time it scrolls into the viewport.
 * Content stays visible if JavaScript never runs, because the hidden state
 * is only applied here.
 * @param {HTMLElement} node
 * @param {number} [delay] milliseconds
 */
export function reveal(node, delay = 0) {
  if (!('IntersectionObserver' in window)) return;

  node.dataset.reveal = 'hidden';
  if (delay) node.style.transitionDelay = `${delay}ms`;

  const observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting) {
        node.dataset.reveal = 'shown';
        observer.disconnect();
      }
    },
    { rootMargin: '0px 0px -10% 0px' }
  );

  observer.observe(node);

  return {
    destroy: () => observer.disconnect()
  };
}
