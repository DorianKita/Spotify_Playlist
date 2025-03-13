import requests
from bs4 import BeautifulSoup


playlist_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = 'https://www.billboard.com/charts/hot-100/' + playlist_year
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=header)
page = response.text

soup = BeautifulSoup(page, 'html.parser')

data = soup.select(selector='div ul li ul li h3')

songs_list = [song.text.strip() for song in data]

print(songs_list)