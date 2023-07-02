import sys
sys.path.append("..")

from fastapi import APIRouter, status

router = APIRouter(
    prefix="/datasets",
    tags=["datasets"],
    responses={404: {"description": "Not found"}}
)


@router.get("/",
            status_code=status.HTTP_200_OK,
            summary="List datasets",
            description="List all available datasets in TSDH")
async def get_datasets():
    """
    Simple GET endpoint to list all datasets in TSDH
    """

    return db.query()
