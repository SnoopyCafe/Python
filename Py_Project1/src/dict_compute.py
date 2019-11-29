import sys

d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = list(d.keys())
best_key_so_far = ks[0]

# initialize variable best_key_so_far to be the first key in d
for k in ks:
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far
    if int(d[best_key_so_far]) <= int(d[k]):
        best_key_so_far = k
        
print("key {} has the highest value {}".format(best_key_so_far, d[best_key_so_far]))
