import pygame
import services.level
import services.settings
import logic.game_loop
import pygameEssentials.renderer
import pygameEssentials.clock
import pygameEssentials.event_queue

def main():
    display = pygame.display.set_mode(
        (services.settings.WIDTH, services.settings.HEIGHT))
    pygame.display.set_caption("Capture The Flag")

    game_clock = pygameEssentials.clock.Clock()
    game_level = services.level.Level()
    game_event_queue = pygameEssentials.event_queue.EventQueue()
    game_renderer = pygameEssentials.renderer.Renderer(display, game_level)
    loop = logic.game_loop.GameLoop(game_level, display, game_renderer, game_event_queue, game_clock)

    pygame.init()
    loop.start()

if __name__ == "__main__":
    main()
