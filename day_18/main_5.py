from turtle import Turtle,Screen
import random


my_turtle = Turtle()
my_turtle.speed(50)
my_turtle.width(0.5)

my_turtle.shape("turtle")

color=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

radio=50

for i in range(200): 
    my_heading=my_turtle.heading()
    my_turtle.color(random.choice(color))
    my_turtle.circle(radio)
    my_turtle.setheading(my_heading+10)
    radio+=5

screen = Screen()
screen.exitonclick()
