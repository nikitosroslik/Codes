def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    return "Невозможно преобразовать"
print(to_float(1234))
