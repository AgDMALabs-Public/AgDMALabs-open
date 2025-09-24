from typing import List, Dict, Any, Literal, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field, conlist

class PointGeometry(BaseModel):
    """Represents a GeoJSON Point geometry."""
    type: Literal["Point"] = "Point"
    # Coordinates are [longitude, latitude, optional_elevation]
    coordinates: conlist(float, min_length=2, max_length=3) = Field(
        ...,
        description="Coordinates of the point [longitude, latitude, optional elevation]."
    )

# 2. Properties for our Yield Feature
class YieldProperties(BaseModel):
    """Properties associated with a single yield measurement."""
    timestamp: datetime = Field(..., description="Timestamp of the yield measurement.")
    yield_value: float = Field(..., ge=0, description="Measured yield value (e.g., kg/hectare).")
    unit: str = Field(..., description="Unit of the yield value (e.g., 'kg/ha', 'bu/acre').")
    # You can add more specific yield-related fields here
    crop_type: Optional[str] = Field(None, description="Type of crop.")
    moisture_content: Optional[float] = Field(None, ge=0, description="Moisture content of the yield.")
    # Add any other relevant attributes for your yield data here

# 3. GeoJSON Feature for a single Yield Measurement
class YieldFeature(BaseModel):
    """Represents a single yield measurement as a GeoJSON Feature."""
    type: Literal["Feature"] = "Feature"
    geometry: PointGeometry = Field(..., description="The geographical point of the measurement.")
    properties: YieldProperties = Field(..., description="Attributes of the yield measurement.")
    # GeoJSON spec allows an optional 'id' field for features
    id: Optional[Union[str, int]] = None

# 4. GeoJSON FeatureCollection for all Yield Data
class GeoJsonYieldData(BaseModel):
    """
    A collection of yield measurements represented as a GeoJSON FeatureCollection.
    This is the primary model for your overall yield dataset.
    """
    type: Literal["FeatureCollection"] = "FeatureCollection"
    features: conlist(YieldFeature, min_length=1) = Field(
        ...,
        description="A list of GeoJSON Features, each representing a yield measurement."
    )
    # Optional metadata for the entire collection
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description="Optional metadata for the entire yield data collection (e.g., source, processing date)."
    )
