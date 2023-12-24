def neighbours(a):
    i = 0
    tot = ''
    bang = True
    while i < len(a):
        if a[i] == '+':
            bang = True
        else:
            bang = False
        i += 2
    print(bang)
    return bang
