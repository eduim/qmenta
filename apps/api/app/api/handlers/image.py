from uuid import UUID
from typing import Annotated
import io
from fastapi.responses import StreamingResponse
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.image_schema import ImageCreate, ImageOut
from app.models.user_model import User
from app.api.dependencies.user_dependencies import get_current_user
from app.services.image_service import ImageService
from app.core.dicom import dicom_to_png

image_router = APIRouter()

@image_router.post('/create', summary="Create image", response_model=ImageOut)
async def create_image(data: ImageCreate, current_user: Annotated[User, Depends(get_current_user)]):
  try:
    return await ImageService.create_image(data, current_user)
  except:
    raise HTTPException(status_code=404, detail="Image not created")
  
@image_router.get('/{image_id}', summary="Get image by id")
async def get_image(image_id: UUID,  current_user: Annotated[User, Depends(get_current_user)]):
  print('here')
  try:
    image = await ImageService.get_image(image_id, current_user)
    image_data = dicom_to_png(image.image_url)
    return StreamingResponse(io.BytesIO(image_data), media_type="image/png")
  except: 
    raise HTTPException(status_code=404, detail="Image not found")

@image_router.get("", summary="Get all images from user")
async def get_all_images( current_user: Annotated[User, Depends(get_current_user)]):
  try: 
    return await ImageService.get_all_images(current_user)
  except:
    raise HTTPException(status_code=404, detail="Images not found")

