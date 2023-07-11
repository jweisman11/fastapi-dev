from fastapi.middleware.cors import CORSMiddleware
from api.main import app

# Middleware CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://crazyurl:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
