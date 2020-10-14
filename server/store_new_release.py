import base64, json, requests, os, datetime

from app import app, db, Artist, Album

class SpotifyClient(object):
    SPOTIFY_URL_TOKEN = "https://accounts.spotify.com/api/token/"
    HEADER = "application/x-www-form-urlencoded"

    def __init__(self):
        self.EXPIRE_DATE = datetime.datetime.now()

    def clientCredentialFlow(self):
        client_id = app.config["CLIENT_ID"]
        client_secret = app.config["CLIENT_SECRET"]
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
        self.EXPIRE_DATE = datetime.datetime.now() + datetime.timedelta(seconds = self.TOKEN["expires_in"])
        return(r.json())

    def getNewRelease(self) :
        if self.EXPIRE_DATE < datetime.datetime.now() or self.TOKEN == {}:
            self.clientCredentialFlow()
        if "error" not in self.TOKEN :
            headers = {
                "Authorization": "Bearer " + self.TOKEN["access_token"]
            }
            newReleaseRequestResult = requests.get("https://api.spotify.com/v1/browse/new-releases", headers=headers)
            if 200 <= newReleaseRequestResult.status_code < 300 :
                # return json.loads(newReleaseRequestResult.text)
                return newReleaseRequestResult.json()
            else :
                print("error " + str(json.loads(newReleaseRequestResult.text)["error"]["status"]) + " : " +  str(json.loads(newReleaseRequestResult.text)["error"]["message"]))
        else :
            print(self.TOKEN)
            return("error : " + self.TOKEN["error_description"])

    def storeNewRelease(self) :
        release = self.getNewRelease()["albums"]["items"]
        new_album_added = 0
        new_artist_added = 0
        for album in release :
            album_exists = Album.query.filter_by(album_id=album["id"]).first()
            if album_exists :
                album_element = None
            else :
                album_element = Album(album_id=album["id"], name=album["name"], 
                                                album_type=album["album_type"], 
                                                release_date=album["release_date"], 
                                                total_tracks=album["total_tracks"])
                db.session.add(album_element)
                new_album_added += 1

            for artist in album["artists"] :
                artist_exists = Artist.query.filter_by(artist_id=artist["id"]).first()
                if artist_exists :
                    artist_element = None
                else :
                    artist_element = Artist(artist_id=artist["id"], name=artist["name"])
                    db.session.add(artist_element)
                    new_artist_added += 1

                if artist_element and album_element and \
                    artist_element not in album_element.artists \
                    and album_element not in artist_element.albums :
                    album_element.artists.append(artist_element)
        db.session.commit()
        return new_album_added, new_artist_added

print("New request made at " + str(datetime.datetime.now()))
spotifyClient = SpotifyClient()
nbr_of_new_album, nbr_of_new_artist = spotifyClient.storeNewRelease()
print("new release stored at date " + str(datetime.datetime.now()) + ".")
print(str(nbr_of_new_album) + " album(s) was(ere) added.")
print(str(nbr_of_new_artist) + " artist(s) was(ere) added." + "\n\n\n")
