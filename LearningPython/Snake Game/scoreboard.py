from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0 , 250)
        self.score = 0
        self.color('green')
        self.write(f'Score: {self.score}', False, 'center', ('Arial', 14, 'normal'))
        self.hideturtle()
    def addscore(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', False, 'center', ('Arial', 14, 'normal'))
    

class OverScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.hideturtle()
    def gameOver(self):
        self.setpos(0, 0)
        self.write('GAME OVER', False, 'center', ('Courier', 30, 'bold'))
    