from typing import Optional, TYPE_CHECKING

from sqlalchemy import JSON, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base

if TYPE_CHECKING:
    # Убирает предупреждения отсутствия импорта и неприятные подчеркивания в
    # PyCharm и VSCode
    from app.hotels.models import Hotels
    from app.bookings.models import Bookings


class Rooms(Base):
    """Модель Номеров.
    Room(комната) с Hotels(Отель) имеет связь One to one;
    Room(комната) с Bookings(Бронирование) имеет связь One to many."""
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[Optional[str]] = mapped_column(JSON)
    price: Mapped[int]
    services: Mapped[list[str]] = mapped_column(JSON)
    quantity: Mapped[int]
    image_id: Mapped[int]

    hotel: Mapped["Hotels"] = relationship(back_populates="rooms")
    bookings: Mapped[list["Bookings"]] = relationship(back_populates="room")

    def __str__(self):
        return f"Номер {self.name}"