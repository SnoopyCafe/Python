nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("parent: ")
    for y in x:
        print("     level2: " + y)


nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)


# Iterate through the list so that if the character ‘m’ is in the 
# string, then it should be added to a new list called m_list. Hint: Because this isn’t just a list of lists, think about what type of object you want your data to be stored in. 
# Conditionals may help you.
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']
m_list = []

for item in d:
   
    if isinstance(item, list):
        #print(item)

        for s in item:
            if isinstance(s, list):
                for x in s:
                    if 'm' in x:
                        m_list.append(x)
            else:
                if 'm' in s:
                    m_list.append(s)
    else:
        if 'm' in item:
            m_list.append(item)
print(m_list)        
