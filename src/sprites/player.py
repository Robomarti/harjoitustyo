import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, p1orp2):
        super().__init__(groups)
        self.p1orp2 = p1orp2
        if p1orp2 == 1:
            self.image = pygame.image.load("src/assets/p1.png").convert_alpha()
        else:
            self.image = pygame.image.load("src/assets/p2.png").convert_alpha()
        
        self.rect = self.image.get_rect(topleft = (0,0))
        self.pos = [0,0,]
        self.may_move = True
    
    def move(self, map,direction):
        map[self.pos[1]][self.pos[0]] = " "
        if direction == "up":
            if self.pos[1] - 2 in range(len(map)) and map[self.pos[1]-1][self.pos[0]] == " ":
                self.pos[1] -= 1
                return True
            return False

        if direction == "down":
            if self.pos[1] + 2 in range(len(map)) and map[self.pos[1]+1][self.pos[0]] == " ":
                self.pos[1] += 1
                return True
            return False

        if direction == "left":
            if self.pos[0] - 2 in range(len(map[0])) and map[self.pos[1]][self.pos[0]-1] == " ":
                self.pos[0] -= 1
                return True
            return False

        if direction == "right":
            if self.pos[0] + 2 in range(len(map[0])) and map[self.pos[1]][self.pos[0]+1] == " ":
                self.pos[0] += 1
                return True
            return False

        
        

            
        