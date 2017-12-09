word = 'бутылок'

for beer_num in range(99, 0, -1):
    print(beer_num, word, 'на стене')
    print(beer_num, word)
    print('Возьми одну')
    print('Пусти по кругу')

    if beer_num == 1:
        print('Не осталось пива на стене')
    else:
        new_num = beer_num -1
        if new_num == 1:
            word = 'бутылка'
        print(new_num, word, 'на стене')
    print()

