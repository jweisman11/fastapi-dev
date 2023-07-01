import sys
sys.path.append("..")
from typing import Annotated, Union

from fastapi import APIRouter, Query, Path, status
from pydantic import BaseModel, Field


# Define Pydantic data model used for API endpoints
# This is normally separated out into a separate `models` folder
class Item(BaseModel):
    name: str = Field(min_length=3)
    description: str | None = Field(
        default=None,
        title="The description of the item",
        max_length=300
    )
    price: float = Field(gt=0)
    tax: float = Field(gt=0)

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo Bar",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }



# The route all API endpoints defined within will fall under
router = APIRouter(
    prefix="/helloworld",
    tags=["helloworld"],
    responses={404: {"description": "Not found"}}
)

#
# Define API Endpoints
#

# Explicitly define HTTP status response
# Include summary and description
@router.get("/get_no_params",
            status_code=status.HTTP_200_OK,
            summary="Submit a GET request",
            description="Submit a GET request with no parameters")
async def get_no_params():

    return {"hello":"world"}


# Include PATH parameter
# Use docstring to define description
@router.get("/get_path_param/{name}",
            status_code=status.HTTP_200_OK,
            summary="Pass string parameter")
async def get_path_param(name: str):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    """
    return {"hello":name}


# Include QUERY parameter
# By defining defaults, the query params are optional
@router.get("/get_query_path",
            status_code=status.HTTP_200_OK,
            summary="Summary of endpoint",
            description="Description of what endpoint does")
async def get_query_path(start: int = 0, stop: int = 10):

    return {
        "start": start,
        "stop": stop
    }

# Include QUERY parameter
# By NOT defining defaults, the query params become required
@router.get("/get_query_path_required",
            status_code=status.HTTP_200_OK,
            summary="Endpoint with required query parameteres",
            description="Description of what endpoint does")
async def get_query_path_required(start: int, stop: int):

    return {
        "start": start,
        "stop": stop
    }



@router.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str, None, Query(alias="item-query")],
    q_multi: Annotated[list[str] | None, Query(max_length=5)]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})

    if q_multi:
        results.update({"q_multi":q_multi})
    return results



# How easy it is to depcreate a specific endpoint
@router.get("/get_deprecated",
            status_code=status.HTTP_200_OK,
            summary="Submit a GET request",
            description="Submit a GET request ",
            deprecated=True)
async def get_deprecated():

    return {"hello":"world"}


# POST = "create new"
# Uses the Item data model from above
# Automatically populates documentation with example
@router.post("/new",
            status_code=status.HTTP_201_CREATED,
            summary="Submit a POST request",
            description="Submit a POST request with cool stuff",
            response_description="Item successfully created.")
async def new_entry(item: Item):
    return item


# Combine Request, PATH param and QUERY param into a single endpoint
@router.post("/new_request_path_query/{name}",
             status_code=status.HTTP_201_CREATED,
             summary="Combine all three parameter types",
             description="This endpoint uses three parameter types: Request, Path, and Query")
async def new_request_path_query(item: Item, name: str, q: str | None = None):

    return {
        "name": name,
        "item": item,
        "q": q
    }

# PUT = "insert, replace if already exists"
@router.put("/update",
            status_code=status.HTTP_201_CREATED)
async def update_entry():
    return {"hello":"world"}

@router.delete("/delete")
async def delete_entry():
    return {"hello":"world"}
