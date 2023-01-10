from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
color = ["CornflowerBlue", "Magenta", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "DarkViolet", "SlateGray",
         "SeaGreen"]
tim.speed("fastest")
tim.hideturtle()
screen.bgcolor("black")
tim.width(2)
radius = 100
for num in range(72):
    tim.color(random.choice(color))
    current_heading = tim.heading()  # tells the position of turtle
    tim.circle(radius)
    tim.setheading(current_heading + 5)
screen.exitonclick()
