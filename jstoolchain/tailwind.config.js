/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html',],
  theme: {
    extend: {
      fontFamily: {
        borel: ['Borel', 'cursive'],
        noto: ['Noto Sans', 'sans-serif']
      },
      colors:{
        "custom-blue1": "#164863",
        "custom-blue2": "#427D9D",
        "custom-blue3": "#9BBEC8",
        "custom-blue4": "#DDF2FD"
      },
    },
  },
  plugins: [],
}

