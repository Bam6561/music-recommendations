import os
from dotenv import find_dotenv, load_dotenv
import requests
import base64
import json
import flask
import random

load_dotenv(find_dotenv()) #Environment variables
spotifyClientID = os.getenv("SPOTIFY_CLIENT_ID")
spotifyClientSecret = os.getenv("SPOTIFY_CLIENT_SECRET")


spotifyClientCredentials = f"{spotifyClientID}:{spotifyClientSecret}" #Spotify credentials & access token
spotifyClientCredentialsB64 = base64.b64encode(spotifyClientCredentials.encode())
authorizationURL = "https://accounts.spotify.com/api/token"
tokenData = {
    "grant_type": "client_credentials"
}
tokenHeaders = {
    "Authorization": f"Basic {spotifyClientCredentialsB64.decode()}"
}
authorizationResponse = requests.post(authorizationURL, data=tokenData, headers=tokenHeaders)
authorizationResponseData = authorizationResponse.json()
accessToken = authorizationResponseData['access_token']
headers = { 
    "Authorization": "Bearer " +accessToken
}

ids = ['6Wr3hh341P84m3EI8qdn9O', '4iJLPqClelZOBCBifm8Fzv', '7H55rcKCfwqkyDFH9wpKM6'] #Rise Against, Pierce the Veil, Christina Perri
queries = "?market=US" 
randomImagePreview =[]
randomSongName = []
randomSongLink = []
randomSongPreviewURL = []
randomArtistName = []
randomArtistLink = []
randomAlbumLink = []

for id in ids: #Artists' top track (US)
    endpoint = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    endpointQueries = f"{endpoint}{queries}"
    result = requests.get(url=endpointQueries, headers=headers)
    randomSelect = random.randint(0, 9) #Random 
    y = 0
    for x in result.json()['tracks']:
        if(y == randomSelect):
            randomImagePreview.append(x['album']['images'][0]['url']) 
            randomSongName.append(x['name']) 
            randomSongLink.append(x['external_urls']['spotify']) 
            randomSongPreviewURL.append(x['preview_url']) 
            randomArtistName.append(x['artists'][0]['name']) 
            randomArtistLink.append(x['album']['artists'][0]['external_urls']['spotify'])
            randomAlbumLink.append(x['album']['external_urls']['spotify']) 
            break
        y += 1
print(randomImagePreview)
print(randomSongName)
print(randomSongLink)
print(randomSongPreviewURL)
print(randomArtistName)
print(randomArtistLink)
print(randomAlbumLink)


##app = flask.Flask(__name__)

##@app.route("/")
##def index():
##    return flask.render_template("index.html")

##app.run(
##    debug=True
##)