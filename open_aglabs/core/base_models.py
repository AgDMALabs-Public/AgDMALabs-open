from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Union


class MLOutput(BaseModel):
    pred: Optional[Union[str, float]] = Field(
        None,
        description="The predicted value"
    )
    model_id: Optional[str] = Field(
        None,
        description="The ID of the model used to make the prediction"
    )
    model_version: Optional[str] = Field(
        None,
        description="The version of the model used to make the prediction"
    )
    model_config =  ConfigDict(
        extra = 'forbid')


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

    class ConfigDict:
        extra = 'forbid'


class Location(BaseModel):
    """
    Values to support the proper documentation of location information
    """
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
    country: Optional[str] = Field(
        None,
        description="The country that the data came from."
    )
    state: Optional[str] = Field(
        None,
        description="What state did the data come from"
    )
    county: Optional[str] = Field(
        None,
        description="What County did the data come from"
    )
    district: Optional[str] = Field(
        None,
        description="What District did the data come from"
    )
    village: Optional[str] = Field(
        None,
        description="What Village did the data come from"
    )
    site: Optional[str] = Field(
        None,
        description="What is the site the data came from"
    )
    field: Optional[str] = Field(
        None,
        description="What is the site the data came from"
    )
    location: Optional[str] = Field(
        None,
        description="the location (by BrApi Def) of there the data came from"
    )

    class ConfigDict:
        extra = 'forbid'
