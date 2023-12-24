a = [1,2,3]
b = [4,5,6]
def v(a, b):
    tota = 1
    totb = 1
    for char in a:
        tota = char * tota
    for char in b:
        totb = char * totb
    return tota + totb
print(v(a, b))
