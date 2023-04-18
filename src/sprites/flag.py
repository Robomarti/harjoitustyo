import pygame

class Flag(pygame.sprite.Sprite):
    def __init__(self, position, groups, image_num):
        super().__init__(groups)
        if image_num == 1:
            self.image = pygame.image.load(
                "src/assets/p1flag.png")
        else:
            self.image = pygame.image.load(
                "src/assets/p2flag.png")
        self.original_position = position
        self.current_position = [position[0],position[1]]
        self.rect = self.image.get_rect(topleft=position)