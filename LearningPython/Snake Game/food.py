from turtle import Turtle as T, Screen
import random
import time
class Food(T):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed(10)
        self.setpos((random.randint(-28, 28) * 10), (random.randint(-28, 28) * 10))

    def refresh(self):
        self.setpos((random.randint(-28, 28) * 10), (random.randint(-28, 28) * 10))
