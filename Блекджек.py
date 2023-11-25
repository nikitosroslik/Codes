deck = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(deck)


print('Добро пожаловать!')
count = 0

while True:
    choice = input('Будете брать карту? да/нет\n')
    if choice == 'да':
        current = deck.pop()
        print('Вам попалась карта достоинством %d' %current)
        count += current
        if count > 21:
            print('Извините, но вы проиграли')
            break
        elif count == 21:
            print('Поздравляю, вы набрали 21!')
            break
        else:
            print('У вас %d очков.' %count)
    elif choice == 'нет':
        print('У вас %d очков и вы закончили игру.' %count)
        break

print('До новых встреч!')


