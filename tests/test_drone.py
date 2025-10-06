import pytest
from open_aglabs.core.base_models import Location
from open_aglabs.drone.model import DroneFlight
from pydantic import ValidationError


def test_valid_drone_flight_creation():
    location_data = {
        "id": "loc-uuid-12345",
        "name": "Field 12 Drone Flight",
        "latitude": 34.0522,
        "longitude": -118.2437,
        "elevation_m": 100.0,
        "crs": "EPSG:4326",
        "site": "AgTech Research Farm",
        "field": "Field_12",
        "location": "Central part of Field 12"
    }
    drone_flight_data = {
        "id": "drone-flight-uuid-67890",
        "location": location_data,
        "droneMake": "DJI",
        "droneModel": "Mavic 3 Multispectral",
        "cameraMake": "DJI",
        "cameraModel": "Mavic 3M Camera",
        "groundControlPoints": True,
        "reflectancePanels": False,
        "reflectancePanelType": "Micasense",
        "flightHeight": 80.0,
        "horizontalOverlapPercentage": 70.0,
        "verticalOverlapPercentage": 70.0,
        "gpsQuality": "RTK",
        "multispecChannels": ["Green", "Red", "Red Edge", "NIR"],
        "directory": "/path/to/flight/data",
        "images": ['1234564565_1.tif', '1234564565_2.tif', '1234564565_3.tif', '1234564565_4.tif']
    }
    drone_flight = DroneFlight(**drone_flight_data)
    assert drone_flight.id == "drone-flight-uuid-67890"
    assert drone_flight.location.name == "Field 12 Drone Flight"
    assert drone_flight.drone_make == "DJI"
    assert drone_flight.drone_model == "Mavic 3 Multispectral"
    assert not drone_flight.reflectance_panels
    assert drone_flight.reflectance_panel_type == "Micasense"
    assert drone_flight.flight_height == 80.0
    assert drone_flight.images == ['1234564565_1.tif', '1234564565_2.tif', '1234564565_3.tif', '1234564565_4.tif']


def test_invalid_location_latitude():
    location_data = {
        "id": "loc-uuid-12345",
        "latitude": 95.0,  # Invalid latitude
        "longitude": -118.2437
    }
    drone_flight_data = {
        "id": "drone-flight-uuid-67890",
        "location": location_data,
        "droneMake": "DJI",
        "droneModel": "Mavic 3 Multispectral",
        "cameraMake": "DJI",
        "cameraModel": "Mavic 3M Camera",
        "groundControlPoints": True,
        "flightHeight": 80.0
    }
    with pytest.raises(ValidationError):
        DroneFlight(**drone_flight_data)


def test_missing_required_field():
    drone_flight_data = {
        "id": "drone-flight-uuid-67890",
        "location": {
            "id": "loc-uuid-12345"
        },
        "droneMake": "DJI",
        # Missing required field "droneModel"
        "cameraMake": "DJI",
        "cameraModel": "Mavic 3M Camera",
        "groundControlPoints": True,
        "flightHeight": 80.0
    }
    with pytest.raises(ValidationError):
        DroneFlight(**drone_flight_data)


def test_invalid_reflectance_panel_type():
    drone_flight_data = {
        "id": "drone-flight-uuid-67890",
        "location": {
            "id": "loc-uuid-12345",
            "latitude": 34.0522,
            "longitude": -118.2437
        },
        "droneMake": "DJI",
        "droneModel": "Mavic 3 Multispectral",
        "cameraMake": "DJI",
        "cameraModel": "Mavic 3M Camera",
        "groundControlPoints": True,
        "reflectancePanels": True,
        "reflectancePanelType": "InvalidType",  # Invalid value
        "flightHeight": 80.0
    }
    with pytest.raises(ValidationError):
        DroneFlight(**drone_flight_data)


def test_empty_images_list():
    drone_flight_data = {
        "id": "drone-flight-uuid-67890",
        "location": {
            "id": "loc-uuid-12345",
            "latitude": 34.0522,
            "longitude": -118.2437
        },
        "droneMake": "DJI",
        "droneModel": "Mavic 3 Multispectral",
        "cameraMake": "DJI",
        "cameraModel": "Mavic 3M Camera",
        "groundControlPoints": False,
        "flightHeight": 80.0,
        "images": []  # Empty images list
    }
    with pytest.raises(ValidationError):
        DroneFlight(**drone_flight_data)
