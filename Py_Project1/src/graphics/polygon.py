# Write a program that asks the user for the number of sides, 
# the length of the side, the color, and the fill color 
# of a regular polygon. The program should draw the polygon and then fill it in.

import turtle

wn = turtle.Screen()
t1 = turtle.Turtle()

sides = 4
len_side = 100
t1.pencolor("black")
t1.fillcolor("blue")
t1.begin_fill()

for i in range(4):
    t1.forward(len_side)
    t1.left(90)
t1.end_fill()    
wn.exitonclick()