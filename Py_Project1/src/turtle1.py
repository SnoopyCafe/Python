import turtle

wn = turtle.Screen()
win_color = input("Enter Window color: ")
tess_color = input("Enter Pen color: ")

if win_color == None:
    wn.bgcolor("aqua")  # set the window background color
else:
    wn.bgcolor(win_color)
    
tess = turtle.Turtle()
tess.shape("circle")

if tess_color == None:
    tess.color("blue")  # make tess blue
else:
    tess.color(tess_color)
   
tess.pensize(3)  # set the width of her pen
tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()  # wait for a user click on the canvas
