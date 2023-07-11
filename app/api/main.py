import sys

sys.path.append("..")


import logging


# Import libraries
from fastapi import FastAPI, APIRouter, Depends, Request
from deps import headers
import time
from endpoints import (
    service,
    login,
    datasets,
    stats,
    data_operations,
    utils,
    governance,
    users,
    wiki,
)

# Set-up logging for API
logging.basicConfig(
    level=logging.DEBUG,
    # format="%(asctime)s - %(message)s",
    format="%(levelname)s: %(asctime)s - %(name)s - %(filename)s - LINE: %(lineno)d - MESSAGE: %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

endpoint_name = "fetch_stuff"
logging.debug(f"test message - {endpoint_name}")
# logging.info("test message")
# logging.warning("test message")
# logging.error("test message")
# logging.critical("test message")


# Define the API's description using Markdown
description = """
DHS I&A Developer API helps you do dev-low, deploy-high. 🚀

## TSDH Datasets

You can **read items**
"""

# Define the top-level metadata about the API
app_metadata = {
    "title": "DHS I&A Top Secret Data Hub (TSDH) API",
    "description": description,
    "version": "0.1.0",
    "contact": {"name": "Mission Solutions Division", "email": "DHS-IA-MSD@email.com"},
}


# docExpansion: https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/?sbsearch=docExpansion
# Set all API docs sections to be "collapsed" by default but can change
app = FastAPI(**app_metadata, swagger_ui_parameters={"docExpansion": "none"})
api_router = APIRouter(dependencies=[Depends(headers.custom_headers)])


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# Routes to groups of endpoints
# Each route is prefixed with a unique and descriptive name
api_router.include_router(wiki.router, prefix="/wiki", tags=["wiki"])
api_router.include_router(datasets.router, prefix="/dataset", tags=["TSDH Datasets"])
api_router.include_router(service.router, prefix="/admin", tags=["Admin"])
api_router.include_router(login.router, prefix="/login", tags=["Login"])
api_router.include_router(stats.router, prefix="/stats", tags=["Statistics"])
api_router.include_router(data_operations.router, prefix="/ops", tags=["Operations"])
api_router.include_router(utils.router, prefix="/utils", tags=["Utilities"])
api_router.include_router(governance.router, prefix="/governance", tags=["Governance"])
api_router.include_router(users.router, prefix="/user", tags=["Users"])

# Include GLOBAL prefix for all routes and endpoints
app.include_router(api_router, prefix="/api/v1")
