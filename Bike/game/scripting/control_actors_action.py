import constants
from game.scripting.action import Action
from game.shared.point import Point

class ControlActorsAction(Action):

    def __init__(self, keyboard_service):

        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)


    def execute_p1(self, cast, script):
        
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

        bike = cast.get_first_actor('bike')
        bike.turn_head(self._direction)


    def execute_p2(self, cast, script):
        
        #player 1 left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)

        #player 1 right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)

        #player 1 up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)

        #player 1 down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)

        bike = cast.get_first_actor('bike')
        bike.turn_head(self._direction)    