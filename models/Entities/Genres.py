from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.db.database import Base


class Genres(Base):
    __tablename__ = 'Genres'

    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)
    track = relationship('Tracks')
