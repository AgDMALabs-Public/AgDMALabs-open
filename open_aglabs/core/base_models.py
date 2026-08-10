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


class OntologyTerm(BaseModel):
    """
    A reference to a term in an external ontology or controlled vocabulary.
    """
    common_name: Optional[str] = Field(
        None,
        description="The common name of the term."
    )
    ontology_source: Optional[str] = Field(
        None,
        description="The ontology the term belongs to, ideally a resolvable URL. "
                    "EX: https://cropontology.org"
    )
    ontology_name: Optional[str] = Field(
        None,
        description="The scientific or canonical name of the term within the ontology."
    )
    ontology_id: Optional[str] = Field(
        None,
        description="The identifier of the term within the ontology. EX: CO_335:0000123"
    )
    model_config = ConfigDict(
        extra='forbid',
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "common_name": "drought tolerance",
                "ontology_source": "https://cropontology.org",
                "ontology_name": "drought tolerance",
                "ontology_id": "CO_335:0000123"
            }
        }
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
    plot_id: Optional[str] = Field(
        None,
        description="The plot ID to match back to the plot map"
    )
    plotbook_id: Optional[str] = Field(
        None,
        description="The plotbook ID to match back to the plot map"
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
    url: Optional[str] = Field(
        None,
        description="The path to the protocol documentation."
    )
    details: Optional[str] = Field(
        None,
        description="The path to the protocol documentation."
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
    planting_date: Optional[str] = Field(
        None,
        description="The date the crop was planted, or is intended to be planted."
    )
    season_code: Optional[str] = Field(
        None,
        description="The season code for the crop in YYYY:Country:Crop:time_of_year, where time of year can be spring, summer ... or the month."
    )
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


class CollectionProperties(BaseModel):
    """
    Pydantic model representing Collection-level metadata.
    In Ona App The collection model is referred to as Session.
    A collection is an instance of data collected for a Individual trait or a group of traits that belong to a particular trial.
    """
    id: Optional[str] = Field(
        None,
        description="Collection ID. A unique identifier for the collection. To Track all plot and image entities that are part of this collection")
    num_images: Optional[str] = Field(
        None,
        description="The number of images captured for a given collection.")
    num_plots: Optional[str] = Field(
        None,
        description="Number of plots collected for a given collection.")
    start_datetime: Optional[str] = Field(
        None,
        description="Start date time as unique collection start time.")
    end_datetime: Optional[str] = Field(
        None,
        description="End date time as unique collection end time.")
    username: Optional[str] = Field(
        None,
        description="Username of data collector.")
    user_details: Optional[dict] = Field(
        None,
        description="User details. For Future scope of Expansion")
    runtime_environment: Optional[dict] = Field(
        None,
        description="The software enviroment that was used to capture the data. EX: Sandbox of Prod")
    model_config = ConfigDict(
        extra='forbid')
