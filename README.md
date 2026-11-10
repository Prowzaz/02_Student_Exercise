# Object-Oriented Polygon Art

Student project using Python's `turtle` module and a student-designed `Polygon` class.

## Run locally

Requires Python 3 with Tkinter and a graphical desktop. Open a terminal in this folder.

```bash
python3 05_polygon_art_starter.py
python3 06_animated_polygon_art_starter.py
```

The first program creates static overlapping polygon artwork; the second animates Polygon objects.

`polygon_shape.py` keeps geometry and its turtle in private-by-convention attributes. Each polygon owns its own `_pen`; the animation driver calls `move_to()` and does not manipulate that internal turtle.

## Git milestones

- **Commit 1:** completed `polygon_shape.py` and working static artwork (`05_polygon_art_starter.py`).
- **Commit 2:** completed animation (`06_animated_polygon_art_starter.py`).

Only submit this student project folder to a **public GitHub repository** and submit the repository URL.
Do not include instructor solutions.

The assignment requires two clearly ordered Git milestones: commit the completed class and static artwork first, then commit the animation separately. Publish both commits to the public repository and verify that they appear in its history before submitting its URL.
