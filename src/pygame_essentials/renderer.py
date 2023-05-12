import pygame
import ui.uiLayer
import services.settings


class Renderer:
    """The class responsible for displaying and updating different images.

    Attributes:
        _display: A reference to pygame's display module, used for controlling the game window.
        _level: A reference to the Level class responsible for upkeeping the game map.
        _p1_projectile: A reference to the class responsible for the first player's projectiles.
        _p2_projectile:  A reference to the class responsible for the second player's projectiles.
    """

    def __init__(self, display, level, p1_projectile, p2_projectile):
        """The constructor of the class

        Args:
            display: A reference to the display module.
            level: A reference to the Level class.
            p1_projectile: A reference to the class responsible for the first player's projectiles.
            p2_projectile: A reference to the class responsible for the second player's projectiles.
        """

        self._display = display
        self._level = level
        self._p1_projectile = p1_projectile
        self._p2_projectile = p2_projectile
        self._p1_name = services.settings.PLAYER1_NAME
        self._p2_name = services.settings.PLAYER2_NAME

    def render_game(self, turns, player_one, player_two):
        """Draws the projectiles, sprites under the all_sprites group, and the text on the screen.

        Args:
            turns: An integer telling how many turns are left.
            player_one: A reference to the first player.
            player_two: A reference to the second player.
        """

        self._display.fill("black")
        self._level.all_sprites.draw(self._display)
        pygame.draw.circle(self._display, self._p1_projectile.color,
                           self._p1_projectile.location, self._p1_projectile.radius)
        pygame.draw.circle(self._display, self._p2_projectile.color,
                           self._p2_projectile.location, self._p2_projectile.radius)
        ui.uiLayer.showText("Turns left: " + str(turns), 20, 450)
        ui.uiLayer.showText(str(self._p1_name) + "'s points: " +
                            str(player_one.points), 20, 100)
        ui.uiLayer.showText(str(self._p2_name) + "'s points: " +
                            str(player_two.points), 20, 750)
        pygame.display.update()

    def render_game_over(self, player_one, player_two):
        """Renders a simple image to the screen telling which player won.
        """

        if player_one.points > player_two.points:
            image = pygame.image.load("src/assets/p1_win_image.png").convert()
        elif player_one.points < player_two.points:
            image = pygame.image.load("src/assets/p2_win_image.png").convert()
        else:
            image = pygame.image.load("src/assets/tie_image.png").convert()
        self._display.blit(image, (0,0))
        pygame.display.update()

    def render_play_again(self):
        """Renders a simple image to the screen asking if the players want to play again.
        """

        image = pygame.image.load("src/assets/play_again_image.png").convert()
        self._display.blit(image, (0,0))
        pygame.display.update()

    def render_player_one_turn(self):
        """Renders a simple image to the screen telling that it's the first player's
        turn.
        """

        image = pygame.image.load("src/assets/p1_turn_image.png").convert()
        self._display.blit(image, (0,0))
        pygame.display.update()

    def render_player_two_turn(self):
        """Renders a simple image to the screen telling that it's the second player's
        turn.
        """

        image = pygame.image.load("src/assets/p2_turn_image.png").convert()
        self._display.blit(image, (0,0))
        pygame.display.update()
