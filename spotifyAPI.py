import os
from dotenv import find_dotenv, load_dotenv
import requests
import base64
import json
import random

class spotifyAPI:
    def __init__(self):
        self.artistID = ['6Wr3hh341P84m3EI8qdn9O', '4iJLPqClelZOBCBifm8Fzv', 
        '7H55rcKCfwqkyDFH9wpKM6'] # Rise Against, Pierce the Veil, Christina Perri
        self.randomImagePreview = []
        self.randomSongName = []
        self.randomSongLink = []
        self.randomSongPreviewURL = []
        self.randomArtistName = []
        self.randomArtistLink = []

    def fetchArtistSongData(self):
        # Environment variables
        load_dotenv(find_dotenv())  
        spotifyClientID = os.getenv("SPOTIFY_CLIENT_ID")
        spotifyClientSecret = os.getenv("SPOTIFY_CLIENT_SECRET")

        # Spotify credentials & access token
        spotifyClientCredentials = f"{spotifyClientID}:{spotifyClientSecret}" 
        spotifyClientCredentialsB64 = base64.b64encode(
        spotifyClientCredentials.encode())
        authorizationURL = "https://accounts.spotify.com/api/token"
        tokenData = {
            "grant_type": "client_credentials"
        }
        tokenHeaders = {
            "Authorization": f"Basic {spotifyClientCredentialsB64.decode()}"
        }
        authorizationResponse = requests.post(
            authorizationURL, data=tokenData, headers=tokenHeaders)
        authorizationResponseData = authorizationResponse.json()
        accessToken = authorizationResponseData['access_token']
        spotifyHeaders = {
            "Authorization": "Bearer " + accessToken
        }
        queries = "?market=US"

        for id in self.artistID:  # Artists' top track (US)
            endpoint = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
            endpointQueries = f"{endpoint}{queries}"
            result = requests.get(url=endpointQueries, headers=spotifyHeaders)
            randomSelect = random.randint(0, 9)  # Random
            y = 0
            for x in result.json()['tracks']:
                if(y == randomSelect):
                    self.randomImagePreview.append(x['album']['images'][0]['url'])
                    self.randomSongName.append(x['name'])
                    self.randomSongLink.append(x['external_urls']['spotify'])
                    self.randomSongPreviewURL.append(x['preview_url'])
                    self.randomArtistName.append(x['artists'][0]['name'])
                    self.randomArtistLink.append(
                    x['album']['artists'][0]['external_urls']['spotify'])
                    break
                y += 1

