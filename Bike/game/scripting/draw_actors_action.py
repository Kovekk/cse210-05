from game.scripting.action import Action

class DrawActorsAction(Action):

    def __init__(self, video_service):
        
        self._video_service = video_service

    
    def execute(self, cast, script):

        trail = cast.get_actors("trails")
        bike_one = cast.get_first_actor("bike_one")
        bike_two = cast.get_first_actor("bike_two")
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(bike_one)
        self._video_service.draw_actor(bike_two)
        self._video_service.draw_actors(trail)
        self._video_service.draw_actors(messages)
        self._video_service.flush_buffer()