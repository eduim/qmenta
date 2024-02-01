import "./styles/button.scss";

export default function Button({
  children,
  type,
  clickHandler,
}: {
  children: React.ReactNode;
  type?: React.ButtonHTMLAttributes<HTMLButtonElement>["type"];
  clickHandler?: React.MouseEventHandler<HTMLButtonElement>;
}) {
  return (
    <button className="button-ui" onClick={clickHandler} type={type}>
      {children}
    </button>
  );
}
