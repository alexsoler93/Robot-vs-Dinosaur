

class Blaster_Gun:

    def __init__ (self):
        self.ammo = 50
        self.size = 'large'
        self.damage_per_shot = 25

    def shootgb(self):
        dinohealth -= self.damage_per_shot
        self.damage_per_shot -= self.ammo

        if (self.ammo) == 0:
            print('RELOAD')
        else:
            print()
    
    def reload(self):
        self.ammo += 50
           

