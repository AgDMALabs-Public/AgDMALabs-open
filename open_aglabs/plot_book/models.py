import uuid
from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List, Any
from open_aglabs.core.base_models import Location, TrialProperties


class PlotEntry(BaseModel):
    """
    Represents a single entry in a PlotBook.
    Each entry includes a reference_id for cross-referencing.
    """
    # Unique Reference ID for cross-referencing in other systems
    plot_id: str = Field(
        description="A unique ID used to refer to this specific entry in other datasets. Will map to plot ID."
    )
    plot_barcode: Optional[str] = Field(
        None,
        description="The plot barcode.")
    plot_name: Optional[str] = Field(
        None,
        description="Human readable unique name for the plot.")
    observation_unit_name: Optional[str] = Field(
        ...,
        validation_alias=AliasChoices("observationUnitName", "observation_unit_name"),
        description="The unique identifier for the specific unit being observed."
    )
    plot_number: Optional[int] = Field(
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
    replicate: int = Field(
        None,
        validation_alias=AliasChoices("replicate"),
        description="The replicate number for the plot."
    )
    number_of_plants_per_row: Optional[str] = Field(
        None,
        description="Plot-level metadata for number of plants planted per row."
    )
    number_of_rows: Optional[str] = Field(
        None,
        description="Plot level metadata on the number of rows planted."
    )
    seeds_per_hole: Optional[str] = Field(
        None,
        description="Plot level metadata for the number of seeds planted per hole."
    )
    width_m: Optional[float] = Field(
        None,
        description="Plot level metadata for the plot width in m."
    )
    length_m: Optional[float] = Field(
        None,
        description="Plot level metadata for the plot length in m."
    )
    spacing_between_plants_m: Optional[float] = Field(
        None,
        description="Plot level metadata for the spacing between plants."
    )
    spacing_between_plots_m: Optional[float] = Field(
        None,
        description="Plot level metadata for the spacing between plots."
    )
    spacing_between_reps_m: Optional[float] = Field(
        None,
        description="Plot level metadata for the spacing between replications."
    )
    spacing_between_rows_m: Optional[float] = Field(
        None,
        description="Plot level metadata for the spacing between rows."
    )

    model_config = ConfigDict(
        populate_by_name=True,
        extra='forbid'
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
    location_properties: Optional[Location] = Field(
        None,
        description=''
    )
    trial_properties: Optional[TrialProperties] = Field(
        None,
        description=''
    )

    model_config = ConfigDict(
        populate_by_name=True,
        extra='forbid',
        json_schema_extra={
            "example": {
                "plotbook_id": "plotbook-uuid-12345",
                "location_properties": {
                    "id": "loc-uuid-12345",
                    "name": "Research Plot A",
                    "latitude": 34.0522,
                    "longitude": -118.2437,
                    "elevation_m": 150.5,
                    "crs": "EPSG:4326",
                    "geometry": "POINT (-118.2437 34.0522)",
                    "admin_level_0": "USA",
                    "admin_level_1": "California",
                    "site": "AgTech Research Farm",
                    "field": "Field_7B",
                    "location": "A"
                },
                "trial_properties": {
                    "id": "trial-2025-A",
                    "name": "Drought Resistance 2025",
                    "url": "https://aglabs.open/protocols/drought_v1",
                    "details": "Testing new hybrids for water stress tolerance."
                },
                "entries": [
                    {
                        "plot_id": "plot-uuid-001",
                        "plot_barcode": "BC-1001",
                        "plot_name": "Plot 101 (Test)",
                        "observation_unit_name": "Unit-101",
                        "plot_number": 101,
                        "row": 1,
                        "column": 1,
                        "block_number": 1,
                        "germplasm_name": "Hybrid-A",
                        "entry_type": "Test",
                        "replicate": 1,
                        "number_of_plants_per_row": "20",
                        "number_of_rows": "2",
                        "seeds_per_hole": "1",
                        "width_m": 1.5,
                        "length_m": 5.0,
                        "spacing_between_plants_m": 0.15,
                        "spacing_between_rows_m": 0.75,
                        "spacing_between_plots_m": 0.5,
                        "spacing_between_reps_m": 2.0
                    },
                    {
                        "plot_id": "plot-uuid-002",
                        "plot_barcode": "BC-1002",
                        "plot_name": "Plot 102 (Check)",
                        "observation_unit_name": "Unit-102",
                        "plot_number": 102,
                        "row": 1,
                        "column": 2,
                        "block_number": 1,
                        "germplasm_name": "Standard-Check",
                        "entry_type": "Check",
                        "replicate": 1,
                        "number_of_plants_per_row": "20",
                        "number_of_rows": "2",
                        "width_m": 1.5,
                        "length_m": 5.0
                    }
                ]
            }
        })

