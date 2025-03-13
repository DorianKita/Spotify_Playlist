import requests
from bs4 import BeautifulSoup

URL = 'https://www.billboard.com/charts/hot-100/2000-01-08/'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}



# playlist_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url=URL, headers=header)
page = response.text

soup = BeautifulSoup(page, 'html.parser')

data = soup.select(selector='div ul li ul li h3')
songs_list = []

for song in data:
    songs_list.append(song.text.strip())

print(songs_list)