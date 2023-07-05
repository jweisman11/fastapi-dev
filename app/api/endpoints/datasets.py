import sys

sys.path.append("..")

from fastapi import APIRouter, status
from data.initialData import DATASETS

router = APIRouter()


@router.get("/health", status_code=200)
async def root() -> dict:
    """
    Root GET
    """

    return {"msg": "Hello, World!"}


# @api_router.get("/{dataset_id}", status_code=200, response_model=Recipe)
@router.get("/{dataset_id}", status_code=status.HTTP_200_OK)
async def fetch_dataset(*, dataset_id: int) -> dict:
    """
    Fetch a single dataset by ID
    """

    result = [dataset for dataset in DATASETS if dataset["id"] == dataset_id]
    if result:
        return result[0]
