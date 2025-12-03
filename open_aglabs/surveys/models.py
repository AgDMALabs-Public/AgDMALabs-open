from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from typing import List, Dict, Optional
from open_aglabs.core.base_models import MLOutput, Location, Notes, TrialProperties, AgronomicProperties, ProtocolProperties

class QuestionAnswer(BaseModel):
    """A model to hold a question and its corresponding answer."""
    question: str = Field(
        ...,
        description="The question text.")
    answer: str = Field(
        ...,
        description="The answer text.")
    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "question": "How much yield do you lose because of fall armyworm? Please think back over the last 3 seasons. (Percent or bags per acre are fine.)",
                "answer": "Test, test, test, can you hear me?"
            }
        }
    )


class VoiceFile(BaseModel):
    """A model to represent a voice file and its associated data."""
    path: str = Field(
        ...,
        description="The path to the voice file.")
    id: str = Field(
        ...,
        description="The unique ID of the voice file.")
    question: str = Field(
        ...,
        description="The question associated with the voice file.")
    answer: str = Field(
        ...,
        description="The transcribed answer from the voice file.")
    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "path": "voice_20251126_122230.wav",
                "id": str(uuid4()),
                "question": "Q1",
                "answer": "I would expect it to be more tolerant to drought."
            }
        }
    )

class ImageFile(BaseModel):
    """A model to represent a voice file and its associated data."""
    path: str = Field(
        ...,
        description="The name of the voice file.")
    id: str = Field(
        ...,
        description="The unique ID for the image file")
    question: str = Field(
        ...,
        description="The question associated with the image")
    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "path": "voice_20251126_122230.wav",
                "id": str(uuid4()),
                "question": "Q1",
            }
        }
    )


class SurveyDataModel(BaseModel):
    """A Pydantic model for the provided survey data structure."""
    path: Optional[str] = Field(
        None,
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
    answers: Dict[str, QuestionAnswer] = Field(
        ...,
        description="A dictionary of questions and answers.")
    followups: Dict[str, QuestionAnswer] = Field(
        ...,
        description="A dictionary of followup questions and answers.")
    voice_files: List[VoiceFile] = Field(
        ...,
        description="A list of voice files and their associated data.")
    image_files: List[ImageFile] = Field(
        ...,
        description="A list of image files and their associated data.")
    notes: Optional[List[Notes]] = Field(
        None
    )
    model_config = ConfigDict(
        extra='forbid',
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": str(uuid4()), # required
                "path": "/surveys/2025/kenya_field_xyz.json",
                "collection_date": "2025-11-18", # required
                "trial_properties": {
                    "name": "maize_variety_survey_2025" # required
                },
                "protocol_properties": {
                    "name": "maize_survey_v1.0", # required
                    "id": None,
                    "url": None,
                },
                "location_properties": {
                    "id": "loc-uuid-12345",
                    "name": "Research Plot A",
                    "latitude": 0.78,
                    "longitude": 35.2,
                    "admin_level_0": "Kenya", # required
                    "site": "CIMMYT-Kiboko", # required
                    "grower": "local_farmer_coop",
                    "field": "EF-3", # required
                    "location": "" # required
                },
                "agronomic_properties": {
                    "crop_type": "corn", # required
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
                        "answer": "Around 10 percent."
                    },
                    "Q2": {
                        "question": "What are the most important traits for a new maize variety?",
                        "answer": "Drought tolerance is number one, and good husk cover."
                    }
                },
                "followups": {
                    "Q2": {
                        "question": "Why is drought tolerance so critical in this area?",
                        "answer": "The rains have become less predictable over the last five years."
                    }
                },
                "voice_files": [
                    {
                        "path": "voice_20251118_103000.mp3",
                        "id": str(uuid4()),
                        "question": "Q1",
                        "answer": ""
                    }
                ],
                "image_files": [
                    {
                        "path": "voice_20251118_103000.jpg",
                        "id": str(uuid4()),
                        "question": "Q1"
                    }
                ],
                "notes": [
                    {
                        "message": "The farmer was interrupted multiple times during the survey.",
                        "author": "survey_agent_01"
                    }
                ]
            }
        }
    )

