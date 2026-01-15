from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List, Any


class PlotEntry(BaseModel):
    """
    Represents a single entry in a PlotBook.
    Each entry includes a reference_id for cross-referencing.
    """
    # Unique Reference ID for cross-referencing in other systems
    reference_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="A unique ID used to refer to this specific entry in other datasets."
    )

    # Mandatory Fields
    study_name: str = Field(
        ...,
        validation_alias=AliasChoices("studyName", "study_name"),
        description="The name of the trial or study."
    )
    observation_unit_name: str = Field(
        ...,
        validation_alias=AliasChoices("observationUnitName", "observation_unit_name"),
        description="The unique identifier for the specific unit being observed."
    )
    plot_number: int = Field(
        ...,
        validation_alias=AliasChoices("plotNumber", "plot_number"),
        description="The numerical identifier for the plot."
    )

    # Row can also be called 'range'
    row: int = Field(
        ...,
        validation_alias=AliasChoices("row", "range"),
        description="The row or range coordinate in the field layout."
    )
    column: int = Field(
        ...,
        validation_alias=AliasChoices("column"),
        description="The column coordinate in the field layout."
    )

    # Optional Fields
    block_number: Optional[int] = Field(
        None,
        validation_alias=AliasChoices("blockNumber", "block_number"),
        description="The block number if the field is divided into blocks."
    )
    germplasm_name: Optional[str] = Field(
        None,
        validation_alias=AliasChoices("germplasmName", "germplasm_name"),
        description="The name of the germplasm or seed variety."
    )
    entry_type: Optional[str] = Field(
        None,
        validation_alias=AliasChoices("entryType", "entry_type"),
        description="Classification of the entry (e.g., Filler, Check, Test)."
    )
    replicate: Optional[int] = Field(
        None,
        validation_alias=AliasChoices("replicate"),
        description="The replicate number for the plot."
    )

    extended_metadata: Optional[PlotMetadata] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra='ignore'
    )


class PlotBook(BaseModel):
    """
    The main PlotBook class containing a unique ID and a list of entries.
    Holds the overall structure of the plots before start of trial.
    Any and all changes done to the plot itself can be tracked as part of the plotbook which remains as the SoT during the duration of that trial.
    """
    plotbook_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="A unique identifier for this entire plotbook collection."
    )
    entries: List[PlotEntry] = Field(
        default_factory=list,
        description="List of all plot entries in this plotbook."
    )
    land_varieties: Optional[str] = Field(
        None,
        description="The land variety that was imaged."
    )

    model_config = ConfigDict(populate_by_name=True)