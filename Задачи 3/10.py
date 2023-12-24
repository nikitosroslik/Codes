def coins(a):
    total = sum(a)
    if total % 3 == 0:
        return True
    else:
        return False
a = [3, 3, 4, 4, 5, 5]
result = coins(a)
print(result)  
