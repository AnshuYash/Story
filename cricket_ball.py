from turtle import *

X = 0
Y = 300


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.up()
        self.hideturtle()
        self.goto(X, Y)
        self.shapesize(0.7, 0.7)
        self.showturtle()
        self.hit_dir = [1, 2, 3, 4, 5]
        self.hit_var = 0
        self.move_ball = True
        self.move_ball_1 = True

    def move_2(self):
        self.goto(0, self.ycor() - 7)

    def reset_ball(self):
        self.hideturtle()
        self.goto(0, 300)
        self.showturtle()

    def hit_1(self):
        if self.ycor() <= 500 and self.xcor() <= 1300:
            self.goto(self.xcor() + 10, self.ycor() + 10)

    def hit_2(self):
        if self.ycor() <= 500 and self.xcor() >= -1300:
            self.goto(self.xcor() - 10, self.ycor() + 10)

    def hit_3(self):
        if self.ycor() <= 1700 and self.xcor() <= 800:
            self.goto(self.xcor() + 8, self.ycor() + 15)

    def hit_4(self):
        if self.ycor() <= 1700 and self.xcor() >= -800:
            self.goto(self.xcor() - 8, self.ycor() + 15)

    def hit_5(self):
        if self.ycor() <= 1500 and self.xcor() >= -0:
            self.goto(0, self.ycor() + 20)

    def out(self):
        self.goto(self.xcor(), -295.)
        self.showturtle()
