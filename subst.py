def s(subst, st):
    if subst.lower() in st.lower():
        return 'Есть контакт!'
    else:
        return 'Мимо!'
print(s('Макс', 'Максимум'))
print(s('макс', 'долбоеб'))