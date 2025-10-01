from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, Field

from open_aglabs.planting.models import PlantingEvent
from open_aglabs.applicator.models import ApplicationEvent
from open_aglabs.harvest.models import HarvestEvent


class TillageEvent(BaseModel):
    """
    Represents a single tillage event for a field.
    """
    event_id: str = Field(
        ...,
        alias="eventId",
        description="Unique identifier for this specific tillage event.",
        examples=["TILL-2025-FIELD-A-003"]
    )
    timestamp: datetime = Field(
        ...,
        description="The date and time the tillage occurred."
    )
    tillage_type: str = Field(
        ...,
        alias="tillageType",
        description="The type of tillage performed (e.g., 'Conventional', 'No-till', 'Minimum-till', 'Chisel Plow').",
        examples=["Chisel Plow"]
    )
    implement_used: Optional[str] = Field(
        None,
        alias="implementUsed",
        description="The specific implement used for tillage.",
        examples=["John Deere 2700 Ripper"]
    )
    depth_cm: Optional[float] = Field(
        None,
        alias="depthCm",
        ge=0,
        description="Average tillage depth in centimeters.",
        examples=[20.0]
    )
    notes: Optional[str] = Field(
        None,
        description="Any additional notes about the tillage event."
    )

    class Config:
        extra = "forbid"
        validate_by_name = True  # Allow population using 'class' or 'class_name'
        json_schema_extra = {
            "example": {
                "eventId": "TILL-2025-FIELD-A-003",
                "timestamp": "2025-03-10T14:00:00Z",
                "tillageType": "Chisel Plow",
                "implementUsed": "Case IH Chisel Plow",
                "depthCm": 25.0,
                "notes": "Primary tillage after winter. Good soil penetration."
            }
        }


class FieldManagement(BaseModel):
    """
    Represents the management history for a single agricultural field over a season,
    including planting, application, and tillage events.
    """
    field_id: str = Field(
        ...,
        alias="fieldId",
        description="Unique identifier for the agricultural field.",
        examples=["FIELD-A-2025"]
    )
    season_year: int = Field(
        ...,
        alias="seasonYear",
        description="The calendar year for which this management data is relevant.",
        examples=[2025]
    )
    planting_events: List[PlantingEvent] = Field(
        ...,
        description="A list of all the planting events."
    )
    application_events: List[ApplicationEvent] = Field(
        ...,
        description="A list of all the application events."
    )
    tillage_events: List[TillageEvent] = Field(
        ...,
        description="A list of all the tillage events."
    )
    harvest_events: List[HarvestEvent] = Field(
        ...,
        description="A list of all the harvest Events."
    )

    class Config:
        extra = "forbid"
        validate_by_name = True  # Allow population using 'class' or 'class_name'
        json_schema_extra = {
            "example": {
                "fieldId": "FIELD-A-2025",
                "seasonYear": 2025,
                "planting_events": [
                    {
                        "eventId": "PLANT-2025-FIELD-A-001",
                        "timestamp": "2025-04-20T08:00:00Z",
                        "cropType": "Corn",
                        "variety": "Pioneer P1197AM",
                        "seedingRate": 34500,
                        "seedingUnit": "seeds/acre",
                        "depthCm": 5.5,
                        "notes": "Field A planted with corn, good soil moisture."
                    }],
                'tillage_events': [{
                    "eventId": "TILL-2025-FIELD-A-003",
                    "timestamp": "2025-03-10T14:00:00Z",
                    "tillageType": "Chisel Plow",
                    "implementUsed": "Case IH Chisel Plow",
                    "depthCm": 25.0,
                    "notes": "Primary tillage after winter. Good soil penetration."
                }],
                'application_events': [{
                    "eventId": "APP-2025-FIELD-A-002",
                    "timestamp": "2025-05-15T10:30:00Z",
                    "applicationType": "Herbicide",
                    "productName": "Glyphosate 41%",
                    "applicationRate": 2.0,
                    "rateUnit": "L/ha",
                    "method": "Broadcast",
                    "equipment": "Tractor Sprayer",
                    "notes": "Post-emergent herbicide application on weeds."
                },
                    {
                        "eventId": "APP-2025-FIELD-A-004",
                        "timestamp": "2025-07-01T09:00:00Z",
                        "applicationType": "Fertilizer",
                        "productName": "Urea",
                        "applicationRate": 150.0,
                        "rateUnit": "kg/ha",
                        "method": "Side-dress",
                        "equipment": "Fertilizer Spreader",
                        "notes": "Nitrogen application at V8 growth stage."
                    }
                ],
                'harvest_events': [{
                    "eventId": "TILL-2025-FIELD-A-003",
                    "timestamp": "2025-03-10T14:00:00Z",
                    "harvestType": "destructive",
                    "harvest_method": "machine",
                    "crop_yield": 200,
                    "crop_yield_units": "bu/acre",
                    "notes": "The first and only harvest of the season."
                }]
            }
        }
