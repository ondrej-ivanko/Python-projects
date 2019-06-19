from Ships import Ship
from Pirates import Pirate

ghost_ship = Ship()
gythianki_ship = Ship()
# print(ghost_ship.captain_drank_how_much_rum())
# print(ghost_ship.ship_status())
ghost_ship.battle(gythianki_ship)
print(ghost_ship.ship_status())
print(gythianki_ship.ship_status())
new_pirate = Pirate("Joey")
new_pirate.drink_some_rum()
new_pirate.get_amount_of_rum_drank()