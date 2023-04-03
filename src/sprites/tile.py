import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups, imgNum):
        super().__init__(groups)
        if imgNum == 1:
            self.image = pygame.image.load("src/assets/wall.png").convert_alpha()
        elif imgNum == 2:
            self.image = pygame.image.load("src/assets/p1gUp.png").convert_alpha()
        elif imgNum == 3:
            self.image = pygame.image.load("src/assets/p1gMid.png").convert_alpha()
        elif imgNum == 4:
            self.image = pygame.image.load("src/assets/p1gLow.png").convert_alpha()
        elif imgNum == 5:
            self.image = pygame.image.load("src/assets/p2gUp.png").convert_alpha()
        elif imgNum == 6:
            self.image = pygame.image.load("src/assets/p2gMid.png").convert_alpha()
        elif imgNum == 7:
            self.image = pygame.image.load("src/assets/p2ggLow.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)