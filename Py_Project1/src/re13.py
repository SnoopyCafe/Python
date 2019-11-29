# Search for lines that start with From and have an at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    letter_counts = re.findall('Author:.*@(\S+)', line)
    if not letter_counts : continue
    print letter_counts

