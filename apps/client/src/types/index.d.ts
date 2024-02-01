interface AuthReponse extends Response {
  access_token?: string;
  detail?: string;
}
export type APIResponse = AuthReponse | Reponse;
export type Images = {
  image_id: string;
  created_at: string;
  image_url: string;
  user: UserCollection;
};

type UserCollection = {
  id: string;
  collection: user;
};

export type User = {
  email: string;
  user_id: string;
  username: string;
};

export interface AuthState {
  isAuthenticated: boolean;
  token: string;
}

export type AuthActions = AuthActionLogin | AuthActionLogout;

export interface AuthActionLogin {
  type: "LOGIN";
  payload: AuthReponse["token"];
}

export interface AuthActionLogout {
  type: "LOGOUT";
}

export type CredentialsForm = {
  email: string;
  password: string;
};

export type FetchFunction = (
  url: string,
  options?: RequestInit
) => Promise<Response>;
