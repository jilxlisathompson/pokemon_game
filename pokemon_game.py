import requests
import json

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list[:3]:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
player_url = f'https://pokeapi.co/api/v2/pokemon/{choice}/'
player_response = requests.get(url)
player_pokemon_data = json.loads(response.text)
player_move_power = 40


#Tell the player what pokemon they've picked
print('Name: {}'.format(player_pokemon_data['name']))


#pick a pokemon for the cpu, and make relevant api calls
cpu_pokemon_name = 'rattata'
cpu_url = f'https://pokeapi.co/api/v2/pokemon/{cpu_pokemon_name}/'
cpu_response = requests.get(cpu_url)
cpu_pokemon_data = json.loads(response.text)
cpu_move_power = 40


