import requests
from fastapi import APIRouter


router = APIRouter()


@router.get(
    path="/{search_term}",
    response_model="",
    summary="Fetch wiki entry for dataset by name",
    description="TODO: Update description",
    response_description="",
)
async def wiki_entry_for_dataset(search_term: str | None = None) -> dict:
    """
    Fetch wikipedia entry for a particular dataset
    """

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": search_term,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
    }

    response = requests.get(url, params=params)
    return response.json()
