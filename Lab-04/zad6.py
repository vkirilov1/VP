n = int(input("Input number: "))

dictionary = dict()

keys = []
values = []
for i in range(0, n+n):
    element = input("Type text: ")
    if i % 2 == 0:
        keys.append(element)
    else:
        values.append(element)

for i in range(0, len(keys)):
    dictionary[keys[i]] = values[i]


m = int(input("Input number: "))
list1 = []
for i in range(0, m):
    element = input("Type text: ")
    list1.append(element)

for a in list1:
    if a in dictionary:
        value = dictionary[a]
        list1[list1.index(a)] = value
        del dictionary[a]

print(dictionary)
print(list1)