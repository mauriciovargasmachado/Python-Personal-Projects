from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen =Screen()
#my_screen.setup(600*600)
my_screen.bgcolor("black")
my_screen.title("SNAKE")
my_screen.tracer(0)

snake=Snake() 
food=Food()
scoreboard=Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_on = True

while game_on:
    my_screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.relocation()
        snake.extend_snake()
        scoreboard.new_score()

    if snake.snake_head.xcor()>380 or snake.snake_head.xcor()<-380 or snake.snake_head.ycor()>300 or snake.snake_head.ycor()<-300:
        game_on=False
        scoreboard.game_over()

    #for segment in snake.segments[1:]:

        #if snake.snake_head.distance(segment) < 10:
            #game_on=False
            #scoreboard.game_over()


my_screen.exitonclick()