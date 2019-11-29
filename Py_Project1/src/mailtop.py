fname = raw_input('Enter file name: ')
fhand = open(fname)
char = dict()
for line in fhand:
    if not line.startswith('From ') : continue
    pieces = line.split()
    email = pieces[1]
    char[email] = char.get(email,0) + 1

bigc = None
bige = None
for word in char:
    value = char[word]
    if bigc == None or value > bigc:
        bigw = word
        bigc = value

print bigw, bigc


  
