def change(lst):
    l1 = lst[0]
    l2 = lst[len(lst) - 1]
    lst[len(lst) -1 ] = l1
    lst[0] = l2
    print(lst)
    return lst
change([1,2,3])    