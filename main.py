import spotifyAPI
import geniusAPI
import flask

app = flask.Flask(__name__)

def main():
    spotify = spotifyAPI.spotifyAPI()
    genius = geniusAPI.geniusAPI()
    spotify.fetchArtistSongData()
    for x in spotify.randomSongName:
        genius.fetchSongLyrics(x)
    print(genius.songLyrics)

if __name__ == "__main__":
    main()

#@app.route("/")
#def index():
#    spotify = spotifyAPI()
#    genius = geniusAPI()
#    print(spotify.fetchArtistSongData())
#    return flask.render_template("index.html")

#app.run(
#    debug=True
#)