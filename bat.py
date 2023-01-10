from turtle import *

UP = 90
DOWN = 270


class BAT:
    def __init__(self):
        self.pos = [(-50, 0), (-50, 19), (-50, 38)]
        self.bat_seg = []
        self.create_bat()
        self.count = 0

    def create_bat(self):
        for post in self.pos:
            self.add_segments(post)

    def add_segments(self, position1):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.shapesize(stretch_len=0.9, stretch_wid=0.9)
        new_segment.color("Magenta")
        new_segment.speed("fastest")
        new_segment.goto(position1)
        self.bat_seg.append(new_segment)

    def up_move(self):
        for seg_num in range(len(self.bat_seg) - 1, 0, -1):
            new_x = self.bat_seg[seg_num - 1].xcor()
            new_y = self.bat_seg[seg_num - 1].ycor()+1
            self.bat_seg[seg_num].goto(new_x, new_y)
        self.bat_seg[0].fd(20)
    def down_move(self):
        for seg_num in range( 0,len(self.bat_seg) - 1):
            new_x = self.bat_seg[seg_num - 1].xcor()
            new_y = self.bat_seg[seg_num - 1].ycor()-2
            self.bat_seg[seg_num].goto(new_x, new_y)
        self.bat_seg[2].goto(self.bat_seg[0].xcor(), self.bat_seg[2].ycor() - 20)

    def up(self):
        # self.bat_seg[0].color("red")

        self.bat_seg[0].setheading(UP)
        self.up_move()
        # self.bat_seg[0].goto(self.bat_seg[0].xcor(), self.bat_seg[0].ycor() + 20)
        # self.bat_seg[1].goto(self.bat_seg[0].xcor(), self.bat_seg[0].ycor() - 19)
        # self.bat_seg[2].goto(self.bat_seg[0].xcor(), self.bat_seg[0].ycor() - 38)

    def down(self):
        # self.bat_seg[2].color("red")
        # self.bat_seg[0].setheading(DOWN)
        self.bat_seg[2].goto(self.bat_seg[0].xcor(), self.bat_seg[2].ycor() - 20)
        self.bat_seg[1].goto(self.bat_seg[0].xcor(), self.bat_seg[2].ycor() + 19)
        self.bat_seg[0].goto(self.bat_seg[0].xcor(), self.bat_seg[2].ycor() + 38)
