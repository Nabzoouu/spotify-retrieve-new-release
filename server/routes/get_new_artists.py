import datetime

def build_get_new_artists(app, db, **kwargs):
  @app.route('/api/artists/', defaults={'delta': app.config["DELTA_JOURS"]})
  @app.route("/api/artists/<int:delta>", methods=["GET"])
  def get_new_artists(delta):
    list_album = kwargs['Album'].query.filter(kwargs['Album'].release_date >= datetime.date.today()- datetime.timedelta(days=delta)).all()
    result = {}
    for album in list_album :
      for artist in album.retrieve_artist() :
        new_album = {'album_id' : album.to_json()['album_id'],
                      'name' : album.to_json()['name'],
                      'release_date' : album.to_json()['release_date'],
                      'total_tracks' : album.to_json()['total_tracks']
                    }
        if artist['name'] in result :
          result[artist['name']]['new_albums'].append(new_album)
        else :
          result[artist['name']] = {'artist_id':artist['artist_id'], 'new_albums' : [new_album]}
    return result