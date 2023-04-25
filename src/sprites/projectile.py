import services.settings


class Projectile():
    def __init__(self):
        self.location = [-100, -100]
        self.radius = 10
        self.velocity = 1
        self.color = "yellow"
        self.target_location = [-100, -100]

    def move(self):
        self.location[0] += abs(self.location[0] -
                                self.target_location[0]) / services.settings.FPS
