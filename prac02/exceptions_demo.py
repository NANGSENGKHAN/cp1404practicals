try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""1.When will a ValueError occur? 
   A ValueError occur when a built-in operation or function receives an argument that 
   has the right type but am inappropriate value, and the situation is not described by a more precise exception such as
   IndexError.
   2.When will a ZeroDivision occur?
   ZeroDivision occur when attempting to divide a number by zero.
   3.Could you change the code to avoid the possibility of a ZeroDivisionError? 
   If you could figure out the answer to question 3, then make this change now.
   Changing the code to avoid ZeroDivisionError.
    """