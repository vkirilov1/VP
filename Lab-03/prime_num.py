num = int(input())

if num > 1:
    if num == 2:
        print("prime")
    elif num == 3:
        print("prime")
    elif num % 2 == 0 or num % 3 == 0:
        print("not prime")
    else:
        print("prime")
else:
    print("not prime")
