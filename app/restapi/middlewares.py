from starlette.middleware.base import BaseHTTPMiddleware
from app.utils import get_current_user
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings

class UserConfirmMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        cur_user = await get_current_user()
        if cur_user.confirmed == False:
            raise HTTPException(403, detail="user not confirmed")
        return response

middlewares = [
    Middleware(UserConfirmMiddleware),
    Middleware(CORSMiddleware,
        allow_headers=["*"],
        allow_origins=settings.ALLOWED_HOSTS,
        allow_methods=["*"],
        allow_credentials=True,
    )

]
