from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.db.database import Base


class MediaTypes(Base):
    __tablename__ = 'MediaTypes'

    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String)
    track = relationship('Tracks')
