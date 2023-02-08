from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint

from models.db.database import Base


class PlaylistTracks(Base):
    __tablename__ = 'PlaylistTracks'
    __table_args__ = (
        PrimaryKeyConstraint('PlaylistId', 'TrackId'),
    )

    PlaylistId = Column(Integer, ForeignKey('Playlists.PlaylistId'))
    TrackId = Column(Integer, ForeignKey('Tracks.TrackId'))
