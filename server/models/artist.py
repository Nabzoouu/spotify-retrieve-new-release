from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy.orm import relationship

def build_Artist(db, album_artist):
  class Artist(db.Model):
    __tablename__ = "artist"
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

  return Artist
