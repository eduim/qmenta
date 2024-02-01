from pydantic_settings import BaseSettings
from decouple import config 
class Settings(BaseSettings):
  API_STR: str = '/api'
  JWT_SECRET: str = config('JWT_SECRET', cast=str)
  ALGORITHM: str ='HS256'
  ACESSS_TOKEN_EXPIRATION: int = 60*24*7
  PROJECT_NAME: str = 'QMENTA'
  MONGODB_URI: str = config('MONGODB_URI', cast=str)
  CLIENT_URI: str = config('CLIENT_URI', cast=str)

  class Config:
    case_sensitive = True

settings = Settings()    