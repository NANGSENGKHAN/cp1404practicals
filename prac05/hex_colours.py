"""
CP1404/CP5632 Practical
Hex colours look up
"""

"""Author: Nang Seng Khan
   Date: 20/04/2020 
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""

COLOUR_TO_CODE = {'AliceBlue': '#f0f8ff',
                  'AntiqueWhite': '#faebd7',
                  'black': '#000000',
                  'BlanchedAlmond': '#ffebcd',
                  'blue1': '#0000ff',
                  'blue2': '#0000ee',
                  'blue4': '#00008b',
                  'BlueViolet': '#8a2be2',
                  'CadetBlue': '#5f9ea0',
                  'chocolate': '#d2691e',
                  'cyan1': '#00ffff',
                  'DarkGreen': '#006400',
                  'DarkKhaki': '#bdb76b',
                  'DarkBlue': '#0000aa'
                  }


def main():
    # Ask user for input for colour
    colour_name = input("Enter a colour: ").strip()

    while colour_name !="":
        print("Colour code is {} for {}".format(COLOUR_TO_CODE.get(colour_name), colour_name))
        colour_name = input("Enter a colour: ").strip()


main()