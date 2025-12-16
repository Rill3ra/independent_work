# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Определение модели входных данных
class TextInput(BaseModel):
    text: str

# Определение модели выходных данных
class TextOutput(BaseModel):
    original_text: str
    formatted_text: str

def format_text_logic(input_text: str) -> str:
    """Логика форматирования: инверсия регистра."""
    return input_text.swapcase()

@app.post("/format", response_model=TextOutput)
def format_text_endpoint(data: TextInput):
    """
    Конечная точка для форматирования текста.
    """
    formatted = format_text_logic(data.text)
    
    return TextOutput(
        original_text=data.text,
        formatted_text=formatted
    )

# Дополнительная базовая точка для проверки доступности
@app.get("/")
def read_root():
    return {"message": "Text Formatting Service is running"}
