import random

count = int(input("Input the size of the list: "))

numbers = []
summed_numbers = []

for i in range(count):
    numbers.append(random.randint(1, 99))

for n in range(0, len(numbers)):
    if n+1 == len(numbers):
        break
    new_element = numbers[n] + numbers[n+1]
    summed_numbers.append(new_element)

result = []
for a in range(0, len(numbers)):
    result.append(numbers[a])
    if a == len(summed_numbers):
        break
    result.append(summed_numbers[a])

print("Random list: " + str(numbers))
print("List with summed numbers: " + str(result))