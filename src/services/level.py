import pygame
import services.settings
import sprites.tile
import sprites.flag


class Level:
    """A class that constructs and updates the map in a matrix form.

    Attributes:
        all_sprites: A group of sprites that should be drawn
        game_map: A reference to the game_map attribute of the GameLoop class.
        flag_1: A reference to the first player's flag.
        flag_1_original_coordinates. The original location of the first player's flag.
        flag_2: A reference to the second player's flag.
        flag_2_original_coordinates. The original location of the second player's flag.

    """

    def __init__(self):
        """A constructor that creates a new level.

        """

        self.all_sprites = pygame.sprite.Group()
        self.game_map = None
        self.flag_1 = None
        self.flag_1_original_coordinates = []
        self.flag_2 = None
        self.flag_2_original_coordinates = []
        self.player_one = None
        self.player_two = None

    def create_map(self, game_map, player_one, player_two):
        """Creates a new map for the level from a given matrix.

        Creates new instances of sprites for the walls of the map, for the goals, and for the flags.
        Also saves the respawn points for the players.

        Args:
            game_map: A reference to the game_map attribute of the GameLoop class.
            player_one: : A reference to the player1 attribute of the GameLoop class.
            player_two: : A reference to the player2 attribute of the GameLoop class.
        """

        self.player_one = player_one
        self.player_two = player_two
        self.game_map = game_map
        height = len(self.game_map)
        width = len(self.game_map[0])
        for i in range(height):
            for j in range(width):
                x_coordinate = j * services.settings.TILESIZE
                y_coordinate = i * services.settings.TILESIZE
                self.create_assets(i, j, x_coordinate, y_coordinate)

    def create_assets(self, i, j, x_coordinate, y_coordinate):
        """Creates new sprites (graphics) for the map.
        Also sets the respawn positions for the players and flags.

        Args:
            i: the y-coordinate where the object should be checked from game_map.
            j: the x-coordinate where the object should be checked from game_map.
            x_coordinate: the y-coordinate where the sprite should be spawned.
            y_coordinate: the x-coordinate where the sprite should be spawned.
        """

        # pylint: disable=too-many-statements
        # All the statements are needed, and there is little
        # point in making another method using them.

        if self.game_map[i][j] == "x":
            sprites.tile.Tile((x_coordinate, y_coordinate), [self.all_sprites], 1)
        elif self.game_map[i][j] == "p1":
            self.player_one.original_position = [j, i]
        elif self.game_map[i][j] == "p2":
            self.player_two.original_position = [j, i]
        elif self.game_map[i][j] == "p1gu":
            sprites.tile.Tile((x_coordinate, y_coordinate), [self.all_sprites], 2)
        elif self.game_map[i][j] == "p1g":
            sprites.tile.Tile((x_coordinate, y_coordinate), [self.all_sprites], 3)
        elif self.game_map[i][j] == "p1gl":
            sprites.tile.Tile((x_coordinate, y_coordinate), [self.all_sprites], 4)
        elif self.game_map[i][j] == "p2gu":
            sprites.tile.Tile((x_coordinate, y_coordinate), [self.all_sprites], 5)
        elif self.game_map[i][j] == "p2g":
            sprites.tile.Tile((x_coordinate, y_coordinate), [self.all_sprites], 6)
        elif self.game_map[i][j] == "p2gl":
            sprites.tile.Tile((x_coordinate, y_coordinate), [self.all_sprites], 7)
        elif self.game_map[i][j] == "p1flag":
            self.flag_1 = sprites.flag.Flag([x_coordinate, y_coordinate,], [self.all_sprites], 1)
            self.flag_1_original_coordinates = [i, j]
        elif self.game_map[i][j] == "p2flag":
            self.flag_2 = sprites.flag.Flag([x_coordinate, y_coordinate,], [self.all_sprites], 2)
            self.flag_2_original_coordinates = [i, j]

    def update_map(self):
        """Updates the locations of players and flags on the map.

        Args:
            player_one: : A reference to the player1 attribute of the GameLoop class.
            player_two: : A reference to the player2 attribute of the GameLoop class.
        """

        height = len(self.game_map)
        width = len(self.game_map[0])
        for i in range(height):
            for j in range(width):
                if self.game_map[i][j] == "p1":
                    self.update_player(self.player_one, 1, j, i)
                elif self.game_map[i][j] == "p2":
                    self.update_player(self.player_two, 2, j, i)
                elif self.game_map[i][j] == "p1flag":
                    self.update_flags(self.flag_1, j, i)
                elif self.game_map[i][j] == "p2flag":
                    self.update_flags(self.flag_2, j, i)

    def update_player(self, player, p1orp2, j, i):
        """Updates the player's location on the screen.

        Args:
            player: A reference to the player.
            p1orp2: A number used to identify the player.
            j: The player's locations x-coordinate.
            i: The player's locations y-coordinate.
        """

        if p1orp2 == 1:
            flag = self.flag_2
        else:
            flag = self.flag_1

        player.pos = [j, i,]
        render_pos_x = player.rendering_pos[0] * services.settings.TILESIZE
        render_pos_y = player.rendering_pos[1] * services.settings.TILESIZE
        player.rect.topleft = (render_pos_x, render_pos_y)
        if player.has_flag:
            flag.current_position = [j, i,]
            flag.rect.topleft = (render_pos_x, render_pos_y)

    def update_flags(self, flag, j, i):
        """Updates the flags location on the screen.

        Args:
            flag: A reference to the flag.
            j: The flag's locations x-coordinate.
            i: The flag's locations y-coordinate.
        """

        x_coordinate = j * services.settings.TILESIZE
        y_coordinate = i * services.settings.TILESIZE
        flag.current_position = [j, i,]
        flag.rect.topleft = (x_coordinate, y_coordinate)

    def reset_flag1(self, player_two):
        """Relocates the first player's flag to its original location.

        Args:
            player_two: : A reference to the player2 attribute of the GameLoop class.
        """

        self.flag_1.current_position = self.flag_1.original_position
        x_coordinate = self.flag_1_original_coordinates[0]
        y_coordinate = self.flag_1_original_coordinates[1]
        self.game_map[x_coordinate][y_coordinate] = "p1flag"
        player_two.reset_flag = False

    def reset_flag2(self, player_one):
        """Relocates the second player's flag to its original location.

        Args:
            player_one: : A reference to the player1 attribute of the GameLoop class.
        """

        self.flag_2.current_position = self.flag_2.original_position
        x_coordinate = self.flag_2_original_coordinates[0]
        y_coordinate = self.flag_2_original_coordinates[1]
        self.game_map[x_coordinate][y_coordinate] = "p2flag"
        player_one.reset_flag = False
