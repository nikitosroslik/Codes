def number_to_words(number):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
             'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
            'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот',
                'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    if number < 0 or number > 999:
        return "Число должно быть от 0 до 999"
    if number == 0:
        return "ноль"
    words = []
    hundreds_digit = number // 100
    if hundreds_digit > 0:
        words.append(hundreds[hundreds_digit])
    tens_digit = (number % 100) // 10
    units_digit = number % 10
    if tens_digit == 1:
        words.append(teens[units_digit])
    else:
        if tens_digit > 1:
            words.append(tens[tens_digit])
        if units_digit > 0:
            words.append(units[units_digit])
    return ' '.join(words)
number = 123
result = number_to_words(number)
print(result)
