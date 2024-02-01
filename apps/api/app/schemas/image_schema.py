from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class ImageCreate(BaseModel):
  image_url: str = Field(..., description='Image url')

class ImageOut(BaseModel):
  image_id: UUID
  image_url: str
  created_at: datetime
  
  
