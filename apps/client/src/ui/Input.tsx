import "./styles/input.scss";
export default function Input({
  type,
  name,
  value,
  placeholder,
  checked,
  changeHandler,
}: {
  type: React.HTMLInputTypeAttribute | undefined;
  name?: string;
  value?: string | number | readonly string[] | undefined;
  placeholder?: string | undefined;
  checked?: boolean;
  changeHandler?: React.ChangeEventHandler<HTMLInputElement>;
}) {
  if (type === "checkbox") {
    return (
      <input
        className="input-ui-checkbox"
        type={type}
        name={name}
        checked={checked}
        onChange={changeHandler}
      ></input>
    );
  }

  return (
    <input
      className="input-ui"
      type={type}
      name={name}
      value={value}
      checked={checked}
      placeholder={placeholder}
      onChange={changeHandler}
    ></input>
  );
}
