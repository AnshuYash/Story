from turtle import *

screen = Screen()
screen.register_shape("img/out_1.gif")


class Stump2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("img/out_1.gif")
        self.up()
        self.goto(0, 290)
