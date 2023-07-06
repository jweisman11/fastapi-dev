# Import libraries
from fastapi import FastAPI, APIRouter
from endpoints import (
    service,
    login,
    datasets,
    stats,
    data_operations,
    utils,
    governance,
    users,
)

# Define the API's description using Markdown
description = """
DHS I&A Developer API helps you do dev-low, deploy-high. 🚀

## TSDH Datasets

You can **read items**
"""

# Define the top-level metadata about the API
app_metadata = {
    "title": "DHS I&A Developer API",
    "description": description,
    "version": "0.1.0",
    "contact": {"name": "Mission Solutions Division", "email": "DHS-IA-MSD@email.com"},
}

app = FastAPI(**app_metadata)
api_router = APIRouter()

# Include routes to each grouping of endpoints
api_router.include_router(service.router, prefix="/service", tags=["Admin"])
api_router.include_router(login.router, prefix="/login", tags=["Login"])
api_router.include_router(datasets.router, prefix="/dataset", tags=["TSDH Datasets"])
api_router.include_router(stats.router, prefix="/stats", tags=["Statistics"])
api_router.include_router(data_operations.router, prefix="/ops", tags=["Operations"])
api_router.include_router(utils.router, prefix="/utils", tags=["Utilities"])
api_router.include_router(governance.router, prefix="/governance", tags=["Governance"])
api_router.include_router(users.router, prefix="/user", tags=["Users"])
app.include_router(api_router, prefix="/api/v1")
