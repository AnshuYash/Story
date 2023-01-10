from turtle import *
import time

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

    def move(self):
        self.up()
        self.hideturtle()
        self.goto(X, Y)
        self.showturtle()
        self.move_ball = True
        while self.move_ball:
            if self.ycor() > -315:
                self.goto(0, self.ycor() - 10)
                time.sleep(0.03)
            else:
                self.move_ball = False
        if self.ycor() < -310:
            self.hideturtle()
            self.goto(0, -310)
            self.showturtle()

    def move_2(self):
        self.goto(0, self.ycor() - 5)

    def reset_ball(self):
        self.goto(0, 300)

    def hit_1(self):
        self.move_ball_1 = True
        while self.move_ball_1:
            # self.goto(1000,1)
            if self.ycor() <= 1 and self.xcor() <= 1300:
                self.goto(self.xcor() + 10, self.ycor() + 3.5)
                time.sleep(0.03)
            else:
                self.move_ball_1 = False
        self.hideturtle()
        return

    def hit_2(self):
        # self.goto(-1000, 0)
        self.move_ball_1 = True
        while self.move_ball_1:
            if self.ycor() <= 1 and self.xcor() >= -1300:
                self.goto(self.xcor() - 10, self.ycor() + 3.5)
                time.sleep(0.03)
            else:
                self.move_ball_1 = False
        self.hideturtle()
        return

    def hit_3(self):
        # self.goto(400, 1500)
        self.move_ball_1 = True
        while self.move_ball_1:
            if self.ycor() <= 1500 and self.xcor() <= 400:
                self.goto(self.xcor() + 5, self.ycor() + 10)
                time.sleep(0.03)
            else:
                self.move_ball_1 = False
        self.hideturtle()
        return

    def hit_4(self):
        # self.goto(-400, 1500)
        self.move_ball_1 = True
        while self.move_ball_1:
            if self.ycor() <= 1500 and self.xcor() >= -400:
                self.goto(self.xcor() - 5, self.ycor() + 10)
                time.sleep(0.03)
            else:
                self.move_ball_1 = False
        self.hideturtle()
        return

    def hit_5(self):
        # self.goto(0, -1500)
        self.move_ball_1 = True
        while self.move_ball_1:
            if self.ycor() <= 1500 and self.xcor() >= -0:
                self.goto(0, self.ycor() + 10)
                time.sleep(0.03)
            else:
                self.move_ball_1 = False
        # if self.ycor() <= 1500 and self.xcor() >= -0:
        #     self.goto(0, self.ycor() + 10)
        #     time.sleep(0.03)
        self.hideturtle()
        return

    def out(self):
        self.goto(self.xcor(), -305.)
        self.showturtle()
