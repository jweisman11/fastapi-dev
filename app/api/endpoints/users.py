import sys

sys.path.append("..")

from fastapi import APIRouter, status
from schemas.users import User


router = APIRouter()


@router.get(
    path="/list_all_users",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="",
    description="",
    response_description="",
    deprecated=False,
)
async def fetch_all_users() -> list:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.get(
    path="/self",
    response_model="",  # User,
    status_code=status.HTTP_200_OK,
    summary="",
    description="",
    response_description="",
    deprecated=False,
)
async def fetch_self() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.get(
    path="/is_superuser/{user_id}",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="",
    description="",
    response_description="",
    deprecated=False,
)
async def check_if_superuser() -> bool:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.get(
    path="/user_type/{user_id}",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="",
    description="",
    response_description="",
    deprecated=False,
)
async def check_user_type() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.post(
    path="/new_user",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="",
    description="",
    response_description="",
    deprecated=False,
)
async def create_new_user() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


# TODO: Update to pass user_id via query params, not path
@router.put(
    path="/update_user",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="",
    description="",
    response_description="",
    deprecated=False,
)
async def check_user_type(user_id: int) -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.delete(
    path="/remove_user",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="",
    description="",
    response_description="",
    deprecated=False,
)
async def check_user_type(user_id: int) -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}
