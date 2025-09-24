from typing import Optional, Union
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CompoundModel(BaseModel):
    compound: str = Field(
        ...,
        alias="compound",
        description="The name of the compound.",
        examples=["glyphosate"]
    )
    percentage: float = Field(
        ...,
        alias="percentage",
        description="The amount of the compound in the product, expressed as a percentage of the total product mass.",
        examples=[47.7]
    )


class NutrientComposition(BaseModel):
    """
    A nested model to contain the specific chemical analysis results of a soil sample.
    Units are generally in parts per million (ppm) unless otherwise specified.
    """
    nitrogen: float = Field(
        ...,
        alias="nitrogen",
        le=100,
        ge=0,
        description="The amount of nitrogen (N) in the Product.",
        examples=[10]
    )
    phosphorous: float = Field(
        ...,
        alias="phosphorous",
        le=100,
        ge=0,
        description="The amount of phosphorus (P2O5) in the Product.",
        examples=[24]
    )

    # Macronutrients
    potassium: float = Field(
        ...,
        alias="potassium",
        le=100,
        ge=0,
        description="The amount of potassium (K2O) in the Product."
    )
    sulfur: Optional[float] = Field(
        0.0,
        alias="sulfur",
        le=100,
        ge=0,
        description="The amount of sulfur (S) in the Product.",
    )
    zinc: Optional[float] = Field(
        0.0,
        alias="zinc",
        le=100,
        ge=0,
        description="The amount of zinc (Zn) in the Product."
    )

    calcium: Optional[float] = Field(
        0.0,
        alias="calcium",
        le=100,
        ge=0,
        description="Zinc (Zn) concentration in parts per million."
    )
    copper: Optional[float] = Field(
        0.0,
        alias="copper",
        le=100,
        ge=0,
        description="The amount of copper (Cu) in the Product."
    )
    boron: Optional[float] = Field(
        0.0,
        alias="boron",
        le=100,
        ge=0,
        description="The amount of boron (B) in the Product."
    )
    manganese: Optional[float] = Field(
        0.0,
        alias="manganese",
        le=100,
        ge=0,
        description="The amount of manganese (Mn) in the Product."
    )
    magnesium: Optional[float] = Field(
        0.0,
        alias="magnesium",
        le=100,
        ge=0,
        description="The amount of magnesium (Mg) in the Product."
    )

    molybdenum: Optional[float] = Field(
        0.0,
        alias="molybdenum",
        le=100,
        ge=0,
        description="The amount of molybdenum (Mo) in the Product."
    )
    iron: Optional[float] = Field(
        0.0,
        alias="iron",
        le=100,
        ge=0,
        description="The amount of iron (Fe) in the Product."
    )


class PesticideModel(BaseModel):
    name: str
    percentage: float


class CropModel(BaseModel):
    name: str
    percentage: float


class HerbicideProduct(BaseModel):
    name: str
    regId: str
    company: str
    active_ingredient: list[PesticideModel]
    approved_crop: list[CropModel]


class InsecticideProduct(BaseModel):
    name: str
    regId: str
    company: str
    active_ingredient: list[PesticideModel]
    approved_crop: list[CropModel]


class FungicideProduct(BaseModel):
    name: str
    regId: str
    company: str
    active_ingredient: list[PesticideModel]
    approved_crop: list[CropModel]


class Product(BaseModel):
    """
    Represents a single soil sample, including its location, depth, and lab analysis results.
    """
    name: str = Field(
        ...,
        alias="name",
        description="The name of the product.",
        examples=["Round-up"]
    )
    product_id: str = Field(
        ...,
        alias="productId",
        description="A unique identifier for the product.",
        examples=["SS-2025-FIELD-A-001"]
    )
    company: str = Field(
        ...,
        alias="company",
        description="The Company that made the product.",
        examples=["Company A"]
    )
    registration_id: str = Field(
        ...,
        alias="registrationId",
        description="The Registraiton ID for the product.",
        examples=["123456789"]
    )
    nutrients: NutrientComposition = Field(
        ...,
        alias="nutrientComposition",
        description="The nutrient analysis of the product."
    )
    herbicides: list[PesticideModel] = Field(
        None,
        alias="herbicideComposition",
        description="The herbicides in the product."
    )
    insecticides: list[PesticideModel] = Field(
        None,
        alias="insecticideComposition",
        description="The insecticides in the product."
    )
    fungicides: list[PesticideModel] = Field(
        None,
        alias="fungicideComposition",
        description="The fungicides in the product."
    )
    nematicides: list[PesticideModel] = Field(
        None,
        alias="nematicideComposition",
        description="The nematicides in the product."
    )
    growth_regulators: list[PesticideModel] = Field(
        None,
        alias="growthRegulatorComposition",
        description="The growth regulators in the product."
    )

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "SuperGrow Fertilizer",
                "productId": "FG-SG-001",
                "company": "AgriSolutions Inc.",
                "registrationId": "REG12345AGRI",
                "nutrients": {
                    "nitrogen": 10.0,
                    "phosphorous": 20.0,
                    "potassium": 10.0,
                    "sulfur": 5.0,
                    "zinc": 0.5,
                    "calcium": 2.0,
                    "copper": 0.1,
                    "boron": 0.05,
                    "manganese": 0.2,
                    "magnesium": 1.5,
                    "molybdenum": 0.01,
                    "iron": 0.3
                },
                "herbicides": [
                    {
                        "name": "Glyphosate",
                        "percentage": 41.0
                    }
                ],
                "insecticides": [],
                "fungicides": [],
                "nematicides": [],
                "growthRegulators": []
            }
        }
