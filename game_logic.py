import pokemon_game as pg

player_health = 400
cpu_health = 300


player_pokemon = {
                "total_health": player_health,
                "current_health": player_health,
                "move_power": pg.player_move_power,
              }


cpu_pokemon = {
                "total_health": cpu_health,
                "current_health": cpu_health,
                "move_power": pg.cpu_move_power,
              }

#