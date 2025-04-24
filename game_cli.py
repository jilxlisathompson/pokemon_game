import pprint

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


    #is there a fetch function i can put here?

    return player_selection


