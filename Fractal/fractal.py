from turtle import *

# TODO:
#   Zkuste upravit jednotlivé parametry a po změně každého spustit program

n = 50

speed("fastest")
left(90)
forward(3*n)
#
color("dark green")
backward(n*4.8)
def tree(d, s):
    if d <= 0:
        return
    forward(s)
    tree(d-1, s*.8)
    right(120)
    tree(d-3, s*.5)
    right(120)
    tree(d-3, s*.5)
    right(120)
    backward(s)
tree(15, n)
backward(n/2)
exitonclick()