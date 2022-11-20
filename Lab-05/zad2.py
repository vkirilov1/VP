def palindrom_check(number):
    if str(number) == str(number)[::-1]:
        return 1
    else:
        return 0


num = int(input("Enter number: "))

print(palindrom_check(num))