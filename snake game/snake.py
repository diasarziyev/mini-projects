import time
from turtle import Screen
from Food import Food
from Snakew import Snake
from scoreboard import Score

screen=Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)
snake=Snake()
food=Food()
score=Score()
is_on=True
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.reset()
        snake.reset()
    for square in snake.squares[1:]:
        if snake.head.distance(square)<10:
            score.reset()
            snake.reset()


screen.exitonclick()