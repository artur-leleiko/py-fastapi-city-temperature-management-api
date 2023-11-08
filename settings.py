from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI city temperature management API"

    DATABASE_URL: str | None = "sqlite+aiosqlite:///./cities_temperature.db"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
