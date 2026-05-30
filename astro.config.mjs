// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://valyriantech.github.io',
  base: '/ValyrianNewsNetwork',
  output: 'static',
  vite: {
    plugins: [tailwindcss()]
  }
});