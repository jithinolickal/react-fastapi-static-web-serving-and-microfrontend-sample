import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: "/frontend" // This is the base path for the app. This is used in backend to serve the frontend. Will get added to the html file as a prefix.
})
