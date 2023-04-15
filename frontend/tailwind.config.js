/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js}"
  ],
  theme: {
    extend: {
      colors: {
        // 'unripe-green': '#46b04f',
        'pastel-orange': '#FCD58B',
        //'unripe-green': '#feda00',
        'orange': '#ffa200',
        'dark-gray': '#262626',
        'mellow-yellow': '#f7f6c5',
        'another-yellow': '#FEEF92',
        'magenta': '#d81e5b',
        'pink': '#CE5E84',
      },
      backgroundImage: {
        'yellow-bananas': "url('./src/assets/yellow-banana-bg.jpg')",
      },
    },
  },
  plugins: [],
}

