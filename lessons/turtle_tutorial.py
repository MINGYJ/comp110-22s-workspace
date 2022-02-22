"""Tutle tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()


i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

done()