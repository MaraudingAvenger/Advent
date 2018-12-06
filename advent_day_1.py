import pickle
import os

with open(os.getcwd() + '/files/nums.pickle', 'rb') as file:
    nums = pickle.load(file)

freq_set = set()
freq = 0

freq_set.add(freq)
repetition = False

count=1
while not repetition:
    for num in nums:
        freq += num

        if freq in freq_set:
            print("Repeated frequency! -->", freq)
            print("Last operation:", num)
            repetition = True
            break
        
        freq_set.add(freq)

    else:
        print("No repetition of frequencies {}".format(count))
        count += 1
        print("Current freq:", freq)
