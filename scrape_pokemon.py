
import requests
from bs4 import BeautifulSoup

#Access Pokemon Page
page = requests.get("https://www.pokemon.com/us/pokedex/bulbasaur")
print('Status Code: ' + str(page.status_code))

#Getting Pokemon Information
soup = BeautifulSoup(page.content, 'lxml')

#Getting Pokemon Name
div_name = soup.find('div', {'class' : 'pokedex-pokemon-pagination-title'})
print(div_name)

name = div_name.text.strip()
name = name.replace(" ","")
name_number = name.split("\n")
print(name_number)

#Getting Pokemon Type
div_type = soup.find('div', {'class' : 'dtm-type'})
types = div_type.text
types = types.split("\n")
types = list(filter(None, types))
print(types)