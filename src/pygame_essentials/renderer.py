import pygame
import ui.uiLayer


class Renderer:
    def __init__(self, display, level, p1_projectile, p2_projectile):
        self._display = display
        self._level = level
        self._p1_projectile = p1_projectile
        self._p2_projectile = p2_projectile

    def render(self, turns, player_one, player_two):
        self._display.fill("black")
        self._level.all_sprites.draw(self._display)
        pygame.draw.circle(self._display, self._p1_projectile.color,
                           self._p1_projectile.location, self._p1_projectile.radius)
        pygame.draw.circle(self._display, self._p2_projectile.color,
                           self._p2_projectile.location, self._p2_projectile.radius)
        ui.uiLayer.showText("Turns left: " + str(turns), 20, 450)
        ui.uiLayer.showText("Player 1 points: " + str(player_one.points), 20, 100)
        ui.uiLayer.showText("Player 2 points: " + str(player_two.points), 20, 750)
        pygame.display.update()
