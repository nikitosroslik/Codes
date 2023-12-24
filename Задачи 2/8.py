def reverse(a):
    tot = ''
    for char in a:
        if char.istitle() == True:
            tot = char.lower() + tot
        else:
            tot = char.upper() + tot
    print(tot)
    return tot
reverse('SFistheworst')
