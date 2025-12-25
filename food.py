from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.color("blue")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-380, 380)
        new_y = random.randint(-280, 280)
        self.goto(new_x,new_y)
