from turtle import Turtle,Screen


my_turtle = Turtle()

my_turtle.shape("turtle")

my_turtle.color("blue")


for i in range(25):

    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
    my_turtle.right(15)

    

screen = Screen()
screen.exitonclick()