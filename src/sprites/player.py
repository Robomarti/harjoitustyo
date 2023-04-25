import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, p1orp2, pos, real_pos):
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
        self.has_flag = False
        self.reset_flag = False
        self.points = 0
        self.goal = "p"+str(self.p1orp2)+"gu" + "p" + \
            str(self.p1orp2)+"g" + "p"+str(self.p1orp2)+"gl"

    def move(self, game_map, direction):
        if direction == "up":
            wanted_pos = game_map[self.real_pos[1]-1][self.real_pos[0]]
            if wanted_pos in self.goal and self.has_flag:
                self.points += 1
                self.has_flag = False
                self.reset_flag = True
            else:
                can_move_to_wanted_pos = wanted_pos in " " + \
                    "p"+str(self.opponent_num)+"flag"
                if abs(self.pos[1] - self.real_pos[1]) == 0 and can_move_to_wanted_pos:
                    self.pos[1] -= 1
                    self.pos[0] = self.real_pos[0]

        elif direction == "down":
            wanted_pos = game_map[self.real_pos[1]+1][self.real_pos[0]]
            if wanted_pos in self.goal and self.has_flag:
                self.points += 1
                self.has_flag = False
                self.reset_flag = True
            else:
                can_move_to_wanted_pos = wanted_pos in " " + \
                    "p"+str(self.opponent_num)+"flag"
                if abs(self.pos[1] - self.real_pos[1]) == 0 and can_move_to_wanted_pos:
                    self.pos[1] += 1
                    self.pos[0] = self.real_pos[0]

        elif direction == "left":
            wanted_pos = game_map[self.real_pos[1]][self.real_pos[0]-1]
            if wanted_pos in self.goal and self.has_flag:
                self.points += 1
                self.has_flag = False
                self.reset_flag = True
            else:
                can_move_to_wanted_pos = wanted_pos in " " + \
                    "p"+str(self.opponent_num)+"flag"
                if abs(self.pos[0] - self.real_pos[0]) == 0 and can_move_to_wanted_pos:
                    self.pos[0] -= 1
                    self.pos[1] = self.real_pos[1]

        elif direction == "right":
            wanted_pos = game_map[self.real_pos[1]][self.real_pos[0]+1]
            if wanted_pos in self.goal and self.has_flag:
                self.points += 1
                self.has_flag = False
                self.reset_flag = True
            else:
                can_move_to_wanted_pos = wanted_pos in " " + \
                    "p"+str(self.opponent_num)+"flag"
                if abs(self.pos[0] - self.real_pos[0]) == 0 and can_move_to_wanted_pos:
                    self.pos[0] += 1
                    self.pos[1] = self.real_pos[1]

        else:
            wanted_pos = ""

        if wanted_pos == "p"+str(self.opponent_num)+"flag":
            self.has_flag = True

    def apply_real_position(self):
        self.real_pos = self.pos
