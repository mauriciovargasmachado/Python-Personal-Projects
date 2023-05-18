from turtle import Turtle,Screen
import random


my_turtle = Turtle()
my_turtle.speed(2)
my_turtle.width(5)
my_turtle.colormode(255)

my_turtle.shape("turtle")

def random_color():
    r=random.randint(0,155)
    g=random.randint(0,155)
    b=random.randint(0,155)
    randon_color=(r, g, b)
    print (randon_color)

direction=[0,90,180,270,360]

for i in range(100):
    my_turtle.color(random_color())
    my_turtle.forward(25)
    my_turtle.setheading(random.choice(direction))