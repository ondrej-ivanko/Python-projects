from Ships import Ship
from random import randint

class Armada():

    def __init__(self):
        self.armada = self.fill_armada()

    def fill_armada(self):
        new_armada = []
        for i in range(1, randint(2, 10)):
            new_armada.append(Ship())
        return new_armada

    def war(self, opposing_armada):
        print("Your armada currently have " + str(len(self.armada)) + " ships")
        print("Opposing armada currently have " + str(len(opposing_armada.get_armada())) + " ships")
        while len(self.armada) != 0 and len(opposing_armada.get_armada()) != 0:
            if self.armada[0].battle(opposing_armada.get_armada()[0]):
                opposing_armada.get_armada().pop(0)
            else:
                self.armada.pop(0)
        if len(self.armada) == 0:
            print("Your armada lost.")
            return False
        elif len(opposing_armada.get_armada()) == 0:
            print("Your armada won.")
            return True

    def get_armada(self):
        return self.armada