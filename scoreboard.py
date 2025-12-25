from turtle import Turtle,Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.present_score()

    def present_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.present_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",40,"bold"))