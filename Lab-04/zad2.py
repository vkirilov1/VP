n = int(input("Enter number: "))
sum = 1

if n <= 0:
    print("Number can't be 0 or lower!")
else:
    for i in range(1, n+1):
        sum *= i
    print(sum)