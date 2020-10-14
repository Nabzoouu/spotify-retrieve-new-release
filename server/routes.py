import datetime

def build_routes(app, db, spotifyClient, **kwargs):
  @app.route("/api/artists", methods=["GET"])
  def getArtiste():
    list_album = kwargs['Album'].query.filter(kwargs['Album'].release_date >= datetime.date.today()- datetime.timedelta(days=30)).all()
    result = []
    for album in list_album :
      for artist in album.retrieve_artist() :
        if artist not in result :
          result.append(artist)
    
    return {"result" : result }

