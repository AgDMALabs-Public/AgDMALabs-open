from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List
from uuid import uuid4

from ..core.base_models import MLOutput, Location, Notes
from ..core.constants import CROP_LIST, SOIL_COLOR, IMAGE_TYPE_LIST, ORIENTATION_LIST
from open_aglabs.mobile.trial.models import Trial
from open_aglabs.mobile.collection.models import Collection
from ..mobile.plot.models import PlotMetadata


class ImageProtocol(BaseModel):
    """
    Pydantic model to store data about an image of agricultural materials.
    Also Stores The protocol used for Imaging.
    """
    name: str = Field(...,
                      description="The Name of the protocol used to capture the image.")
    sample_type: str = Field(...,
                             description="What is being imaged (e.g., 'corn field', 'soil', 'tomato fruit').")
    camera_height_mm: float = Field(...,
                                    gt=0,
                                    description="Height of the camera from the sample in millimeters.")
    camera_angle: float = Field(...,
                                ge=0,
                                description="The angle that the camera is at relative to vertical. eg: top down is 0")
    magnification: float = Field(...,
                                 gt=0,
                                 description="Magnification level used for the image capture.")
    lighting_conditions: Optional[str] = Field(None,
                                               description="Description of the lighting conditions (e.g., 'natural sunlight', 'LED array', 'dark field').")
    notes: Optional[str] = Field(None,
                                 description="Any additional relevant notes or observations.")


class PlantHealth(BaseModel):
    """
    Pydantic model representing plant health stressors and diseases.
    Mapped from image.agronomic_properties.planthealth.*
    """
    other_disease: Optional[str] = Field(
        None,
        description="Presence of disease on imaged plant for disease outside of drop down list."
    )
    ranked_stressors: Optional[str] = Field(
        None,
        description="Ranking the diseases and other stressors present in the imaged plant."
    )
    stressors: Optional[str] = Field(
        None,
        description="Presence of stressor on imaged plant from drop down list."
    )

    model_config = ConfigDict(extra='forbid')


class AgronomicProperties(BaseModel):
    """
    Pydantic model representing approved values to be captured about images of agricultural data.
    """
    crop_type: Optional[Literal[*CROP_LIST]] = Field(
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
        description="The level of weed presence in the image. high would be complete coverage, low would be less than 10% coverage."
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
    plant_health: Optional[PlantHealth] = Field(
        None,
        description="Details regarding plant health, diseases, and stressors."
    )

    model_config = ConfigDict(
        extra='forbid'
    )


class CameraProperties(BaseModel):
    """
    Values to support the proper documentation of camera, if you add information to this json please update this doc. https://docs.google.com/spreadsheets/d/1zljGA5xtwtLNXqjohfXeJzh6SFwdObAjmb5gHflQfIA/edit?gid=1769639569#gid=1769639569
    Adding Specifications related to mobile device
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
    device_id: Optional[str] = Field(
        None,
        validation_alias=AliasChoices('deviceID', 'device_id'),
        description="Unique persistent CPU ID or collection ID."
    )
    model_specification: Optional[str] = Field(
        None,
        description="Phone model question/specification string (e.g., Manufacturer=samsung, Model=SM-A556E). IF Device is Mobile"
    )

    model_config = ConfigDict(
        extra='allow'   # ADDED TO ENSURE CC from android https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics can be added.
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
        ge=0,
        description="The angle of the camera when the photo was taken"

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
        ge=0,
        le=100000,
        description="The amount of Lux being generated by a sutnetic light source or measured by a lux meter."

    )
    setting: Optional[str] = Field(
        None,
        description="Where was the image taken"
    )

    model_config = ConfigDict(
        extra='allow' # changed to add CaptureResult spec of Android https://developer.android.com/reference/android/hardware/camera2/CaptureResult.
    )


class ImageQuality(BaseModel):
    """
    The properties associated with Image Quality
    """
    exposure: Optional[float] = Field(
        None,
        description="The exposure of the image.",
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
        description="The height of the image in pixels.",
        ge=0,
        le=30000
    )
    width: Optional[float] = Field(
        None,
        description="The width of the image in pixels",
        ge=0,
        le=30000
    )
    est_gsd_mm: Optional[float] = Field(
        None,
        description="The estimated ground sample distance of the image in mm.",
        gt=0
    )
    orientation: Optional[Literal[*ORIENTATION_LIST]] = Field(
        None,
        description="The orientation of the image.",
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

    model_config = ConfigDict(
        extra='forbid'
    )

class SyntheticImageProperties(BaseModel):
    """
    Values associated with Synthetic Images
    """
    model: Optional[str] = Field(
        None,
        description="The model of the synthetic image."
    )
    seed: Optional[int] = Field(
        None,
        description="The seed used to generate the synthetic image."
    )
    noise: Optional[float] = Field(
        None,
    )
    model_config = ConfigDict(
        extra='allow'
    )

class Image(BaseModel):
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
    protocol_name: Optional[str] = Field(
        None,
        description="The name of the protocol used to capture the image."
    )
    protocol_version: Optional[str] = Field(
        None,
        description="The version of the protocol used to capture the image."
    )
    protocol_url: Optional[str] = Field(
        None,
        description="The URL of the protocol used to capture the image."
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
    image_quality: Optional[ImageQuality] = Field(
        None
    )
    agronomic_properties: Optional[AgronomicProperties] = Field(
        None
    )
    trial_properties: Optional[Trial] = Field(
        None,
        description="Trial and plot layout information."
    )
    collection_properties: Optional[Collection] = Field(
        None,
        description="Collection level information, will only contain CollectionID"
    )
    plot_properties:Optional[PlotMetadata] = Field(
        None,
        description="Plot level information, will only contain PlotID and other required fields"
    )
    synthetic_image_properties: Optional[SyntheticImageProperties] = Field(
        None
    )

    notes: Optional[List[Notes]] = Field(
        None
    )

    model_config = ConfigDict(
        extra='allow',
        json_schema_extra={
            "example": {
                "path": "/images/field_A/row_1/image_001.jpg",
                "id": str(uuid4()),
                "device": "drone",
                "type": "original",
                "camera_properties": {
                    "model": "DJI Mavic 2 Pro",
                    "make": 1.0,
                    "iso": 100.0,
                    "magnification": 1.0,
                    "device_id": "b2f20fd1b69e6f61",
                    "model_specification": "Samsung SM-A556E"
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
                    "notes": "Standard flight path",
                    "sop": {
                         "hardware_name": "Pixel 6",
                         "sop_name": "Standard Capture v2"
                    }
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
                    "fertilizer_level": "standard",
                    "plant_health": {
                        "stressors": "drought",
                        "ranked_stressors": "1. drought, 2. pests"
                    }
                },
                "synthetic_image_properties": {
                    "model": 'v1',
                    "seed": 12345,
                    "noise": 0.01,
                },
                "trial_properties": {
                    "trial_name": "Trial-2025-A",
                    "plot_number": "101"
                }
            }
        }
    )
