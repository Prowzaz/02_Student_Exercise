"""A regular polygon drawn with its own turtle."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the polygon settings and create its private drawing turtle."""
        if not isinstance(sides, int) or isinstance(sides, bool) or sides < 3:
            raise ValueError("sides must be an integer of at least 3")
        if side_length <= 0:
            raise ValueError("side_length must be greater than 0")
        if pen_size <= 0:
            raise ValueError("pen_size must be greater than 0")

        self._x = x
        self._y = y
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen_size = pen_size
        self._angle = angle
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.speed(0)

    def draw(self):
        """Draw a regular polygon starting at (x, y)."""
        pen = self._pen
        pen.penup()
        pen.goto(self._x, self._y)
        pen.setheading(self._angle)
        pen.pencolor(self._color)
        pen.pensize(self._pen_size)
        pen.pendown()

        for _ in range(self._sides):
            pen.forward(self._side_length)
            pen.left(360 / self._sides)

        pen.penup()

    def move_to(self, x, y):
        """Move this polygon to a new starting vertex and redraw it."""
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()
