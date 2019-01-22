
import requests
from bs4 import BeautifulSoup

#Access Pokemon Page
page = requests.get("https://www.pokemon.com/us/pokedex/bulbasaur")
print('Status Code: ' + str(page.status_code))

#Getting Pokemon Information
soup = BeautifulSoup(page.content, 'lxml')

#Getting Pokemon Name
div_name = soup.find_all('div', {'class' : 'pokedex-pokemon-pagination-title'})
print(div_name)

test = BeautifulSoup(str(div_name),'lxml')
print(test)
#tag = test.find_all('div')
#print(tag.string)
