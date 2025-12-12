from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Literal

from open_aglabs.core.base_models import Location, AgronomicProperties, TrialProperties


class DroneAcquisitionProperties(BaseModel):
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
    drone_make: str = Field(
        ...,
        alias="droneMake",
        description="Make of the drone")
    drone_model: str = Field(
        ...,
        alias="droneModel",
        description="Model of the drone")
    camera_make: str = Field(
        ...,
        alias="cameraMake",
        description="Make of the camera")
    camera_model: str = Field(
        ...,
        alias="cameraModel",
        description="Model of the camera")
    ground_control_points: bool = Field(
        ...,
        alias="groundControlPoints",
        description="Indicates if ground control points were used during the flight")
    reflectance_panels: bool = Field(...,
                                     alias="reflectancePanels",
                                     description="Indicates if reflectance panels were used for radiometric calibration")
    reflectance_panel_type: Optional[Literal["Micasense", "Thermal", "Parrot", "Other"]] = Field(
        None,
        alias="reflectancePanelType",
        description="The type of reflectance panels used. Must be one of 'Micasense', 'Thermal', 'Parrot', or 'Other'."
    )

    flight_height_m: float = Field(
        ...,
        alias="flightHeight",
        description="Flight height in meters above ground level")
    horizontal_overlap_percentage: float = Field(
        ...,
        alias="horizontalOverlapPercentage",
        description="Image horizontal overlap percentage as a float (e.g., 75.0 for 75%)")
    vertical_overlap_percentage: float = Field(
        ...,
        alias="verticalOverlapPercentage",
        description="Image vertical overlap percentage as a float (e.g., 75.0 for 75%)")
    gps_quality: str = Field(
        ...,
        alias="gpsQuality",
        description="The quality of the GPS data (e.g., RTK, DGPS, etc.)")
    multispec_channels: Optional[List[str]] = Field(
        None,
        alias="multispecChannels",
        description="List of multispectral channels if applicable (e.g., ['Red', 'Green', 'Blue', 'NIR'])")

    model_config = ConfigDict(
        extra='forbid'
    )


class DroneFlight(BaseModel):
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
    drone_acquisition_properties: DroneAcquisitionProperties = Field(
        ...,
        description="Make of the drone")
    agronomic_properties: AgronomicProperties = Field(
        None,
        alias="agronomicProperties",
        description="Dictionary containing agronomic properties of the drone flight.")
    images: List[str] = Field(
        ...,
        description="List of images associated with the flight")

    model_config = ConfigDict(
        extra="forbid",
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "drone-flight-uuid-67890",
                "location": {
                    "id": "loc-uuid-12345",
                    "name": "Field 12 Drone Flight",
                    "latitude": 34.0522,
                    "longitude": -118.2437,
                    "elevation_m": 100.0,
                    "crs": "EPSG:4326",
                    "site": "AgTech Research Farm",
                    "field": "Field_12",
                    "location": "Central part of Field 12"
                },
                "droneMake": "DJI",
                "droneModel": "Mavic 3 Multispectral",
                "cameraMake": "Micasense",
                "cameraModel": "Altum",
                "groundControlPoints": True,
                "reflectancePanels": False,
                "reflectancePanelType": "Micasense",
                "flightHeight": 80.0,
                "horizontalOverlapPercentage": 70.0,
                "verticalOverlapPercentage": 70.0,
                "gpsQuality": "RTK",
                "multispecChannels": ["Green", "Red", "Red Edge", "NIR"],
                "directory": "/path/to/flight/data",
                "images": ['1234564565_1.tif', '1234564565_2.tif', '1234564565_3.tif', '1234564565_4.tif']
            }
        }
    )
