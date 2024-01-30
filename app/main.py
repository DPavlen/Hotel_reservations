from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI()


class SHotel(BaseModel):
    """Схема данных для отелей. Валидация параметров."""
    address: str
    name: str
    stars: int 

class HotelsSearchArgs:
    """Вынесенеие аргументов get-запроса в отдельную сущность.
    Классическая инициализация параметров через магический __init__."""
    def __init__(
            self,
            location: str,
            date_from: date, 
            date_to: date,
            has_spa: bool = Query(default=None),
            stars: Optional[int] = Query(None, ge=1, le=5),    
    ) -> None:
            self.location = location,
            self.date_from = date_from,
            self.date_to = date_to,
            self.has_spa = has_spa,
            self.stars = stars,


# Где response_model=list[SHotel] пример ответа [{}]
@app.get("/hotels")
def get_hotels(
    search_args: HotelsSearchArgs = Depends()
) -> list[SHotel]:
    hotels = [
        {
            "address": "ул. Гагарина, 1, Алтай",
            "name": "Super_hotel",
            "stars": 5
        }
    ]
    """Опциональные параметры None для has_spa, stars."""
    return search_args


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