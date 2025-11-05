from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict
from ..core.base_models import Location

class HarvestEvent(BaseModel):
    """
    Represents a single tillage event for a field.
    """
    id: str = Field(
        ...,
        alias="Id",
        description="Unique identifier for this specific harvest event.",
        examples=["TILL-2025-FIELD-A-003"]
    )
    file_path: Optional[str] = Field(
        default_factory=str,
        alias="Path",
        description="The path to the spatial data."
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
    nominal_moisture: Optional[float] = Field(
        None,
        alias="cropNominalMoisture",
        ge=0,
        le=100,
        description="The nominal moisture content of the crop.",
        examples=[15.5]
    )
    area: Optional[float] = Field(
        None,
        description="The area harvested.",
        examples=[100.0]
    )
    area_units: Optional[str] = Field(
        None,
        description="The units for the area harvested.",
        examples=[100.0]
    )
    mass: Optional[float] = Field(
        None,
        description="The mass harvested.",
    )
    mass_units: Optional[str] = Field(
        None,
        description="The units for the mass harvested.",
        examples=['kg']
    )
    nominal_volume: Optional[float] = Field(
        None,
        description="The amount of mass in the volume measurement, EX: 56 lbs of corn in a bu.",
        examples=[56.0]
    )
    nominal_mass_units: Optional[str] = Field()
    notes: Optional[str] = Field(
        None,
        description="Additional notes about the harvest event."
    )
    model_config = ConfigDict(
        extra="forbid",
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "HARV-2025-FIELD-A-001",
                'file_path': 'path/to/harvest/data.geojson',
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
                "cropNominalMoisture": 15.5,
                "area": 100.0,
                "area_units": "acres",
                "mass": 1000.0,
                "mass_units": "lbs",
                "nominal_volume": 56.0,
                "notes": "First pass of corn harvest in Field A. Good yield observed."
            }
        }
    )
