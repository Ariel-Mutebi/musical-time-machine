import re
import requests
from bs4 import BeautifulSoup

date_string = input("What day do you want to musically travel back to? Type the date in the format YYYY-MM-DD: ")
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0"}
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_string}", headers=headers)
response.raise_for_status()
let_him_cook = BeautifulSoup(response.text, "html.parser")
song_titles = [re.sub(r'[\n\t]', '', h3.getText()) for h3 in let_him_cook.select("li>h3#title-of-a-story")]
print(song_titles)