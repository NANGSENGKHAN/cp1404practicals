"""
CP1404/CP5632 Practical
Programming Language client code.
"""

"""Author: Nang Seng Khan
   Date: 04/03/2020
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""

from prac06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, "1995")
    python = ProgrammingLanguage("Python", "Dynamic", True, "1991")
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, "1991")
    java = ProgrammingLanguage("Java", "Static", True, "1995")
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, "1983")
    programming_languages = [ruby, python, visual_basic, java, c_plus_plus]

    print("The dynamically typed languages are: ")
    for programming_language in programming_languages:
        if programming_language.is_dynamic():
            print(programming_language.name)


if __name__ == '__main__':
    main()
