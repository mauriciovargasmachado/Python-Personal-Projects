from turtle import Turtle, Screen

mao = Turtle()
screen=Screen()
mao.shape("turtle")

def mov_foward():
    mao.forward(10)

def mov_backwards():
    mao.forward(-10)

def mov_right():
    mao.right(15)

def mov_left():
    mao.left(15)

def clear():
    mao.clear()
    mao.penup()
    mao.home()
    mao.pendown()


screen.listen()
screen.onkey(key="8",fun=mov_foward)
screen.onkey(key="2",fun=mov_backwards)
screen.onkey(key="6",fun=mov_right)
screen.onkey(key="4",fun=mov_left)
screen.onkey(key="space",fun=clear)
screen.exitonclick()