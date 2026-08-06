from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Literal

from open_aglabs.core.base_models import MLOutput, OntologyTerm


class SurveyTopic(BaseModel):
    """
    A group of related annotations discovered across a set of survey responses.

    Topics describe the result set as a whole rather than any one survey record,
    which is why they sit alongside the annotations rather than inside them.
    """
    topic_id: str = Field(
        ...,
        description="The unique ID for the topic within this result set."
    )
    label: Optional[str] = Field(
        None,
        description="A short human readable label for the topic."
    )
    description: Optional[str] = Field(
        None,
        description="A longer description of what the topic covers."
    )
    keywords: Optional[List[str]] = Field(
        None,
        description="The terms most characteristic of the topic."
    )
    parent_topic_id: Optional[str] = Field(
        None,
        description="The ID of the parent topic, for hierarchical schemes."
    )
    member_count: Optional[int] = Field(
        None,
        ge=0,
        description="The number of annotations assigned to this topic."
    )
    ml_output: Optional[MLOutput] = Field(
        None,
        description="The model provenance for the topic."
    )
    notes: Optional[str] = Field(
        None,
        description="Any additional notes about the topic."
    )
    model_config = ConfigDict(
        extra='allow',
        json_schema_extra={
            "example": {
                "topic_id": "t-04",
                "label": "drought and water stress",
                "description": "Responses concerning rainfall reliability and drought.",
                "keywords": ["drought", "rain", "water", "ukame"],
                "parent_topic_id": "t-01",
                "member_count": 118
            }
        }
    )


class SurveyAnnotation(BaseModel):
    """
    A structured finding derived from a survey response.

    Annotations are produced by analysing the text of an answer, whether that
    text was typed, transcribed from a voice file, or captured in an interview.
    An annotation that describes the result set as a whole rather than a single
    response leaves survey_id unset.
    """
    annotation_name: str = Field(
        ...,
        description="The label for what was found. EX: drought tolerance"
    )
    standardized_annotation_name: Optional[str] = Field(
        None,
        description="The name of the standardized annotation, that can be matched to a db "
                    "for reference"
    )
    annotation_type: Optional[str] = Field(
        None,
        description="The kind of annotation. Free text so that each domain can define its own; "
                    "see SURVEY_ANNOTATION_TYPE_LIST for recommended values. "
                    "EX: trait, topic, constraint, practice."
    )
    subject: Optional[str] = Field(
        None,
        description="The entity the annotation is about, where the response names one. "
                    "EX: a variety, product or practice."
    )
    survey_id: Optional[str] = Field(
        None,
        description="The ID of the SurveyDataModel record this annotation was derived from. "
                    "Omit for annotations that describe the result set as a whole."
    )
    question_id: Optional[str] = Field(
        None,
        description="The key of the answer in SurveyDataModel.answers this annotation was "
                    "derived from."
    )
    question_key: Optional[str] = Field(
        None,
        description="The question_key of the answer this annotation was derived from."
    )
    evidence: Optional[str] = Field(
        None,
        description="The verbatim text from the response that supports this annotation."
    )
    evidence_verified: Optional[bool] = Field(
        None,
        description="Whether the evidence was confirmed to appear verbatim in the source response."
    )
    language: Optional[str] = Field(
        None,
        description="The language of the annotation and its evidence, as a BCP-47 tag."
    )
    sentiment: Optional[str] = Field(
        None,
        description="The sentiment expressed toward the subject. "
                    "EX: positive, negative, neutral, mixed."
    )
    sentiment_score: Optional[float] = Field(
        None,
        ge=-1.0,
        le=1.0,
        description="The sentiment as a signed score, from -1.0 to 1.0."
    )
    topic_id: Optional[str] = Field(
        None,
        description="The ID of the SurveyTopic this annotation was assigned to, where topic "
                    "modelling was used."
    )
    ontology_term: Optional[OntologyTerm] = Field(
        None,
        description="The ontology term this annotation maps to."
    )
    ml_output: Optional[MLOutput] = Field(
        None,
        description="The model provenance and confidence for this annotation."
    )
    notes: Optional[str] = Field(
        None,
        description="Any additional notes about the annotation."
    )
    model_config = ConfigDict(
        extra='allow',
        json_schema_extra={
            "example": {
                "annotation_name": "drought tolerance",
                "standardized_annotation_name": "drought_tolerance",
                "annotation_type": "trait",
                "subject": "Lyamungu 90",
                "survey_id": "550e8400-e29b-41d4-a716-446655440000",
                "question_id": "Q2",
                "question_key": "variety_preference_reason",
                "evidence": "...kwa sababu inavumilia ukame",
                "evidence_verified": True,
                "language": "sw",
                "sentiment": "positive",
                "sentiment_score": 0.8,
                "topic_id": "t-04",
                "ontology_term": {
                    "common_name": "drought tolerance",
                    "ontology_source": "https://cropontology.org",
                    "ontology_name": "drought tolerance",
                    "ontology_id": "CO_335:0000123"
                },
                "ml_output": {
                    "pred": "drought tolerance",
                    "confidence": 0.91,
                    "model_id": "entity-extraction",
                    "model_version": "entity_v1"
                }
            }
        }
    )


class SurveyResultsStandardization(BaseModel):
    """
    A set of structured findings derived from one or more survey records.
    """
    schema_name: Literal["SurveyResultsStandardization"] = Field(
        ...,
        description="The name of the schema"
    )
    survey_ids: Optional[List[str]] = Field(
        None,
        description="The IDs of the SurveyDataModel records these results were derived from."
    )
    annotations: List[SurveyAnnotation] = Field(
        ...,
        description="The annotations extracted from the survey responses."
    )
    topics: Optional[List[SurveyTopic]] = Field(
        None,
        description="The topics referenced by the annotations, where topic modelling was used."
    )
    model_config = ConfigDict(
        extra='forbid',
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "schema_name": "SurveyResultsStandardization",
                "survey_ids": ["550e8400-e29b-41d4-a716-446655440000"],
                "annotations": [
                    {
                        "annotation_name": "drought tolerance",
                        "annotation_type": "trait",
                        "subject": "Lyamungu 90",
                        "survey_id": "550e8400-e29b-41d4-a716-446655440000",
                        "question_id": "Q2",
                        "evidence": "...kwa sababu inavumilia ukame",
                        "language": "sw",
                        "sentiment": "positive",
                        "topic_id": "t-04",
                        "ontology_term": {
                            "common_name": "drought tolerance",
                            "ontology_source": "https://cropontology.org",
                            "ontology_id": "CO_335:0000123"
                        }
                    },
                    {
                        "annotation_name": "poor germination",
                        "annotation_type": "constraint",
                        "survey_id": "550e8400-e29b-41d4-a716-446655440000",
                        "question_id": "Q3",
                        "evidence": "mbegu nyingi hazikuota",
                        "language": "sw",
                        "sentiment": "negative",
                        "sentiment_score": -0.6
                    }
                ],
                "topics": [
                    {
                        "topic_id": "t-04",
                        "label": "drought and water stress",
                        "keywords": ["drought", "rain", "ukame"],
                        "member_count": 118
                    }
                ]
            }
        }
    )
