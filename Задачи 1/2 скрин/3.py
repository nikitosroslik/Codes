def mul_to_int(a, b):
    x = a * b
    if float(x).is_integer():
        return int(x)
    return x
print(mul_to_int(1.5,2))