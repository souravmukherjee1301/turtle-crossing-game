from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Randomly create new cars and add it to the list."""
        if random.randint(1, 6) == 1:  # Only create some cars, not too many
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars towards the left"""
        for car in self.all_cars:
            car.backward(self.car_speed)  # Moves each car left

    def increase_speed(self):
        """Increase speed after each level."""
        self.car_speed += MOVE_INCREMENT
