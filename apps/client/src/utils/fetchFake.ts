import { BASE_URL } from "./constants";
import { buildToken } from "./utils";

export function fakeFetch(
  url: string,
  options?: RequestInit
): Promise<Response> {
  switch (url) {
    case `${BASE_URL}"/auth/login`: {
      const { email, password } = JSON.parse(options?.body as string);
      return new Promise((resolve) => {
        setTimeout(() => {
          const token = buildToken(email, password);
          const fakeResponse = new Response(JSON.stringify({ token }));
          resolve(fakeResponse);
        }, 1000);
      });
    }
    default:
      throw new Error(`Unhandled endpoint: ${url}`);
  }
}
