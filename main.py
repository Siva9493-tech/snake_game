from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800,height=600)
snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_right,"Right")
screen.onkey(snake.move_left,"Left")


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food)<15:
       food.refresh()
       score.increase_score()
       snake.extend_segment()

    if snake.head.xcor()>380 or snake.head.xcor()<-380 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.game_over()

    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()



screen.exitonclick()