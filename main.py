import os
from dotenv import find_dotenv, load_dotenv
import requests
import base64
import json

load_dotenv(find_dotenv())
clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")
clientCredentials = f"{clientID}:{clientSecret}"
clientCredentialsB64 = base64.b64encode(clientCredentials.encode())
authorizationURL = "https://accounts.spotify.com/api/token"
tokenData = {
    "grant_type": "client_credentials"
}
tokenHeaders = {
    "Authorization": f"Basic {clientCredentialsB64.decode()}"
}
authorizationResponse = requests.post(authorizationURL, data=tokenData, headers=tokenHeaders)
authorizationResponseData = authorizationResponse.json()
accessToken = authorizationResponseData['access_token']