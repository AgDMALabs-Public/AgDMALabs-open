from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Literal

from ..core.base_models import Location


class DroneFlight(BaseModel):
    id: str = Field(
        ...,
        description="Unique identifier for this drone flight."
    )
    location: Location = Field(...,
                               description="Location of the drone flight.")
    drone_make: str = Field(...,
                            alias="droneMake",
                            description="Make of the drone")
    drone_model: str = Field(...,
                             alias="droneModel",
                             description="Model of the drone")
    camera_make: str = Field(...,
                             alias="cameraMake",
                             description="Make of the camera")
    camera_model: str = Field(...,
                              alias="cameraModel",
                              description="Model of the camera")
    ground_control_points: bool = Field(...,
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

    flight_height: float = Field(...,
                                 alias="flightHeight",
                                 description="Flight height in meters above ground level")
    horizontal_overlap_percentage: float = Field(...,
                                                 alias="horizontalOverlapPercentage",
                                                 description="Image horizontal overlap percentage as a float (e.g., 75.0 for 75%)")
    vertical_overlap_percentage: float = Field(...,
                                               alias="verticalOverlapPercentage",
                                               description="Image vertical overlap percentage as a float (e.g., 75.0 for 75%)")
    gps_quality: str = Field(...,
                             alias="gpsQuality",
                             description="The quality of the GPS data (e.g., RTK, DGPS, etc.)")
    multispec_channels: Optional[List[str]] = Field(None,
                                                    alias="multispecChannels",
                                                    description="List of multispectral channels if applicable (e.g., ['Red', 'Green', 'Blue', 'NIR'])")
    directory: Optional[str] = Field(None,
                                     alias="directory",
                                     description="The directory where the flight data is stored")
    images: List[str] = Field(...,
                              alias="images",
                              description="List of image IDs associated with the flight")

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
