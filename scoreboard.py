from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.L_score = 0
        self.R_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 260)
        # with open("p1.txt", mode="w") as file1:
        #     file1.write(str(self.L_score))
        self.write(self.L_score, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 260)
        # with open("p1.txt", mode="w") as file2:
        #     file2.write(str(self.R_score))
        self.write(self.R_score, align="center", font=("Arial", 50, "normal"))

    def l_score(self):
        self.L_score += 1
        self.clear()
        self.update_scoreboard()

    def r_score(self):
        self.R_score += 1
        self.clear()
        self.update_scoreboard()

    def game_end(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
