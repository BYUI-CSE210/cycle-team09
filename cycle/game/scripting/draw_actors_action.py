from game.scripting.action import Action
class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    The responsibility of DrawActorsAction is to draw all the actors.
    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """
    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
    def execute(self, cast, script):
        """Executes the draw actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        players = cast.get_actors("players")
        player1 = players[0]
        player2 = players[1]
        p1_trail = player1.get_trail()
        p2_trail = player2.get_trail()
        scores = cast.get_actors("scores")

        p1_score = scores[0]
        p2_score = scores[1]
        
        self._video_service.clear_buffer()
        self._video_service.draw_actors(p1_trail)
        self._video_service.draw_actors(p2_trail)
        self._video_service.draw_actor(p1_score)
        self._video_service.draw_actor(p2_score)
        self._video_service.flush_buffer()
