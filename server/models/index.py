from models.album import build_Album
from models.artist import build_Artist
from models.album_artist import build_Album_artist

def build_db(db):
  Album_artist = build_Album_artist(db)
  Album = build_Album(db, Album_artist)
  Artist = build_Artist(db, Album_artist)
  return Album, Artist, Album_artist
