class Pirate():

    def __init__(self, name, rum_dranked_count = 0, intoxication = False,  isAlive = True, isCaptain = False):
        self.name = name
        self.rum_dranked_count = rum_dranked_count
        self.intoxication = intoxication
        self.isAlive = isAlive
        self.isCaptain = isCaptain

    def set_pirate_as_captain(self):
        self.isCaptain = True

    def drink_some_rum(self):
        self.rum_dranked_count += 1
        self.intoxication = True

    def get_amount_of_rum_drank(self):
        return self.rum_dranked_count

    def how_is_it_going_mate(self):
        if self.rum_drank_count <= 4:
            print("Pour me anudder.")
        else:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")

    def pirate_dies(self):
        self.isAlive = False
        print("One of the pirates died.")

    def life_checker(self):
        return self.isAlive