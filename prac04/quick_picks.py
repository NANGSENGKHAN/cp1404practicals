"""
CP1404/CP5632 Practical
Quick pick program
"""

"""Author: Nang Seng Khan
   Date: 20/04/2020 
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""

import random

number_of_line = 6
minimum = 1
maximum = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for n in range(number_of_line):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
