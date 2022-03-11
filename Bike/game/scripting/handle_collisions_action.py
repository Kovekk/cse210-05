import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):

    def __init__(self):

        self._is_game_over = False
        self._winner = ""


    def execute(self, cast, script):

        if not self._is_game_over:
            self._handle_segment_collision(cast, script)

    def _handle_segment_collision(self, cast, script):
        segments = cast.get_actors("segments")
        bike_one = cast.get_actors("bikes")
        bike_two = cast.get_actors("bikes")
        
        for segment in segments:
            if segment.get_position().equals(bike_one.get_position()):
                self._is_game_over = True
                self._winner = bike_two
            if segment.get_position().equals(bike_two.get_position()):
                self._is_game_over = True
                self._winner = bike_one

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            bike_one = cast.get_actors("bikes")
            bike_two = cast.get_actors("bikes")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            bike_one.set_color(constants.WHITE)
            bike_two.set_color(constants.WHITE)
