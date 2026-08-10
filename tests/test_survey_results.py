from uuid import uuid4

import pytest
from open_aglabs.surveys.results_models import (
    SurveyAnnotation,
    SurveyResultsStandardization,
    SurveyTopic,
)
from pydantic import ValidationError


def _results_payload(survey_id):
    return {
        "schema_name": "SurveyResultsStandardization",
        "survey_ids": [survey_id],
        "annotations": [
            {
                "annotation_name": "drought tolerance",
                "standardized_annotation_name": "drought_tolerance",
                "annotation_type": "trait",
                "subject": "Lyamungu 90",
                "survey_id": survey_id,
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
                    "ontology_id": "CO_335:0000123",
                },
                "ml_output": {
                    "pred": "drought tolerance",
                    "confidence": 0.91,
                    "model_id": "entity-extraction",
                    "model_version": "entity_v1",
                },
            }
        ],
        "topics": [
            {"topic_id": "t-01", "label": "agronomy", "member_count": 402},
            {
                "topic_id": "t-04",
                "label": "drought and water stress",
                "parent_topic_id": "t-01",
                "keywords": ["drought", "rain", "ukame"],
                "member_count": 118,
            },
        ],
    }


def test_survey_results_standardization_initialization():
    survey_id = str(uuid4())
    data = _results_payload(survey_id)
    results = SurveyResultsStandardization(**data)
    assert results.schema_name == "SurveyResultsStandardization"
    assert results.survey_ids == [survey_id]
    annotation = results.annotations[0]
    assert annotation.annotation_name == "drought tolerance"
    assert annotation.ontology_term.ontology_id == "CO_335:0000123"
    assert annotation.ml_output.model_version == "entity_v1"
    assert annotation.sentiment_score == 0.8


def test_survey_results_round_trip():
    """The document survives serialization, including the topic hierarchy."""
    data = _results_payload(str(uuid4()))
    results = SurveyResultsStandardization(**data)
    round_tripped = SurveyResultsStandardization.model_validate_json(results.model_dump_json())
    assert round_tripped.topics[1].parent_topic_id == "t-01"
    assert round_tripped.annotations[0].topic_id == "t-04"


def test_survey_annotation_allows_producer_specific_fields():
    """Producers may attach their own fields to an annotation, as PlantAnnotation allows."""
    annotation = SurveyAnnotation(
        annotation_name="drought tolerance",
        annotation_type="trait",
        emotion="hope",
        respondent_gender="female",
        phrase_source="inavumilia ukame",
    )
    dumped = annotation.model_dump()
    assert dumped["emotion"] == "hope"
    assert dumped["respondent_gender"] == "female"
    assert dumped["phrase_source"] == "inavumilia ukame"


def test_survey_annotation_requires_a_name():
    with pytest.raises(ValidationError):
        SurveyAnnotation(annotation_type="trait")


def test_survey_annotation_sentiment_score_is_bounded():
    with pytest.raises(ValidationError):
        SurveyAnnotation(annotation_name="drought tolerance", sentiment_score=1.5)


def test_corpus_level_annotation_omits_survey_id():
    """An annotation about the result set as a whole has no source record."""
    annotation = SurveyAnnotation(annotation_name="drought", annotation_type="topic")
    assert annotation.survey_id is None


def test_survey_results_rejects_unknown_field():
    """The container stays strict even though annotations are extensible."""
    data = _results_payload(str(uuid4()))
    data["extra_field"] = "invalid"
    with pytest.raises(ValidationError):
        SurveyResultsStandardization(**data)


def test_survey_results_rejects_wrong_schema_name():
    data = _results_payload(str(uuid4()))
    data["schema_name"] = "PlantAnnotationStandardization"
    with pytest.raises(ValidationError):
        SurveyResultsStandardization(**data)


def test_survey_topic_hierarchy():
    parent = SurveyTopic(topic_id="t-01", label="agronomy")
    child = SurveyTopic(topic_id="t-04", label="drought", parent_topic_id=parent.topic_id)
    assert child.parent_topic_id == "t-01"
    assert parent.parent_topic_id is None
