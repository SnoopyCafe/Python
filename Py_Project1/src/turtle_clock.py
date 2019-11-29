import turtle

wn = turtle.Screen()
#win_color = input("Enter Window color: ")
#tess_color = input("Enter Pen color: ")

wn.bgcolor("aqua")  # set the window background color
    
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("blue")  # make tess blue
t1.pensize(3)
t1.stamp()
t1.up()
clock_tick = 30  #At 30 degree increments

for _ in range(12):
    t1.forward(100)
    t1.down()
    t1.forward(10)
    t1.up()
    t1.forward(20)
    t1.stamp()
    t1.setpos(0,0)
    t1.right(clock_tick)


wn.exitonclick()  # wait for a user click on the canvas
