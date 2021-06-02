import aioredis
from app.core.config import settings
from app.crud import cruduser
from .session import SessionLocal


reg_confirm_redis = aioredis.from_url(settings.REDIS_REG_CONFIRM_URL)
reg_confirm_redis.set_response_callback('EXPIRE', lambda username: cruduser.delete_by_username(SessionLocal(), username))

del_users_redis = aioredis.from_url(settings.REDIS_DEL_USERS_URL)
