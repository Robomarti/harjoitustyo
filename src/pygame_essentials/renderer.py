import pygame
import ui.uiLayer


class Renderer:
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self, turns):
        self._display.fill("black")
        self._level.all_sprites.draw(self._display)
        ui.uiLayer.showText("Turns left: " + str(turns))
        pygame.display.update()
