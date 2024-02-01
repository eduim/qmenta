import { useContext, createContext, useReducer, useEffect } from "react";
import type { AuthReponse, AuthState, AuthActions } from "../types";
import Cookies from "js-cookie";
const authReducer = (state: AuthState, action: AuthActions) => {
  if (action.type === "LOGIN") {
    const token = action.payload;
    localStorage.setItem("access_token_qmenta", token);
    return {
      isAuthenticated: true,
      token: action.payload!,
    };
  }
  if (action.type === "LOGOUT") {
    localStorage.removeItem("access_token_qmenta");
    Cookies.remove("access_token_qmenta");

    return {
      isAuthenticated: false,
      token: "",
    };
  }
  return state;
};

const AuthContext = createContext<{
  state: AuthState;
  dispatch: React.Dispatch<AuthActions>;
}>({
  state: {
    isAuthenticated: false,
    token: "",
  },
  dispatch: () => {},
});

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(authReducer, {
    isAuthenticated: false,
    token: "",
  });

  useEffect(() => {
    let token = localStorage.getItem("access_token_qmenta");

    if (!token) {
      token = Cookies.get("access_token_qmenta") as unknown as string | null;
    }

    if (token) {
      dispatch({ type: "LOGIN", payload: token });
    }
  }, []);

  return (
    <AuthContext.Provider value={{ state, dispatch }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => {
  const { state, dispatch } = useContext(AuthContext);

  const getAccessToken = (): AuthReponse["access_token"] => state.token;
  const saveUser = (token: AuthReponse["access_token"]) => {
    dispatch({ type: "LOGIN", payload: token });
  };

  const logout = () => {
    dispatch({ type: "LOGOUT" });
  };

  return {
    getAccessToken,
    saveUser,
    logout,
    isAuthenticated: state.isAuthenticated,
  };
};
