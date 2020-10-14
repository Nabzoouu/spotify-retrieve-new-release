import requests

BASE = 'http://localhost:3000'

response = requests.get(BASE + "/api/artists")
print(response.text)
# input()