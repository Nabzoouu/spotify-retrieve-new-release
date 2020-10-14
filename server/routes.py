def build_routes(app, db, spotifyClient):
  @app.route("/api/artists", methods=["GET"])
  def getArtiste():
    return (spotifyClient.getNewRelease())

