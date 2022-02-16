"""TODO: Describe your scene program."""

__author__ = "730475325"

from turtle import Turtle, colormode, done 


def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)
    mm: Turtle = Turtle()
    mm.color(75, 156, 211)
    mm.speed(7)
    gg: Turtle = Turtle()
    gg.color(19, 41, 75)
    gg.speed(16)
    draw_square(mm, 100, 0, 0)
    done()


def draw_square(zz: Turtle, length: float, x: float, y: float) -> None:
    """Draw squares."""
    times: int = 0
    while times < 9:
        zz.penup()
        zz.goto(x, y)
        zz.setheading(0.0)
        zz.left(135)
        zz.forward(length * (2 ** 0.5) / 2)
        zz.setheading(0.0)
        zz.pendown()
        i: int = 0
        while i < 4:
            zz.forward(length)
            zz.right(90)
            i = i + 1
        times += 1
        length += 50