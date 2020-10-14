from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

def build_Album(db, album_artist):
  class Album(db.Model):
    __tablename__ = "album"
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
      return [ {"artist_id": artist.artist_id, 
                "name": artist.name,
                } for artist in self.artists
              ]

  return Album
