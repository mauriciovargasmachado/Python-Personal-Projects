import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
#screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")
screen.onkey(player.go_down,"Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    cars_manager.create_car()
    cars_manager.move_cars()

    for i in cars_manager.all_cars:
        if i.distance(player)<20:
            game_on=False
            scoreboard.game_over()

    if player.goal():
        player.restart()
        cars_manager.level_up()
        scoreboard.increase_level()
        
        


screen.exitonclick()