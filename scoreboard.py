from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Start at level 1
        self.hideturtle()  # Don't show a turtle, just text
        self.penup()  # No drawing
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the level displayed on the screen"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase level and update display"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display 'Game Over' message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
