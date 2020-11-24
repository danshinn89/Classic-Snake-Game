#Classic game of snake using turtle class


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_Active = True
while game_Active:
    screen.update()
    #DELAY FOR 0.1 SECOND then refresh the screen
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_Active = False
        scoreboard.game_over()

    #detect collision with tail
    #if head collides with any part of the tail game will end
    for square in snake.squares[1:]:

        if snake.head.distance(square) < 10:
            game_Active = False
            scoreboard.game_over()


screen.exitonclick()
