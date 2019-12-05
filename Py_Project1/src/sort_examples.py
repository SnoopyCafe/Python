
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

def second_let(s):
    return s[1]

print(absolute(3))
print(absolute(-119))

for y in L1:
    print(absolute(y))

L2 = sorted(L1, key=absolute)
print(L2)

print(sorted(L1, reverse=True, key=absolute))


ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
func_sort = sorted(ex_lst, key=second_let)

print(func_sort)
