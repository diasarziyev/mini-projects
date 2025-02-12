from turtle import Turtle, Screen
screen=Screen()
screen.listen()
starting_positions=[(0, 0), (-20, 0), (-40, 0)]
move_distance=20
up=90
left=180
down=270
right=0
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.squares=[]
        self.create_snake()
        self.head=self.squares[0]
    def create_snake(self):
        for position in starting_positions:
            self.add_square(position)
    def move(self):
        for sq in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[sq - 1].xcor()
            new_y = self.squares[sq - 1].ycor()
            self.squares[sq].goto(new_x, new_y)
        self.squares[0].forward(move_distance)
    def add_square(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.squares.append(square)
    def reset(self):
        for sq in self.squares:
            sq.goto(2000,2000)
        self.squares.clear()
        self.create_snake()
        self.head=self.squares[0]
    def extend(self):
        self.add_square(self.squares[-1].position())
    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)
    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)