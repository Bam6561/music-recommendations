import spotifyAPI
import geniusAPI
import flask
import os

app = flask.Flask(__name__)

@app.route("/")
def index():
    spotify = spotifyAPI.spotifyAPI() # Spotify Access
    genius = geniusAPI.geniusAPI() # Genius Access
    spotify.fetchArtistSongData() # Randomized tracks
    for x in spotify.randomSongName: # Song lyrics for randomized tracks 
        genius.fetchSongLyrics(x)
    return flask.render_template("index.html", len = len(spotify.artistID), imagePreview = spotify.randomImagePreview, 
    songName = spotify.randomSongName, songLink = spotify.randomSongLink, songPreviewURL = spotify.randomSongPreviewURL, 
    artistName = spotify.randomArtistName, artistLink = spotify.randomArtistLink, songLyrics = genius.songLyrics)

app.run(debug=True, host = '0.0.0.0', port=int(os.getenv('PORT',8080))
)