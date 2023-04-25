import copy
import pygame
import services.settings
import sprites.player
import sprites.projectile
import pygame_essentials.renderer


class GameLoop:
    def __init__(self, level, display, event_queue, clock):
        self._level = level
        self._display = display
        self._clock = clock
        self._event_queue = event_queue

        self.player1 = sprites.player.Player(
            [self._level.visible_sprites], 1, [5, 5,], [5, 5,])
        self.player2 = sprites.player.Player(
            [self._level.visible_sprites], 2, [10, 5,], [10, 5])

        self.game_map = copy.deepcopy(services.settings.MAP)
        self._level.create_map(self.game_map)
        self._level.update_map(self.player1, self.player2)

        self.current_turn = 1
        self.current_player = self.player1

        self.p1_projectile = sprites.projectile.Projectile()
        self.p2_projectile = sprites.projectile.Projectile()

        self.current_projectile = self.p1_projectile

        self._renderer = pygame_essentials.renderer.Renderer(
            display, self._level, self.p1_projectile, self.p2_projectile)
        self.turns = 30

    def start(self):
        while True:
            if self._handle_events() == False:
                break
            self._render()
            self._clock.tick(services.settings.FPS)

            if self.current_turn == 3:
                self.p1_projectile.move()
                self.p2_projectile.move()

    def _handle_events(self):
        if self.player1.reset_flag:
            self._level.reset_flag2(self.player1)
        if self.player2.reset_flag:
            self._level.reset_flag1(self.player2)

        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONUP and not self.current_player is None:
                pos = event.pos
                self.current_projectile.location = self.current_player.pos
                self.current_projectile.target_location = pos
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP and not self.current_player is None:
                    # only erase previous position if the action is to move
                    self.game_map[self.current_player.pos[1]
                                  ][self.current_player.pos[0]] = " "
                    self.current_player.move(self.game_map, "up")

                if event.key == pygame.K_DOWN and not self.current_player is None:
                    self.game_map[self.current_player.pos[1]
                                  ][self.current_player.pos[0]] = " "
                    self.current_player.move(self.game_map, "down")

                if event.key == pygame.K_LEFT and not self.current_player is None:
                    self.game_map[self.current_player.pos[1]
                                  ][self.current_player.pos[0]] = " "
                    self.current_player.move(self.game_map, "left")

                if event.key == pygame.K_RIGHT and not self.current_player is None:
                    self.game_map[self.current_player.pos[1]
                                  ][self.current_player.pos[0]] = " "
                    self.current_player.move(self.game_map, "right")

                if event.key == pygame.K_SPACE:
                    self._change_turns()
                # debug keybinds
                if event.key == pygame.K_m:
                    print(self.game_map)
                if event.key == pygame.K_f:
                    print(self.current_player, self.current_player.has_flag,
                          self.current_player.reset_flag)
                # show temporary player position on screen, even if player has not moved
                if not self.current_player is None:
                    self.game_map[self.current_player.pos[1]][self.current_player.pos[0]
                                                              ] = "p" + str(self.current_player.p1orp2)
                # update map after every action
                self._level.update_map(self.player1, self.player2)

    def _change_turns(self):
        if not self.current_player is None:
            self.game_map[self.current_player.pos[1]][self.current_player.pos[0]
                                                      ] = "p" + str(self.current_player.p1orp2)
        if self.current_turn == 1:
            self.current_turn = 2
            self.current_player = self.player2
        elif self.current_turn == 2:
            self.current_turn = 3
            self.current_player = None
        else:
            self.player1.apply_real_position()
            self.player2.apply_real_position()
            self.current_turn = 1
            self.current_player = self.player1
            self.turns -= 1

    def _render(self):
        self._renderer.render(self.turns, self.player1, self.player2)
