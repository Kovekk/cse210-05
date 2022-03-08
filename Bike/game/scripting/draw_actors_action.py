from game.scripting.action import Action

class DrawActorsAction(Action):

    def __init__(self, video_service):
        
        self._video_service = video_service

    
    def execute(self, cast, script):

        score = cast.get_first_actor('scores')
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        segments = snake.get_segments()
        messages = cast.get_actors('messages')

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()