"""Fixed program to determine score status, with function"""

"""Author: Nang Seng Khan
   Date: 04/03/2020 
"""


# Note boundary conditions (50 should be a pass, not > 50)
# Note efficiency and nesting; use the fewest number of if/elif as possible

def main():
    """Get a numeric score and display."""
    score = float(input("Enter score: "))
    print(get_score(score))


def get_score(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()
