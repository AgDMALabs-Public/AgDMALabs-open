from pydantic import BaseModel, Field
from typing import Optional, Literal
from uuid import uuid4

from ..core.base_models import MLOutput, Location
from ..core.constants import CROP_LIST, SOIL_COLOR


class ImageProtocol(BaseModel):
    """
    Pydantic model to store data about an image of agricultural materials.
    """
    name: str = Field(...,
                      description="The Name of the protocol used to capture the image.")
    sample_type: str = Field(...,
                             description="What is being imaged (e.g., 'corn field', 'soil', 'tomato fruit').")
    camera_height_mm: float = Field(...,
                                    gt=0,
                                    description="Height of the camera from the sample in millimeters.")
    camera_angle: float = Field(...,
                                description="The angle that the camera is at relative to vertical. eg: top down is 0")
    magnification: float = Field(...,
                                 gt=0,
                                 description="Magnification level used for the image capture.")
    lighting_conditions: Optional[str] = Field(None,
                                               description="Description of the lighting conditions (e.g., 'natural sunlight', 'LED array', 'dark field').")
    notes: Optional[str] = Field(None,
                                 description="Any additional relevant notes or observations.")


class AgronomicProperties(BaseModel):
    """
    Pydantic model representing approved values to be captured about images of agricultural data.
    """
    crop_type: Optional[
        Literal[*CROP_LIST]] = Field(
        None,
        description="The type of crop present in the image."
    )
    growth_stage: Optional[str] = Field(
        None,
        description="The growth stage of the crop, if a crop is present"
    )
    soil_color: Optional[Literal[*SOIL_COLOR]] = Field(
        None,
        description="The predominant color of the soil in the image."
    )
    weed_pressure: Optional[Literal["high", "high-medium", "medium", "medium-low", "low"]] = Field(
        None,
        description="The level of weed presence in the image."
    )
    irrigation_level: Optional[Literal["high", "standard", "low", "none"]] = Field(
        None,
        description="The observed irrigation level."
    )
    tillage_type: Optional[Literal["conventional", "reduced", "no-till"]] = Field(
        None,
        description="The type of tillage observed."
    )
    fertilizer_level: Optional[Literal["high", "standard", "low"]] = Field(
        None,
        description="The observed fertilizer level."
    )

    class ConfigDict:
        extra = 'forbid'


class CameraProperties(BaseModel):
    """
    Values to support the proper documentation of camera, if you add information to this json please update this doc. https://docs.google.com/spreadsheets/d/1zljGA5xtwtLNXqjohfXeJzh6SFwdObAjmb5gHflQfIA/edit?gid=1769639569#gid=1769639569
    """
    make: Optional[float] = Field(
        None,
        description="The make (manufacturer) of the camera, represented as a number."
    )
    model: Optional[str] = Field(
        None,
        description="The model of the camera."
    )
    iso: Optional[float] = Field(
        None,
        description="The iso setting of the camera."
    )
    magnification: Optional[float] = Field(
        None,
        description="The magnification setting of the camera."
    )


class AcquisitionProperties(BaseModel):
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
    camera_height_m: Optional[float] = Field(
        None,
        description="The height of the camera in meters",
        ge=0
    )
    camera_angle_deg: Optional[float] = Field(
        None,
        description="The angle of the camera when the photo was taken",
        ge=-180,
        le=180
    )
    object_resolution: Optional[str] = Field(
        None,
        description="Image Level / Collection Level depending on variance."
    )
    object_resolution_ml: Optional[MLOutput] = Field(
        None,
        description="The resolution of the object in the image predicted by a ML model."
    )
    light_source: Optional[str] = Field(
        None,
        description="What light source was used to collect the image."
    )
    lighting_lux: Optional[float] = Field(
        None,
        description="Image Level / Collection Level depending on variance.",
        ge=0,
        le=100000
    )
    setting: Optional[str] = Field(
        None,
        description="Where was the image taken"
    )

    class ConfigDict:
        extra = 'forbid'


