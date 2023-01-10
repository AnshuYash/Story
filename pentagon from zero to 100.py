from turtle import Turtle, Screen
import random

tim = Turtle()
tim.hideturtle()
screen = Screen()
color = ["CornflowerBlue", "Magenta", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "DarkViolet", "SlateGray",
         "SeaGreen"]
tim.speed("fastest")
screen.bgcolor("black")
tim.width(2)
# radius= 100
for num in range(10, 100):
    # tim = Turtle("pentagon")
    tim.color(random.choice(color))
    current_heading = tim.heading()  # tells the position of turtle
    tim.setheading(current_heading + 10)
    for number in range(5):
        tim.fd(num)
        tim.rt(72)
screen.exitonclick()
