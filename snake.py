from turtle import *
POSITION= [(0,0), (0,-20),(0,-40)]

UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head=self.all_segments[0]

    def create_snake(self):
        for pos in POSITION:
            self.add_new_segment(pos)

    def add_new_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.speed(1)
        new_segment.color("white")
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def extend_segment(self):
        self.add_new_segment(self.all_segments[-1].position())



    def move_snake(self):
        for segment in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[segment - 1].xcor()
            new_y = self.all_segments[segment - 1].ycor()
            self.all_segments[segment].goto(new_x, new_y)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
