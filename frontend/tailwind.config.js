/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js}"
  ],
  theme: {
    extend: {
      colors: {
        'unripe-green': '#d9f99d',
        'mellow-yellow': '#FEEF92',
      },
      backgroundImage: {
        'yellow-bananas': "url('./src/assets/yellow-banana-bg.jpg')",
      },
    },
  },
  plugins: [],
}

