def dislike_6(a):
    if (type (a) is int or type(a) is float) and a == 6:
        return 'Только не 6!'
    return 'Хорош'
print(dislike_6(6))
print(dislike_6(52))
print(dislike_6("Макс"))