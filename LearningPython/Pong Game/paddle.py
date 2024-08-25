from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.speed(0)
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.setpos(position)

    def new_method(self):
        self.setpos(350, 0)
    def moveUp(self):
        for n in range(5):
            ycord = self.ycor() + 8
            self.goto(self.xcor(), ycord)
    
    def moveDown(self):
        for n in range(5):
            ycord = self.ycor() - 8
            self.goto(self.xcor(), ycord)
        