import os

class Settings:
    TITLE = os.getenv("TITLE")
    DEBUG = True
    # POSTGRES_DSN: str
    # REDIS_DSN: str
    ALLOWED_HOSTS = ['*']
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')# openssl rand -hex 32
    ACCESS_TOKEN_EXPIRE_MINUTES = 10080 # one week
    PORT = 8000
    TEMPLATES_DIR = 'app/templates/build'
    PROJECT_NAME = "Crew st"
    REDIS_URL = ""
    REDIS_CACHE_EXP_TIME = 86400 # DAY

settings = Settings()
