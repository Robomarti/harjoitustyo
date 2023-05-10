import services.settings


class Projectile():
    """A class that is responsible for calculating the location, radius and color of the
    projectiles used in the game.

    Attributes:
        location: The current location of the projectile. This is used to draw the projectile,
        and to detect its collisions.
        target_location: The location where the projectile should travel.
        radius: The radius of the projectile, impacts how the projectile is drawn.
        vector: The distance that the projectile travels per frame.
        color: The color of the projectile, impacts how the projectile is drawn.
    """

    def __init__(self):
        """The constructor of the class.

        """

        self.location = [-100, -100]
        self.target_location = [-100, -100]
        self.radius = 10
        self.vector = [0, 0]
        self.color = "yellow"

    def calculate_vector(self):
        """Calculates the distance that the projectile should travel in a single frame.

        """

        self.vector[0] = (self.target_location[0] -
                          self.location[0]) / services.settings.FPS
        self.vector[1] = (self.target_location[1] -
                          self.location[1]) / services.settings.FPS

    def move(self):
        """Adds the distance of the vector to the projectiles location, causing it to move.

        """

        self.location[0] += self.vector[0]
        self.location[1] += self.vector[1]

    def die(self):
        """Hides the projectile from the screen.

        """

        self.location = [-100, -100]
        self.target_location = [-100, -100]
        self.vector = [0, 0]
