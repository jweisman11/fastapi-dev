# Import libraries
from fastapi import FastAPI

# Local imports
from routers import helloworld, auth

app = FastAPI()


# Include
app.include_router(helloworld.router)
app.include_router(auth.router)
# app.include_router(users.router)
# app.include_router(metadata.router)
# app.include_router(search.router)
