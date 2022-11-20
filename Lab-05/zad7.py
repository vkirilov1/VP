def digitize(num):
    tp = ()
    if type(num) != int:
        return "Error! Number must be an Integer!"
    else:
        list1 = [int(x) for x in str(num)]
        tp = tuple(list1)
    return tp


a, b, c, d = digitize(1337)
print(a, b, c, d)