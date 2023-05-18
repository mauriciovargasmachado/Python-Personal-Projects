from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()
screen.bgcolor("black")
screen.title("MV Pong")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_on=True

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() <-300:
        ball.bounce_wall()

    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() <-320 :
        ball.bounce_paddle()
    

    if ball.xcor() >350:
        ball.reset()
        ball.bounce_paddle()
        scoreboard.l_point()

    if ball.xcor() <-350:
        ball.reset()
        ball.bounce_paddle()
        scoreboard.r_point()







screen.exitonclick()