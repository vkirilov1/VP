def find_largest(list1):
    biggest = -99999999999999999999
    for i in list1:
        if i >= biggest:
            biggest = i

    return biggest


x = [4, 6, 8, 24, 12, 2]
print(find_largest(x))