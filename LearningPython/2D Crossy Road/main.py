import time
from turtle import Screen, Turtle
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, level
from scoreboard import Scoreboard

car = CarManager()
t = Player()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(t.move, 'Up')




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.createCar()
    car.moveCar()
    


 
screen.exitonclick()
