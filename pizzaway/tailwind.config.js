/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: {
    content: ['./**/*.html'],
  },
  theme: {
    extend: {
      colors: {
        'pizza-red': '#FF0000',
        'pizza-yellow': '#FFD700',
        'light-pizza-yellow': '#FFEDA4',
      },
    },
  },
  variants: {},
  plugins: [],
}