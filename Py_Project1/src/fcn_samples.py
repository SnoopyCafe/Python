import sys

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        

# Lamda functions
def make_incrementor(n):
    return lambda x: x + n

def concat(*args, sep="/"):
    return sep.join(args)

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('carrots')
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('pear', False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn('fruit')
print(fruit_ans)
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('plum', True, {'plum':8})
print(param_check)


print(my_function.__doc__)

f = make_incrementor(42)
print(f(0),f(1))

sys.exit(0)

print(concat("earth","mars","pluto"))
sys.exit(0)

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#parrot(1000)                                          # 1 positional argument
#parrot(voltage=1000)                                  # 1 keyword argument
#parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
#parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
#parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
