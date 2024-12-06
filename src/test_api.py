import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock
from .main import app

client = TestClient(app)

test_data = [
    {
        "input_data": {"name": "Contact Form", "f_name1": "test@test.com", "f_name2": "+7 123 456 78 90"},
        "expected_response": {"template_name": "Contact Form"},
    },
    {
        "input_data": {"name": "Feedback Form", "f_name1": "Some feedback", "f_name2": "Other feedback"},
        "expected_response": {"template_name": "Feedback Form"},
    },
    {
        "input_data": {"name": "Registration Form", "f_name1": "2023-10-28", "f_name2": "+7 123 456 78 90"},
        "expected_response": {"template_name": "Registration Form"},
    },
    {
        "input_data": {"name": "Unknown Form", "f_name1": "random", "f_name2": "random"},
        "expected_response": {"f_name1": "text", "f_name2": "text"},
    },
]

@pytest.fixture
def sync_client():
    return client

@pytest.mark.parametrize("test_case", test_data)
def test_get_templates(sync_client, test_case):
    """
    Тестирование эндпоинта /get_form для всех заданных шаблонов.
    """
    response = sync_client.post("/get_form", json=test_case["input_data"])
    assert response.status_code == 200, f"Неожиданный статус-код: {response.status_code}"
    assert response.json() == test_case["expected_response"], (
        f"Ответ API не совпадает с ожидаемым.\n"
        f"Ожидалось: {test_case['expected_response']}\n"
        f"Получено: {response.json()}"
    )
