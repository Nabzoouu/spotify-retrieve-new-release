from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy import Table, Column, Integer, ForeignKey

from models.index import build_db
from routes.index import build_routes
from cli_command.init_db_test import build_init_test_db_command
from cli_command.drop_db import build_drop_db_cli_command

app = Flask(__name__)

if app.config["ENV"] == "production":
  app.config.from_object("config.ProductionConfig")
else:
  app.config.from_object("config.DevelopmentConfig")
app.config.from_pyfile("secret/credentials.py")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = f"{app.config['TYPE_OF_DATABASE']}://{app.config['POSTGRES_USER']}:{app.config['POSTGRES_PASSWORD']}@{app.config['DATABASE_HOST']}:{app.config['DATABASE_PORT']}/{app.config['DATABASE_NAME']}"

db = SQLAlchemy(app)
(Album, Artist, Album_artist) = build_db(db)

db.create_all()

build_routes(app, db, Album = Album, Artist = Artist)

if app.config["ENV"] != "production":
  build_drop_db_cli_command(db, app)
  build_init_test_db_command(app, db, Album = Album, Artist = Artist)

if __name__ == "__main__":
  app.run(debug=app.config["DEBUG"], host=app.config["APP_HOST"], port=app.config["APP_PORT"])