import pytest
from open_aglabs.core.base_models import Location
from open_aglabs.drone.model import DroneFlight
from pydantic import ValidationError

import pytest
from open_aglabs.core.base_models import Location, AgronomicProperties, TrialProperties
from open_aglabs.drone.model import DroneAcquisitionProperties
from open_aglabs.drone.model import DroneFlight


def test_valid_drone_flight():
    data = {
        "id": "drone-flight-uuid-98765",
        "name": "Corn Health Assessment Flight",
        "task": "canopy_analysis",
        "location": {
            'id': "loc-uuid-54321",
            'name': "West Field Drone Flight",
            'latitude': 35.1234,
            'longitude': -119.5678,
            'elevation_m': 120.0,
            'crs': "EPSG:4326",
            'site': "AgriCore Research Facility",
            'field': "West_Field_03",
            'location': "Section B"
        },
        "trialProperties": {
            'name': "Fungicide Efficacy Trial 2025"
    },
        "drone_acquisition_properties": {
            'drone_make': "Quantum-Systems",
            'drone_model': "Trinity F90+",
            'camera_make': "Sony",
            'camera_model': "UCM-R",
            'groundControlPoints': True,
            'reflectancePanels': True,
            'reflectancePanelType': 'Micasense',
            'flightHeight': 90.0,
            'horizontalOverlapPercentage': 75.0,
            'verticalOverlapPercentage': 75.0,
            'gpsQuality': "RTK",
            'multispecChannels': ["Red", "Green", "Blue", "NIR"]
        },
        "agronomicProperties": {
            'crop_type': "corn",
            'growth_stage': "VT",
            'soil_color': "light",
            'weed_pressure': "low",
            'irrigation_level': "high",
            'tillage_type': "conventional",
            'fertilizer_level': "high"
    },
        "images": [
            "flight_98765_img_001.tif",
            "flight_98765_img_002.tif",
            "flight_98765_img_003.tif",
            "flight_98765_img_004.tif",
            "flight_98765_img_005.tif"
        ]
    }
    drone_flight = DroneFlight(**data)
    assert drone_flight.id == "drone-flight-uuid-98765"
    assert drone_flight.name == "Corn Health Assessment Flight"
    assert drone_flight.task == "canopy_analysis"
    assert drone_flight.location.latitude == 35.1234
    assert drone_flight.trial_properties.name == "Fungicide Efficacy Trial 2025"
    assert drone_flight.drone_acquisition_properties.drone_make == "Quantum-Systems"
    assert drone_flight.drone_acquisition_properties.drone_model == "Trinity F90+"
    assert drone_flight.agronomic_properties.crop_type == "corn"
    assert len(drone_flight.images) == 5


def test_drone_flight_missing_required_field():
    data = {
        "name": "Corn Health Assessment Flight",
        "task": "canopy_analysis",
        "location": Location(
            id="loc-uuid-54321",
            name="West Field Drone Flight",
            latitude=35.1234,
            longitude=-119.5678,
            elevation_m=120.0,
            crs="EPSG:4326",
            site="AgriCore Research Facility",
            field="West_Field_03",
            location="Section B"
        ),
        "drone_acquisition_properties": DroneAcquisitionProperties(
            drone_make="Quantum-Systems",
            drone_model="Trinity F90+",
            camera_make="Sony",
            camera_model="UCM-R",
            groundControlPoints=True,
            reflectancePanels=True,
            reflectancePanelType='Micasense',
            flightHeight=90.0,
            horizontalOverlapPercentage=75.0,
            verticalOverlapPercentage=75.0,
            gpsQuality="RTK",
            multispecChannels=["Red", "Green", "Blue", "NIR"]
        ),
        "images": [
            "flight_98765_img_001.tif",
            "flight_98765_img_002.tif"
        ]
    }
    with pytest.raises(Exception):
        DroneFlight(**data)

