def add(num, num1):
    return num + num1


def substraction(num, num1):
    return num - num1


def multiplication(num, num1):
    return num * num1


def division(num, num1):
    return num / num1


operation = input("Enter operation: ")
n = int(input("Enter first number: "))
n1 = int(input("Enter second number: "))


if operation.lower() == "add":
    print(add(n, n1))
elif operation.lower() == "substraction":
    print(substraction(n, n1))
elif operation.lower() == "multiplication":
    print(multiplication(n, n1))
elif operation.lower() == "division":
    print(division(n, n1))
else:
    print("unknown operation!")