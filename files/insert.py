from models.db.database import session
from models.Entities.Albums import Albums
from models.Entities.Artists import Artists
from models.Entities.Genres import Genres
from models.Entities.MediaTypes import MediaTypes
from models.Entities.Playlists import Playlists
from models.Entities.PlaylistTracks import PlaylistTracks
from models.Entities.Tracks import Tracks


def insert():
    # Artists

    artist0 = Artists(Name="The Rolling Stones")
    artist1 = Artists(Name="The Animals")
    artist2 = Artists(Name="Stevie Nicks")
    artist3 = Artists(Name="Chuck Berry")
    artist4 = Artists(Name="Pat Benatar")
    artist5 = Artists(Name="Little Richard")
    artist6 = Artists(Name="The Hollies")
    artist7 = Artists(Name="Badfinger")
    artist8 = Artists(Name="The Yardbirds")
    artist9 = Artists(Name="Refused")

    session.add_all([artist0, artist1, artist2, artist3, artist4, artist5,
                    artist6, artist7, artist8, artist9])

    # Albums

    album0 = Albums(Title="Let it bleed", ArtistId=0)
    album1 = Albums(Title="The Animals", ArtistId=1)
    album2 = Albums(Title="Bella Donna", ArtistId=2)
    album3 = Albums(Title="Chuck", ArtistId=3)
    album4 = Albums(Title="Crimes of Passion", ArtistId=4)
    album5 = Albums(Title="Here's Little Richard", ArtistId=5)
    album6 = Albums(Title="Singles A's & B's", ArtistId=6)
    album7 = Albums(Title="Straight Up", ArtistId=7)
    album8 = Albums(Title="Heart Full of Soul", ArtistId=8)
    album9 = Albums(Title="Samurai", ArtistId=9)

    session.add_all([album0, album1, album2, album3, album4, album5,
                    album6, album7, album8, album9])

    # Genres

    genre0 = Genres(Name="Folk-Rock")
    genre1 = Genres(Name="Rock")
    genre2 = Genres(Name="Rhythm And Blues")
    genre3 = Genres(Name="HardcorePunk")

    session.add_all([genre0, genre1, genre2, genre3])

    # MediaTypes

    mediaType0 = MediaTypes(Name="mass-media")
    mediaType1 = MediaTypes(Name="old school")

    session.add_all([mediaType0, mediaType1])

    # Tracks

    track1 = Tracks(
        Name="Gimme Shelter",
        AlbumId=1,
        MediaTypeId=2,
        GenreId=2,
        Composer="The Rolling Stones",
        Milliseconds=271000,
        Bytes=3.45,
        UnitPrice=56.9,
    )
    track2 = Tracks(
        Name="House Of The Rising Sun",
        AlbumId=2,
        MediaTypeId=2,
        GenreId=1,
        Composer="The Animals",
        Milliseconds=249000,
        Bytes=7.3,
        UnitPrice=39,
    )
    track3 = Tracks(
        Name="Edge of Seventeen",
        AlbumId=3,
        MediaTypeId=2,
        GenreId=2,
        Composer="Stevie Nicks",
        Milliseconds=329000,
        Bytes=3.5,
        UnitPrice=10,
    )
    track4 = Tracks(
        Name="Big Boys",
        AlbumId=4,
        MediaTypeId=2,
        GenreId=3,
        Composer="Chuck Berry",
        Milliseconds=186000,
        Bytes=1.9,
        UnitPrice=12.4,
    )
    track5 = Tracks(
        Name="You Better Run",
        AlbumId=5,
        MediaTypeId=2,
        GenreId=2,
        Composer="Pat Benatar",
        Milliseconds=184000,
        Bytes=12.9,
        UnitPrice=40,
    )
    track6 = Tracks(
        Name="Long Tall Sally",
        AlbumId=6,
        MediaTypeId=2,
        GenreId=3,
        Composer="Little Richard",
        Milliseconds=126000,
        Bytes=6.8,
        UnitPrice=54,
    )
    track7 = Tracks(
        Name="Long Cool Woman In A Black Dress",
        AlbumId=7,
        MediaTypeId=2,
        GenreId=2,
        Composer="The Hollies",
        Milliseconds=200000,
        Bytes=4.8,
        UnitPrice=10,
    )
    track8 = Tracks(
        Name="Baby Blue",
        AlbumId=8,
        MediaTypeId=2,
        GenreId=2,
        Composer="Badfinger",
        Milliseconds=218000,
        Bytes=3.4,
        UnitPrice=90,
    )
    track9 = Tracks(
        Name="Heart Full Of Soul",
        AlbumId=9,
        MediaTypeId=2,
        GenreId=1,
        Composer="The Yardbirds",
        Milliseconds=150000,
        Bytes=12,
        UnitPrice=49,
    )
    track10 = Tracks(
        Name="Chippin In",
        AlbumId=10,
        MediaTypeId=1,
        GenreId=4,
        Composer="Refused",
        Milliseconds=126000,
        Bytes=7.3,
        UnitPrice=90,
    )

    session.add_all([track1, track2, track3, track4, track5,
                    track6, track7, track8, track9, track10])

        # PlayLists

    playlist1 = Playlists(Name="British Invasion")
    playlist2 = Playlists(Name="Breaking Bad")
    playlist3 = Playlists(Name="60-79")
    playlist4 = Playlists(Name="80's classy")
    playlist5 = Playlists(Name="Take Down Arasaka")
    playlist6 = Playlists(Name="One More Time")

    session.add_all([playlist1, playlist2, playlist3, playlist4, playlist5,
                    playlist6])

    # PlaylistTracks

    playListTrack0 = PlaylistTracks(PlaylistId=6, TrackId=10)
    playlistTrack1 = PlaylistTracks(PlaylistId=1, TrackId=1)
    playlistTrack2 = PlaylistTracks(PlaylistId=1, TrackId=2)
    playlistTrack3 = PlaylistTracks(PlaylistId=2, TrackId=8)
    playlistTrack4 = PlaylistTracks(PlaylistId=6, TrackId=4)
    playlistTrack5 = PlaylistTracks(PlaylistId=5, TrackId=10)
    playlistTrack6 = PlaylistTracks(PlaylistId=3, TrackId=9)
    playlistTrack7 = PlaylistTracks(PlaylistId=3, TrackId=6)
    playlistTrack8 = PlaylistTracks(PlaylistId=3, TrackId=1)
    playlistTrack9 = PlaylistTracks(PlaylistId=3, TrackId=2)

    session.add_all([playListTrack0, playlistTrack1, playlistTrack2, playlistTrack3, playlistTrack4, playlistTrack5,
                    playlistTrack6, playlistTrack7, playlistTrack8, playlistTrack9])

    session.commit()
