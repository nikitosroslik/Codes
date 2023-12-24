def shortener(st):
    while'(' in st or ')' in st:
        left = st.rfind('(')
        right = st.rfind(')', left)
        st = st.replace(st[left:right + 1], '')
    return st
print(shortener('Максим (ушел) пришел в школу (домой)'))  
