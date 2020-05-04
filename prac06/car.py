"""
CP1404/CP5632 Practical
Car class
"""

"""Author: Nang Seng Khan
   Date: 02/05/2020
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""


class Car:
    """Represent a car"""

    def __init__(self, name="", fuel=0):
        """Construct or initialise a car object with name, fuel and odometer"""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of the car object"""
        output = "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)
        return output

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
