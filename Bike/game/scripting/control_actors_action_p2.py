import constants
from game.scripting.action import Action
from game.shared.point import Point

class ControlActorsActionP2(Action):

    def __init__(self, keyboard_service):

        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)


    def execute(self, cast, script):
        
        #player 2 left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)

        #player 2 right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)

        #player 2 up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)

        #player 2 down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)

        bike = cast.get_first_actor('bikesp2')
        bike.turn_bike(self._direction)