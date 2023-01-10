# import turtle
from turtle import *

screen = Screen()

screen.register_shape("img/q01.gif")
screen.register_shape("img/q02.gif")


class Batter(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("img/q01.gif")
        self.penup()
        self.goto(0, -200)

    def hit(self):
        # self.goto(0, -200)
        self.shape("img/q02.gif")

    def hit1(self):
        # self.goto(0, -200)
        self.shape("img/q01.gif")

    def move_l(self):
        if self.xcor() > -94:
            self.goto(self.xcor() - 15, -200)
        else:
            self.goto(self.xcor(), -200)

    def move_r(self):
        if self.xcor() < 104:
            self.goto(self.xcor() + 15, -200)
        else:
            self.goto(self.xcor(), -200)
