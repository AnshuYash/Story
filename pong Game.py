import random
import time
import turtle
from turtle import Turtle, Screen
from ball import Ball
from bat_1 import Bat_1
from bat_2 import Bat_2
from boundary import Boundary
from middle_line import Middle_Line
from scoreboard import Scoreboard

timmy = Turtle()
turtle.colormode(255)
timmy.color("RED")
timmy.penup()
timmy.hideturtle()
timmy.goto(0, -100)
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.tracer(0)
bound = Boundary()
mid = Middle_Line()
pad11 = Bat_1()
pad22 = Bat_2()
# score = Scoreboard()
screen.update()


def start_game():
    screen.clear()
    screen.setup(800, 600)
    screen.bgcolor(255,123,84)
    screen.tracer(0)
    Boundary()
    Middle_Line()
    pad1 = Bat_1()
    pad2 = Bat_2()
    score = Scoreboard()
    ball = Ball()
    screen.update()

    def reset_game():
        score.game_end()
        choice = screen.textinput(title="Enter your choice!", prompt="Type y to play another game or n to quit")
        if choice == "y":
            screen.clear()
            screen.bgcolor("Black")
            start_game()
        else:

            screen.bgcolor("Black")
            timmy.goto(0, -50)
            mid.hide_line()
            score.game_end()
            timmy.color("cyan")
            timmy.write("Please click on screen to exit", align="center", font=("Brush Script MT", 40, "normal"))
            screen.exitonclick()

    timmy.clear()
    screen.listen()
    screen.onkey(key="w", fun=pad1.go_up)
    screen.onkey(key="s", fun=pad1.go_down)
    screen.onkey(key="Up", fun=pad2.go_up)
    screen.onkey(key="Down", fun=pad2.go_down)

    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()
        ball.move()
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()
        if 40 > ball.distance(pad2) > 20:
            ball.bounce_x()
            score.r_score()
        if 40 > ball.distance(pad1) > 20:
            ball.bounce_x()
            score.l_score()
        # game end
        if ball.xcor() > 640 and ball.distance(pad2) > 50:
            reset_game()

        if ball.xcor() < -640 and ball.distance(pad1) > 50:
            reset_game()


def menu():
    screen.listen()
    timmy.penup()
    timmy.hideturtle()
    timmy.write("Press Space key to star the game!", align="center", font=("Castellar", 30, "bold"))
    screen.onkey(key="space", fun=start_game)


menu()
screen.exitonclick()
