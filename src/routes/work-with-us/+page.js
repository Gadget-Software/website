import copyHtml from './copy.html?raw';

/** @type {import('./$types').PageLoad} */
export function load({ params }) {
  return {
    copyHtml,
  };
}
