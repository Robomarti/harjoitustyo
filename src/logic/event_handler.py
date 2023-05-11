import pygame
import services.settings


def handle_events(game_loop):
    """A method that handles inputs from players and the resetting of the flags.

    Args:
        game_loop: A reference to the GameLoop class that is calling this method.
    """

    # pylint: disable=inconsistent-return-statements
    # According to the course material, this is a
    # good way of handling exit inputs. Also, if
    # the method returned a value for every event, it would exit
    # the for loop every time, resulting in some inputs such as
    # the close inputs to not work at all.

    if game_loop.player1.reset_flag:
        game_loop.level.reset_flag2(game_loop.player1)
    if game_loop.player2.reset_flag:
        game_loop.level.reset_flag1(game_loop.player2)

    for event in game_loop.event_queue.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONUP and not game_loop.current_player is None:
            pos = event.pos
            game_loop.current_projectile.location = [
                game_loop.current_player.pos[0] * services.settings.TILESIZE,
                game_loop.current_player.pos[1] * services.settings.TILESIZE]
            game_loop.current_projectile.target_location = [pos[0], pos[1]]
            game_loop.current_projectile.calculate_vector()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_n:
                return False
            if event.key == pygame.K_y:
                return True
            handle_key_ups(event, game_loop)

def handle_key_ups(event, game_loop):
    """A method that handles inputs that are the type of KEYUP from players.

    KEYUP means that the input is taken into consideration only when the the user
    lets go of the key, so that we don't get 60 or more inputs of the same key every second.

    Args:
        game_loop: A reference to the GameLoop class that is calling this method.
    """

    if event.key == pygame.K_UP and not game_loop.current_player is None:
        game_loop.game_map[game_loop.current_player.pos[1]
                           ][game_loop.current_player.pos[0]] = " "
        game_loop.current_player.move(game_loop.game_map, "up")

    if event.key == pygame.K_DOWN and not game_loop.current_player is None:
        game_loop.game_map[game_loop.current_player.pos[1]
                           ][game_loop.current_player.pos[0]] = " "
        game_loop.current_player.move(game_loop.game_map, "down")

    if event.key == pygame.K_LEFT and not game_loop.current_player is None:
        game_loop.game_map[game_loop.current_player.pos[1]
                           ][game_loop.current_player.pos[0]] = " "
        game_loop.current_player.move(game_loop.game_map, "left")

    if event.key == pygame.K_RIGHT and not game_loop.current_player is None:
        game_loop.game_map[game_loop.current_player.pos[1]
                           ][game_loop.current_player.pos[0]] = " "
        game_loop.current_player.move(game_loop.game_map, "right")

    if event.key == pygame.K_SPACE:
        game_loop.change_turns()

    if not game_loop.current_player is None:
        game_loop.game_map[game_loop.current_player.pos[1]]\
            [game_loop.current_player.pos[0]] = "p" + \
            str(game_loop.current_player.p1orp2)

    game_loop.level.update_map()
