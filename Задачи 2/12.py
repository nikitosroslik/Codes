a = 'Mmax'
def double(a:str):
    a =  a.lower()
    lst_char1 = ''
    lst_char2 = ''
    da = False
    for char in a:
        lst_char2 = lst_char1
        lst_char1 = char
        if lst_char1 == lst_char2:
            da = True
            break
    return da
print(double(a))
