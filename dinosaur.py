

class Dinosaur:

    def __init__(self):
        self.health = 100
        self.bite_power = 25

    def bite(self, robot):
        robot.health -= self.bite_power



