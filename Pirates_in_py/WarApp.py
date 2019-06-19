from Armada import Armada

sovetska_armada = Armada()
mongolska_armada = Armada()
sovetska_armada.war(mongolska_armada)
for ship in sovetska_armada.get_armada():
    print(ship.ship_status())