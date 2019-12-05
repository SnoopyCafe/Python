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

print(keep_evens([3, 4, 6, 7, 0, 1]))


lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2 = list(filter(lambda val: 'o' in val, lst))
print(lst2)
