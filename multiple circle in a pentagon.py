from turtle import Turtle,Screen
import random
tim = Turtle()
screen = Screen()
color = ["blue","orange", "purple" , "pink","grey" ,"magenta","green", "violet" ,"White" , "Yellow"]
tim.speed("fastest")
screen.bgcolor("black")
tim.width(2)
for num in range(10,101,10):
    #number = int((100/num)-1) 
    tim.color(random.choice(color))
    tim.circle(num)
tim.color("black")
tim.penup()
tim.bk(75)
tim.pendown()
tim.color("Red")
tim.width(5)
tim.fd(145)
tim.lt(72)
tim.fd(145)
tim.lt(72)
tim.fd(145)
tim.lt(72)
tim.fd(145)
tim.lt(72)
tim.fd(145)

screen.exitonclick()
