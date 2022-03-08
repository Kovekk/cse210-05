from game.scripting.action import Action

class DrawActorsAction(Action):

    def __init__(self, video_service):
        
        self._video_service = video_service

    
    def execute(self, cast, script):

        trail = cast.get_first_actor('trails')
        bike = cast.get_first_actor("bikes")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(bike)
        self._video_service.draw_actors(trail)
        self._video_service.flush_buffer()