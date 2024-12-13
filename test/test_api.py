import pytest
import requests
from jsonschema import validate, ValidationError

url = "https://fake-json-api.mock.beeceptor.com/companies"

expected_json_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "address": {"type": "string"},
            "zip": {"type": "string"},
            "country": {"type": "string"},
            "employeeCount": {"type": "integer"},
            "industry": {"type": "string"},
            "marketCap": {"type": "integer"},
            "domain": {"type": "string"},
            "logo": {"type": "string", "format": "uri"},
            "ceoName": {"type": "string"},
            "ceoFullName": {"type": "string"},
            "directorName": {"type": "string"},
            "executiveDirectorName": {"type": "string"}
        },
        "required": [
            "id", "name", "address", "zip",
            "country", "employeeCount", "industry",
            "marketCap", "domain", "logo"
        ]
    }
}

def test_validate_json_schema():
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
    else:
        pytest.fail(f"Request to {url} failed with status code {response.status_code}")
    try:
        validate(instance=response_json, schema=expected_json_schema)
        print("JSON structure is correct and matches the schema.")
    except ValidationError as e:
        print(f"ERROR: Response does not match expected JSON schema. Details: {e.message}")
        pytest.fail(f"Response does not match expected JSON schema: {e.message}")
