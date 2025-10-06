from typing import Optional, Literal, List
from pydantic import BaseModel, Field, ConfigDict

from ..core.constants import AMOUNT_UNITS, RATE_UNITS

class SimpleProduct(BaseModel):
    product_id: str = Field(
        ...,
        description="Unique identifier for this product."
    )
    product_name: str = Field(
        ...,
        description="Name of the product."
    )
    amount: float = Field(
        ...,
        description="Amount of the product."
    )
    amount_units: Literal[*AMOUNT_UNITS] = Field(

    )
    rate: Optional[float] = Field(
        None,
        description="Rate of the product."
    )
    rate_units: Optional[Literal[*RATE_UNITS]] = Field(
        None,
        description="Units of the rate."
    )
    ratio: Optional[float] = Field(
        None,
        ge=0,
        le=100,
        description="Ratio of the product."
    )



class TankMix(BaseModel):
    id: str = Field(
        ...,
        description="Unique identifier for this tank mix."
    )
    name: str = Field(
        ...,
        description="Name of the tank mix."
    )
    mix_content: List[SimpleProduct] = Field(
        ...,
        description="List of products in the tank mix."
    )