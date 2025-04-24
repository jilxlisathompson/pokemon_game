def select_pokemon(my_pokemon_choice):
    # get pokemon using api call
    if valid:
        return pokemon
    else:
        return None

print("Select your pokemon!")
while True:
    pokemon_choice = input("Pokemon choice: ")
    selected_pokemon = select_pokemon(pokemon_choice)
    if selected_pokemon:
        break
    else:
        print("Invalid pokemon!")

