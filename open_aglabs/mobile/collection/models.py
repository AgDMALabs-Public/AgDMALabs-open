from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List, Any

from pydantic.v1 import Required

class Collection(BaseModel):
    """
    Pydantic model representing Collection-level metadata.
    In Ona App The collection model is referred to as Session.
    A collection is an instance of data collected for a Individual trait or a group of traits that belong to a particular trial.
    """
    collection_id: Required[str] = Field(None, description="Collection ID. A unique identifier for the collection. To Track all plot and image entities that are part of this collection")
    num_images: Optional[str] = Field(None, description="The number of images captured for a given collection.")
    num_plots: Optional[str] = Field(None, description="Number of plots collected for a given collection.")
    plot_collection:Optional[list]=Field(None, description="List of plotIds collected for a given collection.")

    start_datetime: Optional[str] = Field(None, description="Start date time as unique collection start time.")
    end_datetime: Optional[str] = Field(None, description="End date time as unique collection end time.")

    start_datetime_username: Optional[str] = Field(None, description="Unique collection ID (date-time + username).")
    username: Optional[str] = Field(None, description="Username of data collector.")
    user_details: Optional[dict] = Field(None, description="User details. For Future scope of Expansion")
    environment_details: Optional[dict] = Field(None, description="Environment details")

    # update: Optional[str] = Field(None, description="Update status/info.") DEPRECATED

    trial: Optional[str] = Field(None, validation_alias='trial_name', description="The trial name.")
    trial_details: Optional[dict] = Field(None, description="The trial details.")
    trial_source_url: Optional[str] = Field(None, description="The source url of the trial layout.")


    model_config = ConfigDict(extra='forbid')
