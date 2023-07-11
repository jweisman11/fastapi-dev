import sys

sys.path.append("..")

from fastapi import APIRouter, status


router = APIRouter()


@router.get(
    path="/all",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="Get basic statistics of all TSDH datasets",
    description="",
    response_description="",
    deprecated=False,
)
async def root() -> dict:
    """
    Root GET
    """

    return {"msg": "All users"}


@router.get(
    path="/{dataset_id}",
    response_model="",  # User,
    status_code=status.HTTP_200_OK,
    summary="Check basic statistics of datasets by ID",
    description="",
    response_description="",
    deprecated=False,
)
async def health_check_all(dataset_id: int) -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.get(
    path="/record-count/{dataset_id}",
    response_model="",  # User,
    status_code=status.HTTP_200_OK,
    summary="Total number of records in TSDH dataset by ID",
    description="",
    response_description="",
    deprecated=False,
)
async def health_check_by_dataset() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.get(
    path="/last-n-records/{dataset_id}",
    response_model="",  # User,
    status_code=status.HTTP_200_OK,
    summary="Retreive the last n records in TSDH dataset by ID",
    description="",
    response_description="",
    deprecated=False,
)
async def health_check_by_dataset() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.get(
    path="/mean-median-mode/{dataset_id:int}/{column_name:str}",
    response_model="",  # User,
    status_code=status.HTTP_200_OK,
    summary="Calculate mean, median and mode for a single column",
    description="",
    response_description="",
    deprecated=False,
)
async def health_check_by_dataset(dataset_id: int, column_name: str) -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.post(
    path="/create-custom-stat",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Create a custom static for a TSDH dataset",
    description="",
    response_description="",
    deprecated=False,
)
async def create_custom_stat() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


# TODO: Update to pass user_id via query params, not path
@router.put(
    path="/update-custom-stat",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Update a custom statistic for a TSDH dataset",
    description="",
    response_description="",
    deprecated=False,
)
async def update_custom_stat() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.delete(
    path="/delete-custom-stat",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Delete a custom statistic for a TSDH endpoint",
    description="",
    response_description="",
    deprecated=False,
)
async def delete_custom_stat() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}
