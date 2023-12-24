damn = [12,13,14,15]
fae = []
def gag(arr):
    lastchar = 0
    for char in damn:
        fae.append(lastchar + char)
        lastchar = char
    print(fae)
    return fae
gag(damn)
