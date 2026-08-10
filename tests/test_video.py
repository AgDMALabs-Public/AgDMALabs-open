from open_aglabs.video.models import AgVideoModel


def test_agvideo_model_optional_fields():
    assert AgVideoModel(path="test_path", id="test_id").dict() == {
        "path": "test_path",
        "id": "test_id",
        "device": None,
        "type": None,
        "protocol_properties": None,
        "trial_properties": None,
        "camera_properties": None,
        "location_properties": None,
        "acquisition_properties": None,
        "video_quality": None,
        "agronomic_properties": None,
        "collection_properties": None,
        "notes": None
    }
    