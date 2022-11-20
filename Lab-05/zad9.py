def is_valid_triangle(a, b, c):
    exists = True

    if type(a) != int or type(b) != int or type(c) != int:
        return "A, B and C must be whole numbers!"

    else:
        if a + b <= c:
            exists = False
        elif a + c <= b:
            exists = False
        elif b + c <= a:
            exists = False
        else:
            exists = True

    return exists


can_triangle_exist = is_valid_triangle

print(can_triangle_exist(3, 7, 3))
print(is_valid_triangle(3, 5, 3))