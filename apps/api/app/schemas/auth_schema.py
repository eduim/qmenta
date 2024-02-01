from uuid import UUID
from pydantic import BaseModel

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None