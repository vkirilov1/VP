import math

r = float(input('Enter radius: '))
perimeter = 2 * math.pi * r
area = math.pi * r * r

print('The perimeter of the circle is: ', round(perimeter, 3))
print('The area of the circle is: ', round(area, 3))