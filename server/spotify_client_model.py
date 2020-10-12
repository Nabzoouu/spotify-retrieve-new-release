import base64, json, requests, os, datetime


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
        print(self.EXPIRE_DATE < datetime.datetime.now())
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
        return newRelease

# spotifyClient = SpotifyClient()
# print(spotifyClient.getNewRelease())

# print(spotifyClient.storeNewRelease({'test':'test'}))

