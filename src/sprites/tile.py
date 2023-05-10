import pygame


class Tile(pygame.sprite.Sprite):
    """A sprite for displaying the walls and goals of the map.    
    """

    def __init__(self, position, groups, image_num):
        """The constructor of the class

        Args:
            position: The position where the sprite should be drawn.
            groups: An array of the sprite groups that the flag should be a part of.
            image_num: Tells which image should be drawn.
        """

        super().__init__(groups)
        if image_num == 1:
            self.image = pygame.image.load(
                "src/assets/wall.png").convert_alpha()
        elif image_num == 2:
            self.image = pygame.image.load(
                "src/assets/p1gUp.png").convert_alpha()
        elif image_num == 3:
            self.image = pygame.image.load(
                "src/assets/p1gMid.png").convert_alpha()
        elif image_num == 4:
            self.image = pygame.image.load(
                "src/assets/p1gLow.png").convert_alpha()
        elif image_num == 5:
            self.image = pygame.image.load(
                "src/assets/p2gUp.png").convert_alpha()
        elif image_num == 6:
            self.image = pygame.image.load(
                "src/assets/p2gMid.png").convert_alpha()
        else:
            self.image = pygame.image.load(
                "src/assets/p2gLow.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
