"""
CP1404/CP5632 Practical
Guitar program.
"""

"""Author: Nang Seng Khan
   Date: 02/05/2020
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""

"""These are my guitars:
Guitar 1: Fender Stratocaster (2014), worth $ 765.40
Guitar 2: Gibson L-5 (1922), $ 16,035.40 (vintage)
Guitar 3: Line 6 JTV-59 (2010), worth$ 1,512.90
"""
from prac06.guitar import Guitar


def main():
    guitars = []  # list of guitar objects
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $ "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):  # i starts at 1 instead of 0
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
        print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f} {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars :(Quick, go and buy one!")


main()
