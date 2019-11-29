'''
Method    Parameters    Description
keys    none    Returns a view of the keys in the dictionary
values    none    Returns a view of the values in the dictionary
items    none    Returns a view of the key-value pairs in the dictionary
get    key    Returns the value associated with key; None otherwise
get    key,alt    Returns the value associated with key; alt otherwise
'''

medals = {'gold':33,"silver":17,'bronze':12}
print(medals)

#Assignment
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers['Phelps'] = swimmers['Phelps'] + 5
print(swimmers['Phelps'])

### .keys
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

print(type(inventory.keys()))
ks = list(inventory.keys())
print(ks)

# .values / .items
print(list(inventory.values()))
print(list(inventory.items()))

for k in inventory:
    print("Got",k,"that maps to",inventory[k])
    
# Aliasing
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'
print(opposites['right'])

# Copying
acopy = opposites.copy()
acopy['right'] = 'left'    # does not change opposites

