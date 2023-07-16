from functools import lru_cache

from fastapi import FastAPI, Depends

from config import Settings

app = FastAPI()


@lru_cache
def get_settings():
    return Settings()


@app.get("/vars")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "default_variable": settings.DEFAULT_VAR,
        "apiKey": settings.API_KEY,
        "app max integer": settings.APP_MAX,
    }
