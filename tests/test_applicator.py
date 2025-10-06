import pytest
from open_aglabs.applicator.models import ApplicatorZone, ApplicationEvent
from open_aglabs.core.base_models import Location
from pydantic import ValidationError

from datetime import datetime



def test_valid_applicator_zone():
    data = {
        "id": "zone1",
        "geometry": "POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))",
        "tank_id": "tankA",
        "tank_mix": "mix1",
        "rate": 50
    }
    applicator_zone = ApplicatorZone(**data)
    assert applicator_zone.id == "zone1"
    assert applicator_zone.geometry == "POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))"
    assert applicator_zone.tank_id == "tankA"
    assert applicator_zone.tank_mix == "mix1"
    assert applicator_zone.rate == 50


def test_applicator_zone_missing_required_field():
    data = {
        "geometry": "POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))",
        "tank_id": "tankA",
        "tank_mix": "mix1",
        "rate": 50
    }
    with pytest.raises(ValidationError):
        ApplicatorZone(**data)


def test_applicator_zone_empty_tank_mix():
    data = {
        "id": "zone1",
        "geometry": "POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))",
        "tank_id": "tankA",
        "tank_mix": "",
        "rate": 50
    }
    applicator_zone = ApplicatorZone(**data)
    assert applicator_zone.tank_mix == ""


def test_valid_application_event():
    valid_data = {
        "schema_name": "ApplicationEvent",
        "eventId": "APP-2025-FIELD-A-002",
        "location": {
            "id": "loc-uuid-12345",
            "name": "Test Location",
            "latitude": 45.12345,
            "longitude": -93.12345,
            "elevation_m": 300.0,
            "crs": "EPSG:4326"
        },
        "timestamp": "2025-10-01T12:00:00Z",
        "applicationType": "Fertilizer",
        "mixName": "Urea",
        "applicationRate": 1.5,
        "rateUnit": "kg/ha",
        "method": "Broadcast",
        "equipment": "Tractor Sprayer",
        "notes": "Test note"
    }
    event = ApplicationEvent(**valid_data)
    assert event.schema_name == "ApplicationEvent"
    assert event.id == "APP-2025-FIELD-A-002"
    assert isinstance(event.location, Location)
    assert event.location.id == "loc-uuid-12345"
    assert event.timestamp == datetime.fromisoformat("2025-10-01T12:00:00+00:00")
    assert event.application_type == "Fertilizer"
    assert event.mix_name == "Urea"
    assert event.rate == 1.5
    assert event.rate_unit == "kg/ha"
    assert event.method == "Broadcast"
    assert event.equipment == "Tractor Sprayer"
    assert event.notes == "Test note"


def test_invalid_application_event_missing_required_field():
    invalid_data = {
        "schema_name": "ApplicationEvent",
        "eventId": "APP-2025-FIELD-A-002",
        "timestamp": "2025-10-01T12:00:00Z",
        "applicationType": "Fertilizer",
        "applicationRate": 1.5,
        "rateUnit": "kg/ha"
    }
    with pytest.raises(ValidationError):
        ApplicationEvent(**invalid_data)


def test_invalid_application_rate_negative_value():
    invalid_data = {
        "schema_name": "ApplicationEvent",
        "eventId": "APP-2025-FIELD-A-002",
        "timestamp": "2025-10-01T12:00:00Z",
        "applicationType": "Fertilizer",
        "mixName": "Urea",
        "applicationRate": -5.0,
        "rateUnit": "kg/ha"
    }
    with pytest.raises(ValidationError):
        ApplicationEvent(**invalid_data)


def test_extra_field_in_application_event():
    invalid_data = {
        "schema_name": "ApplicationEvent",
        "eventId": "APP-2025-FIELD-A-002",
        "timestamp": "2025-10-01T12:00:00Z",
        "applicationType": "Herbicide",
        "mixName": "Glyphosate",
        "applicationRate": 2.0,
        "rateUnit": "L/ha",
        "extra_field": "Extra data"
    }
    with pytest.raises(ValidationError):
        ApplicationEvent(**invalid_data)

