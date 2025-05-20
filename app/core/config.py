from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_SERVICE_KEY: str
    # Add other settings here as needed

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()