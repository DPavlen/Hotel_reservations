from fastapi import FastAPI
import requests


app = FastAPI()

# Стучимся к приложению app
@app.get("/hotels/{hotel_id}")
def get_hotels(hotel_id: int, date_from, date_to):
    """hotel_id - параметр пути(path).
    date_from и date_to - параметры запроса.(query)."""
    return hotel_id, date_from, date_to


r = requests.get(
    "http://127.0.0.1:8000/hotels/12",
    params={"date_from": "today", "date_to": "tomorrow",}
)