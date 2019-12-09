import sys

tester = {'info': [
         {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science", 'important classes': ['SI 106', 'ENGLISH 125', 'SI 110', 'AMCULT 202']},
         {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science', "important classes": ['SI 106', 'SI 410', 'PSYCH 111']},
         {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology', 'important classes': ['WOMENSTD 220', 'SOC 101', 'ENS 384']},
         {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science', "important classes": ['SOC 101', 'AMCULT 334', 'EECS 281']},
         {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History', 'important classes': ['ENGLISH 125', 'HIST 259', 'ENGLISH 130']},
         {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior', 'important classes': ['PIANO 101', 'STUDIO 300', 'THEORY 229', 'MUSC 356']}]}

lol = [v for each_item in tester['info'] for (k,v) in each_item.items() if k == 'important classes']
print([new_list_item for each_item in lol for new_list_item in each_item])

#print([new_list_item for each_item in lol for new_list_item in each_item])
#print([v for each_item in tester['info'] for (k,v) in each_item.items() if k == 'important classes'])
sys.exit(0)

#Print the max value for each position
# L1 = [1, 2, 3, 4]
# L2 = [4, 3, 2, 3]
# L3 = [0, 5, 0, 5]
# 
# maxs = []
# maxs = [max(w,x,y) for w,x,y in zip(L1,L2,L3)]
# print(maxs)
# 
# sys.exit(0)

# tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
# #1 for rtns the list of dicts in 'info', 2nd for iterates over the list dicts for the (key, value) pairs
# #compri = [v for value in tester['info'] for (k,v) in value.items() if k == 'name']  
# 
# compri = [value for value in tester['info']] #for v in value.items()] # if k == 'class standing' and v=='Junior']
# #print(compri)
# compri_sample = [v for x in tester['info'] if x['class standing'] == 'Junior' for (k,v) in x.items()]
# #next = [v for (k,v) in compri_sample]
# print(compri_sample)

#Combine a List of Lists into one
def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result

list_of_lists = [["hi", "bye"], ["hello", "goodbye"], ["hola", "adios", "bonjour", "au revoir"]]
print([new_list_item for each_item in list_of_lists for new_list_item in each_item])


things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(yourlist)

def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))


things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])

# The zip function takes multiple lists and turns them into a list of 
# tuples (actually, an iterator, but they work like lists for most practical purposes), 
# pairing up all the first items as one tuple, all the second items as a tuple, and so on. 
# Then we can iterate through those tuples, and perform some operation on all the first items, all the second items, and so on.


L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)

#Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, 
#create a new list, L3, that sums the two numbers if
#the number from L1 is greater than 10 and the number from L2 is less than 5.
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3 = [x1 + x2 for x1,x2 in zip(L1,L2) if x1>10 and x2<5]
print(L3)