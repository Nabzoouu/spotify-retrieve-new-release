from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, ForeignKey

def build_Album_artist(db):
  Album_artist = db.Table("album_artist",
      db.Column("artist_id", db.String(100), db.ForeignKey("artist.artist_id")),
      db.Column("album_id", db.String(100), db.ForeignKey("album.album_id"))
  )
  return Album_artist
