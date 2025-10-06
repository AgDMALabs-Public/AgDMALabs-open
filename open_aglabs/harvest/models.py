from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict
from ..core.base_models import Location

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
    location: Optional[Location] = Field(
        None
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

    model_config = ConfigDict(
        extra="forbid",
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "eventId": "HARV-2025-FIELD-A-001",
                "location": {
                    "id": "loc-harvest-789",
                    "name": "Field A Harvest Zone 1",
                    "latitude": 34.123,
                    "longitude": -118.456,
                    "elevation_m": 120.0,
                    "crs": "EPSG:4326",
                    "geometry": "POINT (-118.456 34.123)",
                },
                "timestamp": "2025-09-20T10:00:00Z",
                "harvestType": "Destructive",
                "implementUsed": "Combine Harvester",
                "cropYield": 250.75,
                "cropYieldUnits": "bu/acre",
                "notes": "First pass of corn harvest in Field A. Good yield observed."
            }
        }
    )
