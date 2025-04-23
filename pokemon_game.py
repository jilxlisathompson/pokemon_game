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
url = f'https://pokeapi.co/api/v2/pokemon/{choice}/'
response = requests.get(url)
player_pokemon_data = json.loads(response.text)

# to get ability
# abilities = pokemon_data['abilities'][0]
# ability = abilities['ability']
#
# # to format height and weight properly
# height = int(pokemon_data['height'])
# weight = int(pokemon_data['weight'])
#
# height_formatted = height / 10
# weight_formatted = weight / 10

# Print the pokemon's data
# print('Weight: {}'.format(weight_formatted) + "(kgs)")
# print('Height: {}'.format(height_formatted) + "(m)")
# print('Ability: {}'.format(ability['name']))

print('Name: {}'.format(player_pokemon_data['name']))

cpu_pokemon_name = 'rattata'
cpu_url = f'https://pokeapi.co/api/v2/pokemon/{cpu_pokemon_name}/'
cpu_response = requests.get(cpu_url)
cpu_pokemon_data = json.loads(response.text)