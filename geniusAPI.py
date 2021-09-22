import os
from dotenv import find_dotenv, load_dotenv
import requests
import base64
import json

class geniusAPI:
    def __init__(self):
        self.songLyrics = []

    def fetchSongLyrics(self, songName):
        geniusToken = os.getenv("GENIUS_TOKEN")  # Genius credentials
        geniusUrl = "http://api.genius.com/search"
        tokenHeaders = {
            'Authorization': 'Bearer ' + geniusToken
        }
        params = {
            'q': songName
        }
        geniusResponse = requests.get( # Parse Genius lyrics link
            geniusUrl, params=params, headers=tokenHeaders)
        geniusSongPath = geniusResponse.json()['response']['hits'][0]['result']['path']
        self.songLyrics.append("http://genius.com" + geniusSongPath)
