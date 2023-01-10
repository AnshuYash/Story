from turtle import Screen, Turtle
from Snake import Snake
from food import Food
from Scoreboard import Scoreboard
from Boundary import Boundary
import time

screen = Screen()

timmy = Turtle()
timmy.color("Yellow")
timmy.penup()
timmy.goto(0, -50)
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("Black")
tim = Boundary()
scoreboard = Scoreboard()


def start_the_game():
    timmy.clear()
    screen.setup(width=600, height=600)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)
    game_on = True
    tim = Boundary()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while game_on:
        screen.update()
        time.sleep(0.2)
        snake.move()
        w_x = food.xcor()
        w_y = food.ycor()
        s_x = snake.head.xcor()
        s_y = snake.head.ycor()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.snake_size()
            scoreboard.increase_score()
        if s_x > 280 or s_x < -280 or s_y > 280 or s_y < -280:
            scoreboard.reset()
            choice = screen.textinput(title="Enter your choice!", prompt="Type y to play another game or n to quit")
            if choice == "y":
                screen.clear()
                screen.bgcolor("Black")
                start_the_game()
            else:
                screen.clear()
                screen.bgcolor("Black")
                tim.goto(0, 0)
                tim.color("red")
                tim.write("Please click on screen to exit", align="center", font=("Brush Script MT", 40, "normal"))
                screen.exitonclick()
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                choice = screen.textinput(title="Enter your choice!", prompt="Type y to play another game or n to quit")
                if choice == "y":
                    screen.clear()
                    screen.bgcolor("Black")
                    start_the_game()
                else:
                    screen.clear()
                    screen.bgcolor("Black")
                    tim.goto(0, 0)
                    tim.color("Red")
                    tim.write("Please click on screen to exit", align="center",
                              font=("Brush Script MT", 20, "normal"))


def menu():
    for _ in range(1):
        screen.listen()
        timmy.write("Press Space key to star the game!", align="center", font=("Arial", 24, "normal"))
        screen.onkey(key="space", fun=start_the_game)
        timmy.hideturtle()


menu()

screen.exitonclick()
