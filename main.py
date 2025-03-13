import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIFY_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_SECRET = os.environ['SPOTIFY_SECRET']

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='dolankolan',
    )
)
user_id = sp.current_user()["id"]

playlist_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = 'https://www.billboard.com/charts/hot-100/' + playlist_year
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=header)
page = response.text

soup = BeautifulSoup(page, 'html.parser')

data = soup.select(selector='div ul li ul li h3')

songs_list = [song.text.strip() for song in data]

print(songs_list)