from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.db.database import Base


class Playlists(Base):
    __tablename__ = 'Playlists'

    PlaylistId = Column(Integer, primary_key=True)
    Name = Column(String)
    playlist_track = relationship('PlaylistTracks')
