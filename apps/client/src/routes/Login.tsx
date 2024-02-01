import { useState } from "react";
import Layout from "../layout/Layout";
import { useAuth } from "../auth/AuthProvider";
import { Navigate, useNavigate } from "react-router-dom";
import { ZodError } from "zod";
import { loginCredentialsSchema } from "../schemas/loginSchema";
import Input from "../ui/Input";
import Button from "../ui/Button";
import "./styles/login.scss";
import { buildZodError } from "../utils/utils";
import { CredentialsForm } from "../types";
import ServerAPI from "../api/api";

const api = ServerAPI(fetch);
export default function Login() {
  const [credentials, setCredentials] = useState<CredentialsForm>({
    email: "",
    password: "",
  });
  const [errorMessage, setErrorMessage] = useState<string | undefined>(
    undefined
  );

  const auth = useAuth();
  const goTo = useNavigate();

  function handleCredentialsChange(e: React.ChangeEvent<HTMLInputElement>) {
    setCredentials({
      ...credentials,
      [e.target.name]: e.target.value,
    });
  }

  async function handleCredentialsSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    try {
      const { email, password } = loginCredentialsSchema.parse(credentials);

      const response = await api.login({ email, password });

      if (response?.access_token) {
        auth.saveUser(response.access_token);
        goTo("/dashboard");
      } else {
        if (response) {
          setErrorMessage(response.detail);
        }
      }
    } catch (err) {
      if (err instanceof ZodError) {
        const errorMessage = buildZodError(err.errors);
        setErrorMessage(errorMessage as string);
      }
    }
  }

  if (auth.isAuthenticated) {
    return <Navigate to="/dashboard" />;
  }

  return (
    <Layout>
      <form
        data-test-id="login-form"
        onSubmit={handleCredentialsSubmit}
        className="login-form"
      >
        <h1>Login</h1>
        <label>Email</label>
        <Input
          type="text"
          name="email"
          changeHandler={handleCredentialsChange}
        />
        <label>Password</label>
        <Input
          type="password"
          name="password"
          changeHandler={handleCredentialsChange}
        />
        <Button>Login</Button>
        {errorMessage && <p className="warning">{errorMessage}</p>}
      </form>
    </Layout>
  );
}
