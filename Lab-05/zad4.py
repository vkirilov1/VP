def comparison(list1, number):
    for element in list1:
        if element > number:
            list1[list1.index(element)] = 0
    return list1


list2 = [1, 5, 7, 3, 5, 7, 4, 3, 15, 30, 24, 23, 12]
number = int(input("Enter number to compare: "))

print(comparison(list2, number))