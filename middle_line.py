from turtle import Turtle

class Middle_Line(Turtle):
    def __init__ (self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.width(4)
        self.goto(0,300)
        self.color("White")
        self.rt(90)
        self.pendown()
        for _ in range(30):
            self.fd(10)
            self.penup()
            self.fd(10)
            self.pendown()
        self.hideturtle()

    def hide_line(self):
        self.penup()
        self.speed("fastest")
        self.width(4)
        self.goto(0, 300)
        self.color("black")
        self.pendown()
        for _ in range(30):
            self.fd(10)
            self.penup()
            self.fd(10)
            self.pendown()
        self.hideturtle()

