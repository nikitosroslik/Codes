def hlop(array):
    bang = True
    lastchar = -10000000000000
    for char in array:
        if char > lastchar:
            lastchar = char
            continue
        else:
            bang = False
            break
    if bang == True:
        print('Возрастает')
    else:
        print('Не возрастает')
    
a = [1,2,3,4]
hlop(a)
