import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Bike(Actor):

    def __init__(self):
        super().__init__()
        self._segments = []

    def move_next(self):
        for segment in self._segments:
            segment.move_next()
    
   
    def get_bike(self):
        return self._segments[0]

    
    def turn_bike(self, velocity):
        self._segments[0].set_velocity(velocity)

    
    def _prepare_bike(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.BIKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = '8'
            color = constants.YELLOW

            bike = Actor()
            bike.set_position(position)
            bike.set_velocity(velocity)
            bike.set_text(text)
            bike.set_color(color)