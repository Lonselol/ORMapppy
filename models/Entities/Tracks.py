from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, REAL
from sqlalchemy.orm import relationship

from models.db.database import Base


class Tracks(Base):
    __tablename__ = 'Tracks'

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('Albums.AlbumId'))
    MediaTypeId = Column(Integer, ForeignKey('MediaTypes.MediaTypeId'))
    GenreId = Column(Integer, ForeignKey('Genres.GenreId'))
    Composer = Column(String)
    Milliseconds = Column(BigInteger)
    Bytes = Column(REAL)
    UnitPrice = Column(REAL)
    playlist_track = relationship('PlaylistTracks')
