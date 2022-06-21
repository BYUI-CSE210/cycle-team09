from game.casting.actor import Actor

class P1Score(Actor):
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
        self._points = 0
        self.add_points(0)
        
    def add_points(self, points):
        """Adds the points to the total score for player 1
        
        Args:
            points (int): The points earned after a colission
        """

        self._points += points
        self.set_text(f"P1 Score: {self._points}")
