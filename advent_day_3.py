import os
import re
import pandas as pd
import numpy as np

with open(os.getcwd()+'/files/day_3.txt', 'r') as f:
    cuts = [line.strip() for line in f.readlines()]

sheet = [[0 for _ in range(1, 1001)] for _ in range(1, 1001)]

patt = re.compile(
    '#(?P<num>[0-9]{1,4}) @ (?P<left>[0-9]{1,4})' +
    ',(?P<top>[0-9]{1,4}): (?P<width>[0-9]{1,4})' +
    'x(?P<height>[0-9]{1,4})'
    )

def get_points(x):
    match  = re.match(patt, x).groupdict()

    num    = int(match['num'])
    top    = int(match['top'])
    height = int(match['height'])
    left   = int(match['left'])
    width  = int(match['width'])

    return num, top, height, left, width

def mark(check, num):
    if check == 0:
        return num
    return 'X'

def mark_cut(cut):
    num, top, height, left, width = get_points(cut)

    for y in range(top, top+height):
        for x in range(left, left+width):
            sheet[y][x] = mark(sheet[y][x], num)

for cut in cuts:
    mark_cut(cut)

count = 0
for row in sheet:
    for col in row:
        if col == 'X':
            count += 1

print("Square inches of overlap:", count)

def check_overlap(cut):
    num, top, height, left, width = get_points(cut)

    overlap = False
    for row in range(top, top+height):
        for col in range(left, left+width):
            if sheet[row][col] == 'X':
                overlap = True
    if not overlap:
        print("ID", num, "does not overlap!")

for cut in cuts:
    check_overlap(cut)


#########################################################################
#  Just for fun, uncomment the section below, adjust the second for     #
#   loop's range to your maximum output area's char width/4, and enjoy  #
#   the ascii art output :)                                             #
#########################################################################
#
#for i in range(150):
#    for j in range(50):
#        try:
#            if sheet[i][j] == 0:
#                print("{:^4s}".format("."), end="")
#            else:
#                print("{:^4d}".format(sheet[i][j]), end='')
#        except:
#            print("{:^4s}".format(sheet[i][j]), end='')
#    print()
