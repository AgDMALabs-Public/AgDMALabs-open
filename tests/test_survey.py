from uuid import uuid4

import pytest
from open_aglabs.surveys.models import SurveyDataModel, QuestionAnswer, \
    AssociatedSurveyFile, SimpleAssociatedSurveyFile
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
                   'question_key': None,
                   'status': None,
                   'language': None,
                   "audio": [{"path": "voice_clip.mp3",
                              'media_type': 'audio',
                              "id": str(uuid4()),
                              'processing_metrics': {
                                  "model": "voice-v1",
                                  "confidence": 0.95,
                                  "status": "completed",
                                  "attempts": 1,
                                  "errors": [],
                                  "model_version": None,
                                  "language": None
                              },
                              'answer': None,
                              'mime_type': None,
                              'duration_s': None,
                              'file_size': None,
                              'original_filename': None
                              }],
                   "image": [{"path": "image_20251201.png",
                              'media_type': 'image',
                              "id": str(uuid4()),
                              'processing_metrics': {
                                  "model": "object-detection-v1",
                                  "confidence": 0.95,
                                  "status": "completed",
                                  "attempts": 1,
                                  "errors": [],
                                  "model_version": None,
                                  "language": None
                              },
                              'answer': None,
                              'mime_type': None,
                              'duration_s': None,
                              'file_size': None,
                              'original_filename': None
                              }]
                   }
        },
        "followups": {
            "Q1": {"question": "Why so high?",
                   'question_key': None,
                   'status': None,
                   'language': None,
                   "answer": "Good rains this season.",
                   "audio": None,
                   "image": None}
        },
        "audio_files": [
            {"path": "voice_clip.mp3",
             "id": str(uuid4()),
             "media_type": 'audio',
             "question_id": ["Q1"],
             "question": ["Q1"],
             "answer": [""]}
        ],
        "image_files": [
            {"path": "image_20251201.png",
             "media_type": 'image',
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


def test_survey_media_record_fields():
    """A media file carries its own derived text and file metadata."""
    data = {
        "id": str(uuid4()),
        "path": "/surveys/2025/sample_data.json",
        "collection_date": "2025-12-01",
        "language": "sw",
        "complete": True,
        "answers": {
            "Q1": {
                "question": "Unapendelea aina gani ya maharage?",
                "answer": "Lyamungu 90",
                "language": "sw",
                "audio": [{
                    "path": "voice_clip.wav",
                    "id": str(uuid4()),
                    "media_type": "audio",
                    "mime_type": "audio/wav",
                    "duration_s": 42.5,
                    "file_size": 680000,
                    "original_filename": "rec_0031.wav",
                    "answer": "Lyamungu 90 kwa sababu inavumilia ukame",
                    "processing_metrics": {
                        "model": "multimodal_chat:gemini-2.0-flash",
                        "model_version": "2026-06-01",
                        "confidence": 0.94,
                        "status": "completed",
                        "attempts": 1,
                        "errors": [],
                        "language": "sw"
                    }
                }]
            }
        }
    }
    survey = SurveyDataModel(**data)
    clip = survey.answers["Q1"].audio[0]
    assert clip.answer == "Lyamungu 90 kwa sababu inavumilia ukame"
    assert clip.mime_type == "audio/wav"
    assert clip.duration_s == 42.5
    assert clip.processing_metrics.language == "sw"
    assert clip.processing_metrics.model_version == "2026-06-01"
    assert survey.language == "sw"
    assert survey.complete is True


def test_survey_video_media_type():
    """Video is a first-class capture type and needs a media_type value."""
    file = SimpleAssociatedSurveyFile(
        path="clip.mp4", id=str(uuid4()), media_type="video", mime_type="video/mp4")
    assert file.media_type == "video"


def test_survey_answer_status_without_answer():
    """A question that was asked but not answered is representable."""
    qa = QuestionAnswer(question="Umri wako?", status="skipped", language="sw")
    assert qa.answer is None
    assert qa.status == "skipped"


def test_survey_invalid_answer_status():
    with pytest.raises(ValidationError):
        QuestionAnswer(question="Umri wako?", status="not_a_status")


def test_associated_survey_file_requires_path_and_id():
    """A record-level file entry must identify a file."""
    with pytest.raises(ValidationError):
        AssociatedSurveyFile(question="What is the yield?", answer="20 t/ha")


def test_survey_collection_and_protocol_properties():
    """Collection metadata and questionnaire version have a home."""
    data = {
        "id": str(uuid4()),
        "path": "/surveys/2025/sample_data.json",
        "collection_date": "2025-12-01",
        "protocol_properties": {"name": "crop_survey_v2.0", "version": "2.1.0"},
        "collection_properties": {
            "username": "enumerator_042",
            "start_datetime": "2025-12-01T09:14:00Z",
            "end_datetime": "2025-12-01T09:41:00Z",
        },
        "location_properties": {"latitude": -3.38, "longitude": 36.7, "accuracy_m": 4.8},
        "answers": {"Q1": {"question": "What is the yield?", "answer": "20 tons/ha"}},
    }
    survey = SurveyDataModel(**data)
    assert survey.protocol_properties.version == "2.1.0"
    assert survey.collection_properties.username == "enumerator_042"
    assert survey.location_properties.accuracy_m == 4.8
