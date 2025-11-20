from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List, Any

from pydantic.v1 import Required

class SoP(BaseModel):
    """
    Pydantic model representing a Standard Operating Procedure for Image Capture.
    Mapped from image.ImageProtocol.SoP.*
    """
    hardware_name: Optional[str] = Field(
        None,
        description="The hardware used for image collection."
    )
    hardware_version: Optional[str] = Field(
        None,
        description="Hardware version for the given hardware used."
    )
    sop_name: Optional[str] = Field(
        None,
        description="SOP name as defined for image capture SOPs."
    )
    phone_orientation: Optional[str] = Field(
        None,
        description="Phone orientation used to capture the image."
    )
    # DEPRECATED AS ITS COVERED IN ONA SPECIFIC VARS
    # image_collection_method: Optional[str] = Field(
    #     None,
    #     description="Image collection method."
    # )
    # target_trait: Optional[str] = Field(
    #     None,
    #     description="The trait targeted in the image."
    # )


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
    plot_id: Required[str] = Field(None, description="Unique Plot ID under a collection.")
    barcode_plotnumber: Optional[str] = Field(None, description="The plot number extracted from barcode.")
    block_name: Optional[str] = Field(None, description="Plot property: the block name.")
    manual_plotnumber: Optional[str] = Field(None, description="The plot number as selected from the data collector.")
    plot_barcode: Optional[str] = Field(None, description="The plot barcode.")
    plot_number: Optional[str] = Field(None, description="Plot number.")
    rownumber_genotype: Optional[str] = Field(None, description="The row number and genotype for the trials that have genotype and spacing diversity.")

    trial: Required[str] = Field(None, validation_alias='trial_name', description="The trial name.")
    trial_details: Required[dict] = Field(None, description="The trial details.")
    trial_source_url: Required[str] = Field(None, description="The source url of the trial layout.")

    collection_id:  Required[str] = Field(None, description="Collection ID. A unique identifier for the collection. To Track all entities that are part of this collection")

    plot_start_datetime: Optional[str] = Field(None, description="Start date time as unique collection start time.")
    plot_end_datetime: Optional[str] = Field(None, description="End date time as unique collection end time.")

    durationOfCollection:Optional[int] = Field(None, description="Duration of collection.")
    unitOfDuration:Optional[str] = Field(None, description="unit of collection.")

    sop: Optional[SoP] = Field(
        None,
        description="Standard Operating Procedure details."
    )

    genotype_properties: Optional[Genotype] = Field(
        None,
        description="GenoType details."
    )

    model_config = ConfigDict(extra='forbid')
