number = int(input("Enter your number: "))
bit = int(input("Enter your bit: "))

if number & (1 << bit) > 0:
    print("True")
else:
     print("False")
