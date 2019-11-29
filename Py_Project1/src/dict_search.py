import sys

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

wrd_lst = sentence.strip('.').split()
wrd_cnt = {}
for word in wrd_lst:
    if word not in wrd_cnt:
        # we have not seen this character before, so initialize a counter for it
        wrd_cnt[word] = 0
    wrd_cnt[word] += 1

for key in wrd_cnt:
    print("Word: {}  Occurrences: {}".format(key,wrd_cnt[key]))

print(wrd_cnt)
sys.exit()

# Character count
f = open('files/school_prompt2.txt', 'r')
txt = f.read()
f.close()

# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for char in txt:
    if char not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[char] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[char] = letter_counts[char] + 1

for char in letter_counts:
    print("char: {} occurrences: {}".format(char, str(letter_counts[char])))

# print("a: " + str(letter_counts['a']) + " occurrences")
# print("t: " + str(letter_counts['t']) + " occurrences")
# print("s: " + str(letter_counts['s']) + " occurrences")


