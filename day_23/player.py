from turtle import Turtle

STARTING_POSITION = (0, -300)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 300


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def goal(self):
        if self.ycor()>300:
            return True
        else:
            return False
        
    def restart (self):
        self.goto(STARTING_POSITION)