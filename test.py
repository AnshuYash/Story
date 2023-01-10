from turtle import *

tim = Turtle()
sc = Screen()


def fun1():
    print("1")


def fun2():
    print("2")


def fun3():
    print("3")


sc.listen()
sc.onkey(key="space", fun=fun1)
sc.exitonclick()
