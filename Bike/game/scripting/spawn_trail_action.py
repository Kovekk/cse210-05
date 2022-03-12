from typing import NewType
from game.scripting.action import Action
from game.casting.actor import Actor

class SpawnTrailAction(Action):

    def execute(self, cast, script):

        bike_one = cast.get_first_actor("bike_one")
        bike_two = cast.get_first_actor("bike_two")
        bikes = [bike_one, bike_two]

        for bike in bikes:
            position = bike.get_position()
            color = bike.get_color()
            new_trail = Actor()
            new_trail.set_position(position)
            new_trail.set_color(color)
            new_trail.set_text("#")
            cast.add_actor("trails", new_trail)