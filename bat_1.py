from turtle import Turtle
class Bat_1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(6,1)
        self.penup()
        self.goto(-645,0)
    def go_up(self):
        new_y = self.ycor()+40
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor()-40
        self.goto(self.xcor(), new_y)



    
