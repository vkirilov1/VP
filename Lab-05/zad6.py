def list_avg(list1, multiplier=1):
    sum1 = 0
    size = 0

    for a in list1:
        if type(multiplier) == int:
            if type(a) != int and type(a) != float:
                continue
            else:
                size += 1
                sum1 += a * multiplier
                continue
        else:
            return "Multiplier must be an Integer!"

    average = sum1/size
    return average


print(list_avg([1, 2, 4, "a", 5, "4", 8.7], 15))