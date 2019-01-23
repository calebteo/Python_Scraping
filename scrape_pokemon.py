
import requests
from bs4 import BeautifulSoup

def main():
    print("Initalise Request")
    result = request_result("us/pokedex/bulbasaur")

    if result[0] == 200 :
        print("Extracting Data")
        # Getting Pokemon Information
        soup = BeautifulSoup(result[1], 'lxml')
        pokemonlist = extract_pokemon_data(soup)
        print(pokemonlist)

    else :
        print("Error Status Code: " + str(result[0]))

def request_result(url):
    #Access Pokemon Page
    page = requests.get("https://www.pokemon.com/" + url)
    print('Status Code: ' + str(page.status_code))
    result = [page.status_code, page.content]
    return result


def extract_pokemon_data(soup) :
    #Getting Pokemon Name
    div_name = soup.find('div', {'class' : 'pokedex-pokemon-pagination-title'})
    #print(div_name)

    name = div_name.text.strip()
    name = name.replace(" ","")
    name_number = name.split("\n")
    #print(name_number)

    #Getting Pokemon Type
    div_type = soup.find('div', {'class' : 'dtm-type'})
    types = div_type.text
    types = types.split("\n")
    types = list(filter(None, types))
    #print(types)

    return name_number + types

main()