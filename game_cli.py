import pprint
import requests

def enter_to_continue():
    input("Press ENTER to continue.")
    return

def greeting():
    print("Hello! Welcome to the game.")
    enter_to_continue()
    return

def select_move():
    input("You're going to select tackle.")
    player_choice = 'tackle'
    return player_choice

def select_pokemon(pokemon_list = ('bulbasaur', 'charmander', 'squirtle')):
    player_selection = '-'
    while player_selection not in pokemon_list:
        input("Please enter a Pokemon from the list")
        pprint.pp(pokemon_list)

    player_pokemon = fetch_pokemon_data(player_selection)

    return player_pokemon


def fetch_pokemon_data(pokemon_id) -> dict:

    """Makes an api request to fetch the data for a pokemon,
     given either a numerical id or the pokemons name"""

    pokemon_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/')

    return pokemon_data.json()


