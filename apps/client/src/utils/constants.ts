if (!import.meta.env.VITE_BASE_URL) {
  throw new Error("VITE_BASE_URL is not defined");
}
export const BASE_URL = import.meta.env.VITE_BASE_URL;
