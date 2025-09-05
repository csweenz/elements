import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [
    react(),
    {
      name: 'healthz-middleware',
      configureServer(server) {
        server.middlewares.use('/healthz', (_req, res) => {
          res.setHeader('Content-Type', 'application/json');
          res.end(JSON.stringify({ status: 'ok' }));
        });
      }
    }
  ]
})
