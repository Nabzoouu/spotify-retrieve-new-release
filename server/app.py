from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy import Table, Column, Integer, ForeignKey

from spotify_client_model import build_spotify_client
from models.database import build_db
from routes import build_routes

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@172.17.0.2:5432/new-release'

db = SQLAlchemy(app)

Artist, Album, Album_artist = build_db(db)
db.drop_all()
db.create_all()

spotifyClient = build_spotify_client(db, app.config['CLIENT_ID'], app.config['CLIENT_SECRET'], Album=Album, Artist=Artist, Album_artist=Album_artist)

build_routes(app, db, spotifyClient)

print(spotifyClient.storeNewRelease({}))

if __name__ == "__main__":
  app.run(debug=True, host='localhost', port='3000')