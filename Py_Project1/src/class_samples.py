import math
import test
import sys

class AppleBasket():
    def __init__(self, color, qty):
        self.apple_color = color
        self.apple_quantity = qty
    
    def __str__(self):
        return f"A basket of {self.apple_quantity} {self.apple_color} apples."

    def increase(self):
        self.apple_quantity += 1
        
class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY
        
    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)  #return an Object (Point)

def distance(point1, point2):
    xdiff = point2.getX()-point1.getX()
    ydiff = point2.getY()-point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

print(AppleBasket('red', 10))
sys.exit(0)

p = Point(4,3)
q = Point(5,12)
print(distance(p,q), p.halfway(q))

#Object sorting
L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)


#####test.testEqual(bkt.apple_quantity, 10)
