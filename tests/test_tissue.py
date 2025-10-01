from datetime import datetime

import pytest
from open_aglabs.tissue.models import TissueSample


def test_tissue_sample_initialization():
    sample_data = {
        "sampleId": "TS-2025-FZ-001",
        "sampleLocationId": "TS-2025-FIELD-A-LOC-001",
        "timestamp": "2025-08-21T10:30:00Z",

        "labId": "TissueLab-A",
        "sampleRadiusM": 0.2,
        "growthStage": "Flowering",
        "plantFraction": "Leaf",
        "plantSamples": "10",
        "location": {
            "latitude": 34.0522,
            "longitude": -118.2437,
        },
        "analysisResults": {
            "phosphorusPct": 0.5,
            "potassiumPct": 9,
        }
    }

    sample = TissueSample(**sample_data)

    assert sample.sample_id == "TS-2025-FZ-001"
    assert sample.sample_location_id == "TS-2025-FIELD-A-LOC-001"
    assert sample.timestamp == datetime.fromisoformat("2025-08-21T10:30:00+00:00")
    assert sample.location.latitude == 34.0522
    assert sample.location.longitude == -118.2437
    assert sample.lab_id == "TissueLab-A"
    assert sample.sample_radius_m == 0.2
    assert sample.growth_stage == "Flowering"
    assert sample.plant_fraction == "Leaf"
    assert sample.number_of_plants_sampled == 10
    assert sample.analysis_results.phosphorus_pct == 0.5
    assert sample.analysis_results.potassium_pct == 9


def test_tissue_sample_missing_required_fields():
    incomplete_data = {
        "sampleId": "TS-2025-FZ-002",
        "location": {
            "latitude": 34.0522,
            "longitude": -118.2437,
        },
        "sampleRadiusM": 0.2,
        "growthStage": "Vegetative",
        "plantFraction": "Stem",
    }

    with pytest.raises(ValueError):
        TissueSample(**incomplete_data)


def test_tissue_sample_invalid_latitude():
    invalid_latitude_data = {
        "sampleId": "TS-2025-FZ-003",
        "sampleLocationId": "TS-2025-FIELD-A-LOC-002",
        "timestamp": "2025-08-21T10:30:00Z",
        "location": {
            "latitude": -100.0,  # Invalid latitude
            "longitude": -118.2437,
        },
        "labId": "TissueLab-B",
        "sampleRadiusM": 0.5,
        "growthStage": "Reproductive",
        "plantFraction": "Root",
        "plantSamples": "15",
        "analysisResults": {
            "phosphorusPct": 0.6,
            "potassiumPpm": 30.0,
        }
    }

    with pytest.raises(ValueError):
        TissueSample(**invalid_latitude_data)


def test_tissue_sample_valid_with_partial_analysis_results():
    valid_data = {
        "sampleId": "TS-2025-FZ-004",
        "sampleLocationId": "TS-2025-FIELD-B-LOC-001",
        "timestamp": "2025-08-21T12:45:00Z",
        "location": {
            "latitude": 40.7128,
            "longitude": -74.0060,
        },
        "labId": "TissueLab-C",
        "sampleRadiusM": 0.3,
        "growthStage": "Maturity",
        "plantFraction": "Flower",
        "plantSamples": "5",
        "analysisResults": {
            "phosphorusPct": 0.7,
        }
    }

    sample = TissueSample(**valid_data)

    assert sample.analysis_results.phosphorus_pct == 0.7
    assert sample.analysis_results.potassium_pct is None
