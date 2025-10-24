import pandas as pd
from .base_models import Location


def dict_to_model(data: dict, model_class):
    """Extract fields using both field names and aliases."""
    valid_keys = set()

    # Collect both field names and their aliases
    for field_name, field_info in model_class.model_fields.items():
        valid_keys.add(field_name)  # Add the actual field name
        if field_info.alias:
            valid_keys.add(field_info.alias)  # Add the alias if it exists

    # Filter the dict to only include valid keys
    filtered_data = {k: v for k, v in data.items() if k in valid_keys}

    return model_class(**filtered_data)

