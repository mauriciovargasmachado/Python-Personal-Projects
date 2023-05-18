from turtle import Turtle, Screen
import random


screen=Screen()
screen.setup(500,500)
user_input=screen.textinput("Make your bet!!!", "Which turtle will win the race?")
color=["red","green","blue","black","yellow"]
y_positions=[100,50,0,-50,-100]

list_of_turtles=[]
game_on=False

for i in range(0,5):

    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(-230,y_positions[i])
    list_of_turtles.append(new_turtle)

if user_input:
    game_on=True
    
while game_on:

    for turtle in list_of_turtles:
        if turtle.xcor()>230:
            game_on=False
        velocity=random.randint(1,10)
        turtle.forward(velocity)
    

screen.exitonclick()
    
