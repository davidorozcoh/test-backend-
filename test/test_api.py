import pytest
import json
from jsonschema import validate, ValidationError

file_path = "data.json"

with open(file_path, 'r', encoding='utf-8') as f:
    response_json = json.load(f)

expected_json_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "identificación": {"type": "integer"},
            "nombre": {"type": "string"},
            "dirección": {"type": "string"},
            "código postal": {"type": "string"},
            "país": {"type": "string"},
            "número de empleados": {"type": "integer"},
            "industria": {"type": "string"},
            "capitalización de mercado": {"type": "integer"},
            "dominio": {"type": "string"},
            "logotipo": {"type": "string", "format": "uri"},
            "ceoName": {"type": "string"},
            "nombredelceo": {"type": "string"},
            "nombredeldirector": {"type": "string"},
            "nombre del director ejecutivo": {"type": "string"}
        },
        "required": [
            "identificación", "nombre", "dirección", "código postal",
            "país", "número de empleados", "industria",
            "capitalización de mercado", "dominio", "logotipo"
        ]
    }
}

def test_validate_json_schema():
    try:
        validate(instance=response_json, schema=expected_json_schema)
        print("JSON structure is correct and matches the schema.")
    except ValidationError as e:
        print(f"ERROR: Response does not match expected JSON schema. Details: {e.message}")
        pytest.fail(f"Response does not match expected JSON schema: {e.message}")
