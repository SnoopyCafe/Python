import sys
import math
#Maps are for tranformation
def sumSquares(L):
        return sum(list(map((lambda x: x**2), L)))

nums = [3, 2, 2, -1, 1]
print(sumSquares(nums))
sys.exit()

things = [2, 5, 9]
things4 = list(map((lambda value: 4*value), things))
print(things4)

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))


abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
print(list(map((lambda value: value.upper()),abbrevs)))





