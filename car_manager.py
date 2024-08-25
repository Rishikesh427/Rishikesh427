from turtle import Turtle
import random



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
level = 0

class CarManager:
    def __init__(self):
        self.carlist = []
    def createCar(self):
        chanceCar = random.randint(1, 5)
        if chanceCar == 1:        
            tu = Turtle()
            tu.penup()
            tu.setpos(300, random.randint(-250, 250))
            tu.shape('square')
            tu.shapesize(1, 2)
            tu.color(random.choice(COLORS))
            self.carlist.append(tu)
        else:
            pass
    def moveCar(self):
        for tu in self.carlist:
            tu.backward(STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT)
