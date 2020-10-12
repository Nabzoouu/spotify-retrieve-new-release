from flask import Flask
from spotify_client_model import SpotifyClient

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')

spotifyClient = SpotifyClient(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'])

@app.route("/api/artists", methods=["GET"])
def getArtiste():
    print(spotifyClient.getNewRelease())
    return {'to do' : 'data about artiste'}

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port='3000')