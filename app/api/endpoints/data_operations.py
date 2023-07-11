import sys

sys.path.append("..")

from fastapi import APIRouter, status


router = APIRouter()


@router.get(
    path="/first_5/{dataset_id}",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="Read first 5 records in Dataset by ID",
    description="",
    response_description="",
    deprecated=False,
)
async def read_last_five_records(dataset_id: int) -> dict:
    """
    Root GET
    """

    return {"msg": "All users"}


@router.get(
    path="/last_5/{dataset_id}",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="Read last 5 records in Dataset by ID",
    description="",
    response_description="",
    deprecated=False,
)
async def read_last_five_records(dataset_id: int) -> dict:
    """
    Root GET
    """

    return {"msg": "All users"}


@router.post(
    path="/upload",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Upload data to a TSDH dataset",
    description="",
    response_description="",
    deprecated=False,
)
async def service_post() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


# TODO: Update to pass user_id via query params, not path
@router.put(
    path="/update",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Update data in a TSDH dataset",
    description="",
    response_description="",
    deprecated=False,
)
async def service_put() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.delete(
    path="/remove",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Delete data from a TSDH dataset",
    description="",
    response_description="",
    deprecated=False,
)
async def service_delete() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}
