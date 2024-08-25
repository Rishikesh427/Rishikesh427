from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
    
    def move(self):
        newy = self.ycor() + 2
        newx = self.xcor() + 2
        self.goto(newx , newy)