from turtle import Turtle,Screen


my_turtle = Turtle()

my_turtle.shape("turtle")

my_turtle.color("blue")


for i in range(10):

    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(1)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(1)
    my_turtle.left(90)



screen = Screen()
screen.exitonclick()