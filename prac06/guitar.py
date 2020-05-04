from datetime import datetime


class Guitar:
    """Represent a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Construct or initialise a guitar object with name, year and cost"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar object"""
        output = "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)
        return output

    def get_age(self):
        """Return the age based on hte current year grabbed from the system"""
        return datetime.now().year - self.year

    def is_vintage(self):
        """Determine whether a Guitar object is vintage based on age"""
        age = self.get_age()
        return age >= 50
