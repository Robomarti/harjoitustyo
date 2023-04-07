import pygame
import settings
import level
import game_loop
import renderer
import clock
import event_queue

def main():
    display = pygame.display.set_mode(
        (settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Capture The Flag")

    game_clock = clock.Clock()
    game_level = level.Level()
    game_event_queue = event_queue.EventQueue()
    game_renderer = renderer.Renderer(display, game_level)
    loop = game_loop.GameLoop(game_level, display, game_renderer, game_event_queue, game_clock)

    pygame.init()
    loop.start()

if __name__ == "__main__":
    main()
