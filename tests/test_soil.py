from datetime import datetime

import pytest
from open_aglabs.core.base_models import Location
from open_aglabs.soil.models import SoilSample, SoilAnalysis
from pydantic import ValidationError


def test_valid_soil_sample_creation():
    valid_data = {
        "sampleId": "SS-2025-FIELD-A-001",
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
            "ph": 6.5,
            "organicMatterPercent": 3.2,
            "nitrogenPpm": 25.0,
            "phosphorusPpm": 55.0,
            "potassiumPpm": 150.0,
            "sulfurPpm": 12.0,
            "calciumPpm": 1500.0,
            "magnesiumPct": 250.0,
            "zincPpm": 2.1,
            "ironPpm": 45.0,
            "manganesePpm": 30.0,
            "copperPpm": 0.8,
            "boronPpm": 0.5,
            "molybdenumPpm": 0.1,
            "cationExchangeCapacity": 18.5
        },
        "notes": ["Sample taken before fall fertilization.", "Area with historical lower yields."]
    }

    sample = SoilSample(**valid_data)
    assert sample.sample_id == "SS-2025-FIELD-A-001"
    assert sample.timestamp == datetime.fromisoformat("2025-08-21T10:30:00+00:00")
    assert sample.lab_id == "AgriLab-1"
    assert sample.sample_radius_m == 2.5
    assert sample.start_depth_cm == 0.0
    assert sample.end_depth_cm == 15.0
    assert sample.extraction_type == "Mehlich-3"
    assert sample.location.id == "loc-soil-sample-1"
    assert sample.analysis_results.ph == 6.5
    assert sample.notes == ["Sample taken before fall fertilization.", "Area with historical lower yields."]


def test_invalid_end_depth_cm():
    invalid_data = {
        "sampleId": "SS-2025-FIELD-A-002",
        "timestamp": "2025-08-21T10:30:00Z",
        "labId": "AgriLab-1",
        "sampleRadiusM": 2.5,
        "startDepthCm": 15.0,
        "endDepthCm": -1.0,
        "extractionType": "Mehlich-3",
        "location": {
            "id": "loc-soil-sample-2",
            "name": "Field B Sample Point 2",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "elevation_m": 50.0,
            "crs": "EPSG:4326",
            "geometry": "POINT (-74.0060 40.7128)",
            "admin_level_0": "USA",
            "admin_level_1": "New York",
            "admin_level_2": "New York County",
            "admin_level_3": "Farm Y",
            "site": "Research Field",
            "field": "Field_B",
            "location": "Center of Field B"
        },
        "analysisResults": {
            "ph": 6.5,
            "organicMatterPercent": 3.2,
            "nitrogenPpm": 25.0,
            "phosphorusPpm": 55.0,
            "potassiumPpm": 150.0,
            "sulfurPpm": 12.0,
            "calciumPpm": 1500.0,
            "magnesiumPct": 250.0,
            "zincPpm": 2.1,
            "ironPpm": 45.0,
            "manganesePpm": 30.0,
            "copperPpm": 0.8,
            "boronPpm": 0.5,
            "molybdenumPpm": 0.1,
            "cationExchangeCapacity": 18.5
        },
        "notes": ["Sample taken after spring fertilization."]
    }

    with pytest.raises(ValidationError):
        SoilSample(**invalid_data)


def test_missing_required_field():
    invalid_data = {
        "timestamp": "2025-08-21T10:30:00Z",
        "sampleRadiusM": 2.5,
        "startDepthCm": 0.0,
        "endDepthCm": 15.0,
        "extractionType": "Mehlich-3",
        "location": {
            "id": "loc-soil-sample-3",
            "name": "Field C Sample Point 3"
        },
        "analysisResults": {
            "ph": 6.5,
            "organicMatterPercent": 3.2,
            "phosphorusPpm": 55.0,
            "potassiumPpm": 150.0,
            "calciumPpm": 1500.0
        },
        "notes": []
    }

    with pytest.raises(ValidationError):
        SoilSample(**invalid_data)
