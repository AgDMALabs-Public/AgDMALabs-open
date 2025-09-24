from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NutrientAnalysis(BaseModel):
    """
    A nested model to contain the specific chemical analysis results of a soil sample.
    Units are generally in parts per million (ppm) unless otherwise specified.
    """
    ph: float = Field(
        ...,
        description="Soil pH value.",
        examples=[6.8]
    )
    organic_matter_percent: float = Field(
        ...,
        alias="organicMatterPercent",
        description="Percentage of organic matter in the soil.",
        examples=[3.5]
    )

    # Macronutrients
    nitrogen_ppm: Optional[float] = Field(
        None,
        alias="nitrogenPpm",
        description="Nitrogen (N) concentration in parts per million."
    )
    phosphorus_ppm: float = Field(
        ...,
        alias="phosphorusPpm",
        description="Phosphorus (P) concentration in parts per million."
    )
    potassium_ppm: float = Field(
        ...,
        alias="potassiumPpm",
        description="Potassium (K) concentration in parts per million."
    )

    zinc_ppm: Optional[float] = Field(
        None,
        alias="zincPpm",
        description="Zinc (Zn) concentration in parts per million."
    )
    iron_ppm: Optional[float] = Field(
        None,
        alias="ironPpm",
        description="Iron (Fe) concentration in parts per million."
    )
    manganese_ppm: Optional[float] = Field(
        None,
        alias="manganesePpm",
        description="Manganese (Mn) concentration in parts per million."
    )
    copper_ppm: Optional[float] = Field(
        None,
        alias="copperPpm",
        description="Copper (Cu) concentration in parts per million."
    )
    boron_ppm: Optional[float] = Field(
        None,
        alias="boronPpm",
        description="Boron (B) concentration in parts per million."
    )

    cation_exchange_capacity: Optional[float] = Field(
        None,
        alias="cationExchangeCapacity",
        description="Cation Exchange Capacity (CEC) in meq/100g."
    )


class SoilSample(BaseModel):
    """
    Represents a single soil sample, including its location, depth, and lab analysis results.
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
    latitude: float = Field(
        ...,
        ge=-90,
        le=90,
        description="Latitude of the sample location in WGS 84 coordinates."
    )
    longitude: float = Field(
        ...,
        ge=-180,
        le=180,
        description="Longitude of the sample location in WGS 84 coordinates."
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
    start_depth_cm: float = Field(
        ...,
        alias="startDepthCm",
        ge=0,
        description="Starting depth of the soil sample in centimeters."
    )
    end_depth_cm: float = Field(
        ...,
        alias="endDepthCm",
        gt=0,
        description="Ending depth of the soil sample in centimeters."
    )
    extraction_type: Optional[str] = Field(
        ...,
        alias="extractionType",
        description="The extraction method used to in the test."
    )
    analysis_results: NutrientAnalysis = Field(
        ...,
        alias="analysisResults",
        description="The results of the nutrient analysis for the sample."
    )

    class Config:
        # Allows you to create a model instance using either the field name or its alias
        # e.g., SoilSample(sampleId="id1") or SoilSample(sample_id="id1")
        allow_population_by_field_name = True

        # Generates an example in the OpenAPI schema for documentation
        schema_extra = {
            "example": {
                "sampleId": "SS-2025-FZ-001",
                "timestamp": "2025-08-21T10:30:00Z",
                "latitude": 40.7128,
                "longitude": -74.0060,
                "labId": "AgriLab-1",
                "startDepthCm": 0,
                "endDepthCm": 15,
                "analysisResults": {
                    "ph": 6.5,
                    "organicMatterPercent": 3.2,
                    "nitrogenPpm": 25.0,
                    "phosphorusPpm": 55.0,
                    "potassiumPpm": 150.0,
                    "zincPpm": 2.1,
                }
            }
        }