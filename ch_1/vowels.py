#-*- coding: utf-8 -*-

vowels = ['a', 'o', 'e', 'i', 'u']

words = ['Milliways', 'Hitch-hiker', 'Galaxy', 'Sky']

for word in words:
    found = []
    print("========================== Result ==========================")
    for letter in word:
        if letter in vowels:
            if letter not in found:
                found.append(letter)
                print(letter)

