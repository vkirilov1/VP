num_count = int(input("Type numbers count: "))
max = -999999999999

for i in range(0, num_count):
    num = int(input("Write a number: "))
    if num > max:
        max = num

print(f"The biggest number is: {max}")