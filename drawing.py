
import turtle

def draw_square(a_turtle):
    for i in range(1,5,1):
        a_turtle.forward(100)
        a_turtle.right(90)

def draw_circle(a_turtle):
    a_turtle.circle(100)

def draw_triangle(a_turtle):
    a_turtle.forward(100)
    a_turtle.right(120)
    a_turtle.forward(100)
    a_turtle.right(120)
    a_turtle.forward(100)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("blue")

    # square = turtle.Turtle()
    # square.color("yellow")
    # square.shape("turtle")
    # square.speed("fastest")
    #
    # for i in range(1,37,1):
    #     draw_square(square)
    #     square.right(10)
    #
    # square.right(90)
    # square.forward(300)

    # circle = turtle.Turtle()
    # circle.shape("turtle")
    # circle.speed("fast")
    # circle.color("white")
    # draw_circle(circle)

    tri = turtle.Turtle()
    tri.shape("triangle")
    tri.color("green")
    tri.speed("fast")
    draw_triangle(tri)

    window.exitonclick()

draw_shapes()