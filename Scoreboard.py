from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("White")
        self.speed("fastest")
        self.goto(0,260)
        self.hideturtle()
        with open("highscore.txt",mode = "r") as high_score:
            self.high_score=int(high_score.read())
        self.update_scoreboard()
    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("highscore.txt",mode = "w") as high_score:
                high_score.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()


    def update_scoreboard(self):
         self.write("Score " + str(self.score)+ str("     ")+"High Score " + str(self.high_score) , align = "center" , font = ("Brush Script MT" ,  "24", "normal"))
    def game_end(self):
        self.goto(0,0)
        self.write("Game Over" ,align = "center" , font = ("Arial" ,  "24", "normal"))
    
