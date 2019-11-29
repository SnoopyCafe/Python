# A drunk pirate makes a random turn and then takes 100 steps forward, 
# makes another random turn, takes another 100 steps, 
# turns another random amount, etc. 

# A social science student records the angle of each turn before the 
# next 100 steps are taken. Her experimental 
# data is 160, -43, 270, -97, -43, 200, -940, 17, -86. 
# (Positive angles are counter-clockwise.) 
# Use a turtle to draw the path taken by our drunk friend. 

# After the pirate is done walking, print the current heading. 
# Assume that the turtle originally has a heading of 0 and accumulate 
# the changes in heading to print out the final. Your solution should 
# work for any sequence of experimental data.

import turtle
from pip._vendor.html5lib.constants import headingElements


def drawTrack(t, turns):
    '''Drunken sailor track '''
    
    current_heading = 0
    
    for turn in turns:
        t.left(turn)  # random turn
        t.forward(100)  # 100 steps forward
        current_heading += turn
        print(turn)

    return current_heading

    
wn = turtle.Screen()
t1 = turtle.Turtle()

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
t1.pencolor("black")
t1.fillcolor("blue")

print("Final heading is", drawTrack(t1,turns) % 360)  # print current heading
wn.exitonclick()
