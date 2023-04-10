import copy
import pygame
import settings
import sprites.player

class GameLoop:
    def __init__(self, level, display, renderer, event_queue, clock):
        self._level = level
        self._display = display
        self._renderer = renderer
        self._clock = clock
        self._event_queue = event_queue

        self.player1 = sprites.player.Player([self._level.visible_sprites], 1)
        self.player2 = sprites.player.Player([self._level.visible_sprites], 2)

        self.game_map = copy.deepcopy(settings.MAP)
        self._level.create_map()
        self._level.update_map(self.game_map, self.player1, self.player2)
        
        self.player1.real_pos = self.player1.pos
        self.player2.real_pos = self.player2.pos

        self.current_turn = 1
        self.current_player = self.player1

    def start(self):
        while True:
            if self._handle_events() == False:
                break
            self._render()
            self._clock.tick(settings.FPS)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    #only erase previous position if the action is to move
                    self.game_map[self.current_player.pos[1]][self.current_player.pos[0]] = " "
                    self.current_player.move(self.game_map, "up")

                if event.key == pygame.K_DOWN:
                    self.game_map[self.current_player.pos[1]][self.current_player.pos[0]] = " "
                    self.current_player.move(self.game_map, "down")

                if event.key == pygame.K_LEFT:
                    self.game_map[self.current_player.pos[1]][self.current_player.pos[0]] = " "
                    self.current_player.move(self.game_map, "left")

                if event.key == pygame.K_RIGHT:
                    self.game_map[self.current_player.pos[1]][self.current_player.pos[0]] = " "
                    self.current_player.move(self.game_map, "right")

                if event.key == pygame.K_SPACE:
                    self.current_player.apply_real_position()
                    self._change_turns()
                #debug keybinds
                if event.key == pygame.K_d:
                    self.current_player.apply_real_position()
                if event.key == pygame.K_m:
                    print(self.game_map)
                if event.key == pygame.K_p:
                    print(self.current_player,self.current_player.has_flag)
                #show temporary player position on screen, even if player has not moved
                self.game_map[self.current_player.pos[1]][self.current_player.pos[0]] = "p" + str(self.current_player.p1orp2)
                #update map after every action
                self._level.update_map(self.game_map, self.player1, self.player2)

    def _change_turns(self):
        self.game_map[self.current_player.pos[1]][self.current_player.pos[0]] = "p" + str(self.current_player.p1orp2)
        if self.current_turn == 1:
            self.current_turn = 2
            self.current_player = self.player2
        else:
            self.current_turn = 1
            self.current_player = self.player1

    def _render(self):
        self._renderer.render()
