from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, Field, ConfigDict
from open_aglabs.core.base_models import Location


class SoilAnalysis(BaseModel):
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
    sulfur_ppm: float = Field(
        ...,
        alias="potassiumPpm",
        description="Potassium (K) concentration in parts per million."
    )
    calcium_ppm: float = Field(
        ...,
        alias="calciumPpm",
        description="Calcium (Ca) concentration in parts per million."
    )
    magnesium_ppm: Optional[float] = Field(
        None,
        alias="magnesiumPct",
        ge=0,
        description="Magnesium (Mg) concentration in parts per million."
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
        ge=0,
        description="Boron (B) concentration in parts per million."
    )
    molybdenum_ppm: Optional[float] = Field(
        None,
        alias="molybdenumPpm",
        ge=0,
        description="Molybdenum (Mo) concentration in parts per million."
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
    schema_name: Literal["SoilSample"] = Field(
        "SoilSample",
        description="The name of the schema used to validate the data."
    )
    sample_id: str = Field(
        ...,
        alias="sampleId",
        description="Unique identifier for the soil sample.",
        examples=["SS-2025-FIELD-A-001"]
    )
    event_id: Optional[str] = Field(
        default_factory=str,
        alias="eventId",
        description="Unique identifier for the sample event.",
        examples=["1234-345-334-9876"]
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
    location: Location = Field(
        ...,
        alias="location",
        description="The location of the sample defined by the Location model."
    )
    analysis_results: SoilAnalysis = Field(
        ...,
        alias="analysisResults",
        description="The results of the nutrient analysis for the sample."
    )

    notes: list[str] = Field(
        ...,
        alias="notes",
        description="Notes associated with eh sample."
    )

    model_config = ConfigDict(
        extra="forbid",
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "schema_name": "SoilSample",
                "sampleId": "SS-2025-FIELD-A-001",
                "eventId": "1234-345-334-9876",
                "timestamp": "2025-08-21T10:30:00Z",
                "labId": "AgriLab-1",
                "sampleRadiusM": 2.5,
                "startDepthCm": 0.0,
                "endDepthCm": 15.0,
                "extractionType": "Mehlich-3",
                "location": {
                    "id": "loc-soil-sample-1",
                    "name": "Field A Sample Point 1",
                    "latitude": 40.7128,
                    "longitude": -74.0060,
                    "elevation_m": 50.0,
                    "crs": "EPSG:4326",
                    "geometry": "POINT (-74.0060 40.7128)",
                    "admin_level_0": "USA",
                    "admin_level_1": "New York",
                    "admin_level_2": "New York County",
                    "admin_level_3": "Farm X",
                    "site": "Research Farm",
                    "field": "Field_A",
                    "location": "Center of Field A"
                },
                "analysisResults": {
                    "ph": 6.9,
                    "organicMatterPercent": 3.2,
                    "nitrogenPpm": 25.0,
                    "phosphorusPpm": 55.0,
                    "potassiumPpm": 150.0,
                    "sulfurPpm": 12.0,
                    "calciumPpm": 1500.0,
                    "magnesiumPpm": 250.0,
                    "zincPpm": 2.1,
                    "ironPpm": 45.0,
                    "manganesePpm": 30.0,
                    "copperPpm": 0.8,
                    "boronPpm": 0.5,
                    "molybdenumPpm": 0.1,
                    "cationExchangeCapacity": 18.5
                },
                "notes": ["Sample taken before fall fertilization.",
                          "Area with historical lower yields."]
            }
        }
    )


class SoilAggregate(BaseModel):
    """
    Represents a single soil sample, including its location, depth, and lab analysis results.
    """
    schema_name: Literal["SoilAggregate"] = Field(
        "SoilAggregate",
        description="The name of the schema used to validate the data."
    )
    event_id: str = Field(
        ...,
        alias="eventId",
        description="Unique identifier for the sample event.",
        examples=["SS-2025-FIELD-A-001"]
    )
    file_path: Optional[str] = Field(
        ...,
        alias="filePath",
        description="The path to the spatial data."
    )
    timestamp: datetime = Field(
        ...,
        description="The date and time the sample was collected."
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
    location: Location = Field(
        Location,
        alias="location",
        description="The location of the sample defined by the Location model."
    )
    analysis_results: SoilAnalysis = Field(
        SoilAnalysis,
        alias="analysisResults",
        description="The results of the nutrient analysis for the sample."
    )
    notes: list[str] = Field(
        [],
        alias="notes",
        description="Notes associated with eh sample."
    )

    model_config = ConfigDict(
        extra="forbid",
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "schema_name": "SoilAggregate",
                "eventId": "1234-456-234-1987",
                "timestamp": "2025-08-21T10:30:00Z",
                "labId": "AgriLab-1",
                "startDepthCm": 0.0,
                "endDepthCm": 15.0,
                "extractionType": "Mehlich-3",
                "location": {
                    "id": "loc-soil-sample-2",
                    "name": "Field A Sample Point 1",
                    "latitude": 40.7128,
                    "longitude": -74.0060,
                    "elevation_m": 50.0,
                    "crs": "EPSG:4326",
                    "geometry": "POINT (-74.0060 40.7128)",
                    "admin_level_0": "USA",
                    "admin_level_1": "New York",
                    "admin_level_2": "New York County",
                    "admin_level_3": "Farm X",
                    "site": "Research Farm",
                    "field": "Field_A",
                    "location": "Center of Field A"
                },
                "analysisResults": {
                    "ph": 6.5,
                    "organicMatterPercent": 3.2,
                    "nitrogenPpm": 25.0,
                    "phosphorusPpm": 55.0,
                    "potassiumPpm": 150.0,
                    "sulfurPpm": 12.0,
                    "calciumPpm": 1500.0,
                    "magnesiumPpm": 250.0,
                    "zincPpm": 2.1,
                    "ironPpm": 45.0,
                    "manganesePpm": 30.0,
                    "copperPpm": 0.8,
                    "boronPpm": 0.5,
                    "molybdenumPpm": 0.1,
                    "cationExchangeCapacity": 18.5
                },
                "notes": []
            }
        }
    )
