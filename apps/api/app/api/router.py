from fastapi import APIRouter
from app.api.handlers import user, image

from app.api.auth import jwt

router = APIRouter()
router.include_router(user.users_router, prefix='/users')
router.include_router(jwt.auth_router, prefix='/auth')
router.include_router(image.image_router, prefix='/images')