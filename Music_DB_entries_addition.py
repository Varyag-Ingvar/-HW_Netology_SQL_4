from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker

db = 'postgresql://ivoronkov:u123456@localhost:5432/ivoronkov'
engine = create_engine(db)

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    artist_name = Column(String(100), nullable=False)


class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    album_name = Column(String(100), nullable=False)
    release_year = Column(Integer)


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    genre_name = Column(String(100), nullable=False)


class Collection(Base):
    __tablename__ = 'collection'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    collection_name = Column(String(150), nullable=False)
    release_year = Column(Integer)


class Track(Base):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    track_name = Column(String(150), nullable=False)
    duration = Column(Integer)
    album_id = Column(Integer, ForeignKey(Album.id))


class CollectionTrack(Base):
    __tablename__ = 'collection_track'

    collection_id = Column(Integer, ForeignKey(Collection.id), primary_key=True)
    track_id = Column(Integer, ForeignKey(Track.id), primary_key=True)


class ArtistGenre(Base):
    __tablename__ = 'artist_genre'

    artist_id = Column(Integer, ForeignKey(Artist.id), primary_key=True)
    genre_id = Column(Integer, ForeignKey(Genre.id), primary_key=True)


class ArtistAlbum(Base):
    __tablename__ = 'artist_album'

    artist_id = Column(Integer, ForeignKey(Artist.id), primary_key=True)
    album_id = Column(Integer, ForeignKey(Album.id), primary_key=True)


Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Artist(artist_name='queen'),
    Artist(artist_name='roxette'),
    Artist(artist_name='metallica'),
    Artist(artist_name='scorpions'),
    Artist(artist_name='linkin park'),
    Artist(artist_name='rammstein'),
    Artist(artist_name='ace of base'),
    Artist(artist_name='eminem'),
    Artist(artist_name='armin van buuren'),
    Artist(artist_name='andrea bocelli'),
    Album(album_name='a kind of magic', release_year=1986),
    Album(album_name='tourism', release_year=1992),
    Album(album_name='master of puppets', release_year=1986),
    Album(album_name='crazy world', release_year=1990),
    Album(album_name='meteora', release_year=2003),
    Album(album_name='mutter', release_year=2001),
    Album(album_name='happy nation', release_year=1992),
    Album(album_name='the slim shady lp', release_year=1999),
    Album(album_name='imagine', release_year=2008),
    Album(album_name='bocelli', release_year=1995),
    Genre(genre_name='rock'),
    Genre(genre_name='pop'),
    Genre(genre_name='rap'),
    Genre(genre_name='opera'),
    Genre(genre_name='trance'),
    Collection(collection_name='greatest hits 2', release_year=1991),
    Collection(collection_name='hard rock forever 3', release_year=1998),
    Collection(collection_name='hip hop hits 5', release_year=2000),
    Collection(collection_name='opera hits 4', release_year=1997),
    Collection(collection_name='top of the pop 22', release_year=1999),
    Collection(collection_name='the best of vocal trance 7', release_year=2010),
    Collection(collection_name='euro dance hits 18', release_year=2015),
    Collection(collection_name='rock rocket 6', release_year=1996),
    Track(track_name='a kind of magic', duration=264),
    Track(track_name='who wants to live forever', duration=315),
    Track(track_name='it must have been love', duration=258),
    Track(track_name='joyride', duration=240),
    Track(track_name='master of puppets', duration=516),
    Track(track_name='battery', duration=313),
    Track(track_name='wind of change', duration=313),
    Track(track_name='send me an angel', duration=273),
    Track(track_name='breaking the habit', duration=196),
    Track(track_name='from the inside', duration=176),
    Track(track_name='mein herz brennt', duration=280),
    Track(track_name='feuer frei', duration=188),
    Track(track_name='guilty conscience', duration=199),
    Track(track_name='never say never', duration=419),
    Track(track_name='vivo per lei', duration=263),
    Track(track_name='all that she wants', duration=210),
    CollectionTrack(track_id=76, collection_id=41),
    CollectionTrack(track_id=77, collection_id=41),
    CollectionTrack(track_id=78, collection_id=42),
    CollectionTrack(track_id=79, collection_id=48),
    CollectionTrack(track_id=80, collection_id=42),
    CollectionTrack(track_id=81, collection_id=42),
    CollectionTrack(track_id=82, collection_id=48),
    CollectionTrack(track_id=83, collection_id=48),
    CollectionTrack(track_id=84, collection_id=48),
    CollectionTrack(track_id=85, collection_id=48),
    CollectionTrack(track_id=86, collection_id=42),
    CollectionTrack(track_id=87, collection_id=42),
    CollectionTrack(track_id=88, collection_id=43),
    CollectionTrack(track_id=89, collection_id=46),
    CollectionTrack(track_id=90, collection_id=44),
    CollectionTrack(track_id=91, collection_id=47),
    ArtistGenre(artist_id=91, genre_id=26),
    ArtistGenre(artist_id=92, genre_id=26),
    ArtistGenre(artist_id=93, genre_id=26),
    ArtistGenre(artist_id=94, genre_id=26),
    ArtistGenre(artist_id=95, genre_id=26),
    ArtistGenre(artist_id=96, genre_id=26),
    ArtistGenre(artist_id=97, genre_id=27),
    ArtistGenre(artist_id=98, genre_id=28),
    ArtistGenre(artist_id=99, genre_id=30),
    ArtistGenre(artist_id=100, genre_id=29),
    ArtistAlbum(artist_id=91, album_id=91),
    ArtistAlbum(artist_id=92, album_id=92),
    ArtistAlbum(artist_id=93, album_id=93),
    ArtistAlbum(artist_id=94, album_id=94),
    ArtistAlbum(artist_id=95, album_id=95),
    ArtistAlbum(artist_id=96, album_id=96),
    ArtistAlbum(artist_id=97, album_id=97),
    ArtistAlbum(artist_id=98, album_id=98),
    ArtistAlbum(artist_id=99, album_id=99),
    ArtistAlbum(artist_id=100, album_id=100),
]
)

session.commit()
session.close()
