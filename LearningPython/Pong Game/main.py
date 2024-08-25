from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

scr = Screen()
scr.setup(800, 600)
scr.bgcolor('black')
scr.tracer(0)

ball = Ball()

r_pdl = Paddle((350, 0))
l_pdl = Paddle((-350, 0))

scr.listen()
scr.onkey(l_pdl.moveUp, "w")
scr.onkey(l_pdl.moveDown, "s")
scr.onkey(r_pdl.moveUp, "Up")
scr.onkey(r_pdl.moveDown, "Down")



isOn = True
while isOn:
    scr.update()
    ball.move()
scr.exitonclick()