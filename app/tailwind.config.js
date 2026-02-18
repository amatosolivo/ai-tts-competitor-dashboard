/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                apple: {
                    bg: "#F5F5F7",
                    text: "#1D1D1F",
                    accent: "#0071E3",
                }
            },
            fontFamily: {
                sans: ['Inter', 'SF Pro Text', 'Helvetica Neue', 'sans-serif'],
            },
        },
    },
    plugins: [],
}
