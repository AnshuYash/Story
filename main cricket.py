from turtle import *
from batter import Batter
from border import Border
from cricket_ball import Ball
from stump import Stump1
from stump2 import Stump2
import math
from scoreboard import Scoreboard
from instruct import Instruct

X = 0
Y = 300
hit_var = 0
screen = Screen()
screen.bgcolor("green")
screen.screensize(800, 800)
screen.tracer(0)
tim = Turtle()
tim.hideturtle()
# cricket pitch
bor = Border()
# stump
stump_1 = Stump1()
stump_2 = Stump2()
# cricket bat
bat = Batter()
# ball
ball = Ball()
# scoreboard
score = Scoreboard()
score.write_score(score.runs, score.ball)
# instructions
ins = Instruct()
ball_move_on = False


# hitting a ball
def impact_ball_1():
    global hit_var, ball_move_on
    hit_var = 1
    if ball_out(ball.ycor()):
        ball_move_on = True
    else:
        wicket_down()


def impact_ball_2():
    global hit_var, ball_move_on
    hit_var = 2
    if ball_out(ball.ycor()):
        ball_move_on = True
    else:
        wicket_down()


def impact_ball_3():
    global hit_var, ball_move_on
    hit_var = 3
    if ball_out(ball.ycor()):
        ball_move_on = True
    else:
        wicket_down()


def impact_ball_4():
    global hit_var, ball_move_on
    hit_var = 4
    if ball_out(ball.ycor()):
        ball_move_on = True
    else:
        wicket_down()


def impact_ball_5():
    global hit_var, ball_move_on
    hit_var = 5
    if ball_out(ball.ycor()):
        ball_move_on = True
    else:
        wicket_down()


# checking if ball hit the bat or missed it
def ball_out(y_cor):
    if -280 < y_cor < -195 and (math.sqrt((bat.xcor() - ball.xcor()) * (bat.xcor() - ball.xcor())) <= 30):
        return True
    else:
        stump_1.out()
        ball.out()
        return False


def wicket_down():
    global ball_move_on, game_on
    game_on = False
    ball.out()
    ball_move_on = False
    stump_1.out()
    bat.hit()
    screen.update()
    # bat.hit1()


screen.update()


# game
def game():
    global hit_var, ball_move_on
    game_on = True
    tim.clear()
    while game_on:
        screen.update()
        score.write_score(score.runs, score.ball)
        # key functions
        screen.listen()
        screen.onkey(key="Left", fun=bat.move_l)
        screen.onkey(key="Right", fun=bat.move_r)
        screen.onkey(key="1", fun=impact_ball_1)
        screen.onkey(key="2", fun=impact_ball_2)
        screen.onkey(key="3", fun=impact_ball_3)
        screen.onkey(key="4", fun=impact_ball_4)
        screen.onkey(key="5", fun=impact_ball_5)

        if hit_var == 0:
            ball.move_2()
        # checking for keystroke functions

        if hit_var == 1:
            bat.hit()
            if ball_move_on:
                ball.hit_1()
        if hit_var == 2:
            bat.hit()
            if ball_move_on:
                ball.hit_2()
        if hit_var == 3:
            bat.hit()
            if ball_move_on:
                ball.hit_3()

        if hit_var == 4:
            bat.hit()
            if ball_move_on:
                ball.hit_4()

        if hit_var == 5:
            bat.hit()
            if ball_move_on:
                ball.hit_5()

        if hit_var == 6:
            ball.reset_ball()
            ball_move_on = False
            bat.hit1()
            hit_var = 0
            score.clear()
        if ball.xcor() > 650 or ball.ycor() > 500 or ball.xcor() < -650:
            hit_var = 6
            score.update_score()
            ball_move_on = False
        if ball.ycor() < -295:
            game_on = False
            ball.out()
            ball_move_on = False
            stump_1.out()
            score.game_end()
            choice = screen.textinput(title="Enter your choice!", prompt="Type y to play another game or n to quit")
            if choice == "y":
                game()
            else:
                score.game_end()
        screen.update()


def main_menu():
    tim.color("Black")
    tim.write("Press 'g' to Start the Game!!", align="Center", font=("Arial", 40, "normal"))
    screen.listen()
    screen.onkey(key="g", fun=game)


main_menu()

screen.exitonclick()
