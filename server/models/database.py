from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

def build_db(db):
  album_artist = db.Table('album_artist',
      db.Column('artist_id', db.String(100), db.ForeignKey('artist.artist_id'), primary_key=True),
      db.Column('album_id', db.String(100), db.ForeignKey('album.album_id'), primary_key=True)
  )
    
  class Artist(db.Model):
    __tablename__ = 'artist'
    artist_id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    albums = relationship(
      "Album",
      secondary=album_artist,
      back_populates="artists")

    def __repr__(self):
      return f"input(name = {artist_id}, name = {name}"

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
    
    def __repr__(self):
      return f"input(name = {album_id}, name = {name}"

  return Artist, Album, album_artist
