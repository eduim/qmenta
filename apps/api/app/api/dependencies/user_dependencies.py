from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app.core.config import settings
from app.models.user_model import User
from app.services.user_service import UserService
from app.schemas.auth_schema import TokenPayload
from typing import Annotated

reusable_oauth = OAuth2PasswordBearer(
  tokenUrl=f"{settings.API_STR}/auth/login",
  scheme_name="JWT"
)

async def get_current_user(token: Annotated[str, Depends(reusable_oauth)]) -> User:
  try:
    payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
    token_data = TokenPayload(**payload)
    if datetime.fromtimestamp(token_data.exp) < datetime.now():
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token expired",
        headers={"WWW-Authenticate": "Bearer"},
      )
  except:
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Credentials not valid",
        headers={"WWW-Authenticate": "Bearer"},
      )
  
  user = await UserService.get_user_by_id(token_data.sub)
  
  if not user: 
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User does not exists",
        headers={"WWW-Authenticate": "Bearer"},
      )
  return user
