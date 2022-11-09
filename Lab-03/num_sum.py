num_count = int(input("Type numbers count: "))
sum = 0

for i in range(0, num_count):
    num = int(input("Write a number: "))
    sum += num

print(f"The sum is: {sum}")