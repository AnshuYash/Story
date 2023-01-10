from turtle import Turtle
timmy = Turtle()
timmy.width(2)
timmy.color("coral")
for num in range(1,10):
    a1 = int(num)*10
    timmy.forward(a1)
    timmy.rt(90)
    timmy.forward(a1)
    timmy.rt(90)
    timmy.forward(a1)
    timmy.rt(90)
    timmy.forward(a1)
    timmy.rt(90)
print(timmy)
