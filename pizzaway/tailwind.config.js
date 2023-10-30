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
      },
    },
  },
  variants: {},
  plugins: [],
}