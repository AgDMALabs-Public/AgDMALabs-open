from typing import Optional

from pydantic import BaseModel, Field


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


class IngredientModel(BaseModel):
    name: str
    percentage: float


class PesticideProduct(BaseModel):
    name: str
    regId: str
    company: str
    active_ingredient: list[IngredientModel]
    approved_crop: list[str]


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
    herbicides: PesticideProduct = Field(
        None,
        alias="herbicideComposition",
        description="The herbicides in the product."
    )
    insecticides: PesticideProduct = Field(
        None,
        alias="insecticideComposition",
        description="The insecticides in the product."
    )
    fungicides: PesticideProduct = Field(
        None,
        alias="fungicideComposition",
        description="The fungicides in the product."
    )
    nematicides: PesticideProduct = Field(
        None,
        alias="nematicideComposition",
        description="The nematicides in the product."
    )
    growth_regulators: PesticideProduct = Field(
        None,
        alias="growthRegulatorComposition",
        description="The growth regulators in the product."
    )

    other: PesticideProduct = Field(
        None,
        alias="other",
        description="A place to put products that do not fall under the main category."
    )

    notes: list[str] = Field(
        None,
        alias="notes",
        description="A place to put notes about the product."
    )

    class Config:
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "SuperGrow Fertilizer with Integrated Herbicide",
                "productId": "FG-IH-002",
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
                "herbicides": {
                    "name": "WeedAway Herbicide",
                    "regId": "HERB7890",
                    "company": "PestControl Corp.",
                    "active_ingredient": [
                        {"name": "Glyphosate", "percentage": 41.0},
                        {"name": "2,4-D", "percentage": 15.0}
                    ],
                    "approved_crop": ["Corn", "Soybeans"]
                },
                "insecticides": None,  # Assuming no insecticide in this specific example product
                "fungicides": None,  # Assuming no fungicide
                "nematicides": None,  # Assuming no nematicide
                "growth_regulators": None,  # Assuming no growth regulators
                "other": None,  # Assuming no other specific category
                "notes": ["Broad-spectrum fertilizer and post-emergent herbicide for corn and soybeans."]
            }
        }
