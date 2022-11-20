def square(side):
    return side * side


def rectangle(length, width):
    return length * width


def triangle(base, height):
    return (base * height) / 2


n = input("Figure type: ")

if n == "square":
    a = int(input("Enter side: "))
    print(square(a))


elif n == "rectangle":
    a = int(input("Enter height: "))
    b = int(input("Enter width: "))
    print(rectangle(a, b))


elif n == "triangle":
    a = int(input("Enter side: "))
    h = int(input("Enter height: "))
    print(triangle(a, h))