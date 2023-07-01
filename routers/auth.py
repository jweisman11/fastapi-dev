import sys
sys.path.append("..")

from starlette import status
from starlette.responses import RedirectResponse

from fastapi import Depends, APIRouter, Request
from fastapi.responses import HTMLResponse


router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def read_all_by_user():

    return {"hello":"world"}
