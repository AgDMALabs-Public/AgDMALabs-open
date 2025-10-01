from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ..core.base_models import Location

class TissueAnalysis(BaseModel):
    """
    A nested model to contain the specific chemical analysis results of a soil sample.
    Units are generally in parts per million (ppm) unless otherwise specified.
    """
    # Macronutrients
    nitrogen_pct: Optional[float] = Field(
        None,
        alias="nitrogenPct",
        ge=0,
        le=10,
        description="Nitrogen (N) in the sample, expressed as a percentage of the total sample mass."
    )
    phosphorus_pct: Optional[float] = Field(
        None,
        alias="phosphorusPct",
        ge=0,
        le=10,
        description="Phosphorus (P) in the sample, expressed as a percentage of the total sample mass."
    )
    potassium_pct: Optional[float] = Field(
        None,
        alias="potassiumPct",
        ge=0,
        le=10,
        description="Potassium (K) concentration in percentages of the total sample mass."
    )
    sulfur_pct: Optional[float] = Field(
        None,
        alias="sulfurPct",
        ge=0,
        le=10,
        description="Sulfur (S) concentration in percentages of the total sample mass."
    )
    calcium_pct: Optional[float] = Field(
        None,
        alias="calciumPct",
        ge=0,
        le=10,
        description="Calcium (Ca) concentration in percentages of the total sample mass."
    )

    magnesium_pct: Optional[float] = Field(
        None,
        alias="magnesiumPct",
        ge=0,
        le=10,
        description="Magnesium (Mg) concentration in parts per million."
    )
    zinc_ppm: Optional[float] = Field(
        None,
        alias="zincPpm",
        ge=0,
        le=100000,
        description="Zinc (Zn) concentration in parts per million."
    )
    iron_ppm: Optional[float] = Field(
        None,
        alias="ironPpm",
        ge=0,
        le=100000,
        description="Iron (Fe) concentration in parts per million."
    )
    manganese_ppm: Optional[float] = Field(
        None,
        alias="manganesePpm",
        ge=0,
        le=100000,
        description="Manganese (Mn) concentration in parts per million."
    )
    copper_ppm: Optional[float] = Field(
        None,
        alias="copperPpm",
        ge=0,
        le=100000,
        description="Copper (Cu) concentration in parts per million."
    )
    boron_ppm: Optional[float] = Field(
        None,
        alias="boronPpm",
        ge=0,
        le=100000,
        description="Boron (B) concentration in parts per million."
    )
    molybdenum_ppm: Optional[float] = Field(
        None,
        alias="molybdenumPpm",
        ge=0,
        le=100000,
        description="Molybdenum (Mo) concentration in parts per million."
    )
    protein_pct: Optional[float] = Field(
        None,
        alias="proteinPct",
        ge=0,
        le=100,
        description="The protein in the sample."
    )
    starch_pct: Optional[float] = Field(
        None,
        alias="starchPct",
        ge=0,
        le=100,
        description="The starch in the sample."
    )
    oil_pct: Optional[float] = Field(
        None,
        alias="oilPct",
        ge=0,
        le=100,
        description="The oil in the sample."
    )
    fiber_pct: Optional[float] = Field(
        None,
        alias="fiberPct",
        ge=0,
        le=100,
        description="The fiber in the sample."
    )
    adf_pct: Optional[float] = Field(
        None,
        alias="adfPct",
        ge=0,
        le=100,
        description="The perecnt of acid detergent fiber in the sample."
    )
    ndf_pct: Optional[float] = Field(
        None,
        alias="ndfPct",
        ge=0,
        le=100,
        description="The perecnt of acid detergent fiber in the sample."
    )


class TissueSample(BaseModel):
    """
    Represents a single tissue sample, including its location, depth, and lab analysis results.
    """
    sample_id: str = Field(
        ...,
        alias="sampleId",
        description="Unique identifier for the soil sample.",
        examples=["SS-2025-FIELD-A-001"]
    )
    sample_location_id: str = Field(
        ...,
        alias="sampleLocationId",
        description="Unique identifier for the sample location. This can be used to identify samples from the same location.",
        examples=["SS-2025-FIELD-A-001"]
    )
    timestamp: datetime = Field(
        ...,
        description="The date and time the sample was collected."
    )
    lab_id: Optional[str] = Field(
        None,
        alias="labId",
        description="Identifier for the lab that conducted the analysis."
    )
    sample_radius_m: float = Field(
        ...,
        alias="sampleRadiusM",
        ge=0,
        description="The radius around the point that the sample was taken.."
    )
    growth_stage: str = Field(
        ...,
        alias="growthStage",
        description="The growth stage that the sample was collected."
    )
    plant_fraction: str = Field(
        ...,
        alias="plantFraction",
        description="The plant fraction that was collected."
    )
    number_of_plants_sampled: int = Field(
        ...,
        alias="plantSamples",
        description="The number of plants that were sampled from."
    )
    location: Location = Field(
        ...
    )
    analysis_results: TissueAnalysis = Field(
        ...,
        alias="analysisResults",
        description="The results of the nutrient analysis for the sample."
    )
    notes: Optional[list[str]] = Field(
        None,
        alias="notes",
        description="Notes associated with eh sample."
    )

    class ConfigDict:
        extra = "forbid"
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "sampleId": "TS-2025-FZ-001",
                "sampleLocationId": "TS-2025-FIELD-A-LOC-001",
                "timestamp": "2025-08-21T10:30:00Z",
                "latitude": 34.0522,
                "longitude": -118.2437,
                "labId": "TissueLab-A",
                "sampleRadiusM": 0.2,
                "growthStage": "Flowering",
                "plantFraction": "Leaf",
                "analysisResults": {
                    "nitrogenPct": 3.8,
                    "phosphorusPct": 0.5,
                    "potassiumPpm": 28000.0,
                    "sulfurPct": 0.25,
                    "calciumPct": 0.7,
                    "magnesiumPct": 0.3,
                    "zincPpm": 80.0,
                    "ironPpm": 80.0,
                    "manganesePpm": 160.0,
                    "copperPpm": 22.0,
                    "boronPpm": 16.0,
                    "molybdenumPpm": 0.6,
                    "proteinPct": 20.0,
                    "starchPct": 58.0,
                    "adfPct": 26.0,
                },
                "notes": ['thjs is a test', 'this is a test too']
            }
        }
