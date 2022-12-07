import math

try:
    number = int(input("Enter number: "))
    result = math.sqrt(number)
    print(result)

except ValueError:
    print("Invalid Number")

finally:
    print("Good Bye")