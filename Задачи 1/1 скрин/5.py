def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst
print(list_sort([1, 5, 77]))
