/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'webinterface/templates/*.html',
    'employee/templates/*.html'
  ],
  
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