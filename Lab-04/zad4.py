n = int(input("Enter number: "))
sum = 0
list = []


for i in range(1, n+1):
    currentString = ""

    for k in range(0,i):
        currentString += str(n)

    list.append(currentString)

for num in list:
    sum += int(num)

result = ' + '.join(str(item) for item in list)
print(result + " = " + str(sum))