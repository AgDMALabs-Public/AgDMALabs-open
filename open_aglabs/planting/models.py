from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field



class PlantingEvent(BaseModel):
    """
    Represents a single planting event for a field.
    """
    event_id: str = Field(
        ...,
        alias="eventId",
        description="Unique identifier for this specific planting event.",
        examples=["PLANT-2025-FIELD-A-001"]
    )
    timestamp: datetime = Field(
        ...,
        description="The date and time the planting occurred."
    )
    crop_type: str = Field(
        ...,
        alias="cropType",
        description="The type of crop planted (e.g., 'Corn', 'Soybeans', 'Wheat').",
        examples=["Corn"]
    )
    variety: Optional[str] = Field(
        None,
        description="Specific variety or hybrid of the crop.",
        examples=["Dekalb DKC67-44RIB"]
    )
    seeding_rate: float = Field(
        ...,
        alias="seedingRate",
        description="The rate at which seeds were planted.",
        examples=[34000]
    )
    seeding_unit: str = Field(
        ...,
        alias="seedingUnit",
        description="The unit for the seeding rate (e.g., 'seeds/acre', 'seeds/ha').",
        examples=["seeds/acre"]
    )
    depth_cm: Optional[float] = Field(
        None,
        alias="depthCm",
        ge=0,
        description="Planting depth in centimeters.",
        examples=[5.0]
    )
    notes: Optional[str] = Field(
        None,
        description="Any additional notes about the planting event."
    )

    class ConfigDict:
        extra = "forbid"
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "eventId": "PLANT-2025-FIELD-A-001",
                "timestamp": "2025-04-20T08:00:00Z",
                "cropType": "Corn",
                "variety": "Pioneer P1197AM",
                "seedingRate": 34500,
                "seedingUnit": "seeds/acre",
                "depthCm": 5.5,
                "notes": "Field A planted with corn, good soil moisture."
            }
        }