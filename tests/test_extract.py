from fastapi.testclient import TestClient
from docgen.main import app

client = TestClient(app)


def test_extracts_known_skills():
    payload = client.post("/extract", json={"text": 'This endpoint applies a timeout and a retry. Auth is required.'}).json()
    assert "timeout" in payload["skills"]


def test_empty_is_refused():
    assert client.post("/extract", json={"text": ""}).status_code == 422
