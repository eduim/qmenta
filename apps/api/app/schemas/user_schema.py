from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class UserAuth(BaseModel):
  email: EmailStr = Field(...,description="user email")
  username: str = Field(...,min_length=5, description="user username")
  password: str = Field(...,min_lenght=5, description="user password")

class UserOut(BaseModel):
  user_id: UUID
  username: str
  email: EmailStr

  