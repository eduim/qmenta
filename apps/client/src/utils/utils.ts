import { ZodIssue } from "zod";
export function buildToken(email: string, password: string) {
  return `randomtoken:${email}:${password}`;
}

export function buildZodError(issues: ZodIssue[]) {
  if (issues) {
    const errorMessages = issues.flatMap(
      (error: ZodIssue) => `${error.path[0]} field ${error.message}`
    );
    return errorMessages.join(", ").toString();
  }
}
