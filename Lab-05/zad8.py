def get_collection_builder(col_type):
    if type(col_type) == str:

        if col_type == "tuple":
            def tuple_creation(a, b, c, d):
                tup = (a, b, c, d)
                return tup
            return tuple_creation

        elif col_type == "list":
            def list_creation(a, b, c, d):
                lst = [a, b, c, d]
                return lst
            return list_creation

        elif col_type == "set":
            def set_creation(a, b, c, d):
                st = {a, b, c, d}
                return st
            return set_creation

        else:
            return "Unknown function!"
    else:
        return "Function must be a string!"


tuple_builder = get_collection_builder("tuple")
tup = tuple_builder(1, 2.23, 3, "hi")
print(tup)