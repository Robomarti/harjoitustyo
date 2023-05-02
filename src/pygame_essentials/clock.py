import pygame


class Clock:
    """A class that handles the pacing of the application.

    The pacing is used so that the application does not run faster on faster computers.  

    Args:
        _clock: A class from the pygame.time module, used to handle time-related needs.
    """

    def __init__(self):
        """The constructor of the class

        """

        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Monitors how much time has passed since the last frame.

        Forces the application to wait until the wanted amount of time between frames has passed.
        """

        self._clock.tick(fps)
