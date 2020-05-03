"""
CP1404/CP5632 Practical
Programming Language class with tests.
"""

"""Author: Nang Seng Khan
   Date: 02/05/2020 
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""


class ProgrammingLanguage:
    """Represents a programming language"""

    def __init__(self, name="", typing="", reflection=False, year=""):
        """Construct or Initialise a ProgrammingLanguage object with parameters"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    # is dynamic() - which returns True/False if the programming language is dynamically typed or not
    def is_dynamic(self):
        """Check whether the programming language is dynamic"""
        return self.typing.title() == "Dynamic"  # dynamic or DYNAMIC

    def __str__(self):
        """Return the string representation of the object"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name,
                                                                           self.typing, self.reflection, self.year)


if __name__ == '__main__':
    # unit test the ProgrammingLanguage class
    ruby = ProgrammingLanguage("Python", "Dynamic", True, "1995")
    python = ProgrammingLanguage("Python", "Dynamic", True, "1991")
    visual_basic = ProgrammingLanguage("Python", "Dynamic", False, "1991")
    print(ruby)
    print(python)
    print(visual_basic)
