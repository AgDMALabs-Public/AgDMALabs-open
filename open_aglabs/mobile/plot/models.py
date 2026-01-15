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
    model_config = ConfigDict(extra='forbid')

class PlotMetadata(BaseModel):
    """
    Pydantic model representing Trial and Plot layout information.
    The Trial model is a representation of additional metadata for a particular trial layout.
    Plotbook contains the structure of the plot itself. while plotmetadata tracks the evolution of the plant's genotype and user metrics over different growthstages.
    """
    # Plot properties
    plot_id: Optional[str] = Field(None, description="Unique Plot ID under a collection instance.")
    plot_book_entry_ID: Optional[str] = Field(None, description="Unique Plot entry ID from plotbook source.")
    plot_book_ID: Optional[str] = Field(None, description="A unique identifier for the entire plotbook collection.")
    barcode_plotnumber: Optional[str] = Field(None, description="The plot number extracted from barcode.")
    block_name: Optional[str] = Field(None, description="Plot property: the block name.")
    manual_plotnumber: Optional[str] = Field(None, description="The plot number as selected from the data collector.")
    plot_barcode: Optional[str] = Field(None, description="The plot barcode.")
    plot_number: Optional[str] = Field(None, description="Plot number.")
    # Available in plotbook
    # rownumber_genotype: Optional[str] = Field(None, description="The row number and genotype for the trials that have genotype and spacing diversity.")


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
