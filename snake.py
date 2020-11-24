from turtle import Turtle, position

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        #starting position of turtle squares
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

#Creates snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(position)
        self.squares.append(new_square)

    def move(self):
        for square_number in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_number - 1].xcor()
            new_y = self.squares[square_number - 1].ycor()
            self.squares[square_number].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.squares[-1].position())
