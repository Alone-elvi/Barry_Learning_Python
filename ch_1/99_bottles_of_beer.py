# -*- coding: utf-8 -*-

word = 'бутылок'

for beer_num in range(99, 0, -1):
    print(beer_num, word, 'на стене')
    print(beer_num, word)
    print('Возьми одну')
    print('Пусти по кругу')

    if beer_num == 1:
        print('Не осталось пива на стене')
    else:
        new_num = beer_num - 1
        if 11 <= new_num <= 19:
            word = 'бутылок'
        else:
            if new_num % 10 == 1:
                word = 'бутылка'
            elif new_num % 10 in (2, 3, 4):
                word = 'бутылки'
            else:
                word = 'бутылок'
        print(new_num, word, 'на стене')
    print()

help(range)
