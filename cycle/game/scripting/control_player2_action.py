import constants
from game.scripting.action import Action
from game.shared.point import Point

class ControlPlayer2Action(Action):
    """
    An input action that controls the second player.
    
    The responsibility of ControlActorsAction is to get the direction and move the player 2.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlPlayer2Action using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
    
    def execute(self, cast, script):
        """Executes the control player 2 action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        players = cast.get_actors("players")
        player_2 = players[1]
        player_2.turn_player(self._direction)
        player_2.grow_trail()

        scores = cast.get_actors("scores")
        score = scores[1]
        points = 1
        score.add_points(points)