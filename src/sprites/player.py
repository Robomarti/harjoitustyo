import pygame


class Player(pygame.sprite.Sprite):
    """A class that represents the player, and handles the movement and points of the player.
    
    Attributes:
        p1orp2: Tells which player this instance represents.
        image: A reference to the image file for the player.
        opponent_num: Tells which player this instance does not represent.
        name: The name of the player. This is displayed to the screen.
        rect: A reference to the pygame object responsible for storing rectangular coordinates.
        pos: The current location in an array form.
        real_pos: Saved position of where the player was before making their move.
        rendering_pos: The location of the player that is shown to both players.
        has_flag: Whether the player has the opponents flag currently or not.
        reset_flag: Whether the flag the player is carrying should be respawned or not.
        can_move: Whether the player can move or not. Used to stop movement after gaining a point.
        points: How many points the player has gathered in the current game.
        goal: Tells which tiles are the player's own goal.
        original_position: The coordinates where the player should be respawned.
    """

    # pylint: disable=too-many-instance-attributes
    # I need all of the attributes in order to make the game run.

    def __init__(self, groups, p1orp2, pos, real_pos):
        """The constructor of the class

        Args:
            groups: An array of the sprite groups that the flag should be a part of.
            p1orp2: A number used to identify the player.
            pos: The current location in an array form.
            real_pos: Saved position of where the player was before making their move.
        """

        super().__init__(groups)
        self.p1orp2 = p1orp2
        if p1orp2 == 1:
            self.image = pygame.image.load("src/assets/p1.png")
            self.opponent_num = 2
        else:
            self.image = pygame.image.load("src/assets/p2.png")
            self.opponent_num = 1

        self.rect = self.image.get_rect(topleft=(0, 0))
        self.pos = pos
        self.real_pos = real_pos
        self.rendering_pos = pos
        self.has_flag = False
        self.reset_flag = False
        self.can_move = True
        self.points = 0
        self.goal = "p"+str(self.p1orp2)+"gu" + "p" + \
            str(self.p1orp2)+"g" + "p"+str(self.p1orp2)+"gl"
        self.original_position = [0, 0]

    def move(self, game_map, direction):
        """Handles moving players and capturing the flag.

        Args:
            game_map: A reference to the game_map attribute of the GameLoop class.
            direction: A string that tells the direction of where the player should move.
        """

        if direction == "up":
            wanted_pos = self._move_up(game_map)
        elif direction == "down":
            wanted_pos = self._move_down(game_map)
        elif direction == "left":
            wanted_pos = self._move_left(game_map)
        elif direction == "right":
            wanted_pos = self._move_right(game_map)
        else:
            wanted_pos = ""

        if wanted_pos == "p"+str(self.opponent_num)+"flag":
            self.has_flag = True

    def _move_up(self, game_map):
        """Handles the logic of moving in the upwards direction.
        First it checks what object is on the spot that the player wants to
        move to. Then it checks if the object is one of the objects that the
        player may move to. Finally it adds a point to the player if the player
        moved to a goal and adjusts the players position.

        Args:
            game_map: A reference to the game_map attribute of the GameLoop class.
        """

        wanted_pos = game_map[self.real_pos[1]-1][self.real_pos[0]]
        can_move_to_wanted_pos = self.can_move and \
            wanted_pos in " "+"p"+str(self.opponent_num)+"flag"
        if wanted_pos in self.goal and self.has_flag:
            self.add_point()
        elif abs(self.pos[1] - self.real_pos[1]) == 0 and can_move_to_wanted_pos:
            self.pos[1] -= 1
            self.pos[0] = self.real_pos[0]
        return wanted_pos

    def _move_down(self, game_map):
        """Check the documentation on the _move_up() method.
        """

        wanted_pos = game_map[self.real_pos[1]+1][self.real_pos[0]]
        can_move_to_wanted_pos = self.can_move and \
            wanted_pos in " "+"p"+str(self.opponent_num)+"flag"
        if wanted_pos in self.goal and self.has_flag:
            self.add_point()
        elif abs(self.pos[1] - self.real_pos[1]) == 0 and can_move_to_wanted_pos:
            self.pos[1] += 1
            self.pos[0] = self.real_pos[0]
        return wanted_pos

    def _move_left(self, game_map):
        """Check the documentation on the _move_up() method.
        """

        wanted_pos = game_map[self.real_pos[1]][self.real_pos[0]-1]
        can_move_to_wanted_pos = self.can_move and \
            wanted_pos in " "+"p"+str(self.opponent_num)+"flag"
        if wanted_pos in self.goal and self.has_flag:
            self.add_point()
        elif abs(self.pos[0] - self.real_pos[0]) == 0 and can_move_to_wanted_pos:
            self.pos[0] -= 1
            self.pos[1] = self.real_pos[1]
        return wanted_pos

    def _move_right(self, game_map):
        """Check the documentation on the _move_up() method.
        """

        wanted_pos = game_map[self.real_pos[1]][self.real_pos[0]+1]
        can_move_to_wanted_pos = self.can_move and \
            wanted_pos in " "+"p"+str(self.opponent_num)+"flag"
        if wanted_pos in self.goal and self.has_flag:
            self.add_point()
        elif abs(self.pos[0] - self.real_pos[0]) == 0 and can_move_to_wanted_pos:
            self.pos[0] += 1
            self.pos[1] = self.real_pos[1]
        return wanted_pos

    def add_point(self):
        """Handles the addition of points to the player.
        If the player takes the flag to the goal, they should not
        be able to move anymore on their turn.
        """

        self.points += 5
        self.has_flag = False
        self.reset_flag = True
        self.can_move = False

    def add_point_from_a_kill(self):
        """Handles the addition of points to the player when killing the enemy.
        """
        self.points += 1

    def die(self):
        """Respawns the player to their respawn point.
        """

        self.pos = self.original_position
        self.apply_real_position()

    def apply_real_position(self):
        """Makes sure that the player starts their turn in the correct position.
        Also makes sure that the player can move at the start of their turn.
        """

        self.real_pos = self.pos
        self.can_move = True
