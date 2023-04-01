import pygame, sys, copy
import services.settings
import ui.uiLayer
import repositories.level

import sprites.player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((services.settings.WIDTH, services.settings.HEIGHT))
        pygame.display.set_caption("Capture The Flag")
        self.clock = pygame.time.Clock()

        self.level = repositories.level.Level()

        self.turns = copy.copy(services.settings.TURNS)

        self.player1 = sprites.player.Player([self.level.visible_sprites],1)
        self.player2 = sprites.player.Player([self.level.visible_sprites],2)
        
        self.current_turn = 1
        self.map = copy.deepcopy(services.settings.MAP)
        self.level.update_map(self.map, self.player1, self.player2)
        
    
    def run(self):
        while True:
            self.screen.fill("black")
            self.process_inputs()
            
            self.level.draw_map()
            ui.uiLayer.showText(f"Turn {str(self.turns)}")
            pygame.display.update()
            self.clock.tick(services.settings.FPS)
    
    def process_inputs(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP:
                    if self.current_turn == 1:
                        if event.key == pygame.K_UP:
                            moved = self.player1.move(self.map, "up")
                            if moved:
                                self.current_turn = 2
                        
                        if event.key == pygame.K_DOWN:
                            moved = self.player1.move(self.map, "down")
                            if moved:
                                self.current_turn = 2
                    
                        if event.key == pygame.K_LEFT:
                            moved = self.player1.move(self.map, "left")
                            if moved:
                                self.current_turn = 2
                    
                        if event.key == pygame.K_RIGHT:
                            moved = self.player1.move(self.map, "right")
                            if moved:
                                self.current_turn = 2
                        
                        self.map[self.player1.pos[1]][self.player1.pos[0]] = "p" + str(self.player1.p1orp2)
                        self.level.update_map(self.map, self.player1, self.player2)

                    else:
                        if event.key == pygame.K_UP:
                            moved = self.player2.move(self.map, "up")
                            if moved:
                                self.current_turn = 1
                                self.turns -= 1
                        
                        if event.key == pygame.K_DOWN:
                            moved = self.player2.move(self.map, "down")
                            if moved:
                                self.current_turn = 1
                                self.turns -= 1
                    
                        if event.key == pygame.K_LEFT:
                            moved = self.player2.move(self.map, "left")
                            if moved:
                                self.current_turn = 1
                                self.turns -= 1
                    
                        if event.key == pygame.K_RIGHT:
                            moved = self.player2.move(self.map, "right")
                            if moved:
                                self.current_turn = 1
                                self.turns -= 1
                        
                        self.map[self.player2.pos[1]][self.player2.pos[0]] = "p" + str(self.player2.p1orp2)
                        self.level.update_map(self.map, self.player1, self.player2)
                            
    def exit():
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()