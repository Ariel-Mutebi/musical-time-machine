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
date_string = input("What day do you want to musically travel back to? Type the date in the format YYYY-MM-DD: ")
year = date_string.split("-")[0]

headers = {"User-Agent": os.environ.get("USER_AGENT")}
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_string}", headers=headers)
response.raise_for_status()

let_him_cook = BeautifulSoup(response.text, "html.parser")
song_titles = [re.sub(r'[\n\t]', '', h3.getText()) for h3 in let_him_cook.select("li>h3#title-of-a-story")]

print(song_titles)

# Create list of song URIs
spotify = Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private"
    )
)

song_URIs = []

for song_title in song_titles:
    search_result = spotify.search(q=f"track: {song_title} year:{year}", type="track", limit="1")
    if search_result["tracks"]["total"] > 0:
        song_URIs.append(search_result["tracks"]["items"][0]["uri"])
    else:
        print(f"A song titled {song_title} does not exist on Spotify.")

print(song_URIs)

# create playlist
my_account = spotify.current_user()
my_user_id = my_account["id"]
my_playlist = spotify.user_playlist_create(my_user_id, f"{date_string} Billboard Hot 100", public=False)
spotify.playlist_add_items(my_playlist["id"], song_URIs)