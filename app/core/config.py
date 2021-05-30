from pydantic import BaseSettings

class Settings(BaseSettings):
    TITLE: str
    DEBUG:  bool = True
    POSTGRES_DSN: str
    # REDIS_DSN: str
    ALLOWED_HOSTS: list = ['*']
    JWT_SECRET_KEY: str # openssl rand -hex 32
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080 # one week

settings = Settings()
