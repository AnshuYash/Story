from turtle import *
from batter import Batter
from border import Border
from ball import Ball
from stump import Stump1
from stump2 import Stump2
import math

X = 0
Y = 300
screen = Screen()
screen.bgcolor("green")
screen.screensize(800, 800)
# cricket pitch
bor = Border()
# stump
stump_1 = Stump1()
stump_2 = Stump2()
# cricket bat
bat = Batter()

# ball
ball = Ball()


# hitting a ball
def impact_ball_1():
    bat.hit()
    if ball_out(ball.ycor()):
        ball.hit_1()


def impact_ball_2():
    bat.hit()
    if ball_out(ball.ycor()):
        ball.hit_2()


def impact_ball_3():
    bat.hit()
    if ball_out(ball.ycor()):
        ball.hit_3()


def impact_ball_4():
    bat.hit()
    if ball_out(ball.ycor()):
        ball.hit_4()


def impact_ball_5():
    bat.hit()
    if ball_out(ball.ycor()):
        ball.hit_5()


# new_ball
def new_ball():
    bat.hit1()
    stump_1.not_out()
    ball.move()


# checking if ball hit the bat or missed it
def ball_out(y_cor):
    if -280 < y_cor < -195 and (math.sqrt((bat.xcor() - ball.xcor()) * (bat.xcor() - ball.xcor())) <= 30):
        return True
    else:
        stump_1.out()
        ball.out()
        return False


screen.listen()
screen.onkey(key="Left", fun=bat.move_l)
screen.onkey(key="Right", fun=bat.move_r)
screen.onkey(key="space", fun=new_ball)
screen.onkey(key="1", fun=impact_ball_1)
screen.onkey(key="2", fun=impact_ball_2)
screen.onkey(key="3", fun=impact_ball_3)
screen.onkey(key="4", fun=impact_ball_4)
screen.onkey(key="5", fun=impact_ball_5)
print("go")
if ball.ycor() < -310:
    ball.out()
    stump_1.out()
# game
# game_on = True
# while game_on:
#     # key functions
#     screen.listen()
#     screen.onkey(key="Left", fun=bat.move_l)
#     screen.onkey(key="Right", fun=bat.move_r)
#     screen.onkey(key="space", fun=new_ball)
#     screen.onkey(key="1", fun=impact_ball_1)
#     screen.onkey(key="2", fun=impact_ball_2)
#     screen.onkey(key="3", fun=impact_ball_3)
#     screen.onkey(key="4", fun=impact_ball_4)
#     screen.onkey(key="5", fun=impact_ball_5)
#
#     ball.move_2()
#     if -900>ball.xcor()>900 or ball.ycor() > 1200:
#         ball.reset_ball()
#     if ball.ycor() < -310:
#         print(ball.ycor())
#         ball.out()
#         stump_1.out()
#         game_on = False

screen.exitonclick()
