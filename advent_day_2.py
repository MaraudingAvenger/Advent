import os
from collections import Counter

os.chdir('/home/pi/Python/advent/')

with open(os.getcwd()+'/files/day_2.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

## Part 1 ##
codes = [Counter(line) for line in lines]
twos = ["".join(item.keys()) for item in codes
           if any(val == 2 for val in item.values())]
threes = ["".join(item.keys()) for item in codes
           if any(val==3 for val in item.values())]

print('Part one answer = {}'.format(len(twos) * len(threes)))

## Part 2 ##
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        
        diffs=0
        for letter in range(len(lines[0])):
            if( lines[i][letter]!=lines[j][letter] ):
                diffs += 1
                if(diffs > 1):
                    break


        if diffs == 1:
            final_answer = ''
            for letter in range(len(lines[0])):
                if lines[i][letter] != lines[j][letter]:
                    continue
                else:
                    final_answer += lines[i][letter]
            print('Part 2 answer =', final_answer)

