from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Literal


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
        description="The cultivar of the organism"
    )
    family: Optional[str] = Field(
        None,
        description="The family the organism belongs to."
    )
    genus: Optional[str] = Field(
        None,
        description="The genus the organism belongs to."
    )
    species: Optional[str] = Field(
        None,
        description="The species the organism belongs to."
    )
    subspecies: Optional[str] = Field(
        None,
        description="The subspecies the organism belongs to."
    )
    model_config = ConfigDict(
        extra='forbid',
        validate_by_name=True,  # Allow population using 'class' or 'class_name'
        json_schema_extra={
            "example": {
                "common_name": "corn",
                "cultivar": "field",
                "family": "poaceae",
                "genus": "zea",
                "species": "zea mays",
                "subspecies": "mays"
            }
        }
    )


class PlantDevelopmentalStage(BaseModel):
    common_name: Optional[str] = Field(
        None,
        description="The common name for the plant developmental stage being annotated."
    )
    ontology_source: Optional[str] = Field(
        None,
        description="The ontology name for the plant developmental stage being annotated."
    )
    ontology_name: Optional[str] = Field(
        None,
        description="The scientific name for the plant developmental stage being annotated."
    )
    ontology_id: Optional[str] = Field(
        None,
        description="The ontology ID for the plant developmental stage being annotated."
    )
    crop_growth_stage: Optional[str] = Field(
        None,
        alias="class",  # Use alias to allow 'class' as a field name
        description="The technical name for the crop growth stage of the organism being annotated."
    )

    model_config = ConfigDict(
        extra='forbid',
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "common_name": "corn emergence",
                "ontology_source": "https://obofoundry.org/ontology/po.html",
                "ontology_name": "1 main shoot growth stage",
                "ontology_id": "PO:0007112",
                "crop_growth_stage": "ve"
            }}
    )


class PlantStructure(BaseModel):
    common_name: Optional[str] = Field(
        None,
        description="The common name for the plant structure being annotated."
    )
    state: Optional[str] = Field(
        None,
        description="The state of the plant structure being annotated. Ex Open for a flower."
    )
    ontology_source: Optional[str] = Field(
        None,
        description="The ontology name for the plant structure being annotated."
    )
    ontology_name: Optional[str] = Field(
        None,
        description="The scientific name for the plant structure being annotated."
    )
    ontology_id: Optional[str] = Field(
        None,
        description="The scientific name for the plant structure being annotated."
    )
    model_config = ConfigDict(
        extra='forbid',
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "common_name": "plant",
                "state": "living",
                "ontology_source": "https://obofoundry.org/ontology/po.html",
                "ontology_name": "whole plant",
                "ontology_id": "PO:0000003"
            }
        }
    )


class PlantAnnotation(BaseModel):
    annotation_name: str = Field(
        ...,
        description="The name of the annotation"
    )
    annotation_class_id: int = Field(
        ...,
        description="The ID of the annotation class"
    )
    standardized_annotation_name: Optional[str] = Field(
        None,
        description="The name of the standardized annotation, that can be matched to a db for reference"
    )
    standardized_growth_stage: Optional[int] = Field(
        None,
        description="The growth stage of the standardized annotation, that can be matched to a db for reference"
    )
    organism_properties: OrganismProperties = Field(
        ...,
        description="The taxonomic information for the organism."
    )
    plant_development: PlantDevelopmentalStage = Field(
        ...,
        description="The developmental properties of the plant."
    )
    plant_structure: PlantStructure = Field(
        ...,
        description="The structure properties of the plant."
    )
    notes: Optional[str] = Field(
        None,
        description="Any additional notes about the annotation."
    )
    model_config = ConfigDict(
        extra='allow',
        json_schema_extra={
            "example": {
                "annotation_name": "corn",
                "annotation_class_id": 1,
                "organism_properties": {
                    "common_name": "corn",
                    "cultivar": "field",
                    "family": "poaceae",
                    "genus": "zea",
                    "species": "zea mays",
                    "subspecies": "mays"
                },
                "plant_development": {
                    "common_name": "emergence",
                    "ontology_source": "https://obofoundry.org/ontology/po.html",
                    "ontology_name": "1 main shoot growth stage",
                    "ontology_id": "PO:0007112",
                    "crop_growth_stage": "ve"
                },
                "plant_structure": {
                    "common_name": "plant",
                    "state": "living",
                    "ontology_source": "https://obofoundry.org/ontology/po.html",
                    "ontology_name": "whole plant",
                    "ontology_id": "PO:0000003"
                },
                "notes": "The objective of the annotation task was to label all the emerging for plant for a"
                         " stand count model.."
            }
        }
    )


class PlantAnnotationStandardization(BaseModel):
    schema_name: Literal["PlantAnnotationStandardization"] = Field(
        ...,
        description="The name of the schema"
    )
    annotations: List[PlantAnnotation] = Field(
        ...,
        description="A list of annotations with the metadata to standardize them."
    )
    model_config = ConfigDict(
        extra='forbid',
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "schema_name": "PlantAnnotationStandardization",
                "annotations": [
                    {
                        "annotation_name": "corn",
                        "annotation_class_id": 1,
                        "organism_properties": {
                            "common_name": "corn",
                            "cultivar": "field",
                            "family": "poaceae",
                            "genus": "zea",
                            "species": "zea mays",
                            "subspecies": "mays"
                        },
                        "developmental_properties": {
                            "common_name": "emergence",
                            "ontology_source": "https://obofoundry.org/ontology/po.html",
                            "ontology_name": "1 main shoot growth stage",
                            "ontology_id": "PO:0007112",
                            "crop_growth_stage": "ve"
                        },
                        "structure_properties": {
                            "common_name": "plant",
                            "state": "living",
                            "ontology_name": "whole plant",
                            "ontology_id": "PO:0000003"
                        }
                    },
                    {
                        "annotation_name": "leaf",
                        "annotation_class_id": 2,
                        "organism_properties": {
                            "common_name": "corn",
                            "cultivar": "field",
                            "family": "poaceae",
                            "genus": "zea",
                            "species": "zea mays",
                            "subspecies": "mays"
                        },
                        "developmental_properties": {
                            "common_name": "corn v6",
                            "ontology_source": "https://obofoundry.org/ontology/po.html",
                            "ontology_name": "LP.06 six leaves visible stage",
                            "ontology_id": "PO:0007123",
                            "crop_growth_stage": "v6"
                        },
                        "structure_properties": {
                            "common_name": "leaf",
                            "state": "living",
                            "ontology_name": "cauline leaf",
                            "ontology_id": "PO:0009025"
                        }
                    }
                ]
            }
        }
    )
