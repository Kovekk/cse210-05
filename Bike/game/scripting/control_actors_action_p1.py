import constants
from game.scripting.action import Action
from game.shared.point import Point

class ControlActorsActionP1(Action):

    def __init__(self, keyboard_service):

        self._keyboard_service = keyboard_service
        self._direction = Point(0, constants.CELL_SIZE)


    def execute(self, cast, script):
        
        #player 1 left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)

        #player 1 right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)

        #player 1 up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)

        #player 1 down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)

        bike = cast.get_first_actor('bike_one')
        bike.turn_bike(self._direction)

