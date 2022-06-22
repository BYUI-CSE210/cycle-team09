import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlPlayer1Action(Action):
    """
    An input action that controls the player 1 movements.
    
    The responsibility of ControlActorsAction is to get the direction and move the player 1.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        player1 = cast.get_first_actor("players")
        score = cast.get_first_actor("scores")
        points = 1

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            player1.turn_player(self._direction)
            player1.grow_trail()
            score.add_points(points)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            player1.turn_player(self._direction)
            player1.grow_trail()
            score.add_points(points)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            player1.turn_player(self._direction)
            player1.grow_trail()
            score.add_points(points)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            player1.turn_player(self._direction)
            player1.grow_trail()
            score.add_points(points)
        
        # player1.turn_player(self._direction)
        # player1.grow_trail()
        
        # score = cast.get_first_actor("scores")
        # points = 1
        # score.add_points(points)