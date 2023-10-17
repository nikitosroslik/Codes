def f(letter, st):
    first = st.find(letter)
    if first < 0:
        return None, None
    last = st.rfind(letter)
    return first, last
print(f('м', 'максим'))