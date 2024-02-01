from uuid import UUID

from app.schemas.image_schema import ImageCreate
from app.models.image_model import Image
from app.models.user_model import User
class ImageService:
  @staticmethod
  async def create_image(data: ImageCreate, user: User) -> Image:

    image_in = Image(
      image_url=data.image_url,
      user=user
    )

    return await image_in.save()
    
  async def get_image(data: UUID, user: User) -> Image:
    return await Image.find_one(Image.image_id == data)
  
  async def get_all_images(user: User) -> Image:
    return await Image.find(Image.user.id == user.id).to_list()