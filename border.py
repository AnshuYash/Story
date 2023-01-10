from turtle import *


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.up()
        self.goto(-150, 280)
        self.down()
        self.pensize(3)
        self.speed("fastest")
        # pitch filled
        self.begin_fill()
        self.color("pink")
        self.fd(300)
        self.rt(80)
        self.fd(560)
        self.rt(100)
        self.fd(495)
        self.rt(100)
        self.fd(560)
        self.end_fill()
        # pitch outline
        self.pencolor("red")
        self.rt(80)
        self.fd(300)
        self.rt(80)
        self.fd(560)
        self.rt(100)
        self.fd(495)
        self.rt(100)
        self.fd(560)
        # pitch line bowler side
        self.bk(50)
        self.rt(80)
        # self.pensize(1)
        self.fd(317)
        # pitch line batter side
        self.rt(80)
        self.up()
        self.fd(430)
        self.down()
        self.rt(100)
        # self.pensize(1)
        self.fd(470)
        # wide line bowler side left
        self.up()
        self.goto(-110, 280)
        self.down()
        self.lt(82)
        self.fd(49)
        # wide line batter side left
        self.up()
        self.fd(429)
        self.lt(100)
        self.fd(50)
        # -126 = x
        self.rt(95)
        self.down()
        self.fd(80)
        # wide line bowler side right
        self.up()
        self.goto(110, 280)
        self.down()
        self.lt(12)
        self.fd(49)
        self.up()
        self.fd(429)
        self.rt(100)
        self.fd(50)
        # x = 134
        # y = -191
        self.lt(95)
        self.down()
        self.fd(80)
