import sys

sys.path.append("..")

from fastapi import APIRouter, status


router = APIRouter()


@router.get(
    path="/audit-logs",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="Fetch TSDH audit logs",
    description="",
    response_description="",
    deprecated=False,
)
async def fetch_audit_logs() -> dict:
    """
    TODO: Update docstring
    """

    return {"msg": "All users"}


@router.get(
    path="/api-trail",
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
    path="/failed_requests_all",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="Execute background task",
    description="",
    response_description="",
    deprecated=False,
)
async def fetch_failed_requets() -> dict:
    """
    TODO: Update docstring
    """

    return {"msg": "All users"}


@router.get(
    path="/failed_requests_by_dataset/{dataset_id}",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="Execute background task",
    description="",
    response_description="",
    deprecated=False,
)
async def fetch_failed_requets(dataset_id: int) -> dict:
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
