from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, Field

class HarvestEvent(BaseModel):
    """
    Represents a single tillage event for a field.
    """
    event_id: str = Field(
        ...,
        alias="eventId",
        description="Unique identifier for this specific harvest event.",
        examples=["TILL-2025-FIELD-A-003"]
    )
    timestamp: datetime = Field(
        ...,
        description="The date and time the harvest occurred."
    )
    harvest_type: str = Field(
        ...,
        alias="harvestType",
        description="The type of harvest performed (Destructive, selective).",
        examples=["Destructive"]
    )
    harvest_method: Optional[str] = Field(
        None,
        alias="implementUsed",
        description="The specific implement used for harvest.",
        examples=["Hand"]
    )
    crop_yield: Optional[float] = Field(
        None,
        alias="cropYield",
        ge=0,
        description="the average crop harvest for the harvest event",
        examples=[20.0]
    )
    crop_yield_units: Optional[str] = Field(
        None,
        alias="cropYieldUnits",
        description="The units for the crop harvest.",
        examples=['bu/acre']
    )
    notes: Optional[str] = Field(
        None,
        description="Any additional notes about the harvest event."
    )

    class Config:
        extra = "forbid"
        validate_by_name = True  # Allow population using 'class' or 'class_name'
        json_schema_extra = {
            "example": {
                "eventId": "TILL-2025-FIELD-A-003",
                "timestamp": "2025-03-10T14:00:00Z",
                "harvestType": "destructive",
                "harvest_method": "machine",
                "crop_yield": 200,
                "crop_yield_units": "bu/acre",
                "notes": "The first and only harvest of the season."
            }
        }
