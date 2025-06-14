import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import path from 'path'

// Asegúrate de que __dirname esté definido
const __dirname = path.dirname(new URL(import.meta.url).pathname)

export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    },
  },
  server: {
    host: '0.0.0.0', // Escucha en todas las interfaces
    port: 5173,
    watch: {
      usePolling: true,
    },
  }
})