class ImageQuality(BaseModel):
    """
    The properties associated with Image Quality
    """
    exposure: Optional[float] = Field(
        None,
        description="The amount the image was exposed.",
        ge=1,
        le=100
    )
    aperture: Optional[str] = Field(
        None,
        description="The Aperture of the camera when the image was taken."
    )
    iso: Optional[float] = Field(
        None,
        description="The ISO value when the image was taken",
        ge=0,
        le=100000
    )
    height: Optional[float] = Field(
        None,
        description="The height of the image.",
        ge=0,
        le=10000
    )
    width: Optional[float] = Field(
        None,
        description="The width of the image",
        ge=0,
        le=10000
    )
    channels: Optional[float] = Field(
        None,
        description="The number of channels in the image.",
        ge=1,
    )
    blur_score: Optional[MLOutput] = Field(
        None
    )
    pct_pixel_over_saturation: Optional[float] = Field(
        None,
        description="The percentage of pixels that were over saturated.",
        ge=0,
        le=100
    )
    pct_pixel_under_saturation: Optional[float] = Field(
        None,
        description="The percentage of pixels that were under saturated.",
        ge=0,
        le=100
    )

    class ConfigDict:
        extra = 'forbid'


class Image(BaseModel):
    """
    All the approved values to be captured about Images of Ag Data.
    """
    path: str = Field(
        ...,
        description="The path to the image"
    )
    id: str = Field(
        ...,
        description="The Unique ID of the image, should be the image name, by default UUID4."
    )
    device: str = Field(
        ...,
        description="The type of device that is collecting the images, mobile, auxillery, or drone."
    )
    camera_properties: Optional[CameraProperties] = Field(
        None
    )
    location_properties: Optional[Location] = Field(
        None
    )
    protocol_properties: Optional[ImageProtocol] = Field(
        None
    )
    acquisition_properties: Optional[AcquisitionProperties] = Field(
        None
    )
    image_quality: Optional[ImageQuality] = Field(
        None
    )
    agronomic_properties: Optional[AgronomicProperties] = Field(
        None
    )

    class ConfigDict:
        extra = 'forbid'
        json_schema_extra = {
            "example": {
                "path": "/images/field_A/row_1/image_001.jpg",
                "id": str(uuid4()),
                "device": "drone",
                "camera_properties": {
                    "model": "DJI Mavic 2 Pro",
                    "make": 1.0,
                    "iso": 100.0,
                    "magnification": 1.0
                },
                "location_properties": {
                    "latitude": 34.0522,
                    "longitude": -118.2437,
                    "elevation_m": 100.5,
                    "crs": "EPSG:4326",
                    "country": "USA",
                    "state": "California",
                    "county": "Los Angeles"
                },
                "protocol_properties": {
                    "name": "Drone Survey v1.0",
                    "sample_type": "corn field",
                    "camera_height_mm": 50000.0,
                    "camera_angle": 0.0,
                    "magnification": 1.0,
                    "lighting_conditions": "clear sky",
                    "notes": "Standard flight path"
                },
                "acquisition_properties": {
                    "date": "2025-09-30",
                    "time": "10:30:00",
                    "camera_height_m": 50.0,
                    "camera_angle_deg": 0.0,
                    "object_resolution": "high",
                    "object_resolution_ml": {
                        "pred": 0.05,
                        "model_version": "v1.0"
                    },
                    "light_source": "sunlight",
                    "lighting_lux": 50000.0,
                    "setting": "outdoor"
                },
                "image_quality": {
                    "exposure": 50.0,
                    "aperture": "f/2.8",
                    "iso": 100.0,
                    "height": 4000.0,
                    "width": 6000.0,
                    "channels": 3,
                    "blur_score": {
                        "pred": 2.5,
                        "model": "blur_detector_v1"
                    },
                    "pct_pixel_over_saturation": 1.2,
                    "pct_pixel_under_saturation": 0.5
                },
                "agronomic_properties": {
                    "crop_type": "corn",
                    "growth_stage": "V6",
                    "soil_color": "dark",
                    "weed_pressure": "low",
                    "irrigation_level": "standard",
                    "tillage_type": "no-till",
                    "fertilizer_level": "standard"
                }
            }
        }
