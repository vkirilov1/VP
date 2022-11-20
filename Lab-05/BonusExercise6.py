def recursive_function(x):
    if x == 0:
        return 0
    else:
        return x + recursive_function(x-1)


print(recursive_function(10))