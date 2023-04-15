/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts,scss}'],
  theme: {
    extend: {
      screens: {
        '3xl': '1920px',
      }
    }
  },
  plugins: []
};
