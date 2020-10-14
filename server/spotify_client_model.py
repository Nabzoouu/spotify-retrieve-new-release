import base64, json, requests, os, datetime

def build_spotify_client(db, client_id, client_secret, **kwargs):
    class SpotifyClient(object):
        SPOTIFY_URL_TOKEN = "https://accounts.spotify.com/api/token/"
        HEADER = "application/x-www-form-urlencoded"

        def __init__(self, clientID, clientSecret):
            self.EXPIRE_DATE = datetime.datetime.now()
            self.CLIENT_ID = clientID
            self.CLIENT_SECRET = clientSecret
        
        def clientCredentialFlow(self):
            client_id = self.CLIENT_ID
            client_secret = self.CLIENT_SECRET
            body = {
                "grant_type" : "client_credentials"
            }
            encoded = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
            headers = {
                "Content-Type": self.HEADER,
                "Authorization": f"Basic {encoded}",
            }
            r = requests.post(self.SPOTIFY_URL_TOKEN, params=body, headers=headers)
            self.TOKEN = r.json()
            self.EXPIRE_DATE = datetime.datetime.now() + datetime.timedelta(seconds = self.TOKEN['expires_in'])
            return(r.json())
        
        def getNewRelease(self) :
            if self.EXPIRE_DATE < datetime.datetime.now() or self.TOKEN == {}:
                print('Token expired')
                self.clientCredentialFlow()
            if 'error' not in self.TOKEN :
                headers = {
                    "Authorization": "Bearer " + self.TOKEN['access_token']
                }
                newReleaseRequestResult = requests.get("https://api.spotify.com/v1/browse/new-releases", headers=headers)
                if 200 <= newReleaseRequestResult.status_code < 300 :
                    # return json.loads(newReleaseRequestResult.text)
                    return newReleaseRequestResult.json()
                else :
                    print('error ' + str(json.loads(newReleaseRequestResult.text)['error']['status']) + ' : ' +  str(json.loads(newReleaseRequestResult.text)['error']['message']))
            else :
                print(self.TOKEN)
                return('error : ' + self.TOKEN['error_description'])

        def storeNewRelease(self, newRelease: dict) :
            release = self.getNewRelease()['albums']['items']
            for album in release :
                album_exists = kwargs['Album'].query.filter_by(album_id=album['id']).first()
                if album_exists :
                    print("Album already exists")
                    album_element = None
                else :
                    album_element = kwargs['Album'](album_id=album['id'], name=album['name'], 
                                                    album_type=album["album_type"], 
                                                    release_date=album["release_date"], 
                                                    total_tracks=album["total_tracks"])
                    db.session.add(album_element)
                
                for artist in album["artists"] :
                    artist_exists = kwargs['Artist'].query.filter_by(artist_id=artist['id']).first()
                    if artist_exists :
                        print("artist already exists")
                        artist_element = None
                    else :
                        artist_element = kwargs['Artist'](artist_id=artist['id'], name=artist['name'])
                        db.session.add(artist_element)

                    if artist_element and album_element and \
                       artist_element not in album_element.artists \
                       and album_element not in artist_element.albums :
                        album_element.artists.append(artist_element)
                        artist_element.albums.append(album_element)
                    else :
                        print("Album_artist exists already")
            db.session.commit()
            
            # print(kwargs['Album'].query.filter_by(album_id=album['id']).first().to_json())

            return None
    
    return SpotifyClient(client_id, client_secret)