from turtle import *
from ball import Ball
from brick import Brick
from playsound import playsound
import time
import pygame
from pygame import mixer
pygame.init()


men = Turtle()
men.hideturtle()
net = Turtle()
net.hideturtle()
net.penup()
net.color("Black")
net.goto(0, -30)
# screen
screen = Screen()
screen.tracer(0)
screen.bgcolor("#FFB4B4")
screen.setup(999, 600)
# green colored bricks
g1  = Brick("green",-443, 225)
g2  = Brick("green",-363, 225)
g3  = Brick("green",-283,225)
g4  = Brick("green",-203,225)
g5  = Brick("green",-123, 225)
g6  = Brick("green", -43, 225)
g7  = Brick("green",  37, 225)
g8  = Brick("green", 117, 225)
g9  = Brick("green", 197, 225)
g10 = Brick("green", 277, 225)
g11 = Brick("green", 357, 225)
g12 = Brick("green", 437, 225)
# yellow colored
y1  = Brick("yellow",-443, 185)
y2  = Brick("yellow",-363, 185)
y3  = Brick("yellow",-283, 185)
y4  = Brick("yellow",-203, 185)
y5  = Brick("yellow",-123, 185)
y6  = Brick("yellow", -43, 185)
y7  = Brick("yellow",  37, 185)
y8  = Brick("yellow", 117, 185)
y9  = Brick("yellow", 197, 185)
y10 = Brick("yellow", 277, 185)
y11 = Brick("yellow", 357, 185)
y12 = Brick("yellow", 437, 185)
# magenta
m1  = Brick("magenta",-443, 145)
m2  = Brick("magenta",-363, 145)
m3  = Brick("magenta",-283, 145)
m4  = Brick("magenta",-203, 145)
m5  = Brick("magenta",-123, 145)
m6  = Brick("magenta", -43, 145)
m7  = Brick("magenta",  37, 145)
m8  = Brick("magenta", 117, 145)
m9  = Brick("magenta", 197, 145)
m10 = Brick("magenta", 277, 145)
m11 = Brick("magenta", 357, 145)
m12 = Brick("magenta", 437, 145)
# cyan
c1  = Brick("cyan",-443, 105)
c2  = Brick("cyan",-363, 105)
c3  = Brick("cyan",-283, 105)
c4  = Brick("cyan",-203, 105)
c5  = Brick("cyan",-123, 105)
c6  = Brick("cyan", -43, 105)
c7  = Brick("cyan",  37, 105)
c8  = Brick("cyan", 117, 105)
c9  = Brick("cyan", 197, 105)
c10 = Brick("cyan", 277, 105)
c11 = Brick("cyan", 357, 105)
c12 = Brick("cyan", 437, 105)
# red colored
r1  = Brick("red",-443, 65)
r2  = Brick("red",-363, 65)
r3  = Brick("red",-283, 65)
r4  = Brick("red",-203, 65)
r5  = Brick("red",-123, 65)
r6  = Brick("red", -43, 65)
r7  = Brick("red",  37, 65)
r8  = Brick("red", 117, 65)
r9  = Brick("red", 197, 65)
r10 = Brick("red", 277, 65)
r11 = Brick("red", 357, 65)
r12 = Brick("red", 437, 65)
# brick list
bricks_list = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,m1,m2,m3,m4,m5,m6,m7,m8,m9,
               m10,m11,m12,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12]
r_brick_list = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12]
c_brick_list = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
m_brick_list = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
y_brick_list = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]
g_brick_list = [g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12]

# bat
bat = Turtle()
bat.penup()
bat.shape("square")
bat.shapesize(stretch_len=7, stretch_wid=1)
bat.goto(0, -270)
bat.color("#F637EC")

# score
wet =Turtle()
wet.color("black")
wet.penup()
wet.width(2)
wet.goto(400, 255)
global score
score = 0
final_score = "Score: " + str(score)
wet.write(final_score, align="right", font=("Bookman Old Style", "20", "bold"))

# boundary
wet.hideturtle()
wett = Turtle()
wett.penup()
wett.speed("fastest")
wett.goto(-495,295)
wett.hideturtle()
wett.pendown()
wett.color("#FF0063")
wett.pensize(20)

for _ in range(2):
    wett.fd(985)
    wett.rt(90)
    wett.fd(585)
    wett.rt(90)
screen.update()
# bat movement
def game_start():
    bgSound = mixer.Sound("background.wav")
    bgSound.play(-1)
    ball = Ball()
    men.clear()
    screen.update()
    global score
    a1 = 1
    while (a1 <2):
        time.sleep(0.001)
        screen.update()
        ball.move()
        if (ball.xcor() > 465 or ball.xcor() < -465 ):
            ball.bounce_x()
        if (ball.ycor() > 265 or ball.ycor() < -275 ):
            ball.bounce_y()
        if ball.ycor() < -240  and ball.distance(bat) < 100:
            bounceSound = mixer.Sound("laser.wav")
            bounceSound.play()
            ball.bounce_y()
        # conditionm to break the game
        if ball.ycor() < -273 and ball.distance(bat) > 100:
             net.write(f"You Loose!!", align="Center", font=("Bookman Old Style", "50", "bold"))
             a1 = 2
             return
        def go_right():
            if bat.xcor() < 385:
                bat.fd(80)
                bat.speed("fastest")
        def go_left():
            if bat.xcor() > -385:
                bat.bk(80)
                bat.speed("fastest")
        screen.listen()
        screen.onkey(key="Right", fun=go_right)
        screen.onkey(key="Left" , fun=go_left)
        for item in bricks_list:
            if ball.distance(item) <35:
                if ball.ycor()-item.ycor() <= -25.00 or ball.ycor()-item.ycor() >-50:
                    brickSound = mixer.Sound("crash.wav")
                    brickSound.play()
                    ball.bounce_y()
                    item.color("#FFB4B4")
                    bricks_list.remove(item)
                    for ate in r_brick_list:
                        if ate == item:
                            score += 3
                    for ate in c_brick_list:
                        if ate == item:
                            score += 7
                    for ate in m_brick_list:
                        if ate == item:
                            score += 10
                    for ate in y_brick_list:
                        if ate == item:
                            score += 12
                    for ate in g_brick_list:
                        if ate == item:
                            score += 15
                    wet.clear()
                    final_score = "Score: " + str(score)
                    wet.write(final_score, align="right", font=("Bookman Old Style", "20", "normal"))
        if (len(bricks_list) == 0):
            net.write(f"You Win!!", align="Center", font=("Bookman Old Style", "50", "bold"))

def menu():
    men.penup()
    men.goto(0,-20)
    men.color("black")
    msg = "Press the space key to start the game!!"
    men.write(msg, align="center", font=("Bookman Old Style", "35", "bold"))
    screen.listen()
    screen.onkey(key="space", fun=game_start)
menu()
screen.exitonclick()