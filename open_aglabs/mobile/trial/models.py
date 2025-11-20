from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import Optional, Literal, List, Any

class Trial(BaseModel):
    """
    Pydantic model representing Trial and Plot layout information.
    The Trial model is a representation of additional metadata for a particular trial layout.
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

    trial: Optional[str] = Field(None, validation_alias='trial_name', description="The trial name.")
    trial_details: Optional[dict] = Field(None, description="The trial details.")
    trial_source_url: Optional[str] = Field(None, description="The source url of the trial layout.")

    model_config = ConfigDict(extra='forbid')
