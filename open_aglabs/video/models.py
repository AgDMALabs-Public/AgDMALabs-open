from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List

from open_aglabs.core.base_models import Location, Notes, AgronomicProperties, TrialProperties, \
    ProtocolProperties, CollectionProperties
from open_aglabs.image.models import CameraProperties, AcquisitionProperties

from open_aglabs.core.constants import IMAGE_TYPE_LIST


class VideoQuality(BaseModel):
    """
    The properties associated with Image Quality
    """
    height: Optional[float] = Field(
        None,
        description="The height of the image in pixels.",
        ge=0,
        le=100000
    )
    width: Optional[float] = Field(
        None,
        description="The width of the image in pixels",
        ge=0,
        le=100000
    )
    frame_rate: Optional[float] = Field(
        None,
        description="The frame rate in frames per second.",
        ge=1,
    )
    channels: Optional[float] = Field(
        None,
        description="The number of channels in the image.",
        ge=1,
    )
    orientation: Optional[Literal[*ORIENTATION_LIST]] = Field(
        None,
        description="The orientation of the image."
    )
    rotation: Optional[float] = Field(
        None,
        description="The camera rotation."
    )
    duration: Optional[float] = Field(
        None,
        description="The duration of the video."
    )
    frames: Optional[float] = Field(
        None,
        description="The number of frames in the video."
    )
    model_config = ConfigDict(
        extra='forbid'
    )


class AgVideoModel(BaseModel):
    """
    All the approved values to be captured about Images of Ag Data.
    """
    path: Optional[str] = Field(
        None,
        description="The path to the image"
    )
    id: str = Field(
        ...,
        validation_alias=AliasChoices('image_id', 'id'),
        description="The Unique ID of the image, should be the image name, by default UUID4."
    )
    device: Optional[str] = Field(
        None,
        description="The type of device that is collecting the images, mobile, auxillery, or drone."
    )
    type: Optional[Literal[*IMAGE_TYPE_LIST]] = Field(
        None,
        description="The type of image it is: original, augmented, synthetic."
    )
    protocol_properties: Optional[ProtocolProperties] = Field(
        None
    )
    trial_properties: Optional[TrialProperties] = Field(
        None
    )
    camera_properties: Optional[CameraProperties] = Field(
        None
    )
    location_properties: Optional[Location] = Field(
        None
    )
    acquisition_properties: Optional[AcquisitionProperties] = Field(
        None
    )
    video_quality: Optional[VideoQuality] = Field(
        None
    )
    agronomic_properties: Optional[AgronomicProperties] = Field(
        None
    )
    collection_properties: Optional[CollectionProperties] = Field(
        None,
        description="Collection level information, will only contain CollectionID"
    )
    notes: Optional[List[Notes]] = Field(
        None
    )

    model_config = ConfigDict(
        extra='allow',
        json_schema_extra={
            "example": {
                "path": "/data/2025/trials/trial_101/images/img_5521.mp4",
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "device": "mobile",
                "type": "original",
                "protocol_properties": {
                    "name": "Standard Field Scout v2",
                    "id": "soybean_rust_protocol",
                    "url": "https://aglabs.open/protocols/v2/scout"
                },
                "trial_properties": {
                    "name": "drought_resistance_2025",
                    "id": "trial-2025-001"
                },
                "camera_properties": {
                    "make": "Samsung",
                    "model": "Galaxy S24",
                    "device_id": "phone-001-user-x",
                    "iso": 50.0,
                    "magnification": 1.0,
                    "camera_characteristics": "24mm wide angle"
                },
                "location_properties": {
                    "id": "loc-8821",
                    "name": "Field 7 - Row 10",
                    "latitude": 41.8781,
                    "longitude": -87.6298,
                    "elevation_m": 182.0,
                    "crs": "EPSG:4326",
                    "admin_level_0": "USA",
                    "admin_level_1": "Illinois",
                    "site": "Midwest Research Station",
                    "grower": "J. Doe",
                    "field": "F7"
                },
                "acquisition_properties": {
                    "date": "2025-07-15",
                    "time": "14:30:00",
                    "camera_height_m": 1.5,
                    "camera_angle_deg": -45.0,
                    "light_source": "natural",
                    "lighting_lux": 85000.0,
                    "setting": "field"
                },
                "video_quality": {
                    "height": 3000.0,
                    "width": 4000.0,
                    "channels": 3
                },
                "agronomic_properties": {
                    "crop_type": "soybean",
                    "growth_stage": "R3",
                    "soil_color": "dark",
                    "weed_pressure": "medium-low",
                    "irrigation_level": "none",
                    "tillage_type": "reduced",
                    "plant_health": {
                        "stressors": "drought",
                        "ranked_stressors": "1. drought, 2. insect"
                    }
                },
                "collection_properties": {
                    "id": "col-daily-scout-20250715",
                    "username": "scout_user_1",
                    "start_datetime": "2025-07-15T14:00:00",
                    "num_images": "50"
                },
                "notes": [
                    {
                        "message": "Leaves showing signs of curling.",
                        "author": "field_technician"
                    }
                ]
            }
        }
    )
