import random

count = int(input("Input the size of the list: "))

numbers = []
result = []

for i in range(count):
    numbers.append(random.randint(1, 99))

for n in range(0, count-1):
    new_element = numbers[n] + numbers[n+1]
    result.append(numbers[n])
    result.append(new_element)
result.append(numbers[-1])

print("Random list: " + str(numbers))
print("List with summed numbers: " + str(result))