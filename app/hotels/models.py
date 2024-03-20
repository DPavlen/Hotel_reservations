from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base


class Hotels(Base):
    """# Модель написана в соответствии с современным стилем Алхимии (версии 2.x)."""
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column()
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    room_quantity: Mapped[int]
    image_id: Mapped[int]