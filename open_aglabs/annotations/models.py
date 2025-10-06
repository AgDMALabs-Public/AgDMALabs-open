from pydantic import BaseModel, Field
from typing import Optional


class OrganismProperties(BaseModel):
    """
    Pydantic model for storing plant taxonomic information.
    """
    common_name: Optional[str] = Field(
        None,
        description="The common name of the organism"
    )
    cultivar: Optional[str] = Field(
        None,
        description="The common name of the organism"
    )
    family: Optional[str] = Field(
        None,
        description="The common name of the organism"
    )
    genus: Optional[str] = Field(
        None,
        description="The common name of the organism"
    )
    species: Optional[str] = Field(
        None,
        description="The common name of the organism"
    )
    subspecies: Optional[str] = Field(
        None,
        description="The common name of the organism"
    )
    class ConfigDict:
        extra = 'forbid'
        validate_by_name = True  # Allow population using 'class' or 'class_name'
        json_schema_extra = {
            "example": {
                "common_name": "corn",
                "cultivar": "field",
                "family": "poaceae",
                "genus": "zea",
                "species": "zea mays",
                "subspecies": "mays"
            }
        }


class PlantDevelopmentalStage(BaseModel):
    common: Optional[str] = Field(
        None,
        description="The biological kingdom of the organism (e.g., 'Plantae')."
    )
    scientific: Optional[str] = Field(
        None,
        description="The biological phylum/division of the plant."
    )
    crop_growth_stage: Optional[str] = Field(
        None,
        alias="class",  # Use alias to allow 'class' as a field name
        description="The biological class of the plant."
    )
    order: Optional[str] = Field(
        None,
        description="The biological order of the plant."
    )

    class ConfigDict:
        extra = 'forbid'
        validate_by_name = True  # Allow population using 'class' or 'class_name'


class PlantStructure(BaseModel):
    common: Optional[str] = Field(
        None,
        description="The common name for the plant structure being annotated."
    )
    scientific: Optional[str] = Field(
        None,
        description="The scientific name for the plant structure being annotated."
    )

    class ConfigDict:
        extra = 'forbid'
        validate_by_name = True  # Allow population using 'class' or 'class_name'
        json_schema_extra = {
            "example": {
                "kingdom": "Plantae",
                "phylum": "Tracheophyta",
                "class": "Liliopsida",
                "order": "Poales",
                "family": "Poaceae",
                "genus": "Zea",
                "species": "Zea mays"
            }
        }


class PlantAnnotations(BaseModel):
    organism_properties: OrganismProperties = Field(
        ...,
        description="The taxonomic information for the organism."
    )
    developmental_properties: PlantDevelopmentalStage = Field(
        ...,
        description="The developmental properties of the plant."
    )
    structure_properties: PlantStructure = Field(
        ...,
        description="The structure properties of the plant."
    )
