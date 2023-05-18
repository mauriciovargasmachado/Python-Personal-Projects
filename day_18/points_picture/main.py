from turtle import Turtle,Screen
import random

#Turtle.colormode(255)

my_turtle = Turtle()
my_turtle.speed(20)


#colors=[(30, 12, 6), (8, 35, 17), (8, 16, 36), (51, 120, 78), (151, 76, 49), (38, 10, 16)]

color=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

my_turtle.hideturtle()
my_turtle.setheading(220)
my_turtle.penup()
my_turtle.forward(460)
my_turtle.setheading(0)
number_dots=196

for i in range(1,number_dots):
    
    random_color=random.choice(color)
    my_turtle.dot(20,random_color)    
    my_turtle.penup()
    my_turtle.forward(50)

    if i % 15 ==0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(750)
        my_turtle.setheading(0)



#my_turtle.dot(20,random_color)

screen = Screen()
screen.exitonclick()