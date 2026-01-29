import { defineConfig } from "vite";
import { viteSingleFile } from "vite-plugin-singlefile";

export default defineConfig({
  root: "src",
  plugins: [viteSingleFile()],
  build: {
    outDir: "dist",
    emptyOutDir: false,
    rollupOptions: {
      input: "src/mcp-app.html",
    },
  },
});
