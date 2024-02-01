import { z } from "zod";

export const loginCredentialsSchema = z.object({
  email: z.string().email("must be email"),
  password: z.string().min(6, "must be at least 6 characters"),
});
