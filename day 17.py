from turtle import Turtle
import random

tim = Turtle()
tim.width(3)
# tim.shape("dot")
tim.color("red")
tim.speed("fast")
ment = [0, 90, 180, 270]
for num in range(1, 1000):
    tim.fd(10)
    tim.rt(random.choice(ment))

