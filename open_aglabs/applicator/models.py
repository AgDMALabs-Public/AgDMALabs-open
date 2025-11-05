from typing import Optional, Literal, List
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from ..core.base_models import Location
from ..core.constants import RATE_UNITS


class ApplicationEvent(BaseModel):
    """
    Represents a single application event (e.g., fertilizer, pesticide, herbicide).
    """
    schema_name: Literal["ApplicationEvent"] = Field(
        "ApplicationEvent",
        description="The name of the schema for this model."
    )
    id: str = Field(
        ...,
        alias="Id",
        description="Unique identifier for this specific application event.",
        examples=["APP-2025-FIELD-A-002"]
    )
    file_path: Optional[str] = Field(
        default_factory=str,
        alias="filePath",
        description="The path to the spatial data."
    )
    location: Optional[Location] = Field(
        None
    )
    timestamp: datetime = Field(
        ...,
        description="The date and time the application occurred."
    )
    application_type: Optional[str] = Field(
        None,
        alias="applicationType",
        description="The type of application (e.g., 'Fertilizer', 'Herbicide', 'Fungicide', 'Insecticide').",
        examples=["Herbicide"]
    )
    mix_name: str = Field(
        ...,
        alias="mixName",
        description="The name of the product applied.",
        examples=["Roundup PowerMAX"]
    )
    mix_id: Optional[str] = Field(
        ...,
        alias="mixId",
        description="The unique ID of the mix that was applied.",
        examples=['1234-234-567-1985']
    )
    rate: float = Field(
        ...,
        alias="applicationRate",
        ge=0,
        description="The rate at which the product was applied.",
        examples=[2.5]
    )
    rate_unit: str = Field(
        ...,
        alias="rateUnit",
        description="The unit for the application rate (e.g., 'L/ha', 'gal/acre', 'kg/ha').",
        examples=["L/ha"]
    )
    method: Optional[str] = Field(
        None,
        description="The method of application (e.g., 'Broadcast', 'Foliar', 'In-furrow', 'Side-dress').",
        examples=["Foliar"]
    )
    equipment: Optional[str] = Field(
        None,
        description="The equipment used for the application.",
        examples=["Sprayer"]
    )
    notes: Optional[str] = Field(
        None,
        description="Any additional notes about the application event."
    )

    model_config = ConfigDict(
        extra="forbid",
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "schema_name": "ApplicationEvent",
                "id": "1234-679-123-456-4456",
                "filePath": "path/to/application/data.geojson",
                "location": {  # Nested Location example
                    "id": "loc-uuid-12345",
                    "name": "Research Plot A",
                    "elevation_m": 150.5,
                    "crs": "EPSG:4326",
                    "geometry": "POINT (-118.2437 34.0522)"
                },
                "timestamp": "2025-05-15T10:30:00Z",
                "applicationType": "Herbicide",
                "mixName": "Glyphosate 41%",
                "applicationRate": 2.0,
                "rateUnit": "L/ha",
                "method": "Broadcast",
                "equipment": "Tractor Sprayer",
                "notes": "Post-emergent herbicide application on weeds."
            }
        }
    )


class ApplicatorZone(BaseModel):
    id: str = Field(
        ...,
        description="Unique identifier for this specific zone.",
    )
    geometry: str = Field(
        ...,
        description="The geometry for this zone.",
    )
    tank_id: str = Field(
        ...,
        description="The tank ID for this zone.",
    )
    tank_mix: str = Field(
        ...,
        description="The tank mix for this zone.",
    )
    rate: float = Field(
        ...,
        ge=0,
        description="The rate for this zone.",
    )


class ApplicatorRx(BaseModel):
    schema_name: Literal["ApplicatorRx"] = Field(
        ...,
        description="The name of the schema for this model."
    )
    id: str = Field(
        ...,
        alias="eventId",
        description="Unique identifier for this specific application event.",
        examples=["APP-2025-FIELD-A-002"]
    )
    crs: str = Field(
        ...,
        description="The coordinate reference system for the geometry.",
    )
    units: Literal[*RATE_UNITS] = Field(
        ...,
        description="The units for the rate.",
    )
    zones: List[ApplicatorZone] = Field(
        ...,
        description="A list of all the zones."
    )
    model_config = ConfigDict(
        extra="forbid",
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "schema_name": "ApplicatorRx",
                "Id": "RX-2023-FIELD-B-001",
                "crs": "EPSG:4326",
                "units": "l/ha",
                "zones": [
                    {
                        "id": "zone-1",
                        "geometry": "POLYGON ((-118.25 34.05, -118.24 34.05, -118.24 34.04, -118.25 34.04, -118.25 34.05))",
                        "tank_id": "TANK001",
                        "tank_mix": "Mix_A_Herbicide",
                        "rate": 2.5
                    },
                    {
                        "id": "zone-2",
                        "geometry": "POLYGON ((-118.23 34.05, -118.22 34.05, -118.22 34.04, -118.23 34.04, -118.23 34.05))",
                        "tank_id": "TANK002",
                        "tank_mix": "Mix_B_Fertilizer",
                        "rate": 10
                    }
                ]
            }
        }
    )
