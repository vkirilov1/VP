import Operations

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation: ")

if operation == "add":
    print(f"Sum: {Operations.addNums(a, b)}")

elif operation == "subtract":
    print(f"Sum: {Operations.subtractNums(a, b)}")

elif operation == "division":
    print(f"Sum: {Operations.divideNums(a, b)}")

elif operation == "multiply":
    print(f"Sum: {Operations.multiplyNums(a, b)}")

else:
    print("Invalid operation!")

