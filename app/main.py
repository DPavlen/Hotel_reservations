from fastapi import FastAPI

app = FastAPI()

# Стучимся к приложению app
@app.get("/hotels")
def get_hotels():
    return "Отель Бридж Резорт 5 звезд"