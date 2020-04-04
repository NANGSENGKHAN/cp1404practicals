# odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i)

# a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
for i in range(1, 101):
    print(i)

# b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
i = 20
for i in reversed(range(1, i + 1)):
    print(i)

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line
number_of_star = int(input("Enter a number: "))
for i in range(1):
    print("*" * number_of_star)

# d. print n lines of increasing stars. Using the same number as above print lines of increasing stars, starting at 1.
increase_star = int(input("Enter a number: "))
for increase_star in range(1, increase_star + 1):
    print("*" * increase_star)