import { useAuth } from "../auth/AuthProvider";
import "./styles/layout.scss";
import Button from "../ui/Button";

export default function Layout({ children }: { children: React.ReactNode }) {
  const auth = useAuth();

  return (
    <>
      <header>
        <nav>
          <ul>
            {auth.isAuthenticated && (
              <li>
                <Button clickHandler={auth.logout}>Logout</Button>
              </li>
            )}
          </ul>
        </nav>
      </header>
      <main>{children}</main>
    </>
  );
}
