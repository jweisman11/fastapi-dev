# Global project settings

from pydantic import BaseSettings, PostgresDsn, Optional

class Settings(BaseSettings):
    """
    Global settings used throughout the project to maintain DRY principles
    value: data_type = default_value
    """
    API_V1_STR: str = "/api/v1"

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    # TODO: What is the below line doing?
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    PROJECT_NAME: str = "TSDH API"
