from turtle import Turtle,Screen
import random


my_turtle = Turtle()
my_turtle.speed(2)
my_turtle.width(5)

my_turtle.shape("turtle")

color=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

direction=[0,90,180,270,360]

for i in range(100):
    my_turtle.color(random.choice(color))
    my_turtle.forward(25)
    my_turtle.setheading(random.choice(direction))