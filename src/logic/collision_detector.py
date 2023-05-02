import copy
import services.settings


def detect_collisions(player_one, player_two, projectile_one, projectile_two, game_map):
    """Detects whether or not any collision is happening between the projectiles, walls and players.

    Args:
        player_one: A reference to the first player.
        player_two: A reference to the second player.
        projectile_one: A reference to the projectile of the first player.
        projectile_two: A reference to the projectile of the first player.
        game_map: A reference to the game_map attribute of the GameLoop class.
    """

    projectile_one.move()
    projectile_two.move()
    projectile1_position = [int(projectile_one.location[0] / services.settings.TILESIZE),
                            int(projectile_one.location[1] / services.settings.TILESIZE)]
    projectile2_position = [int(projectile_two.location[0] / services.settings.TILESIZE),
                            int(projectile_two.location[1] / services.settings.TILESIZE)]

    if projectile2_position == player_one.real_pos:
        handle_player_death(game_map, player_one, projectile_two, "p1")

    if projectile1_position == player_two.real_pos:
        handle_player_death(game_map, player_two, projectile_one, "p2")

    if projectile_one.location[0] >= 0 and game_map[projectile1_position[1]]\
        [projectile1_position[0]] == "x":
        projectile_one.die()
    if projectile_two.location[0] >= 0 and game_map[projectile2_position[1]]\
        [projectile2_position[0]] == "x":
        projectile_two.die()

def handle_player_death(game_map, player, projectile, p1orp2: str):
    """Do the necessary actions when a projectile collides with a player

    Args:
        game_map: A reference to the game_map attribute of the GameLoop class.
        player: A reference to the player.
        projectile: A reference to the projectile that killed the player.
        p1orp2: A string to be used in the matrix represantation of the game_map.
    """

    game_map[player.pos[1]][player.pos[0]] = " "
    death_point = copy.deepcopy(player.pos)
    if p1orp2 == "p1":
        opponent_flag = "p2"
    else:
        opponent_flag = "p1"

    if player.has_flag:
        game_map[death_point[1]][death_point[0]] = opponent_flag + "flag"
        player.has_flag = False
    player.die()
    projectile.die()
    game_map[player.pos[1]][player.pos[0]] = p1orp2
