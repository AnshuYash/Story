from turtle import Turtle,Screen
import random
tim = Turtle()
screen = Screen()
color = ["CornflowerBlue" ,"Magenta" ,"IndianRed","DeepSkyBlue","LightSeaGreen" , "DarkViolet" ,"SlateGray","SeaGreen"]
#tim.speed("fastest")
tim.width(3)
def move_curser():
    tim.color(random.choice(color))
    tim.fd(50)
    tim.rt(90)
screen.listen()
screen.onkey(key = "space" , fun = move_curser)
screen.exitonclick()
