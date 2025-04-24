# This script houses the logic for the turn-based battle.



#Define game variables

player_health = 400 # Static for now
cpu_health = 300 # Static for now
is_player_turn = True # True: player's turn.  False: CPU's Turn

#Pokemon object dict
player_pokemon = {
                "is_enemy": False,
                "species": "Bulbasaur",
                "total_health": player_health,
                "current_health": player_health,
                "move_power": 100,
              }

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
        action = input()
        if action == "attack":
            attack(player_pokemon, cpu_pokemon)
            break
        else:
            print("Invalid input. Please try again.")

def print_health_status():
    print("\n--- End of Turn Report ---")
    print(f"{player_pokemon['species']} HP: {player_pokemon['current_health']}/{player_pokemon['total_health']}")
    print(f"{cpu_pokemon['species']} HP: {cpu_pokemon['current_health']}/{cpu_pokemon['total_health']}\n")

def battle(player_pokemon, cpu_pokemon):
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
