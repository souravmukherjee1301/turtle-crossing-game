import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Stops automatic drawing for smooth animation
screen.title("Turtle Crossing Game")  # Added game title

player = Player()  # Create Turtle that you control

# Create Turtle movement for player
screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.reached_finished_lines():
        player.reset_position()

screen.exitonclick()
