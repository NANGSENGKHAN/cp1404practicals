"""Get a password with minimum length and display asterisks"""

"""Author: Nang Seng Khan
   Date: 04/03/2020 
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""

MINIMUM_LENGTH = 4


def main():
    """Get and print password."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password, ensuring it meets the minimum_length requirement."""
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(sequence):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print('*' * len(sequence))


if __name__ == "__main__":
    main()
