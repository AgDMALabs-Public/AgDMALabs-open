from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import List, Dict, Optional, Union, Literal

from open_aglabs.core.base_models import MLOutput, Location, Notes, TrialProperties, AgronomicProperties, \
    ProtocolProperties, CollectionProperties
from open_aglabs.core.constants import MEDIA_TYPE_LIST, ANSWER_STATUS_LIST


class ProcessingMetrics(BaseModel):
    """
    A model to track the metrics of an automated processing task.
    """
    model: Optional[str] = Field(
        None,
        description="The identifier of the model used for processing."
    )
    confidence: Optional[float] = Field(
        None,
        description="The confidence score of the processing result."
    )
    status: Optional[str] = Field(
        None,
        description="The current status of the processing task (e.g., 'pending', 'completed', 'failed')."
    )
    attempts: Optional[int] = Field(
        None,
        description="The number of attempts made to process the task."
    )
    errors: Optional[List[str]] = Field(
        None,
        description="A list of error messages encountered during processing."
    )
    model_version: Optional[Union[str, float, int]] = Field(
        None,
        description="The version of the model used for processing."
    )
    language: Optional[str] = Field(
        None,
        description="The language of the processing output, as a BCP-47 tag. "
                    "EX: the language a voice file was transcribed into."
    )

    model_config = ConfigDict(
        extra='forbid'
    )


class SimpleAssociatedSurveyFile(BaseModel):
    """A model to represent a voice file and its associated data."""
    path: Optional[str] = Field(
        None,
        validation_alias=AliasChoices('path', 'file'),
        description="The name of the voice file.")
    id: Optional[str] = Field(
        None,
        validation_alias=AliasChoices('id', 'image_id', 'audio_id'),
        description="The unique ID for the image file")
    media_type: Optional[Literal[*MEDIA_TYPE_LIST]] = Field(
        None,
        description="The type of media being attached"
    )
    processing_metrics: Optional[ProcessingMetrics] = Field(
        None,
        description="The processing metrics for the media"
    )
    answer: Optional[str] = Field(
        None,
        description="The text derived from this file. EX: the transcribed answer from a voice file."
    )
    mime_type: Optional[str] = Field(
        None,
        description="The IANA media type of the file. EX: audio/wav, video/mp4, image/jpeg."
    )
    duration_s: Optional[float] = Field(
        None,
        ge=0,
        description="The duration of the file in seconds, for time-based media."
    )
    file_size: Optional[int] = Field(
        None,
        ge=0,
        description="The size of the file in bytes."
    )
    original_filename: Optional[str] = Field(
        None,
        description="The filename as supplied by the capturing device."
    )
    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "path": "voice_20251126_122230.wav",
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "media_type": "audio",
                "mime_type": "audio/wav",
                "duration_s": 42.5,
                "file_size": 680000,
                "original_filename": "voice_20251126_122230.wav",
                "answer": "Around 10 percent.",
                "processing_metrics": {
                    "model": "transcription-model-v2",
                    "model_version": "2.1.0",
                    "confidence": 0.985,
                    "status": "completed",
                    "attempts": 1,
                    "errors": [],
                    "language": "sw"
                }
            }
        }
    )


class AssociatedSurveyFile(SimpleAssociatedSurveyFile):
    """A model to represent a voice file and its associated data."""
    path: str = Field(
        ...,
        validation_alias=AliasChoices('path', 'file'),
        description="The name of the voice file.")
    id: str = Field(
        ...,
        validation_alias=AliasChoices('id', 'image_id', 'audio_id'),
        description="The unique ID for the image file")
    question_id: Optional[Union[List[str], str]] = Field(
        None,
        description="The question(s) ID's associated with the voice file.")
    question: Optional[Union[List[str], str]] = Field(
        None,
        description="The question associated with the image")
    answer: Optional[Union[List[str], str]] = Field(
        None,
        description="The transcribed answer from the voice file.")
    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "path": "voice_20251126_122230.wav",
                "id": str(uuid4()),
                "media_type": "audio",
                "processing_metrics": {
                    "model": "transcription-model-v2",
                    "confidence": 0.985,
                    "status": "completed",
                    "attempts": 1,
                    "errors": []
                },
                "question_id": "Q1",
                "question": "What is the yield?",
                "answer": "100 bushels"
            }
        }
    )


