import requests

# This script houses the logic for the turn-based battle.

#Define game variables

player_health = 400 # Static for now
cpu_health = 300 # Static for now

#Pokemon object dict

#Tweaking this just so we have api calls in our running code

def fetch_pokemon_data(pokemon_id) -> dict:
    # This shouldn't be in the cli
    """Makes an api request to fetch the data for a pokemon,
     given either a numerical id or the pokemons name"""

    pokemon_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/')
    return pokemon_data.json()

def select_pokemon(pokemon_list = ('bulbasaur', 'charmander', 'squirtle')):
    player_selection = '-'
    while player_selection not in pokemon_list:
        print("Please enter a Pokemon from the list")
        [print(i) for i in pokemon_list]
        player_selection = input(">")

    chosen_pokemon = fetch_pokemon_data(player_selection)

    return chosen_pokemon


def create_pokemon_dict(pokemon:dict) -> dict:

    pokemon_dict = {
                "species": pokemon["name"].title(),
                "total_health": pokemon["stats"][0]["base_stat"]*10,
                "current_health": pokemon["stats"][0]["base_stat"]*10,
                "move_power": 100,
              }

    return pokemon_dict


player_pokemon_data = select_pokemon()
player_pokemon = create_pokemon_dict(player_pokemon_data)
player_pokemon["is_enemy"] = False

cpu_pokemon_data = fetch_pokemon_data("squirtle")
cpu_pokemon = create_pokemon_dict(cpu_pokemon_data)
cpu_pokemon["is_enemy"] = True


#Pokemon object dict
cpu_pokemon = {
                "is_enemy": True,
                "species": "Squirtle",
                "total_health": cpu_health,
                "current_health": cpu_health,
                "move_power": 70,
              }


def is_active(pokemon):
    if pokemon["current_health"] > 0:
        return True
    else:
        return False


    # attacker deals damage to defender
def attack(attacker, defender):
    # The actual damage calculation
    damage = attacker["move_power"]
    defender["current_health"] -= damage

    # Message formatting
    attacker_prefix = "The enemy" if attacker["is_enemy"] else "Your"
    defender_prefix = "your" if attacker["is_enemy"] else "the enemy"

    print(f"{attacker_prefix} {attacker['species']} attacks {defender_prefix} {defender['species']} for {damage} damage!")

def perform_player_turn():
    while True:
        # prompt player for decision
        print("What will " + player_pokemon["species"] + " do?")
        action = input("Options: Attack\n")
        if action.strip().lower() == "attack":
            attack(player_pokemon, cpu_pokemon)
            break
        else:
            print("Invalid input. Please try again.")

def print_health_status():
    print("\n--- End of Turn Report ---")
    print(f"{player_pokemon['species']} HP: {player_pokemon['current_health']}/{player_pokemon['total_health']}")
    print(f"{cpu_pokemon['species']} HP: {cpu_pokemon['current_health']}/{cpu_pokemon['total_health']}\n")

def battle(player_pokemon, cpu_pokemon):
    is_player_turn = True  # True: player's turn.  False: CPU's Turn
    ## Main battle loop
    while is_active(player_pokemon) and is_active(cpu_pokemon):
        if is_player_turn:
            perform_player_turn()
        else:
            attack(cpu_pokemon, player_pokemon)

        print_health_status()
        # Change turns
        is_player_turn = not is_player_turn

    if is_active(player_pokemon):
        print("You Win!")
    else:
        print("You Lose!")

battle(player_pokemon, cpu_pokemon)