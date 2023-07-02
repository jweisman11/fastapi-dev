# Pydantic models for API

from pydantic import BaseModel, Field, PastDate
from datetime import date, datetime, time, timedelta



class Dataset(BaseModel):
    """
    Create Pydantic schema for the Dataset Object using:
    field_name: field_type
    """
    name: str | None = Field(
        default=None,
        title="Dataset acronym",
        max_length=25)
    full_name: str = Field(
        default=None,
        title="Dataset full name",
        max_length=100)
    description: str | None = Field(
        default=None,
        title="Description of the dataset",
        max_length=300)
    added_on: date = Field(
        default=date.today(),
        title="Date the dataset was added to TSDH")
    start_date: PastDate() = Field(
        default=date.today() - 1,
        title="Oldest date coverered in the dataset")
    end_date: date = Field(
        default=date.today(),
        title="Newest date coverered in the dataset"
    owner: str | None = Field(
        default=None,
        title="Agency which owns the dataset",
        max_length=25)
    deprecrated: bool = Field(
        default=False,
        title="Whether the dataset is still active or available")

    class Config:
        """
        Define example object of Dataset schema
        """
        schema_extra = {
            "examples": [
                {
                    "name": "ADIS",
                    "full_name": "Arrival and Departure Information System",
                    "description": "Consolidates data from a variety of systems to create a unique person-centric record with complete travel history",
                    "added_on": date(2023, 6, 30),
                    "start_date": date(2020, 3, 11),
                    "end_date": date.today(),
                    "owner": "CBP",
                    "deprecated": False
                }
            ]
        }
