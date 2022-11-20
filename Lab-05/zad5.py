def input_nums(n):
    list1 = []
    for i in range(0, n):
        number = input("Enter a list element: ")
        if number.isnumeric():
            list1.append(number)
        else:
            continue
    return list1


def sum_list(list1):
    sum1 = 0
    for element in list1:
        if type(element) == int:
            sum1 += element
        elif type(element) == float:
            sum1 += element
        elif element.isnumeric():
            sum1 += int(element)
        else:
            continue
    return sum1


def max_of_two(a, b):
    if type(a) and type(b) != int and type(a) and type(b) != float:
        return ""
    elif type(a) != int and type(a) != float:
        return b
    elif type(b) != int and type(b) != float:
        return a
    else:
        if a >= b:
            return a
        elif b > a:
            return b


max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3)))
max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2")