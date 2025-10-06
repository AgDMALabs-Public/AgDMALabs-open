import pytest
from open_aglabs.core.base_models import MLOutput
from pydantic import ValidationError


def test_mloutput_valid_data():
    data = {
        "pred": 0.95,
        "model_id": "model123",
        "model_version": "1.0.0",
    }
    ml_output = MLOutput(**data)
    assert ml_output.pred == 0.95
    assert ml_output.model_id == "model123"
    assert ml_output.model_version == "1.0.0"


def test_mloutput_missing_optional_fields():
    data = {
        "pred": "prediction string"
    }
    ml_output = MLOutput(**data)
    assert ml_output.pred == "prediction string"
    assert ml_output.model_id is None
    assert ml_output.model_version is None


def test_mloutput_invalid_pred_type():
    data = {
        "pred": {"invalid": "type"},
        "model_id": "model123",
        "model_version": "1.0.0",
    }
    with pytest.raises(ValidationError):
        MLOutput(**data)


def test_mloutput_disallowed_extra_field():
    data = {
        "pred": 0.95,
        "model_id": "model123",
        "model_version": "1.0.0",
        "extra_field": "not allowed",
    }
    with pytest.raises(ValidationError):
        MLOutput(**data)
