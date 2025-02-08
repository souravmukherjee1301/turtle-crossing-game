from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """Move turtle upwards"""
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """Move turtle backwards"""
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        """Move turtle left words"""
        if self.xcor() > -240:
            self.setx(self.xcor() - 20)

    def move_right(self):
        """Move turtle left words"""
        if self.xcor() < 250:
            self.setx(self.xcor() + 20)

    def reset_position(self):
        """Reset player to starting position when it is level up"""
        self.goto(STARTING_POSITION)

    def reached_finished_lines(self):
        """Check if player reached the finish line"""
        return self.ycor() > FINISH_LINE_Y

