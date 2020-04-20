"""
CP1404/CP5632 Practical
Email to name dictionary
"""

"""Author: Nang Seng Khan
   Date: 20/04/2020 
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""


def main():
    email = input("Email: ")
    email_name = {}
    while email != "":
        name = get_name_email(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print("{} ({})".format(name, email))


def get_name_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
