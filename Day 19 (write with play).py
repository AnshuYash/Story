from turtle import Turtle,Screen
import random
screen = Screen()
tim = Turtle()
tim.speed("fastest")
tim.width(3)
color = ["Magenta" , "DarkViolet" ,"Lime","Yellow" ,"Cyan" ,"DodgerBlue" ,"SpringGreen"]
def curser():
    screen.clear()
def no_draw():
    tim.penup()
    tim.fd(50)
    tim.pendown()
def curser_fd():
    tim.color(random.choice(color))
    tim.fd(50)
def curser_bd():
    tim.color(random.choice(color))
    tim.backward(50)
def curser_rt():
    tim.color(random.choice(color))
    tim.rt(90)
def curser_lt():
    tim.color(random.choice(color))
    tim.lt(90)
screen.listen()
screen.onkey(key = "w",fun = curser_fd)
screen.onkey(key = "s",fun = curser_bd)
screen.onkey(key = "d",fun = curser_rt)
screen.onkey(key = "a",fun = curser_lt)
screen.onkey(key = "space" , fun = no_draw)
screen.onkey(key = "c", fun  =curser)
screen.exitonclick()
