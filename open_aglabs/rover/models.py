from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Literal

from open_aglabs.core.base_models import Location, AgronomicProperties, TrialProperties


class RoverAcquisitionProperties(BaseModel):
    """
    All the approved values to be captured about Images of Ag Data.
    """
    date: Optional[str] = Field(
        None,
        description="The date the image was taken"
    )
    time: Optional[str] = Field(
        None,
        description="The time the image was taken"
    )
    rover_make: str = Field(
        ...,
        description="Make of the drone")
    rover_model: str = Field(
        ...,
        description="Model of the drone")
    camera_make: str = Field(
        ...,
        description="Make of the camera")
    camera_model: str = Field(
        ...,
        description="Model of the camera")
    camera_height_m: float = Field(
        ...,
        alias="cameraHeight",
        description="Flight height in meters above ground level")
    horizontal_overlap_percentage: float = Field(
        ...,
        alias="horizontalOverlapPercentage",
        description="Image horizontal overlap percentage as a float (e.g., 75.0 for 75%)")
    vertical_overlap_percentage: float = Field(
        ...,
        alias="verticalOverlapPercentage",
        description="Image vertical overlap percentage as a float (e.g., 75.0 for 75%)")
    gps_quality: Optional[str] = Field(
        None,
        alias="gpsQuality",
        description="The quality of the GPS data (e.g., RTK, DGPS, etc.)")

    model_config = ConfigDict(
        extra='forbid'
    )


class RoverScan(BaseModel):
    id: str = Field(
        ...,
        description="Unique identifier for this drone flight."
    )
    name: Optional[str] = Field(
        None,
        alias="name",
        description="Name of the drone flight.")
    task: Optional[str] = Field(
        None,
        description="Task associated with the drone flight.")
    location: Location = Field(
        ...,
        description="Location of the drone flight.")
    trial_properties: Optional[TrialProperties] = Field(
        None,
        alias="trialProperties",
        description="Dictionary containing trial properties of the drone flight.")
    rover_acquisition_properties: RoverAcquisitionProperties = Field(
        ...,
        description="Make of the drone")
    agronomic_properties: AgronomicProperties = Field(
        None,
        alias="agronomicProperties",
        description="Dictionary containing agronomic properties of the drone flight.")
    images: Optional[List[str]] = Field(
        None,
        description="List of images associated with the flight")
    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Morning Phenotyping Flight",
                "task": "Canopy Coverage Assessment",
                "location": {
                    "id": "loc-789-xyz",
                    "name": "Field Station Alpha",
                    "latitude": 41.8781,
                    "longitude": -87.6298,
                    "elevation_m": 182.0,
                    "site": "Midwest Research Hub",
                    "field": "Plot-4B",
                    "admin_level_0": "USA",
                    "admin_level_1": "Illinois"
                },
                "trialProperties": {
                    "name": "Drought Resistance Study 2025",
                    "id": "trial-2025-DR-01"
                },
                "rover_acquisition_properties": {
                    "date": "2025-07-15",
                    "time": "10:30:00",
                    "rover_make": "NewCo",
                    "rover_model": "Rover-1",
                    "camera_make": "sony",
                    "camera_model": "MX-1000",
                    "cameraHeight": 45.5,
                    "horizontalOverlapPercentage": 75.0,
                    "verticalOverlapPercentage": 70.0,
                    "gpsQuality": "RTK Fixed"
                },
                "agronomicProperties": {
                    "crop_type": "maize",
                    "growth_stage": "V6",
                    "soil_color": "dark",
                    "irrigation_level": "standard",
                    "tillage_type": "no-till"
                },
                "images": [
                    "s3://ag-data/flights/2025-07-15/img_0001.tif",
                    "s3://ag-data/flights/2025-07-15/img_0002.tif"
                ]
            }
        }
    )
