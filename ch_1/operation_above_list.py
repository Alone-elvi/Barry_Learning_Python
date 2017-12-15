# -*- coding: utf-8 -*-

'''Работа над списками, удаление, добавление
методы: remove, append, extend, pop, insert'''

'''Удаление элементов из списка'''
nums = [1, 2, 3, 4]

# remove, удаляет значения из списка
nums.remove(3)
print('list after remove: ', nums)

# pop, удаляет элемент по индексу и возвращает его

nums.pop()  # Удаление последнего элемнета списка
print("list after pop(): ", nums)

nums.pop(0)  # Удаление элемента списка по инексу "0"
print("list after pop(0): ", nums)

'''Добавление элементов в список'''
# extend, принимает список и добавляет его в конец существующего списка

nums.extend([3, 4])
print('list after extend([3, 4]): ', nums)

# insert, вставляет объект в существующий список перед индексом указанным в первом аргументе
# вставляем в начало списка (0, ...), значение 1
nums.insert(0, 1)
print('list after insert(0, 1): ', nums)

# вставим в список сроку по индексу 2
nums.insert(2, "two-and-half")
print('list after insert(2, "two-and-half"): ', nums)
