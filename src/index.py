import pygame
import services.level
import services.settings
import logic.game_loop
import pygame_essentials.clock
import pygame_essentials.event_queue


def main():
    """A method that starts, restarts and closes the game.

    This creates new instances of classes so that everything
    gets reset between games.
    """

    try:
        while True:
            display_width = services.settings.TILESIZE * len(services.settings.MAP[0])
            display_height = services.settings.TILESIZE * len(services.settings.MAP)
            display = pygame.display.set_mode((display_width, display_height))
            pygame.display.set_caption("Capture The Flag")
            game_clock = pygame_essentials.clock.Clock()
            game_level = services.level.Level()
            game_event_queue = pygame_essentials.event_queue.EventQueue()
            loop = logic.game_loop.GameLoop(
            game_level, display, game_event_queue, game_clock)
            pygame.init()

            if loop.start() is False:
                break
    except:
        print("Something went wrong, did you change the settings incorrectly?")
        print("If so, please revert any changes.")

if __name__ == "__main__":
    main()
