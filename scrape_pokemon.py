
import requests
import time
from bs4 import BeautifulSoup


def main():
    print("Initialise Request")
    base_link = "https://www.pokemon.com/us/pokedex"
    pokemon_list = []
    result = request_result(base_link)

    if result[0] == 200:
        # Getting a list of links of pokemons
        soup = BeautifulSoup(result[1], 'lxml')
        pokemon_urls = []
        links = []

        # Finding all 'li tags' that contain 'a tags' with pokemon links in format /us/pokedex/<pokemon name>
        li = soup.find_all('li')
        for li_tags in li:
            a = li_tags.find('a')
            if a is not None and 'href' in a.attrs:
                link = a.attrs['href']
                links.append(link)

        # From all links extract links with pokedex only i.e. it is a valid link to a pokemon entry
        for link in links:
            if link.find('pokedex') >= 0:
                pokemon_urls.append(link)

        print(pokemon_urls)
        print(len(pokemon_urls))

        # Extract pokemon information from each page with 2 second delay between each entry for safety
        for i in range(1, 10):
            url = "https://www.pokemon.com"+pokemon_urls[i]
            print(url)
            pokemon_results = request_result(url)

            if pokemon_results[0] == 200:
                pokemon_soup = BeautifulSoup(pokemon_results[1], 'lxml')
                pokemon_list.append(extract_pokemon_data(pokemon_soup))
                time.sleep(2)

        print(pokemon_list)

    else:
        print("Error Status Code: " + str(result[0]))


def request_result(url):
    # Access Pokemon Page
    page = requests.get(url)
    print('Status Code: ' + str(page.status_code))
    result = [page.status_code, page.content]
    return result


def extract_pokemon_data(soup):
    # Getting Pokemon Name
    div_name = soup.find('div', {'class' : 'pokedex-pokemon-pagination-title'})
    # print(div_name)

    name = div_name.text.strip()
    name = name.replace(" ","")
    name_number = name.split("\n")
    # print(name_number)

    # Getting Pokemon Type
    div_type = soup.find('div', {'class' : 'dtm-type'})
    types = div_type.text
    types = types.split("\n")
    types = list(filter(None, types))
    # print(types)

    return name_number + types


main()
