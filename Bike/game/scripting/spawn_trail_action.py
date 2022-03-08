from typing import NewType
from game.scripting.action import Action
from game.casting.actor import Actor

class SpawnTrailAction(Action):

    def execute(self, cast, script):

        actors = cast.get_all_actors()
        bikes = actors.get_actors("bikes")

        for bike in bikes:
            position = bike.get_position()
            color = bike.get_color()
            new_trail = Actor()
            new_trail.set_position(position)
            new_trail.set_color(color)
            new_trail.set_text("#")
            cast.add_actor("trails", new_trail)