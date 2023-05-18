from turtle import Turtle,Screen
import random


my_turtle = Turtle()

my_turtle.shape("turtle")

color=["red","blue","black","green"]

def draw (sides):
     
    angle=360/sides

    for i in range(sides):

        my_turtle.forward(100)
        my_turtle.right(angle)

for shape in range (3,10):
    my_turtle.color(random.choice(color))
    draw(shape)
 

    

screen = Screen()
screen.exitonclick()