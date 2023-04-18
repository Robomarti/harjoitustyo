import pygame
import services.level
import services.settings
import logic.game_loop
import pygame_essentials.renderer
import pygame_essentials.clock
import pygame_essentials.event_queue


def main():
    display = pygame.display.set_mode(
        (services.settings.WIDTH, services.settings.HEIGHT))
    pygame.display.set_caption("Capture The Flag")

    game_clock = pygame_essentials.clock.Clock()
    game_level = services.level.Level()
    game_event_queue = pygame_essentials.event_queue.EventQueue()
    game_renderer = pygame_essentials.renderer.Renderer(display, game_level)
    loop = logic.game_loop.GameLoop(
        game_level, display, game_renderer, game_event_queue, game_clock)

    pygame.init()
    loop.start()


if __name__ == "__main__":
    main()
