/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        navy: {
          900: '#060a12',
          850: '#0a0f1d',
          800: '#0f172a',
          700: '#1e293b',
          600: '#334155',
        },
        teal: {
          400: '#2dd4bf',
          500: '#14b8a6',
          600: '#0d9488',
        },
        accent: {
          orange: '#f59e0b',
          amber: '#fbbf24',
        }
      }
    },
  },
  plugins: [],
}

