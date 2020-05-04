"""Gibson L-5 CES get_age() - Expected 98. Got 98
Another Guitar get_age() - Expected 7. Got 7
Gibson L-5 CES is_vintage() - Expected True. Got True
Another Guitar is_vintage() - Expected False. Got False
"""

from prac06.guitar import Guitar


def run_unit_tests():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.48)
    another_guitar = Guitar("another Guitar", 2010, 1099.99)

    print("{} get_age() - Expected 98. Got {}".format(guitar.name, guitar.get_age()))
    print("{} get_age() - Expected 10. Got {}".format(another_guitar.name, another_guitar.get_age()))

    print("{} is_vintage() - Expected True. Got {}".format(guitar.name, guitar.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


if __name__ == '__main__':
    run_unit_tests()
