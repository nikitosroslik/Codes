def umn(string):
    tot = ''
    array1 = []
    array2 = []
    i = 0
    for char in string:
        if  char == ',':
            array1.append(tot)
            tot = ''
            i += 1
            continue
        elif char == ' ':
            i += 1
            continue
        else:
            tot = tot + char
            if i == len(string) - 1:
                array1.append(tot)
            i += 1
    j = 0
    while j < len(array1):
        array2.append(int(array1[j]))
        j += 1
    tot = 1
    i = 0
    while i < len(array2):
        tot = tot * array2[i]
        i += 1
    return tot
print(umn('2, 123, 456, 15'))
