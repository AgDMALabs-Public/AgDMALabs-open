from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List, Any, Required


class Collection(BaseModel):
    """
    Pydantic model representing Collection-level metadata.
    Mapped from collection.*x
    """
    endtime: Optional[str] = Field(None, description="End time of collection.")
    collection_id: Required[str] = Field(None, description="Collection ID. A unique identifier for the collection. To Track all entities that are part of this collection")
    num_images: Optional[str] = Field(None, description="The number of images captured for a given form.")
    num_plots: Optional[str] = Field(None, description="Number of plots collected for a given form submission.")
    start_datetime: Optional[str] = Field(None, description="Start date time as unique collection start time.")
    start_datetime_username: Optional[str] = Field(None, description="Unique collection ID (date-time + username).")
    username: Optional[str] = Field(None, description="Username of data collector.")
    update: Optional[str] = Field(None, description="Update status/info.")

    model_config = ConfigDict(extra='forbid')
