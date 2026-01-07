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
        description="Make of the drone")
    drone_model: str = Field(
        ...,
        description="Model of the drone")
    camera_make: str = Field(
        ...,
        description="Make of the camera")
    camera_model: str = Field(
        ...,
        description="Model of the camera")
    ground_control_points: bool = Field(
        ...,
        alias="groundControlPoints",
        description="Indicates if ground control points were used during the flight")
    reflectance_panels: bool = Field(
        ...,
        alias="reflectancePanels",
        description="Indicates if reflectance panels were used for radiometric calibration")
    reflectance_panel_type: Optional[Literal["Micasense", "Thermal", "Parrot", "Other", None]] = Field(
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
    gps_quality: Optional[str] = Field(
        None,
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
    images: Optional[List[str]] = Field(
        None,
        description="List of images associated with the flight")
    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "drone-flight-uuid-98765",
                "name": "Corn Health Assessment Flight",
                "task": "canopy_analysis",
                "location": {
                    "id": "loc-uuid-54321",
                    "name": "West Field Drone Flight",
                    "latitude": 35.1234,
                    "longitude": -119.5678,
                    "elevation_m": 120.0,
                    "crs": "EPSG:4326",
                    "site": "AgriCore Research Facility",
                    "field": "West_Field_03",
                    "location": "Section B"
                },
                "trialProperties": {
                    "name": "Fungicide Efficacy Trial 2025"
                },
                "drone_acquisition_properties": {
                    "droneMake": "Quantum-Systems",
                    "droneModel": "Trinity F90+",
                    "cameraMake": "Sony",
                    "cameraModel": "UCM-R",
                    "groundControlPoints": True,
                    "reflectancePanels": True,
                    "reflectancePanelType": "Standard",
                    "flightHeight": 90.0,
                    "horizontalOverlapPercentage": 75.0,
                    "verticalOverlapPercentage": 75.0,
                    "gpsQuality": "RTK",
                    "multispecChannels": [
                        "Red",
                        "Green",
                        "Blue",
                        "NIR"
                    ]
                },
                "agronomicProperties": {
                    "crop_type": "corn",
                    "growth_stage": "VT",
                    "soil_color": "light brown",
                    "weed_pressure": "low",
                    "irrigation_level": "high",
                    "tillage_type": "conventional",
                    "fertilizer_level": "high"
                },
                "images": [
                    "flight_98765_img_001.tif",
                    "flight_98765_img_002.tif",
                    "flight_98765_img_003.tif",
                    "flight_98765_img_004.tif",
                    "flight_98765_img_005.tif"
                ]
            }
        }
    )
