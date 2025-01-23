import {defineConfig} from 'vite'
import react from '@vitejs/plugin-react-swc'

export default defineConfig({
    plugins: [
        react(),
    ],
    server: {
        port: 4201,
        host: true,
        cors: true,
        headers: {
            'Vite-Bundle': 'REACT',
        },
        origin: 'http://127.0.0.1:8000',
        proxy: {
            '/static/js-bundles': {
                target: 'http://localhost:8000',
                changeOrigin: true,
            },
        },
        fs: {
            allow: ['..'],
        },
    },
    build: {
        emptyOutDir: true,
        sourcemap: true,
        rollupOptions: {
            output: {
                manualChunks: {
                    react: ['react', 'react-dom'],
                    apollo: ['@apollo/client', 'graphql-ws', 'apollo-upload-client', 'react-router'],
                },
            },
        },
    },
})
