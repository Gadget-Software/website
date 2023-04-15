import adapterStatic from '@sveltejs/adapter-static';
import preprocess from 'svelte-preprocess';

/** @type {import("@sveltejs/kit").Config} */
const config = {
  preprocess: preprocess({
    postcss: true,
  }),

  kit: {
    adapter: adapterStatic({
      pages: 'build',
      assets: 'build',
      fallback: null,
      precompress: true,
      strict: false,
    }),
  },
};

export default config;
