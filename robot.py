from weapon import Blaster_Gun
import random

class Robot:

    def __init__(self):
        self.health = 100
        self.weapon = Blaster_Gun()

    def fire(self, opponent):

        hit_or_miss = random.randint(0,1)
        
        if hit_or_miss == 0:
            print("ATTACK MISSED")
        elif hit_or_miss == 1:
            opponent.health -= self.weapon.damage_per_shot
            print("HIT!")
        else:
            ()

