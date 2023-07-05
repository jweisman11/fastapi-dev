# Import libraries
from fastapi import FastAPI
from endpoints import datasets

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

# Include routes to each grouping of endpoints
app.include_router(datasets.router, prefix="/dataset", tags=["TSDH Datasets"])
