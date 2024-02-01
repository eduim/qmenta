from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import Any, Annotated


from app.schemas.auth_schema import TokenSchema
from fastapi.security import OAuth2PasswordRequestForm


from app.services.user_service import UserService
from app.core.security import create_access_token

auth_router = APIRouter()

@auth_router.post('/login', summary = 'login user')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], response: Response) -> Any:
  user = await UserService.authenticate(email = form_data.username, password = form_data.password)
  
  if not user: 
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="incorrect email or password"
    )
  access_token = create_access_token(data = {'sub': str(user.user_id)})
  if user:
    response.set_cookie(key="access_token_qmenta", value=f"{access_token}", httponly=True)
  return TokenSchema(access_token=access_token, token_type="bearer")

