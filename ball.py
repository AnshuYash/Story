from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Yellow")
        self.shape("circle")
        self.shapesize(1,1)
        self.penup()
        self.level = 1
        self.x_move = 20
        self.y_move = 20

    def move(self):
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        if self.level >2:
            self.speed("fast")
        self.goto(newx, newy)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def set(self):
        self.level = self.level + 0.5
        self.x_move = self.x_move + 2
        self.y_move = self.y_move + 2
    def ball_reset(self):
        self.goto(0,0)
