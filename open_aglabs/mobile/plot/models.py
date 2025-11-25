from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List, Any


class Genotype(BaseModel):
    """
    Pydantic model representing Genotype information.
    """
    development_stage: Optional[str] = Field(
        None,
        description="The development stage of the plant when imaged."
    )
    genotype: Optional[str] = Field(
        None,
        description="The genotype that was imaged."
    )
    growth_stage: Optional[str] = Field(
        None,
        description="The growth stage of the plant when imaged."
    )
    land_varieties: Optional[str] = Field(
        None,
        description="The land variety that was imaged."
    )
    model_config = ConfigDict(extra='forbid')

class PlotMetadata(BaseModel):
    """
    Pydantic model representing Trial and Plot layout information.
    The Trial model is a representation of additional metadata for a particular trial layout.
    """
    # Plot properties
    plot_id: Optional[str] = Field(None, description="Unique Plot ID under a collection.")
    barcode_plotnumber: Optional[str] = Field(None, description="The plot number extracted from barcode.")
    block_name: Optional[str] = Field(None, description="Plot property: the block name.")
    manual_plotnumber: Optional[str] = Field(None, description="The plot number as selected from the data collector.")
    plot_barcode: Optional[str] = Field(None, description="The plot barcode.")
    plot_number: Optional[str] = Field(None, description="Plot number.")
    rownumber_genotype: Optional[str] = Field(None, description="The row number and genotype for the trials that have genotype and spacing diversity.")

    trial: Optional[str] = Field(None, validation_alias='trial_name', description="The trial name.")
    trial_details: Optional[dict] = Field(None, description="The trial details.")
    trial_source_url: Optional[str] = Field(None, description="The source url of the trial layout.")

    collection_id:  Optional[str] = Field(None, description="Collection ID. A unique identifier for the collection. To Track all entities that are part of this collection")

    plot_start_datetime: Optional[str] = Field(None, description="Start date time as unique collection start time.")
    plot_end_datetime: Optional[str] = Field(None, description="End date time as unique collection end time.")

    durationOfCollection:Optional[int] = Field(None, description="Duration of collection.")
    unitOfDuration:Optional[str] = Field(None, description="unit of collection.")

    genotype_properties: Optional[Genotype] = Field(
        None,
        description="GenoType details."
    )

    model_config = ConfigDict(extra='forbid')
