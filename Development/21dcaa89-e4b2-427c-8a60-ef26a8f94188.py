# testing 1
import requests
r = requests.get('http://www.imdb.com/name/nm0000821') # lets look at Amitabh Bachchan's list of movie
from bs4 import BeautifulSoup
webpage = BeautifulSoup(r.text, "html.parser")