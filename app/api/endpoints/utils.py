import sys

sys.path.append("..")

from fastapi import APIRouter, status


router = APIRouter()


@router.get(
    path="/send_email",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="Send Email",
    description="",
    response_description="",
    deprecated=False,
)
async def send_email() -> dict:
    """
    TODO: Update docstring
    """

    return {"msg": "All users"}


@router.get(
    path="/flower",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="Execute background task",
    description="",
    response_description="",
    deprecated=False,
)
async def background_task() -> dict:
    """
    TODO: Update docstring
    """

    return {"msg": "All users"}


@router.get(
    path="/schedule_task",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="Execute background task",
    description="",
    response_description="",
    deprecated=False,
)
async def schedule_task() -> dict:
    """
    TODO: Update docstring
    """

    return {"msg": "All users"}


@router.post(
    path="/",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="",
    description="",
    response_description="",
    deprecated=False,
)
async def service_post() -> dict:
    """
    TODO: Update docstring
    """

    return {"msg": "All users"}


@router.put(
    path="/",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="",
    description="",
    response_description="",
    deprecated=False,
)
async def service_put() -> dict:
    """
    TODO: Update docstring
    """

    return {"msg": "All users"}


@router.delete(
    path="/",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="",
    description="",
    response_description="",
    deprecated=False,
)
async def service_delete() -> dict:
    """
    TODO: Update docstring
    """

    return {"msg": "All users"}
