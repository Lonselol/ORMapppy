from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.db.database import Base


class Albums(Base):
    __tablename__ = 'Albums'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('Artists.ArtistId'))
    track = relationship('Tracks')
