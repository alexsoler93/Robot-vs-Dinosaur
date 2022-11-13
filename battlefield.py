from dinosaur import Dinosaur

from robot import Robot

class Battlefield:
    def __init__(self):
        self.dino = Dinosaur()
        self.robo = Robot()

    def run_game(self):
        Battlefield.display_welcome(self)
        Battlefield.battle_phase(self)

    def display_welcome(self):
        print("Welcome to the battle for the ages!\nWho will come out on top?")

    def battle_phase(self):

        while self.dino.health > 0 and self.robo.health > 0:
            self.dino.bite(self.robo)
            self.robo.fire(self.dino)
            if self.dino.health <= 0:
                print("THE ROBOTS ARE VICTORIOUS\nDOMO ARIGATO")
            elif self.robo.health <=0:
                print("THE DINOS REIGN SUPREME\nRAAAAWR!")
            else:
                ()
