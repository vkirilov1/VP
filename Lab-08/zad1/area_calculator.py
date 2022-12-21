from square_area import squareArea
from triangle_area import triangleArea
from rectangle_area import rectangleArea
from rhombus_area import rhombusArea
from trapezoid_area import trapezoidArea

figure = input("Enter figure type: ")

if figure == "square":
    a = int(input("Type a: "))
    print(f"Area: {squareArea(a)}")

elif figure == "triangle":
    a = int(input("Type a: "))
    h = int(input("Type h: "))
    print(f"Area: {triangleArea(a, h)}")

elif figure == "rectangle":
    a = int(input("Type a: "))
    b = int(input("Type b: "))
    print(f"Area: {rectangleArea(a, b)} ")

elif figure == "rhombus":
    diagonal1 = int(input("Type first diagonal: "))
    diagonal2 = int(input("Type second diagonal: "))
    print(f"Area: {rhombusArea(diagonal1, diagonal2)}")

elif figure == "trapezoid":
    a = int(input("Type a: "))
    b = int(input("Type b: "))
    h = int(input("Type h: "))
    print(f"Area: {trapezoidArea(a, b, h)}")

else:
    print("Invalid figure type!")