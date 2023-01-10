from turtle import Turtle


class Brick (Turtle):
    def __init__(self, color, x1, y1):
        super().__init__()
        self.color("Yellow")
        self.shape("square")
        self.shapesize(stretch_len=4.16, stretch_wid=2)
        self.penup()
        self.color(color)
        self.pencolor("black")
        self.goto(x1, y1)
