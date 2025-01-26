from turtle import Turtle
from Food import Food
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()
    def update(self):
        self.write(f"Score: {self.score} Hihg Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=("Arial", 16, "normal"))