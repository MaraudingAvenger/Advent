import os
import re

os.chdir('/home/pi/Python/advent/')

with open(os.getcwd()+'/files/day_3.txt', 'r') as f:
    cuts = [line.strip() for line in f.readlines()]

patt = re.compile(
    '#(?P<num>[0-9]{1,4}) @ (?P<left>[0-9]{1,4})' +
    ',(?P<top>[0-9]{1,4}): (?P<width>[0-9]{1,4})' +
    'x(?P<height>[0-9]{1,4})'
    )

class Square():
    def __init__(self, bottom, left, top, right):
        self.bottom=bottom
        self.top=top
        self.left=left
        self.right=right

    def overlaps (self, other):
        if not isinstance(other, Square):
            raise TypeError("cannot compare with non Square type")
        if (self.bottom >= other.top or
            self.left >= other.right or
            self.right <= other.left or
            self.top <= other.bottom):
            return False
        return True

    def overlap_amount (self, other):
        if not isinstance(other, Square):
            raise TypeError("cannot compare with non Square type")
        if not self.overlaps(other):
            raise Exception("Squares do not overlap.")
        ##TODO: finish this func
        pass

def get_points(x):
    match  = re.match(patt, x).groupdict()

    top    = int(match['top'])
    bottom = top - int(match['height'])
    left   = int(match['left'])
    right  = left + int(match['width'])

    return bottom, left, top, right


squares = [Square(*get_points(x)) for x in cuts]


    
