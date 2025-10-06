# File: tests/test_models.py

import pytest
from open_aglabs.annotations.models import PlantAnnotationStandardization, PlantAnnotation
from pydantic import ValidationError


def test_valid_plant_annotation_standardization():
    data = {
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
            }
        ]
    }
    plant_annotation_standardization = PlantAnnotationStandardization(**data)
    assert len(plant_annotation_standardization.annotations) == 1
    assert plant_annotation_standardization.annotations[0].annotation_name == "corn"


def test_invalid_missing_annotations_field():
    data = {}
    with pytest.raises(ValidationError) as exc_info:
        PlantAnnotationStandardization(**data)

    assert "Field required" in str(exc_info.value)


def test_disallowed_extra_fields():
    data = {
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
            }
        ],
        "extra_field": "not_allowed"
    }
    with pytest.raises(ValidationError) as exc_info:
        PlantAnnotationStandardization(**data)

    assert "Extra inputs are not permitted" in str(exc_info.value)