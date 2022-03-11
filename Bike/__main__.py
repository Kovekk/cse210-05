import constants

from game.casting.cast import Cast
from game.casting.bike import Bike
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsActionP1
from game.scripting.control_actors_action_p2 import ControlActorsActionP2
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_services import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.scripting.spawn_trail_action import SpawnTrailAction


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("bikes", Bike())
    cast.add_actor("trails", Bike())
    trail = SpawnTrailAction()
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsActionP1(keyboard_service))
    script.add_action("input", ControlActorsActionP2(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()