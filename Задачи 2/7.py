def generate_message(a):
    tot = ""
    dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    for char in a:
        if char.upper() in dict:
            i = dict[char.upper()]
            tot += char * i
    print(tot)
    return tot
generate_message('ABCD')
