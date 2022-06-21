import constants
from game.casting.actor import Actor
from game.shared.point import Point

class P2Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by forcing 
    a colission with the oponent.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """

    def __init__(self):
        """creates new instance of the actor score"""

        super().__init__()
        self._points= 0
        self.add_points(0)
        position = self.get_position()
        # new_position = position.add((35 * constants.CELL_SIZE), 0)
        new_position = Point(((15 * constants.CELL_SIZE) + (35 * constants.CELL_SIZE)), 0 * constants.CELL_SIZE)
        # x = int(constants.MAX_X / 2)
        # y = int(constants.MAX_Y / 1)
        # position = Point(x - i * constants.CELL_SIZE, y)
        # position = Point(x,y)




        self.set_position(new_position)

    def add_points(self, points):
        """Adds the points to the total score for player 2
        
        Args:
            points (int): The points earned after a colission
        """

        self._points += points
        self.set_text(f"P2 Score: {self._points}")