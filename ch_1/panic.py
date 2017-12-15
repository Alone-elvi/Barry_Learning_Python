# -*- coding: utf-8 -*-
"""
Задача: трансформировать строку «Don’t panic!»
в строку «on tap», используя методы списков, рассмотренные
выше. (В выборе этих двух строк нет никакого скрытого смысла: просто в строке «on tap» присутствуют символы,
которые имеются в строке «Don’t panic!»). Изначально программа panic.py дважды выводит «Don’t panic!».
"""
phrase = "Don't panic!"
new_phrase_list = "on tap"
plist = list(phrase)
nplist = list(new_phrase_list)

# Удаляем последние 4 элемента списка
for i in range(4):
    plist.pop()

# Удаляем первый элемент списка
plist.pop(0)

# Удаляем апостроф
plist.remove("'")

print(plist)

# Меняем местами последний и предпоследний элемент списка

plist.extend([plist.pop(), plist.pop()])
print(plist)

# Извлекаем пробел и вставляем его по индексу 3, т.е. между нужными словами
plist.insert(2, plist.pop(3))

# Делаем первую букву фразы заглавной
plist.insert(0, plist.pop(0).upper())

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
