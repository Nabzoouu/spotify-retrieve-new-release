
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from spotify_client_model import SpotifyClient

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@172.17.0.2:5432/new-release'

db = SQLAlchemy(app)
spotifyClient = SpotifyClient(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'], db)

import models.database

print('done')