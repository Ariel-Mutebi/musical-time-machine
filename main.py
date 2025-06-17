import os
import re
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
REDIRECT_URI = "https://ariel-mutebi.github.io/musical-time-machine/"

# Scrape Billboard Hot 100
# date_string = input("What day do you want to musically travel back to? Type the date in the format YYYY-MM-DD: ")
# headers = {"User-Agent": os.environ.get("USER_AGENT")}
# response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_string}", headers=headers)
# response.raise_for_status()
# let_him_cook = BeautifulSoup(response.text, "html.parser")
# song_titles = [re.sub(r'[\n\t]', '', h3.getText()) for h3 in let_him_cook.select("li>h3#title-of-a-story")]
# print(song_titles)

# Test Spotify authentication by getting my user id
spotify = Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=REDIRECT_URI,
    )
)

my_account = spotify.current_user()

print(my_account["id"])