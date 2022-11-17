s1 = {1, 7, 5}
s2 = {1, 2, 3, 4}

if s1.issubset(s2):
    print(s2 - s1)
else:
    print(s1.union(s2))