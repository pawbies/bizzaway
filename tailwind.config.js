/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'webinterface/templates/*.html',
    'employee/templates/*.html'
  ],
  
  theme: {
    extend: {
      colors: {
        'pizza-red': '#B20000',
        'pizza-yellow': '#E6C200',
        'light-pizza-yellow': '#ffde58',

        'pizza-red-dark': '#340740', //https://m2.material.io/design/color/dark-theme.html <- google recommends this so yeah
        'pizza-yellow-dark': '#121212',
        'light-pizza-yellow-dark': '#673973',
        'text-dark': '#9C9C9C'
      },
    },
  },
  variants: {},
  plugins: [],
}