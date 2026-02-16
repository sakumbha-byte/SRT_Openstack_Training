from jsonschema import validate
from jsonschema.exceptions import ValidationError

employee_create_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "maxLength": 256},
        "gender": {"type": "string", "enum": ["Male", "Female", "Other"]},
        "position": {"type": "string", "maxLength": 56},
        "salary": {"type": "number", "minimum": 0},
        "experience": {"type": "integer", "minimum": 0},
        "birth_date": {"type": "string"}
    },
    "required": ["name"],
    "additionalProperties": False
}

employee_update_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "maxLength": 256},
        "gender": {"type": "string", "enum": ["Male", "Female", "Other"]},
        "position": {"type": "string", "maxLength": 56},
        "salary": {"type": "number", "minimum": 0},
        "experience": {"type": "integer", "minimum": 0}
    },
    "additionalProperties": False
}


def validate_create(data):
    try:
        validate(instance=data, schema=employee_create_schema)
    except ValidationError as e:
        raise ValueError(f"Create Validation Error: {e.message}")


def validate_update(data):
    try:
        validate(instance=data, schema=employee_update_schema)
    except ValidationError as e:
        raise ValueError(f"Update Validation Error: {e.message}")
