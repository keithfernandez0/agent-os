from typing import Dict, Any
import pydantic

class ValidationException(Exception):
    """Raised when SOP validation fails."""
    pass

def validate_dict(data: Dict[str, Any], schema_model: pydantic.BaseModel) -> pydantic.BaseModel:
    """Validate a dictionary against a Pydantic model"""
    try:
        return schema_model(**data)
    except pydantic.ValidationError as e:
        raise ValidationException(f"[ERROR] Validation failed: {e}")
