from turtle import Turtle
class Boundary(Turtle):
    def __init__(tim):
        super().__init__()
        tim.width(5)
        tim.speed("fastest")
        tim.color("Green")
        tim.penup()
        tim.goto(0,-290)
        tim.pendown()
        tim.fd (290)
        tim.lt(90)
        tim.fd(585)
        tim.lt(90)
        tim.fd(590)
        tim.lt(90)
        tim.fd(585)
        tim.lt(90)
        tim.fd(300)
        tim.hideturtle()

