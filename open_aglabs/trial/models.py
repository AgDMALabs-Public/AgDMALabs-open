from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List, Any

class Trial(BaseModel):
    """
    Pydantic model representing Trial and Plot layout information.
    Mapped from trial.*
    """
    # Layout properties
    number_of_plants_per_row: Optional[str] = Field(None, description="Plot-level metadata for number of plants planted per row.")
    number_of_rows: Optional[str] = Field(None, description="Plot level metadata on the number of rows planted.")
    number_of_seeds_per_hole: Optional[str] = Field(None, description="Plot level metadata for the number of seeds planted per hole.")
    plot_dimensions_m: Optional[str] = Field(None, description="Plot level metadata for the plot dimensions in m.")
    spacing_between_plants: Optional[str] = Field(None, description="Plot level metadata for the spacing between plants.")
    spacing_between_plots: Optional[str] = Field(None, description="Plot level metadata for the spacing between plots.")
    spacing_between_reps: Optional[str] = Field(None, description="Plot level metadata for the spacing between replications.")
    spacing_between_rows: Optional[str] = Field(None, description="Plot level metadata for the spacing between rows.")

    # Plot properties
    barcode_plotnumber: Optional[str] = Field(None, description="The plot number extracted from barcode.")
    block_name: Optional[str] = Field(None, description="Plot property: the block name.")
    manual_plotnumber: Optional[str] = Field(None, description="The plot number as selected from the data collector.")
    plot_barcode: Optional[str] = Field(None, description="The plot barcode.")
    plot_number: Optional[str] = Field(None, description="Plot number.")
    rownumber_genotype: Optional[str] = Field(None, description="The row number and genotype for the trials that have genotype and spacing diversity.")
    trial: Optional[str] = Field(None, validation_alias='trial_name', description="The trial name.")

    model_config = ConfigDict(extra='forbid')
