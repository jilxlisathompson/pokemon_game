import pokemon_game as pg
import game_cli

#setting health to be static for now
player_health = 400
cpu_health = 300

#creating dict for player pokemon information
player_pokemon = {
                "total_health": player_health,
                "current_health": player_health,
                "move_power": pg.player_move_power,
              }

#creating dict for cpu pokemon information
cpu_pokemon = {
                "total_health": cpu_health,
                "current_health": cpu_health,
                "move_power": pg.cpu_move_power,
              }

#While loop to evaluate the status of the battle
while (player_pokemon["current_health"] > 0) and \
      (cpu_pokemon["current_health"] > 0):

    #player makes move
    character_does_damage()

    cpu_chooses_move()
    character_does_damage()

    #cpu makes move
    #evaluate cpu action


if player_pokemon["current_health"] <= 0:
    print("Oh no you lost!")

if cpu_pokemon["current_health"] <= 0:
    print("Congrats you won!")

exit()