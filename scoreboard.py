from turtle import *
from random import *
Align = "Left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("White")
        self.hideturtle()
        self.runs = 0
        self.ball = 0
        self.over = 0
        self.a = 0
        self.l1 = [1, 2, 4, 6, 2, 4, 1, 2, 1, 2, 4, 6, 2, 4, 1, 6, 4, 6]

    def update_score(self):
        self.a = choice(self.l1)
        self.runs = self.runs + self.a
        self.ball = self.ball + 1
        self.over = round(int(self.ball - (self.ball % 6)) / 6)

    def write_score(self, run, balls):
        self.goto(-650, 300)
        self.write(f"Runs :: {run}", align=Align, font=("Calibri", 20, "normal"))
        self.goto(-650, 270)
        self.write(f"Over :: {self.over}.{balls}", align=Align, font=("Calibri", 20, "normal"))
        self.goto(-650, 240)
        self.write(f"You scored {self.a}", align=Align, font=("Calibri", 25, "normal"))

    def game_end(self):
        self.hideturtle()
        self.goto(-320, 150)
        self.color("Black")
        self.write(f"You loose your wicket!!", align="left", font=("Calibri", 40, "normal"))
        self.goto(-320, 100)
        self.write(f"You scored {self.runs} runs in {self.ball} balls!", align="left", font=("Calibri", 40, "normal"))
