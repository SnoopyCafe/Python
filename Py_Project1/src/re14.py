# Search for lines that start with From and have an at sign
import re
fname = raw_input('Enter file:')
hand = open(fname)
nums = list()
for line in hand:
    line = line.rstrip()
    letter_counts = re.findall('New Revision: ([0-9]+)', line)
    if len(letter_counts) == 1 :
        val = float(letter_counts[0])
        nums.append(val)
print len(nums)
print sum(nums)/len(nums)

