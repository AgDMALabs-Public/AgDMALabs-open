from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ApplicationEvent(BaseModel):
    """
    Represents a single application event (e.g., fertilizer, pesticide, herbicide).
    """
    event_id: str = Field(
        ...,
        alias="eventId",
        description="Unique identifier for this specific application event.",
        examples=["APP-2025-FIELD-A-002"]
    )
    timestamp: datetime = Field(
        ...,
        description="The date and time the application occurred."
    )
    application_type: str = Field(
        ...,
        alias="applicationType",
        description="The type of application (e.g., 'Fertilizer', 'Herbicide', 'Fungicide', 'Insecticide').",
        examples=["Herbicide"]
    )
    product_name: str = Field(
        ...,
        alias="productName",
        description="The name of the product applied.",
        examples=["Roundup PowerMAX"]
    )
    application_rate: float = Field(
        ...,
        alias="applicationRate",
        ge=0,
        description="The rate at which the product was applied.",
        examples=[2.5]
    )
    rate_unit: str = Field(
        ...,
        alias="rateUnit",
        description="The unit for the application rate (e.g., 'L/ha', 'gal/acre', 'kg/ha').",
        examples=["L/ha"]
    )
    method: Optional[str] = Field(
        None,
        description="The method of application (e.g., 'Broadcast', 'Foliar', 'In-furrow', 'Side-dress').",
        examples=["Foliar"]
    )
    equipment: Optional[str] = Field(
        None,
        description="The equipment used for the application.",
        examples=["Sprayer"]
    )
    notes: Optional[str] = Field(
        None,
        description="Any additional notes about the application event."
    )

    class ConfigDict:
        extra = "forbid"
        validate_by_name = True  # Allow population using 'class' or 'class_name'
        json_schema_extra = {
            "example": {
                "eventId": "APP-2025-FIELD-A-002",
                "timestamp": "2025-05-15T10:30:00Z",
                "applicationType": "Herbicide",
                "productName": "Glyphosate 41%",
                "applicationRate": 2.0,
                "rateUnit": "L/ha",
                "method": "Broadcast",
                "equipment": "Tractor Sprayer",
                "notes": "Post-emergent herbicide application on weeds."
            }
        }