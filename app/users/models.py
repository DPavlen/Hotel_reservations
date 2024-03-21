from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.bookings.models import Bookings
from app.database import Base


class Users(Base):
    """Модель юзеров.
    Пользователи (users) могут иметь много Бронирований (Bookings), one to many.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]

    bookings: Mapped[list["Bookings"]] = relationship()

    def __str__(self):
        return f"Пользователь {self.email}"