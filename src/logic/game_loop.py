import copy
from logic.collision_detector import detect_collisions
from logic.event_handler import handle_events
import services.settings
import sprites.player
import sprites.projectile
import pygame_essentials.renderer


class GameLoop:
    """A class that repeats necessary actions until the game ends

    Attributes:
        level: A reference to the Level class responsible for upkeeping the game map.
        _display: A reference to pygame's display module, used for controlling the game window.
        _clock: A reference to the Clock class.
        event_queue: A reference to a component that collects and returns all inputs.
        player1: A reference to the class responsible for the first player.
        player2: A reference to the class responsible for the second player.
        p1_projectile: A reference to the class responsible for the first player's projectiles.
        p2_projectile:  A reference to the class responsible for the second player's projectiles.
        game_map: A copied version of the level map that is imported from the settings file.
        current_turn: Keeps track of which phase of the turn is going on currently.
        current_player: Keeps track of which player the inputs should reference to.
        current_projectile: Keeps track of which player's projectile the inputs should reference to.
        _renderer: A reference to the class responsible for rendering images to the screen.
        turns: Keeps track of how many turns are left until the end of the game.
    """

    # pylint: disable=too-many-instance-attributes
    # I need all of the attributes in order to make the game run.

    def __init__(self, level, display, event_queue, clock):
        """The constructor of the class

        Args:
            level: A reference to the Level class.
            display: A reference to the display module.
            event_queue: A reference to the EventQueue class.
            clock: A reference to the Clock class.
        """

        self.level = level
        self._display = display
        self._clock = clock
        self.event_queue = event_queue

        self.player1 = sprites.player.Player(
            [self.level.all_sprites], 1, [5, 5,], [5, 5,])
        self.player2 = sprites.player.Player(
            [self.level.all_sprites], 2, [10, 5,], [10, 5])
        self.p1_projectile = sprites.projectile.Projectile()
        self.p2_projectile = sprites.projectile.Projectile()

        self.game_map = copy.deepcopy(services.settings.MAP)
        self.level.create_map(self.game_map, self.player1, self.player2)
        self.level.update_map()

        self.current_turn = 1
        self.current_player = self.player1
        self.current_projectile = self.p1_projectile

        self._renderer = pygame_essentials.renderer.Renderer(
            display, self.level, self.p1_projectile, self.p2_projectile)
        self.turns = 30

    def start(self):
        """The main loop that keeps the application running.

        Certain inputs will close the application by breaking out of the while statement.
        """

        while True:
            if handle_events(self) == False:  # pylint: disable=singleton-comparison
                break
            self._render()
            self._clock.tick(services.settings.FPS)

            if self.current_turn == 3:
                detect_collisions(
                    self.player1, self.player2, self.p1_projectile,
                    self.p2_projectile, self.game_map)
                self.level.update_map()

    def change_turns(self):
        """Changes the current phase of the turn, or changes the turn to the next one.

        """

        if not self.current_player is None:
            self.game_map[self.current_player.pos[1]][self.current_player.pos[0]
                                                      ] = "p" + str(self.current_player.p1orp2)
        if self.current_turn == 1:
            self.current_turn = 2
            self.current_player = self.player2
            self.current_projectile = self.p2_projectile
        elif self.current_turn == 2:
            self.current_turn = 3
            self.current_player = None
            self.player1.apply_real_position()
            self.player2.apply_real_position()
        else:
            self.current_turn = 1
            self.current_player = self.player1
            self.current_projectile = self.p1_projectile
            self.turns -= 1

    def _render(self):
        """Renders images to the screen.

        """

        self._renderer.render(self.turns, self.player1, self.player2)
