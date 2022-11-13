import random

class Dinosaur:

    def __init__(self):
        self.health = 100
        self.bite_power = 40

    def bite(self, opponent):
        
        hit_or_miss = random.randint(0,1)

        if hit_or_miss == 0:
            print("ATTACK MISSED")
        elif hit_or_miss == 1:
            opponent.health -= self.bite_power
            print("HIT!")
        else:
            ()




