from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from app.core.db import Base


class MeetingRoom(Base):
    name = Column(String(100), unique=True, nullable=False)
    # Новый атрибут модели. Значение nullable по умолчанию равно True,
    # поэтому его можно не указывать.
    description = Column(Text)
    # Установите связь между моделями через функцию relationship.
    reservation = relationship('Reservation', cascade='delete')
