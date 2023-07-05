import sys

sys.path.append("..")

from fastapi import APIRouter, status
from data.initialData import DATASETS

router = APIRouter()


@router.get(
    path="/health",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="TODO: Add longer description about what this API endpoint does",
    response_description="TODO: Return health status of the dataset API endpoints",
    deprecated=False,
)
async def health_check() -> dict:
    """
    Root GET
    """

    return {"msg": "API is up and running"}


# TODO: add response model
@router.get("/{dataset_id}", status_code=status.HTTP_200_OK)
async def fetch_dataset(*, dataset_id: int) -> dict:
    """
    Fetch a single dataset by ID
    """

    result = [dataset for dataset in DATASETS if dataset["id"] == dataset_id]
    if result:
        return result[0]
