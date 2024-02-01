from passlib.context import CryptContext
from app.core.config import settings 
from datetime import datetime, timedelta, timezone
from jose import jwt

passsword_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password(password: str) -> str:
  return passsword_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
  return passsword_context.verify(password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes = settings.ACESSS_TOKEN_EXPIRATION)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
    return encoded_jwt