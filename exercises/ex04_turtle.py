"""TODO: Describe your scene program."""

__author__ = "730486611"


from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)
    blue_turtle: Turtle = Turtle()
    blue_turtle.color(3, 252, 240)
    fast_turtle: Turtle = Turtle()
    fast_turtle.speed(10)
    blue_turtle.speed(5)
    draw_multipletri(blue_turtle, 0, 0, 10, 500)
    fast_turtle.begin_fill()
    draw_multipletri(fast_turtle, 0, 0, 2, 200)
    fast_turtle.end_fill()
    fast_turtle.color("green")
    draw_hexagon(fast_turtle, 0, 0, 150)
    done()


def draw_equtri(a_turtle: Turtle, length: float) -> None:
    """Draw a equilateral triangle!"""
    a_turtle.penup()
    count: int = 0
    a_turtle.right(150)
    a_turtle.pendown()
    while count < 3:
        a_turtle.forward(length)
        a_turtle.right(120)
        count += 1
    

def draw_multipletri(a_turtle: Turtle, x: float, y: float, times: int, length: float) -> None:
    """Draw a large graph of many triangles, center at x, y."""
    change_angle: float = 360 / times
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(90)
    count: int = 0
    angle: float = 90
    while count < times:
        a_turtle.setheading(angle)
        a_turtle.forward(((3 ** 0.5) / 3) * length)
        draw_equtri(a_turtle, length)
        a_turtle.penup()
        a_turtle.goto(x, y)
        angle += change_angle
        count += 1


def draw_hexagon(a_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draw a hexagon at x, y with length."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(90)
    a_turtle.forward(length)
    a_turtle.right(120)
    count: int = 0
    a_turtle.pendown()
    while count < 6: 
        a_turtle.forward(length)
        a_turtle.right(60)
        count += 1


if __name__ == "__main__":
    main()