from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Union, Literal
from open_aglabs.core.constants import CROP_LIST, SOIL_COLOR, IMAGE_TYPE_LIST, ORIENTATION_LIST


class Other(BaseModel):
    model_config = ConfigDict(
        extra='allow'
    )


class Notes(BaseModel):
    message: str = Field(
        ...,
        description="The message to be stored in the notes field"
    )
    author: str = Field(
        ...,
        description="The author of the message"
    )
    model_config = ConfigDict(
        extra='allow'
    )


class MLOutput(BaseModel):
    pred: Optional[Union[str, float, int]] = Field(
        None,
        description="The predicted value"
    )
    confidence: Optional[float] = Field(
        None,
        description="The confidence score of the prediction."
    )
    model_id: Optional[Union[str, float]] = Field(
        None,
        description="The ID of the model used to make the prediction"
    )
    model_version: Optional[Union[str, float, int]] = Field(
        None,
        description="The version of the model used to make the prediction"
    )
    model_config = ConfigDict(
        extra='forbid'
    )


class ImageTransformations(BaseModel):
    """
    All the approved values to be captured about Images of Ag Data.
    """
    parent_img_id: Optional[str] = Field(
        None,
        description="The UUID of the original Image"
    )
    resize: Optional[str] = Field(
        None,
        description="The details bout how the image was resized."
    )
    cropped: Optional[float] = Field(
        None,
        description="The height of the camera in meters",
        ge=0
    )

    model_config = ConfigDict(
        extra='forbid'
    )


class Location(BaseModel):
    """
    Values to support the proper documentation of location information
    """
    id: Optional[str] = Field(
        None,
        description="The UUID of the location"
    )
    name: Optional[str] = Field(
        None,
        description="The name of the location"
    )
    latitude: Optional[float] = Field(
        None,
        ge=-90.0,
        le=90.0,
        description="The latitude of where the data was taken"
    )
    longitude: Optional[float] = Field(
        None,
        ge=-180.0,
        le=180.0,
        description="The longitude of where the data was taken"
    )
    elevation_m: Optional[float] = Field(
        None,
        ge=-100,
        le=10000,
        description="The elevation of where the data came from"
    )
    crs: Optional[str] = Field(
        None,
        description="The crs of the GPS data"
    )
    geometry: Optional[str] = Field(
        None,
        description="The Geometry in WKT format"
    )
    admin_level_0: Optional[str] = Field(
        None,
        description="This level is for Country / Nation."
    )
    admin_level_1: Optional[str] = Field(
        None,
        description="This is for things like state or the primary subdivision of a country / Nation."
    )
    admin_level_2: Optional[str] = Field(
        None,
        description="This is for things like county or the primary subdivision of a state."
    )
    admin_level_3: Optional[str] = Field(
        None,
        description="This is for things like city/town/village or the primary subdivision of a county."
    )
    site: Optional[str] = Field(
        None,
        description="The site refers to the research site the data came from. A site will have many fields and locations"
                    " associated to it, its similar to farm but used in a research context"
    )
    grower: Optional[str] = Field(
        None,
        description="The grower the managed the field. A grower will have many fields and locations associated to it"
    )
    farm: Optional[str] = Field(
        None,
        description="The Farm the data came from. A farm will have many fields and locations associated to it,'"
                    " its similar to site but used in the commerical context."
    )
    field: Optional[str] = Field(
        None,
        description="What is the field ID that the data came from"
    )
    location: Optional[str] = Field(
        None,
        description="the location (by BrApi Def) of there the data came from"
    )
    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "id": "loc-uuid-12345",
                "name": "Research Plot A",
                "latitude": 34.0522,
                "longitude": -118.2437,
                "elevation_m": 150.5,
                "crs": "EPSG:4326",
                "geometry": "POINT (-118.2437 34.0522)",
                "admin_level_0": "USA",
                "admin_level_1": "California",
                "admin_level_2": "Los Angeles County",
                "admin_level_3": "Los Angeles",
                "site": "AgTech Research Farm",
                "grower": "williams",
                "farm": "california",
                "field": "Field_7B",
                "location": "A"
            }
        }
    )


class TrialProperties(BaseModel):
    """
    Values to support the proper documentation of location information
    """
    id: Optional[str] = Field(
        None,
        description="A unique ID for the trial"
    )
    name: Optional[str] = Field(
        None,
        description="The name of the location"
    )
    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "id": "trial-uuid-12345",
                "name": "breeding_a"
            }
        }
    )


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
    model_config = ConfigDict(
        extra='forbid'
    )


class ProtocolProperties(BaseModel):
    """
    Pydantic model to store data about an image of agricultural materials.
    """
    name: Optional[str] = Field(
        None,
        description="The Name of the protocol used to capture the image.")
    id: Optional[str] = Field(
        None,
        description="What is being imaged (e.g., 'corn field', 'soil', 'tomato fruit').")
    url: Optional[str] = Field(
        None,
        description="The path to the protocol documentation.")
    model_config = ConfigDict(
        extra='forbid'
    )
