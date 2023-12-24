a = [1,2,3,4]
b = [5,6,7,8]
c = []
def third_array(a, b):
    c = []
    for i in range(len(a)):
        c.append([a[i], b[i]])
    return c
print(third_array(a, b))
