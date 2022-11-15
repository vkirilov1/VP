n = int(input("Enter size:"))

for a in range(n):
    print("*", end="")
    for b in range(a):
        print(" *", end="")
    print()