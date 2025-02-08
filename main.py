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
car_manager = CarManager()  # The moving cars

# Create Turtle movement for player
screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create new cars and make them move.
    car_manager.create_car()
    car_manager.move_cars()

    if player.reached_finished_lines():
        player.reset_position()
        car_manager.increase_speed()  # The car moves faster

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

screen.exitonclick()
