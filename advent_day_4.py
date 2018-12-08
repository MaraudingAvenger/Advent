import os
import datetime
from collections import Counter

with open(os.getcwd()+"/files/day_4.txt", 'r') as f:
    lines = sorted([line.strip() for line in f.readlines()])

def make_entry(line):
    date = datetime.datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
    message = line[19:]
    
    if 'Guard' in message:
        id_num = ""
        for l in message[6:12]:
            if l.isdigit():
                id_num += l
        return date, id_num
    
    elif 'falls' in message:
        return date, "X"
        
    elif 'wakes' in message:
        return date, "."
    
    else:
        raise TypeError("Houston, we found a crazy line... \n--" + line)

def count_x(row):
    count = 0
    for item in row:
        if item == 'X':
            count += 1
    return count

entries = sorted(list(map(make_entry, lines)), key=lambda x: x[0])

sleeptime = {item[1]: 0 for item in entries if item[1].isdigit()}
sked = {}


slept = 0
awoke = 0
guard = ""
for entry in entries:
    if entry[1].isdigit():
        guard = entry[1]
    elif entry[1] == 'X':
        slept = entry[0]
    elif entry[1] == '.':
        awoke = entry[0]
        nap = (awoke - slept).seconds // 60
        sleeptime[guard] += nap
        if not sked.get(guard):
            sked[guard] = list(range(slept.minute, awoke.minute))
        else:
            sked[guard].extend(list(range(slept.minute, awoke.minute)))
        

backwards = {v:k for k,v in sleeptime.items()}

g_answer = backwards[max(list(backwards.keys()))]
m_answer = Counter(sked[g_answer]).most_common(1)[0][0]
                         
print("\tGuard that slept the most:",
      g_answer, '--',
      sleeptime[g_answer], 'minutes')

print("\tGuard", g_answer,
      "common minute:", m_answer)

print("Part 1 Final answer =", int(g_answer) * m_answer)



print("\n\tGuard with the most common minute asleep:")
