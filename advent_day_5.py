import os
import re

with open(os.getcwd() + "/files/day_5.txt", 'r') as f:
    polymer = f.read().strip()

biglist = list(polymer)

changed = True

while changed:
    changed=False
    for i in range(len(biglist)):
        try:
            if abs(ord(biglist[i]) - ord(biglist[i+1])) == 32:
                del biglist[i]
                del biglist[i]
                changed = True
        except IndexError:
            pass
   

print("Part 1 answer:", len(biglist))
letters = set(biglist)
newpoly = "".join(biglist)
del biglist

for letter in letters:
    if letter.isupper():
        pass

