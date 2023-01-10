from turtle import *

Align = "left"


class Instruct(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(350, 300)
        self.write("1) Use number keys 1,2,3,4,5 to hit the ball.", align=Align, font=("Arial", 10, "normal"))
        self.goto(350, 250)
        self.write("2) Place your shots timely otherwise \n  you will loose a wicket .", align=Align, font=("Arial", 10, "normal"))
