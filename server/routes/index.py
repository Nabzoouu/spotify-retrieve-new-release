from routes.get_new_artists import build_get_new_artists

def build_routes(app, db, **kwargs):
    get_new_artists = build_get_new_artists(app, db, **kwargs)

    return get_new_artists