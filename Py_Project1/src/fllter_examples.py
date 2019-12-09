import sys

def keep_evens_long(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

#using filter
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

def longlengths(strings):
    return list(map(lambda s: len(s), filter(lambda x: len(x)>=4,strings)))
            
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
print(longlengths(lst))
sys.exit()

print(keep_evens([3, 4, 6, 7, 0, 1]))

lst2 = list(filter(lambda val: 'o' in val, lst))
print(lst2)

