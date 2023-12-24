def ne_ori(s: str):
    tot = ''
    for char in s:
        tot = char + tot
    i = 0
    while tot[i] == '?' or tot[i] == '!':
        i += 1
    if i > 1:
        s = s[:len(s) + 1 - i]
    print(s)
    return s
