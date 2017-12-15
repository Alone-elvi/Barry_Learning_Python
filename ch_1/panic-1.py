# -*- coding: utf-8 -*-

phrase = "Don't panic!"

plist = list(phrase)

print(phrase)
print(plist)

plist = plist[1:-4]
plist[2] = plist[4]
plist[4] = plist[-1]
plist = plist[:-1]

new_phrase = ''.join(plist)

print(plist)
print(new_phrase)
