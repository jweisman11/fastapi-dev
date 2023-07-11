import sys

sys.path.append("..")

from fastapi import APIRouter, status


router = APIRouter()


@router.get(
    path="/",
    response_model="",  # list[User],
    status_code=status.HTTP_200_OK,
    summary="",
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
    path="/access-token",
    response_model="",  # User,
    status_code=status.HTTP_200_OK,
    summary="Check health of all TSDH datasets",
    description="",
    response_description="",
    deprecated=False,
)
async def health_check_all() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


@router.get(
    path="/password-recovery",
    response_model="",  # User,
    status_code=status.HTTP_200_OK,
    summary="Check health of TSDH dataset by ID",
    description="",
    response_description="",
    deprecated=False,
)
async def health_check_by_dataset() -> dict:
    """
    Fetch all users in system
    """

    return {"msg": "All users"}


# @router.post(
#     path="/",
#     response_model="",
#     status_code=status.HTTP_200_OK,
#     summary="",
#     description="",
#     response_description="",
#     deprecated=False,
# )
# async def service_post() -> dict:
#     """
#     Fetch all users in system
#     """

#     return {"msg": "All users"}


# # TODO: Update to pass user_id via query params, not path
# @router.put(
#     path="/",
#     response_model="",
#     status_code=status.HTTP_200_OK,
#     summary="",
#     description="",
#     response_description="",
#     deprecated=False,
# )
# async def service_put() -> dict:
#     """
#     Fetch all users in system
#     """

#     return {"msg": "All users"}


# @router.delete(
#     path="/",
#     response_model="",
#     status_code=status.HTTP_200_OK,
#     summary="",
#     description="",
#     response_description="",
#     deprecated=False,
# )
# async def service_delete() -> dict:
#     """
#     Fetch all users in system
#     """

#     return {"msg": "All users"}
