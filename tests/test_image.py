from uuid import uuid4

import pytest
from open_aglabs.image.models import Image, CameraProperties, Location, AcquisitionProperties, ImageQuality
from pydantic import ValidationError


def test_valid_image():
    data = {
        "path": "/images/field_A/row_1/image_001.jpg",
        "id": str(uuid4()),
        "device": "drone",
        "type": "original",
        "camera_properties": {
            "model": "DJI Mavic 2 Pro",
            "make": 1.0,
            "iso": 100.0,
            "magnification": 1.0
        },
        "location_properties": {
            "id": "location-uuid-001",
            "latitude": 34.0522,
            "longitude": -118.2437,
            "elevation_m": 100.5
        },
        "acquisition_properties": {
            "date": "2025-09-30",
            "time": "10:30:00",
            "camera_height_m": 50.0,
            "camera_angle_deg": 90.0
        },
        "image_quality": {
            "exposure": 50.0,
            "aperture": "f/2.8",
            "iso": 100.0,
            "height": 4000.0,
            "width": 6000.0,
            "channels": 3,
            "pct_pixel_over_saturation": 1.2,
            "pct_pixel_under_saturation": 0.5
        }
    }
    image = Image(**data)
    assert image.path == "/images/field_A/row_1/image_001.jpg"
    assert image.device == "drone"
    assert image.type == "original"
    assert isinstance(image.camera_properties, CameraProperties)
    assert image.camera_properties.model == "DJI Mavic 2 Pro"
    assert isinstance(image.location_properties, Location)
    assert image.location_properties.latitude == 34.0522
    assert isinstance(image.acquisition_properties, AcquisitionProperties)
    assert image.acquisition_properties.camera_angle_deg == 90.0
    assert isinstance(image.image_quality, ImageQuality)
    assert image.image_quality.exposure == 50.0


def test_invalid_image_type():
    with pytest.raises(ValidationError):
        Image(
            path="/images/field_A/row_1/image_001.jpg",
            id=str(uuid4()),
            device="drone",
            type="unsupported_type"
        )


def test_missing_required_fields():
    with pytest.raises(ValidationError):
        Image(
            device="drone",
            type="original"
        )