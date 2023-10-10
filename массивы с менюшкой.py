array_main=[]
array_founded=[]
def add_to_array(add_smth):
    array_main.append(add_smth)
    return array_main

def find_in_array(fnd_smth):
    for char in array_main:
        if fnd_smth == char:
            array_founded.append(fnd_smth)
            return array_founded
        
choice = int(input('1 - Добавить что-то в массив, 2 - Найти что-то в массиве, 3 - Выйти из меню'))
while choice <= 3:
    if choice == 1:
        add_smth = input('Введите то, что вы хотите добавить')
        print (add_to_array(add_smth))
    elif choice == 2:
        fnd_smth = input ('Введите то, что вы хотите найти')
        print (find_in_array(fnd_smth))
    else:
        break
    choice = int(input('1 - добавить что-то в массив, 2 - найти что-то в массиве, 3 - выйти из меню'))
    