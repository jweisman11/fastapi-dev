# Import libraries
from fastapi import FastAPI
from app.api.routers import datasets

app = FastAPI()

# Include
app.include_router(datasets.router)
