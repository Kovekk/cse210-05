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
        self._handle_game_over(cast)

    def _handle_segment_collision(self, cast, script):
        trails = cast.get_actors("trails")
        bike_one = cast.get_first_actor("bike_one")
        bike_two = cast.get_first_actor("bike_two")
        
        for trail in trails:
            if trail.get_position().equals(bike_one.get_position()):
                self._is_game_over = True
                self._winner = "Red player"
            if trail.get_position().equals(bike_two.get_position()):
                self._is_game_over = True
                self._winner = "Yellow player"

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            bike_one = cast.get_first_actor("bike_one")
            bike_two = cast.get_first_actor("bike_two")
            trails = cast.get_actors("trails")

            x = int(constants.MAX_X)
            y = int(constants.MAX_Y)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"Game Over! {self._winner} wins!")
            message.set_position(position)
            cast.add_actor("messages", message)

            bike_one.set_color(constants.WHITE)
            bike_two.set_color(constants.WHITE)
            for trail in trails:
                trail.set_color(constants.WHITE)
