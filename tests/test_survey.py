from uuid import uuid4

import pytest
from open_aglabs.surveys.models import SurveyDataModel
from pydantic import ValidationError


def test_survey_data_model_initialization():
    data = {
        "id": str(uuid4()),
        "path": "/surveys/2025/sample_data.json",
        "collection_date": "2025-12-01",
        "trial_properties": {
            "name": "maize_variety_survey_2025"
        },
        "protocol_properties": {
            "name": "crop_survey_v2.0",
        },
        "location_properties": {
            "admin_level_0": "Kenya",
            "site": "Example Site",
            "field": "Field_1B",
            "location": ""
        },
        "agronomic_properties": {
            "crop_type": "corn",
        },
        "answers": {
            "Q1": {"question": "What is the yield?",
                   "answer": "20 tons/ha",
                   "audio": [{"path": "voice_clip.mp3", "id": str(uuid4())}],
                   "image": [{"path": "image_20251201.png", "id": str(uuid4())}]
                   }
        },
        "followups": {
            "Q1": {"question": "Why so high?",
                   "answer": "Good rains this season.",
                   "audio": None,
                   "image": None}
        },
        "audio_files": [
            {"path": "voice_clip.mp3",
             "id": str(uuid4()),
             "question_id": ["Q1"],
             "question": ["Q1"],
             "answer": [""]}
        ],
        "image_files": [
            {"path": "image_20251201.png",
             "id": str(uuid4()),
             "question": ["Q1"]}
        ],
        "notes": [
            {"message": "Investigate field conditions further.",
             "author": "admin"}
        ]
    }
    survey = SurveyDataModel(**data)
    assert survey.id == data["id"]
    assert survey.path == data["path"]
    assert survey.collection_date == data["collection_date"]
    assert survey.trial_properties.name == data["trial_properties"]["name"]
    assert survey.protocol_properties.name == data["protocol_properties"]["name"]
    assert survey.agronomic_properties.crop_type == data["agronomic_properties"]["crop_type"]
    assert survey.model_dump()["answers"] == data["answers"]
    assert survey.model_dump()["followups"] == data["followups"]
    assert len(survey.audio_files) == 1
    assert survey.audio_files[0].path == data["audio_files"][0]["path"]


def test_survey_data_w_alias_model_initialization():
    data = {
        "id": str(uuid4()),
        "path": "/surveys/2025/sample_data.json",
        "collection_date": "2025-12-01",
        "trial_properties": {
            "name": "maize_variety_survey_2025"
        },
        "protocol_properties": {
            "name": "crop_survey_v2.0",
        },
        "location_properties": {
            "admin_level_0": "Kenya",
            "site": "Example Site",
            "field": "Field_1B",
            "location": ""
        },
        "agronomic_properties": {
            "crop_type": "corn",
        },
        "answers": {
            "Q1": {"question": "What is the yield?", "answer": "20 tons/ha"}
        },
        "followups": {
            "Q1": {"question": "Why so high?", "answer": "Good rains this season."}
        },
        "voice_files": [
            {"file": "voice_clip.mp3", "audio_id": str(uuid4()), "question": ["Q1"], "answer": [""]}
        ],
        "image_files": [
            {"file": "image_20251201.png", "image_id": str(uuid4()), "question": "Q1"}
        ],
        "notes": [
            {"message": "Investigate field conditions further.", "author": "admin"}
        ]
    }
    survey = SurveyDataModel(**data)
    assert survey.audio_files[0].path == data["voice_files"][0]["file"]


def test_invalid_survey_data_model_missing_required_field():
    with pytest.raises(ValidationError):
        SurveyDataModel(collection_date="2025-12-01", answers={}, followups={}, audio_files=[], image_files=[])


def test_invalid_survey_data_model_extra_field():
    data = {
        "id": str(uuid4()),
        "path": "/surveys/2025/sample_data.json",
        "collection_date": "2025-12-01",
        "answers": {
            "Q1": {"question": "What is the yield?", "answer": "20 tons/ha"}
        },
        "followups": {
            "Q1": {"question": "Why so high?", "answer": "Good rains this season."}
        },
        "audio_files": [],
        "image_files": [],
        "extra_field": "invalid"
    }
    with pytest.raises(ValidationError):
        SurveyDataModel(**data)


def test_valid_survey_notes():
    notes = [{"message": "Added details for later review.", "author": "researcher1"}]
    data = {
        "id": str(uuid4()),
        "path": "sample_data.json",
        "collection_date": "2025-11-20",
        "answers": {},
        "followups": {},
        "audio_files": [],
        "image_files": [],
        "notes": notes
    }
    survey = SurveyDataModel(**data)
    assert survey.notes[0].message == notes[0]["message"]
    assert survey.notes[0].author == notes[0]["author"]
