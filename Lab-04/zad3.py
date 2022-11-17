n = int(input("Enter count: "))
numbers_list = []

for i in range(0, n):
    number = int(input("Enter a number to add: "))
    numbers_list.append(number)

list_length = len(numbers_list)
operation = int(input("Enter 1 or 0 command: "))

for i in range(0, list_length):
    if operation == 0:
        if i % 2 == 0:
            numbers_list[i] += 5
    elif operation == 1:
        if i % 2 != 0:
            numbers_list[i] += 10
    else:
        print("unknown command")

print(numbers_list)