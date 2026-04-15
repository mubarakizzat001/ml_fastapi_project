from pydantic_settings import BaseSettings, SettingsConfigDict


_base_settings = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    extra="ignore",
)

class DatabaseSettings(BaseSettings):
    DB_USER:str
    DB_PASSWORD:str
    DB_NAME:str
    DB_HOST:str
    DB_PORT:int

    model_config = _base_settings


    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    


settings = DatabaseSettings()



