import type {
  FetchFunction,
  CredentialsForm,
  AuthReponse,
  Images,
  User,
} from "../types";
import { BASE_URL } from "../utils/constants";
import Cookies from "js-cookie";
const ServerAPI = (fetch: FetchFunction) => ({
  async login({ email, password }: CredentialsForm): Promise<AuthReponse> {
    const formData = new URLSearchParams();
    formData.append("username", email);
    formData.append("password", password);

    const response = await fetch(`${BASE_URL}/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: formData.toString(),
    });
    return await response.json();
  },

  async fetchImagesIds(): Promise<Images[]> {
    const token = getToken();
    const response = await fetch(`${BASE_URL}/images`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    return await response.json();
  },

  async fetchImage(id: string) {
    const token = getToken();
    const response = await fetch(`${BASE_URL}/images/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response;
  },

  async getName(): Promise<User> {
    const token = getToken();
    const response = await fetch(`${BASE_URL}/users/me`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return await response.json();
  },
});

export default ServerAPI;

const getToken = () => {
  const token = Cookies.get("access_token_qmenta")
    ? Cookies.get("access_token_qmenta")
    : localStorage.getItem("access_token_qmenta");
  return token;
};
