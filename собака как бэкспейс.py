def cleaned_str(st):
    clean1=[]
    for symbol in st:
        if symbol == '@' and clean1:
            clean1.pop()
        elif symbol != '@':
            clean1.append(symbol)
    return ''.join(clean1)


print (cleaned_str('гр@оо@лк@оц@ва'))        
