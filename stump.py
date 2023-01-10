from turtle import *

screen = Screen()
screen.register_shape("img/out_11.gif")
screen.register_shape("img/out_22.gif")


class Stump1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("img/out_11.gif")
        self.up()
        self.goto(0, -295)

    def out(self):
        self.shape("img/out_22.gif")
    def not_out(self):
        self.shape("img/out_11.gif")
