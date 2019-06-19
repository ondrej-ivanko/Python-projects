from Pirates import Pirate
from random import randint

class Ship():

    def __init__(self, alive_members = 0, dead_members = 0):
        self.ship_crew = self.fillship()
        self.alive_members = len(self.ship_crew)
        self.dead_members = dead_members        

    def fillship(self):
        new_crew = []
        new_crew.append(Pirate("Barbar Onan", isCaptain = True))
        for pirate in range(1, randint(2, 8)):
            new_crew.append(Pirate("Pirate-" + str(pirate)))
        self.alive_members = len(new_crew)
        return new_crew        

    def get_crew(self):
        return self.ship_crew
    
    def get_alive_crew(self):
        return self.alive_members

    def set_alive_crew(self, num):
        self.alive_members = num

    def get_dead_crew(self):
        return self.dead_members

    def set_dead_crew(self, num):
        self.dead_members = num

    def captain_drank_how_much_rum(self):
        return self.ship_crew[0].get_amount_of_rum_drank()


    def ship_status(self):
        print("Amount of crew members alive: " + str(self.alive_members))
        print("Amount of dead crew: " + str(self.dead_members))
        print("Captain drank " + str(self.captain_drank_how_much_rum()) + " bottles of Rum.")

    def ship_readiness(self):
        ship_readiness = (self.alive_members - self.captain_drank_how_much_rum())
        return ship_readiness

    def set_dead_crew_size(self, died):
        self.dead_members = died

    def battle(self, enemy_ship):
        if self.ship_readiness() >= enemy_ship.ship_readiness():
            dead_enemies = randint(1, len(enemy_ship.get_crew()) + 1)
            for pirate in enemy_ship.get_crew():
                if pirate.life_checker():
                    pirate.pirate_dies()
                    if enemy_ship.alive_members > 0:                    
                        enemy_ship.set_alive_crew(enemy_ship.get_alive_crew() - 1)
                        enemy_ship.set_dead_crew(enemy_ship.get_dead_crew() + 1)
                    dead_enemies -= 1
                else:
                    continue                    
            for pirate in self.get_crew():
                if pirate.life_checker():
                    pirate.drink_some_rum()
            return True

        elif self.ship_readiness() < enemy_ship.ship_readiness():
            dead_enemies = randint(1, len(enemy_ship.get_crew()) + 1)
            for pirate in self.get_crew():
                if pirate.life_checker():
                    pirate.pirate_dies()
                    if self.alive_members > 0:
                        self.set_alive_crew(self.get_alive_crew() - 1)
                        self.set_dead_crew(self.get_dead_crew() + 1)
                    dead_enemies -= 1
                else:
                    continue
            for pirate in enemy_ship.get_crew():
                if pirate.life_checker():
                    pirate.drink_some_rum()
            return False