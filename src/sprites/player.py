import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, p1orp2):
        super().__init__(groups)
        self.p1orp2 = p1orp2
        if p1orp2 == 1:
            self.image = pygame.image.load("src/assets/p1.png").convert_alpha()
        else:
            self.image = pygame.image.load("src/assets/p2.png").convert_alpha()

        self.rect = self.image.get_rect(topleft=(0, 0))
        self.pos = [0, 0,]
        self.real_pos = [0, 0,]

    def move(self, game_map, direction):
        if direction == "up":
            if abs(self.pos[1] - self.real_pos[1]) == 0 and game_map[self.pos[1]-1][self.pos[0]] == " ":
                self.pos[1] -= 1
                self.pos[0] = self.real_pos[0]

        if direction == "down":
            if abs(self.pos[1] - self.real_pos[1]) == 0 and game_map[self.pos[1]+1][self.pos[0]] == " ":
                self.pos[1] += 1
                self.pos[0] = self.real_pos[0]

        if direction == "left":
            if abs(self.pos[0] - self.real_pos[0]) == 0 and game_map[self.pos[1]][self.pos[0]-1] == " ":
                self.pos[0] -= 1
                self.pos[1] = self.real_pos[1]

        if direction == "right":
            if abs(self.pos[0] - self.real_pos[0]) == 0 and game_map[self.pos[1]][self.pos[0]+1] == " ":
                self.pos[0] += 1
                self.pos[1] = self.real_pos[1]

    def apply_real_position(self):
        self.real_pos = self.pos
