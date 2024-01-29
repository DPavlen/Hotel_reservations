from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI()

# Стучимся к приложению app
@app.get("/hotels/{hotel_id}")
def get_hotels(
    location: str,
    date_from: date, 
    date_to: date,
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(None, ge=1, le=5)
    ):
    return date_from, date_to


class SBooking(BaseModel):
    """Схема данных для передачи post-запроса."""
    room_id: int
    date_from: date
    date_to: date



# post-запрос
@app.post("/bookings")
def add_booking(booking: SBooking):
    """add_booking имеет формат схемы SBooking."""
    pass