from turtle import Turtle


START_POSITION=[(-20,0),(0,0),(20,0)]
MOVEMENT=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake():
    
    def __init__(self) -> None:
        self.segments=[]
        self.create_snake()
        self.snake_head=self.segments[0]

    def create_snake(self):
        
        for position in START_POSITION:
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def move(self):
        
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(MOVEMENT)
        
    def up(self):
        
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    
    def down(self):
        
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    
    def left(self):
        
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    
    def right(self):
        
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
        
    