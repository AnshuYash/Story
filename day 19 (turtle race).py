from turtle import Turtle, Screen
import random

screen = Screen()
timmy = Turtle()
timmy.hideturtle()
timmy.color("Black")
all_turtle = []
screen.setup(width=600, height=600)
user_input = screen.textinput(title="Make yor bet",
                              prompt="Enter the color of turtle which you think can win the race: ")
is_race_on = False
color = ["red", "orange", "yellow", "green", "blue", "purple"]
position = [-200, -120, -40, 40, 120, 200]
for num in range(0, 6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(color[num])
    new_turtle.goto(x=-280, y=position[num])
    all_turtle.append(new_turtle)
if user_input:
    is_race_on = True
while is_race_on:
    for new_turtle in all_turtle:
        if new_turtle.xcor() > 280:
            is_race_on = False
            winning_color = new_turtle.pencolor()
            if winning_color == user_input:
                timmy.write("you won. The \n" + str(winning_color) + "\n turtle wins the race.", align="center",
                            font=("Brush Script MT", 40, "normal"))
            else:
                timmy.write("you lost.\nThe " + str(winning_color) + "\nturtle wins the race.", align="center",
                            font=("Brush Script MT", 40, "normal"))
        distance = random.randint(0, 10)
        new_turtle.fd(distance)
screen.exitonclick()
