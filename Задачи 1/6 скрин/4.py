dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
a = list(dict.keys())[0]
b = list(dict.keys())[-1]
c = dict[a]
d = dict[b]
dict[a] = d
dict[b] = c
del dict[list(dict.keys())[1]]
dict["new_key"] = "new_value"
print(dict)
