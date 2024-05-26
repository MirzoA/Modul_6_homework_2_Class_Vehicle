class Vehicle():
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self, horse_power):
        self.horse_power = horse_power
        return horse_power

class Nissan(Car, Vehicle):
    price = 20000
    vehicle_type = "universal"

n = Nissan()
print('The price of my Nissan = ',n.price, ' dollars')
print('The engine power of my Nissan = ', n.horse_powers(80), ' horses')
print('The type of my Nissan is ', n.vehicle_type)

