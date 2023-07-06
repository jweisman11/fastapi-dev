import sys

sys.path.append("..")

from fastapi import APIRouter, status, Header, HTTPException
from data.initialDatasets import DATASETS
from schemas.dataset import Dataset, Classification
from typing import Annotated, List, Union

router = APIRouter()


@router.get(
    path="/",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Get all datasets",
    description="Get all of the available datasets",
    response_description="List of all datasets",
    deprecated=False,
)
async def all_datasets():
    return {"DATASETS": DATASETS}


@router.get(
    path="/{dataset_id:int}",
    response_model=Dataset,
    status_code=status.HTTP_200_OK,
    summary="Get Dataset by ID",
    description="TODO: Add longer description about what this API endpoint does",
    response_description="Return information about an individual dataset",
    deprecated=False,
)
async def fetch_dataset_id(dataset_id: int) -> dict:
    """
    Fetch a single dataset by ID
    """

    result = [dataset for dataset in DATASETS if dataset["id"] == dataset_id]
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No dataset with ID {dataset_id} found",
            headers={"X-Error": "Please try again"},
        )

    if result:
        return result[0]


@router.get(
    path="/schema",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Get all dataset schemas",
    description="",
    response_description="",
    deprecated=False,
)
async def all_dataset_schemas():
    """
    TODO: Update docstring
    """
    return {"DATASETS": DATASETS}


@router.get(
    path="/schema/{dataset_id:int}",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Get schema of dataset by ID",
    description="",
    response_description="",
    deprecated=False,
)
async def all_dataset_schemas_by_id(dataset_id: int):
    """
    TODO: Update docstring
    """
    return {"DATASETS": DATASETS}


@router.get(
    path="/metadata",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Get all datasets metadata",
    description="",
    response_description="",
    deprecated=False,
)
async def all_dataset_metadata():
    """
    TODO: Update docstring
    """
    return {"DATASETS": DATASETS}


@router.get(
    path="/metadata/{dataset_id:int}",
    response_model="",
    status_code=status.HTTP_200_OK,
    summary="Get metadata of dataset by ID",
    description="",
    response_description="",
    deprecated=False,
)
async def dataset_metadata_by_id(dataset_id: int):
    """
    TODO: Update docstring
    """
    return {"DATASETS": DATASETS}


@router.get(
    path="/{dataset_name:str}",
    response_model=Dataset,
    status_code=status.HTTP_200_OK,
    summary="Get Dataset by Name (Acronym)",
    description="Fetch a single dataset by its name. Must pass an acronym",
    response_description="Return information about an individual dataset",
    deprecated=True,
)
async def fetch_dataset_name(dataset_name: str) -> dict:
    """
    Fetch a single dataset by name (acronym)
    """

    result = [
        dataset
        for dataset in DATASETS
        if dataset["name"].upper() == dataset_name.upper()
    ]

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No dataset with name {dataset_name} found",
            headers={"X-Error": "Please try again"},
        )

    if result:
        return result[0]


@router.get(
    path="/classification/{classification}",
    response_model=list[Dataset],
    status_code=status.HTTP_200_OK,
    summary="Get Datasets by Classification",
    description="Retreive all datasets in TSDH by classification level",
    response_description="Array of all datasets matching specified classification level",
    deprecated=True,
)
async def fetch_dataset_classification(dataset_classification: Classification):
    """
    Fetch all datasets by classification level
    """

    result = [
        dataset
        for dataset in DATASETS
        if dataset["classification"].upper() == dataset_classification.value.upper()
    ]

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No dataset with classification {dataset_classification} found",
            headers={"X-Error": "Please try again"},
        )

    if result:
        return result


@router.get(
    path="/search/",
    status_code=status.HTTP_200_OK,
    response_model=list[Dataset],
    summary="Search available datasets",
    description="TODO: Update",
    deprecated=False,
)
async def fetch_dataset_query(
    dataset_name: str | None = None, dataset_classification: Classification = None
):
    """
    Fetch one or more datasets by:
    a) name (aconym)
    b) classification level
    """

    if dataset_classification is not None and dataset_name is not None:
        result = [
            dataset
            for dataset in DATASETS
            if dataset["name"].upper() == dataset_name.upper()
            and dataset["classification"].upper()
            == dataset_classification.value.upper()
        ]
        return result

    if dataset_name is not None:
        result = [
            dataset
            for dataset in DATASETS
            if dataset["name"].upper() == dataset_name.upper()
        ]
        return result

    if dataset_classification is not None:
        result = [
            dataset
            for dataset in DATASETS
            if dataset["classification"].upper() == dataset_classification.value.upper()
        ]
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No datasets found matching search criteria",
        headers={"X-Error": "Please try again"},
    )


@router.post(
    path="/new_dataset/",
    status_code=status.HTTP_201_CREATED,
    response_model="",
    summary="Create new dataset",
    description="TODO: Update description",
    response_description="The new dataset was created",
    deprecated=False,
)
async def new_dataset(dataset: Dataset) -> dict:
    """
    Create new dataset (in-memory only)
    """

    new_dataset = dataset.dict()

    new_dataset["id"] = len(DATASETS) + 1
    DATASETS.append(new_dataset)

    return {"msg": "New dataset has been created"}


@router.put(
    path="/update_dataset/{dataset_id}",
    status_code=status.HTTP_200_OK,
    response_model="",
    summary="Update existing dataset",
    description="TODO: Update description",
    response_description="The dataset has been updated",
    deprecated=False,
)
async def update_dataset(dataset_id: int, dataset: Dataset) -> dict:
    """
    Update existing dataset (in-memory only)
    """
    for i in range(0, len(DATASETS)):
        if DATASETS[i]["id"] == dataset_id:
            DATASETS[i] = {"id": dataset_id, **dataset.dict()}

    return {"msg": "The dataset has been updated"}


@router.delete(
    path="/remove_dataset/{dataset_id:int}",
    status_code=status.HTTP_200_OK,
    response_model="",
    summary="Remove dataset",
    description="TODO: Update description",
    response_description="The dataset has been removed",
    deprecated=False,
)
async def remove_dataset(dataset_id: int) -> dict:
    """
    Remove dataset by Id (in-memory only)
    """
    for i in range(0, len(DATASETS)):
        if DATASETS[i]["id"] == dataset_id:
            del DATASETS[i]
            break

    return {"msg": "The dataset has been removed"}
