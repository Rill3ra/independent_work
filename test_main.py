# test_main.py

from fastapi.testclient import TestClient
from main import app, format_text_logic # Импортируем app и основную логику

# Создаем тестовый клиент
client = TestClient(app)

# Тест основной функции логики (Unit Test)
def test_format_text_logic():
    input_str = "HeLlO wOrLd"
    expected_output = "hElLo WoRlD"
    assert format_text_logic(input_str) == expected_output

# Тест конечной точки API (Integration Test)
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Text Formatting Service is running"

def test_format_endpoint_success():
    payload = {"text": "TestString"}
    response = client.post("/format", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["original_text"] == "TestString"
    assert data["formatted_text"] == "tESTsTRING"

def test_format_endpoint_empty():
    payload = {"text": ""}
    response = client.post("/format", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["original_text"] == ""
    assert data["formatted_text"] == ""
