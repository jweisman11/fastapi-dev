from pydantic import BaseSettings


class Settings(BaseSettings):
    DEFAULT_VAR = (
        "some default string value"  # default value if env variable does not exist
    )
    API_KEY: str = "hello world"
    APP_MAX: int = 100  # default value if env variable does not exist
