# Search for lines that start with From and have an at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    letter_counts = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(letter_counts) > 0 :
        print letter_counts

