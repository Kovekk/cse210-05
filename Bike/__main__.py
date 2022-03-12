import constants

from game.casting.cast import Cast
from game.casting.bike import Bike
from game.scripting.script import Script
from game.scripting.control_actors_action_p1 import ControlActorsActionP1
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
    bike1 = Bike()
    x = int(10 * constants.CELL_SIZE)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity = Point(0, 0)
    text = '8'
    color = constants.YELLOW
    bike1.set_text(text)
    bike1.set_position(position)
    bike1.set_velocity(velocity)
    bike1.set_color(color)
    cast.add_actor("bike_one", bike1)

    bike2 = Bike()
    x = int(50 * constants.CELL_SIZE)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity2 = Point(0, 0)
    text = '8'
    color = constants.RED
    bike2.set_text(text)
    bike2.set_position(position)
    bike2.set_velocity(velocity2)
    bike2.set_color(color)
    cast.add_actor("bike_two", bike2)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsActionP1(keyboard_service))
    script.add_action("input", ControlActorsActionP2(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", SpawnTrailAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()