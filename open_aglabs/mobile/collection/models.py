from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List, Any

class SoP(BaseModel):
    """
    Pydantic model representing a Standard Operating Procedure for Image Capture.
    Mapped from image.ImageProtocol.SoP.*
    """

    """
    ONA Specific Vars
    """
    task:Optional[str] = Field(
        None,
        description="Purpose of Data collection."
    )
    method:Optional[str] = Field(
        None,
        description="Method of Data collection."
    )
    trait:Optional[str] = Field(
        None,
        description="Trait/Traits of Interest for Data collection."
    )
    protocol_cloud:Optional[str] = Field(
        None,
        description="standard protocol name for Data collection."
    )
    protocol_naming:Optional[str] = Field(
        None,
        description="Local Reference protocol name for Data collection."
    )
    protocol_description:Optional[str] = Field(
        None,
        description="A detailed description of how the data needs to be collected."
    )
    protocol_reference_media:Optional[str] = Field(
        None,
        description="A URL of Media(Jpeg/GIFs) depicting, how the data needs to be collected."
    )
    dataType:Optional[str] = Field(
        None,
        description="DataType Enum for Data collection."
    )
    level:Optional[str] = Field(
        None,
        description="Granularity of data collection, Plant/Plot Level."
    )
    protocol_version:Optional[str] = Field(
        None,
        description="Describes the Plant Name and its respective ProtocolVersion."
    )

    model_config = ConfigDict(extra='allow')

class Collection(BaseModel):
    """
    Pydantic model representing Collection-level metadata.
    In Ona App The collection model is referred to as Session.
    A collection is an instance of data collected for a Individual trait or a group of traits that belong to a particular trial.
    """
    collection_id: Optional[str] = Field(None, description="Collection ID. A unique identifier for the collection. To Track all plot and image entities that are part of this collection")
    num_images: Optional[str] = Field(None, description="The number of images captured for a given collection.")
    num_plots: Optional[str] = Field(None, description="Number of plots collected for a given collection.")
    plot_collection:Optional[list]=Field(None, description="List of plotIds collected for a given collection.")

    start_datetime: Optional[str] = Field(None, description="Start date time as unique collection start time.")
    end_datetime: Optional[str] = Field(None, description="End date time as unique collection end time.")

    start_datetime_username: Optional[str] = Field(None, description="Unique collection ID (date-time + username).")
    username: Optional[str] = Field(None, description="Username of data collector.")
    user_details: Optional[dict] = Field(None, description="User details. For Future scope of Expansion")
    environment_details: Optional[dict] = Field(None, description="Environment details")

    # SoP Specific to Protocol Management
    sop: Optional[SoP] = Field(
        None,
        description="Standard Operating Procedure details."
    )

    # update: Optional[str] = Field(None, description="Update status/info.") DEPRECATED

    trial: Optional[str] = Field(None, validation_alias='trial_name', description="The trial name.")
    trial_details: Optional[dict] = Field(None, description="The trial details.")
    trial_source_url: Optional[str] = Field(None, description="The source url of the trial layout.")



    model_config = ConfigDict(extra='forbid')
