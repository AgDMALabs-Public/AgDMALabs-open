import pytest
from open_aglabs.core.base_models import Location, AgronomicProperties, TrialProperties
from open_aglabs.rover.models import RoverScan, RoverAcquisitionProperties


def test_rover_scan_basic_initialization():
    data = {
        "id": "scan-123-abc",
        "name": "Morning Scout",
        "task": "Data Collection",
        "location": {
            "id": "loc-001",
            "name": "Field A",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "elevation_m": 10.5,
            "site": "Farm A",
        },
        "trialProperties": {
            "id": "trial001",
            "name": "Growth Trial"
        },
        "rover_acquisition_properties": {
            "date": "2026-01-07",
            "time": "11:00:00",
            "rover_make": "NewGen",
            "rover_model": "Scout-3000",
            "camera_make": "Canon",
            "camera_model": "Vision-X",
            "cameraHeight": 50.0,
            "horizontalOverlapPercentage": 80.0,
            "verticalOverlapPercentage": 75.0,
            "gpsQuality": "RTK Fixed",
        },
        "agronomicProperties": {
            "crop_type": "maize",
            "growth_stage": "V3",
            "soil_color": "light",
            "irrigation_level": "high",
            "tillage_type": "conventional"
        },
        "images": [
            "s3://images/scan1/img1.jpg",
            "s3://images/scan1/img2.jpg"
        ]
    }

    rover_scan = RoverScan(**data)

    assert rover_scan.id == "scan-123-abc"
    assert rover_scan.name == "Morning Scout"
    assert rover_scan.task == "Data Collection"
    assert rover_scan.location.id == "loc-001"
    assert rover_scan.location.name == "Field A"
    assert rover_scan.location.latitude == 40.7128
    assert rover_scan.trial_properties.id == "trial001"
    assert rover_scan.trial_properties.name == "Growth Trial"
    assert rover_scan.rover_acquisition_properties.camera_model == "Vision-X"
    assert rover_scan.images == ["s3://images/scan1/img1.jpg", "s3://images/scan1/img2.jpg"]


def test_rover_scan_missing_optional_fields():
    data = {
        "id": "scan-456-def",
        "location": {
            "id": "loc-002",
            "name": "Field B",
            "latitude": 35.6895,
            "longitude": 139.6917,
        },
        "rover_acquisition_properties": {
            "rover_make": "DroneCorp",
            "rover_model": "X-400",
            "camera_make": "Nikon",
            "camera_model": "Alpha",
            "cameraHeight": 60.0,
            "horizontalOverlapPercentage": 85.0,
            "verticalOverlapPercentage": 80.0
        }
    }

    rover_scan = RoverScan(**data)

    assert rover_scan.id == "scan-456-def"
    assert rover_scan.name is None
    assert rover_scan.task is None
    assert rover_scan.trial_properties is None
    assert rover_scan.images is None
    assert rover_scan.location.name == "Field B"
    assert rover_scan.rover_acquisition_properties.rover_model == "X-400"


def test_rover_scan_example_validation():
    example = RoverScan.model_config.get("json_schema_extra", {}).get("example")
    rover_scan = RoverScan(**example)

    assert rover_scan.id == "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    assert rover_scan.name == "Morning Phenotyping Flight"
    assert rover_scan.rover_acquisition_properties.rover_make == "NewCo"
    assert rover_scan.agronomic_properties.crop_type == "maize"
    assert len(rover_scan.images) == 2
