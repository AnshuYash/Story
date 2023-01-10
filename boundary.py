from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red","yellow")
        self.goto(-655,300)
        self.pendown()
        self.width(4)
        self.speed("fastest")
        # self.begin_fill()
        self.color("red","pink")
        for _ in range(2):
            self.fd(1310)
            self.rt(90)
            self.fd(600)
            self.rt(90)
        # self.end_fill()
        self.hideturtle()
