def generate(list1):
    for i in range(4, 30):
        if i % 2 == 0:
            list1.append(i)
    return list1


nums = []
print(generate(nums))