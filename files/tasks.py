from models.db.database import session

from models.Entities.Albums import Albums
from models.Entities.Artists import Artists
from models.Entities.Genres import Genres
from models.Entities.Playlists import Playlists
from models.Entities.PlaylistTracks import PlaylistTracks
from models.Entities.Tracks import Tracks

from sqlalchemy.sql import func


def tasks(number: int):
    if number == 0:
        task = session.query(Tracks.Name, Tracks.Composer, Tracks.Milliseconds) \
            .order_by(Tracks.Name).all()

        print("Task A\n")

        for t in task:
            print(f"Name: {t.Name}; ",
                  f"Composer: {t.Composer}; ",
                  f"Length in secs: {t.Milliseconds / 1000};")

        print("\n")

    if number == 1:
        print("Task B\n")
        print(session.query(Tracks).count())
        print("\n")

    if number == 2:
        task = session.query(Albums).limit(10).all()
        print("Task C\n")
        for t in task:
            print(f'Title: {t.Title}; ', f'ArtistId: {t.ArtistId}; ')
        print("\n")

    if number == 3:
        task = session.query(Genres).filter(Genres.Name.like("R%")).all()
        print("Task D\n")
        for t in task:
            print(f'Name: {t.Name}')
        print("\n")

    if number == 4:
        print("Task E\n")
        task = session.query(
            Albums.AlbumId,
            Albums.Title,
            Tracks.Composer,
            func.sum(Tracks.Bytes),
            func.sum(Tracks.UnitPrice)
        ).join(Tracks) \
            .group_by(Tracks.Composer) \
            .filter(Tracks.AlbumId == Albums.AlbumId).all() \

        for t in task:
            print(t)
        print("\n")

    if number == 5:
        print("Task F\n")
        print(session.query(Artists) \
              .join(Tracks, Albums.AlbumId == Tracks.AlbumId)
              .join(Albums, Artists.ArtistId == Albums.ArtistId) \
              .distinct(Artists.Name).count())
        print("\n")

    if number == 6:
        print("Task G\n")
        print(session.query(Artists).select_from(Tracks, Albums, Playlists, PlaylistTracks) \
              .filter(Artists.ArtistId == Albums.ArtistId,
                      Albums.AlbumId == Tracks.AlbumId,
                      Tracks.TrackId == PlaylistTracks.TrackId,
                      Playlists.PlaylistId == PlaylistTracks.PlaylistId,
                      Playlists.PlaylistId == 1) \
              .count())
