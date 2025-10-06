import pytest
from open_aglabs.annotations.models import OrganismProperties
from pydantic import ValidationError


def test_valid_organism_properties_creation():
    data = {
        "common_name": "corn",
        "cultivar": "field",
        "family": "poaceae",
        "genus": "zea",
        "species": "zea mays",
        "subspecies": "mays"
    }
    organism = OrganismProperties(**data)
    assert organism.common_name == "corn"
    assert organism.cultivar == "field"
    assert organism.family == "poaceae"
    assert organism.genus == "zea"
    assert organism.species == "zea mays"
    assert organism.subspecies == "mays"


def test_optional_fields():
    data = {
        "common_name": "soybean"
    }
    organism = OrganismProperties(**data)
    assert organism.common_name == "soybean"
    assert organism.cultivar is None
    assert organism.family is None
    assert organism.genus is None
    assert organism.species is None
    assert organism.subspecies is None

def test_empty_model():
    organism = OrganismProperties()
    assert organism.common_name is None
    assert organism.cultivar is None
    assert organism.family is None
    assert organism.genus is None
    assert organism.species is None
    assert organism.subspecies is None
