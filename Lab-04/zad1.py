n = int(input("Enter number: "))

fibonacci_numbers = [0,1]

list_length = len(fibonacci_numbers)

loop = True
while loop:
    if n+2 == list_length:
        loop = False
    last_element = fibonacci_numbers[list_length - 1]
    pre_last_element = fibonacci_numbers[list_length - 2]
    sum = last_element + pre_last_element
    fibonacci_numbers.append(sum)
    list_length += 1

print("The fibunacci number you entered: " + str(fibonacci_numbers[n]))
print("The 2 fibunacci numbers after the one you entered: " + str(fibonacci_numbers[-2]) + "|" + str(fibonacci_numbers[-1]))