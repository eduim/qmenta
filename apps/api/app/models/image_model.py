
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Link
from pydantic import Field
from .user_model import User 

class Image(Document):
    image_id: UUID = Field(default_factory=uuid4, unique=True)
    image_url: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user: Link[User]
    class Settings:
        name = "images"
