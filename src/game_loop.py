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
                self.game_map[self.current_player.pos[1]][self.current_player.pos[0]] = " "
                if event.key == pygame.K_UP:
                    self.current_player.move(self.game_map, "up")
                if event.key == pygame.K_DOWN:
                    self.current_player.move(self.game_map, "down")
                if event.key == pygame.K_LEFT:
                    self.current_player.move(self.game_map, "left")
                if event.key == pygame.K_RIGHT:
                    self.current_player.move(self.game_map, "right")
                if event.key == pygame.K_SPACE:
                    self.current_player.apply_real_position()
                    self._change_turns()
                if event.key == pygame.K_d:
                    self.current_player.apply_real_position()
                self.game_map[self.current_player.pos[1]][self.current_player.pos[0]] = "p" + str(self.current_player.p1orp2)
                self._level.update_map(self.game_map, self.player1, self.player2)

    def _change_turns(self):
        if self.current_turn == 1:
            self.current_turn = 2
            self.current_player = self.player2
        else:
            self.current_turn = 1
            self.current_player = self.player1

    def _render(self):
        self._renderer.render()
