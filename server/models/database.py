from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

def build_db(db):
  album_artist = db.Table('album_artist',
      db.Column('artist_id', db.String(100), db.ForeignKey('artist.artist_id')),
      db.Column('album_id', db.String(100), db.ForeignKey('album.album_id'))
  )
    
  class Artist(db.Model):
    __tablename__ = 'artist'
    artist_id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    albums = relationship(
      "Album",
      secondary=album_artist,
      back_populates="artists")

    def to_json(self):
        return {
            "artist_id": self.artist_id,
            "name": self.name,
            "albums": [ {"album_id": album.album_id, 
                         "name": album.name, 
                         "album_type": album.album_type, 
                         "total_tracks":album.total_tracks, 
                         "artists":[{"id":artist.artist_id, "name":artist.name} for artist in album.artists], 
                         "release_date":album.release_date} for album in self.albums] if self.albums else None
        }

  class Album(db.Model):
    __tablename__ = 'album'
    album_id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    album_type = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    total_tracks = db.Column(db.Integer, nullable=False)
    artists = relationship(
      "Artist",
      secondary=album_artist,
      back_populates="albums")
    
    def to_json(self):
        return {
            "album_id": self.album_id,
            "name": self.name,
            "album_type": self.album_type,
            "release_date": self.release_date,
            "total_tracks": self.total_tracks,
            "artists": [ {"id": artist.artist_id, 
                          "name": artist.name
                         } for artist in self.artists
                       ] if self.artists else None
        }
    def retrieve_artist(self):
      return [ {"id": artist.artist_id, 
                "name": artist.name,
                # "albums" : [{"album_id": album.album_id, 
                #               "name": album.name,
                #               "album_type": album.album_type,
                #               "release_date": album.release_date,
                #               "total_tracks": album.total_tracks,
                #               "artists": [ {"id": artist.artist_id, 
                #                             "name": artist.name} for artist in album.artists
                #                         ]} for album in artist.albums]
                } for artist in self.artists
              ]
  return Artist, Album, album_artist
