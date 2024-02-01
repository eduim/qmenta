from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user_schema import UserAuth, UserOut
from app.services.user_service import UserService
from typing import Annotated
from app.models.user_model import User
from app.api.dependencies.user_dependencies import get_current_user

users_router = APIRouter()

@users_router.post('/create', summary='create user', response_model=UserOut)
async def create_user(data: UserAuth):
  try:
    return await UserService.create_user(data)
  except:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="User email or name already exists"
    )

@users_router.get("/me", summary = 'get current user with access token', response_model=UserOut)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return current_user