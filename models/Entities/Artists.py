from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.db.database import Base


class Artists(Base):
    __tablename__ = 'Artists'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    Album = relationship('Albums')
