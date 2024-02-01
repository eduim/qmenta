from fastapi import FastAPI
from app.core.config import settings 
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.models.user_model import User
from app.models.image_model import Image
from app.api.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
  """lifespan handler"""
  db_client = AsyncIOMotorClient(settings.MONGODB_URI).qmenta
 
  await init_beanie(
    database=db_client, 
    document_models=[
      User,
      Image
    ])
  yield

app = FastAPI(
  lifespan=lifespan,
  title=settings.PROJECT_NAME,
  openapi_url=f"{settings.API_STR}/openapi.json",
)

origins = [
    settings.CLIENT_URI
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix=settings.API_STR)