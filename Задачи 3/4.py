def sum(s):
    c = '1234567890'
    tot = ''
    array = []
    i = 0
    for char in s:
        if (char in c) == True:
            tot = tot + char
            i += 1
            if i == (len(s)):
                array.append(tot)
        else:
            array.append(tot)
            tot = ''
            i += 1
    i = 0
    for char in array:
        if char == '':
            array = array[:i] + array[i + 1:]
        else:
            i += 1
    i = 0
    for char in array:
        array[i] = int(char)
        i += 1
    tot = 0
    for char in array:
        tot += char
    print(tot)
    return tot
sum('45abnfgds478dsf985')
