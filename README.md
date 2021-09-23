## Music Recommendations Web App
#### Summary
This directory is for a music discovery web application I've written in Python. If you want a preview of its functionality, I've successfully deployed it to this link: https://spotify-music-recommendations.herokuapp.com/
#### Set-up
If you wish to use the same application for your own use, please have the following software and neccessary documentation for later mentioned APIs ready.

 - Visual Studio Code (Programming IDE)
 - Git & Github (Version Control)
 - Python (Programming Language)
 - Flask (Web App)
 - Spotify API (Song Information)
 - Genius API (Song Lyrics)
 - Heroku (Web Application Deployment)

You should be able to use any programming IDE for this application, but I used Visual Studio Code for development on a virtual machine. Github was used to release and commit steady changes to the project and Python and Flask were the programming language of choice. Using Flask, a framework written in Python, one can easily deploy web applications of their own using Jinja template and Werkzeug library. Spotify API was used to query random songs from 3 artists of my choosing's top hits in the US, and Genius API was used to parse the data about those songs - most specifically, their lyrics URL was provided from the interaction. Heroku was used to deploy the application.

#### Usage & Modification
Please remember to install Flask using pip prior to working on this project. 
`$ pip install Flask`
If you choose to fork this repository, you will be missing several variables that are required for the app to function. Namely, these are the client and secret keys for Spotify and Genius API. You can generate your own keys from their respective websites after you've registered to use their APIs.
Spotify API: https://developer.spotify.com/
Genius API: https://docs.genius.com/
Once you've obtained these keys, you can create a .env file where your working repository is, and fill out these following variables:
`export SPOTIFY_CLIENT_ID=""`
`export SPOTIFY_CLIENT_SECRET=""`
`export GENIUS_TOKEN = ""`
After filling out these specific environment variables, you should be able to run your application. However, if you want to make modifications to the existing web app, you should keep in mind how the application works. Located in the spotifyAPI.py file, there is a constructor class variable named artistID. You'll want to look up your favorite artists' id's using Spotify's "copy link to artist" feature from the three dot icon next to their name. After the first / after artist and before the first ? punctuation, you'll be able to copy their ID and insert it into the artistID list. Currently, the application supports 3 artists to be displayed on screen at a time, due to the style.css splitting them into banners 1/3 of the screen wide. However, the code itself can support as many artists as you need to query. You will have to play around with the style.css to adjust accordingly to the changes for the display to be readable.
#### FAQ
Not every software is perfect, and neither is the programmer behind them, so I will document several issues I had both programming - and running the application so that those who come after me can save their valuable time.

- My website is blank! There are no errors, what could be the problem?

Embarassingly enough, please make sure to remember to load your .env file (locally) or give Heroku your environment variables in order to access Spotify & Genius API. There isn't anything wrong with the code - you just haven't given the APIs anything to work with!

-  Why are my requests for parsing the .json of Spotify and Genius API results coming back as errors?

Carefully looking at the indentation of the .json files and understanding what type of data the desired information is nested in is important. Sometimes, you could make the mistake of trying to call a specific tag from a dictionary while it's nested inside a list. Manually going through each tier downwards into the .json file by calling the levels' type can assist you in this.

- My authorization token is invalid, or doesn't exist! How can I fix it?

If your authorization token is invalid, it could be expired, or you have run into the unfortunate outcome that you're dealing with Spotify's API. For Spotify's API, they are incredibly meticulous in the idea of security, so you must encode your {clientID}:{clientSecret} in base64. After encoding your clientID & clientSecret in base64, you must decode it to use for the Authorization header.
#### Possible Features:
Some possible features I would add, if I had more time, is user input fields for artistIDs in the Spotify queries. The code already exists that is hard coded into the program that searches for the same 3 artists' top hits randomly each time, but I could apply a html form that submits the new query back to the application to reload the page or rewrite the div with JQuery's document.getElementByID(). Another possible feature I could add to the existing application would be possibly a dropdown HTML form box feature that has 10 or so predefined artists for someone to select, and the selected one's top hits are shown. Once again, this is an HTML form feature with JQuery to rewrite the page.

#### Reference Links:
**Spotify API:** https://www.youtube.com/watch?v=xdq6Gz33khQ&ab_channel=CodingEntrepreneurs
**Genius API:** https://bigishdata.com/2016/09/27/getting-song-lyrics-from-geniuss-api-scraping/