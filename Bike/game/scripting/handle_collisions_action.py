import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):

    def __init__(self):

        self._is_game_over = False


    def execute(self, cast, script):

        if not self._is_game_over:
            self._handle