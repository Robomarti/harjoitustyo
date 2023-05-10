import pygame


class Flag(pygame.sprite.Sprite):
    """A class responsible for moving the image of the flag.

    Args:
        image: A reference to the image of the flag.
        original_location: A reference to the respawn location of the flag.
        current_position: The current location in an array form. Used to draw the flag.
        rect: A reference to the pygame object responsible for storing rectangular coordinates.
    """

    def __init__(self, location, groups, image_num):
        """The constructor of the class.

        Args:
            location: The first place where the flag spawns, and its respawn location.
            groups: An array of the sprite groups that the flag should be a part of.
            image_num: A number that is used to determine which flag image should be 
            used for this instance of the class.
        """

        super().__init__(groups)
        if image_num == 1:
            self.image = pygame.image.load(
                "src/assets/p1flag.png")
        else:
            self.image = pygame.image.load(
                "src/assets/p2flag.png")
        self.original_position = location
        self.current_position = [location[0], location[1]]
        self.rect = self.image.get_rect(topleft=location)
