import requests
from bs4 import BeautifulSoup

URL = 'https://cuantic.000webhostapp.com/modelo/modeloBD.php'
page = requests.get(URL)

print(page.content.decode('utf-8'))
soup = BeautifulSoup(page.content, 'html.parser')