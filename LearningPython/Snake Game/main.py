from turtle import Screen
from snakeclass import Snake
from food import Food
from scoreboard import Scoreboard, OverScreen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scrb = Scoreboard()
gmo = OverScreen()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()    
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scrb.addscore()
        snake.extend()
    xcoordinate = snake.head.xcor()
    ycoordinate = snake.head.ycor()
    if xcoordinate > 290 or xcoordinate < -290:
        game_is_on = False
        gmo.gameOver()
    elif ycoordinate > 290 or ycoordinate < -290:
        game_is_on = False
        gmo.gameOver()
    time.sleep(0.1)
    

    for segment in snake.segments[1: ]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            gmo.gameOver()


screen.exitonclick()