class QuestionAnswer(BaseModel):
    """A model to hold a question and its corresponding answer."""
    question: str = Field(
        ...,
        description="The question text.")
    answer: Optional[str] = Field(
        None,
        description="The answer text. May be absent when the question was not answered; see status.")
    question_key: Optional[str] = Field(
        None,
        description="A standardized key associated with the questions. EX: if the question is about the fertilizer plan"
                    ", the the key could be fertilizer_management.")
    status: Optional[Literal[*ANSWER_STATUS_LIST]] = Field(
        None,
        description="Why an answer is present or absent. Omit when an answer is given and no "
                    "distinction is needed.")
    language: Optional[str] = Field(
        None,
        description="The language of this question and answer, as a BCP-47 tag, if it differs "
                    "from the record.")
    audio: Optional[List[SimpleAssociatedSurveyFile]] = Field(
        None,
        description="The audio file associated with the answer.")
    image: Optional[List[SimpleAssociatedSurveyFile]] = Field(
        None,
        description="Any Images associated with the answer.")

    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "question": "How much yield do you lose because of fall armyworm? Please think back over the last 3 seasons. (Percent or bags per acre are fine.)",
                "answer": "Test, test, test, can you hear me?",
                "question_key": "fall_armyworm_yield_loss",
                "status": "answered",
                "language": "en",
                "audio": [
                    {
                        "path": "voice_20251126_122230.wav",
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "media_type": "audio",
                        "processing_metrics": {
                            "model": "transcription-model-v2",
                            "confidence": 0.985,
                            "status": "completed",
                            "attempts": 1,
                            "errors": []
                        }
                    }
                ],
                "image": [
                    {
                        "path": "survey_image_20251126.jpg",
                        "id": "550e8400-e29b-41d4-a716-446655440001",
                        "media_type": "image",
                        "processing_metrics": {
                            "model": "object-detection-v1",
                            "confidence": 0.95,
                            "status": "completed",
                            "attempts": 1,
                            "errors": []
                        }
                    }
                ]
            }
        }
    )


class SurveyDataModel(BaseModel):
    """A Pydantic model for the provided survey data structure."""
    path: str = Field(
        ...,
        description="The path to the image"
    )
    id: str = Field(
        ...,
        validation_alias=AliasChoices('image_id', 'id'),
        description="The Unique ID of the image, should be the image name, by default UUID4."
    )
    collection_date: str = Field(
        ...,
        description="The date the survey was collected."
    )
    trial_properties: Optional[TrialProperties] = Field(
        None
    )
    protocol_properties: Optional[ProtocolProperties] = Field(
        None
    )
    location_properties: Optional[Location] = Field(
        None
    )
    agronomic_properties: Optional[AgronomicProperties] = Field(
        None
    )
    collection_properties: Optional[CollectionProperties] = Field(
        None,
        description="Collection level information for the survey session."
    )
    language: Optional[str] = Field(
        None,
        description="The primary language of the survey content, as a BCP-47 tag. EX: en, sw, fr-CA."
    )
    complete: Optional[bool] = Field(
        None,
        description="Whether the survey was completed. False when it was abandoned part way."
    )
    answers: Dict[str, QuestionAnswer] = Field(
        ...,
        description="A dictionary of questions and answers.")
    followups: Optional[Dict[str, QuestionAnswer]] = Field(
        None,
        description="A dictionary of followup questions and answers.")
    audio_files: Optional[List[AssociatedSurveyFile]] = Field(
        None,
        validation_alias=AliasChoices('audio_files', 'voice_files'),
        description="A list of voice files and their associated data.")
    image_files: Optional[List[AssociatedSurveyFile]] = Field(
        None,
        description="A list of image files and their associated data.")
    notes: Optional[List[Notes]] = Field(
        None
    )
    model_config = ConfigDict(
        extra='forbid',
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": str(uuid4()),  # required
                "path": "/surveys/2025/kenya_field_xyz.json",
                "collection_date": "2025-11-18",  # required
                "language": "en",
                "complete": True,
                "trial_properties": {
                    "name": "maize_variety_survey_2025"  # required
                },
                "protocol_properties": {
                    "name": "maize_survey_v1.0",  # required
                    "id": None,
                    "url": None,
                },
                "location_properties": {
                    "id": "loc-uuid-12345",
                    "name": "Research Plot A",
                    "latitude": 0.78,
                    "longitude": 35.2,
                    "admin_level_0": "Kenya",  # required
                    "site": "CIMMYT-Kiboko",  # required
                    "grower": "local_farmer_coop",
                    "field": "EF-3",  #
                    "location": ""  # required
                },
                "agronomic_properties": {
                    "crop_type": "corn",  # required
                    "growth_stage": "VT",
                    "soil_color": "red",
                    "weed_pressure": "medium-low",
                    "irrigation_level": "standard",
                    "tillage_type": "conventional",
                    "fertilizer_level": "standard"
                },
                "answers": {
                    "Q1": {
                        "question": "What percentage of yield loss do you attribute to stem borer?",
                        "answer": "Around 10 percent.",
                        "audio": [
                            {
                                "path": "voice_20251118_103000.mp3",
                                "id": str(uuid4())
                            }
                        ],
                        "image": [
                            {
                                "path": "stem_borer_damage.jpg",
                                "id": str(uuid4())
                            }
                        ]
                    },
                    "Q2": {
                        "question": "What are the most important traits for a new maize variety?",
                        "answer": "Drought tolerance is number one, and good husk cover."
                    }
                },
                "followups": {
                    "Q2": {
                        "question": "Why is drought tolerance so critical in this area?",
                        "answer": "The rains have become less predictable over the last five years.",
                        "audio": [
                            {
                                "path": "followup_q2_voice.mp3",
                                "id": str(uuid4())
                            }
                        ]
                    }
                },
                "notes": [
                    {
                        "message": "The farmer was interrupted multiple times during the survey.",
                        "author": "survey_agent_01"
                    }
                ]
            }
        }
    )
