"""CP1404/CP5632 Practical - Client code to use the Car class."""

"""Author: Nang Seng Khan
   Date: 02/05/2020
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""

from prac06.car import Car


def main():
    car = Car("My car", 180)
    car.drive(30)
    print("fuel =", car.fuel)
    print("odo =", car.odometer)
    print(car)
    print("Car {}, {}".format(car.fuel, car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=car))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)


main()
