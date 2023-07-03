# Import libraries
from fastapi import FastAPI

# Local imports
from routers import helloworld, auth
from db.database import Base, engine

app = FastAPI()

# TODO: Update to use Alembic migrations to create tables
Base.metadata.create_all(bind=engine)

# Include
app.include_router(helloworld.router)
app.include_router(auth.router)
# app.include_router(users.router)
# app.include_router(metadata.router)
# app.include_router(search.router)
